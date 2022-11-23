Logging
==========

All the SolarThing programs are configured to log. By default, each program's systemd service is configured not to log to journalctl.
This saves disk space and allows SolarThing's Log4j configuration to compress or delete old log files.


Viewing Logs
----------------

Viewing SolarThing's log files is a good way to see if anything is going wrong, or to just view debug information to see data.

Let's assume that we have a program configured in the ``/opt/solarthing/program/custom_rover`` directory. To view logs, go ahead and ``cd``:

.. code-block:: shell

    cd /opt/solarthing/program/custom_rover/logs
    ls -l

You will now see all of the logs in the directory. You may see lots of files with a ``.log.gz`` extension. Those files are the old log files.
There should also be three files that have the current logs: ``log_summary.log``, ``log_info.log`` and ``log_debug.log``.

To view info logs:

.. code-block:: shell

    less -R log_info.log

.. note:: 
    
    While you can use ``nano`` to view log files, it is not recommended because it will not view colors well and is not good at opening large files.
    ``vi`` and ``vim`` are also not good for viewing log files containing color.


Now you can browse around.

You can also look at the logs "live", by using this command:

.. code-block:: shell

    tail -f log_debug.log

.. note:: 
    
   By default the debug log output is not "flushed" immediately. That means that while viewing it data will be cut off.
   This is to reduce the amount of time spent writing to disk, which is critical in maintaining a stable system on Raspberry Pis.

If you do not want to switch between ``less -R`` and ``tail -f``, you can just use ``less -R`` by itself. 
When you want to start "tailing" a file, just press Shift+F. When you want to go back to browsing the file, just press CTRL+C.

If you want to reload the file while inside of ``less -R``, just type Shift+R (``R``). ``less`` is such a useful tool!


Types of logs
---------------

You've seen above that there are three log files. The "summary" log files have the least amount of text in them. 
"info" log files are in the middle, and "debug" log files have the most information in them.


Decompressing logs
---------------------

As mentioned earlier, old log files have a ``.log.gz`` extension. If you need to view these log files, you must first decompress them.

Here is an example of how to decompress a particular log file:

.. code-block:: shell

    gunzip -k log_debug_2022.03.20-1.log.gz
    less -R log_debug_2022.03.20-1.log.gz
    

Setting up Graylog
--------------------

If you have many running SolarThing instances, it makes sense to send all of the logs to one place.
Graylog is an application to do just that. I recommend installing this in the same place you have CouchDB installed
(which should be a device that is OK to have lots of disk activity).

.. code-block:: shell

    cd /opt/containers
    mkdir graylog
    cd graylog
    apt-get install -y pwgen  # need this to generate a good password_secret
    pwgen -N 1 -s 96  # copy this output, you will paste it below
    (read -s PASS && printf $PASS | sha256sum)  # type your password here and copy the SHA-256 output to paste later

    mkdir es_data/
    sudo chown -R 1000:root es_data  # es_data requires certain permissions for the elasticsearch image to like it

    mkdir mongo_data/
    sudo chown -R 2000:2000 mongo_data  # mongo allows any uid:gid combination, so we will use 2000 for both here

    mkdir -p graylog_data/config/
    wget https://raw.githubusercontent.com/Graylog2/graylog-docker/4.3/config/graylog.conf
    mv graylog.conf graylog_data/config/
    sudo chown -R 1100:1100 graylog_data  # graylog_data requires certain permissions for the graylog image to like it


Edit ``docker-compose.yml`` in the ``graylog`` directory and paste these contents into it:

.. code-block:: yaml

    # This example based on the combination of examples on https://docs.graylog.org/docs/docker
    version: '3'
    services:
      # MongoDB: https://hub.docker.com/_/mongo/
      mongo:
        image: mongo:4.2
        volumes:
          - ./mongo_data:/data/db
        user: "2000:2000"
      # Elasticsearch: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/docker.html
      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
        volumes:
          - ./es_data:/usr/share/elasticsearch/data
        #user: "2000:2000" Specifying user does not work
        environment:
          - http.host=0.0.0.0
          - transport.host=localhost
          - network.host=0.0.0.0
          - "ES_JAVA_OPTS=-Dlog4j2.formatMsgNoLookups=true -Xms512m -Xmx512m"
        ulimits:
          memlock:
            soft: -1
            hard: -1
        deploy:
          resources:
            limits:
              memory: 1g
      # Graylog: https://hub.docker.com/r/graylog/graylog/
      graylog:
        image: graylog/graylog:4.3
        container_name: graylog
        volumes:
          - ./graylog_data:/usr/share/graylog/data
        #user: "2000:2000"
        environment:
          # CHANGE ME (must be at least 16 characters)! https://docs.graylog.org/docs/manual-setup password_secret. Generated using pwgen
          - GRAYLOG_PASSWORD_SECRET=forpasswordencryption
          # Password: admin
          - GRAYLOG_ROOT_PASSWORD_SHA2=8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
          #- GRAYLOG_HTTP_EXTERNAL_URI=http://127.0.0.1:9000/
          - GRAYLOG_HTTP_EXTERNAL_URI=http://192.168.10.251:9100/
        entrypoint: /usr/bin/tini -- wait-for-it elasticsearch:9200 --  /docker-entrypoint.sh
        restart: unless-stopped
        depends_on:
          - mongo
          - elasticsearch
        ports:
          # Graylog web interface and REST API
          - 9100:9000
          # Syslog TCP
          - 1514:1514
          # Syslog UDP
          - 1514:1514/udp
          # GELF TCP
          - 12201:12201
          # GELF UDP
          - 12201:12201/udp

    #networks: # only uncomment this if you specify $DOCKER_MY_NETWORK in .env file
    #  default:
    #    name: $DOCKER_MY_NETWORK

Now navigate to the IP and port you specified in your docker compose in your web browser.
You should see Graylog appear. You can login with admin/admin or admin/your_password_you_set assuming you changed it from the default.
After this I recommend setting up your own user: https://docs.graylog.org/docs/permission-management

To the right of the "System/Inputs" drop down, there should be an alert. Click it, it will have you add an input.
Add a "GELF UDP" input, name it, and use the defaults, then add it.

Once you have Graylog up and running, it's time to make one of your SolarThing instances send its logs to it.
In the working directory of one of your programs (ex: ``/opt/solarthing/program/automation``), create a file called ``log4j2.xml``
and add the contents of this file to it: https://github.com/wildmountainfarms/solarthing/blob/master/config_templates/log/gelf_log4j2.xml

Restart your SolarThing instance and navigate to search in Graylog. You should see entries popping up.
You can use a search such as ``application: "automation" AND level:[0 TO 6]`` to narrow your results.
The query language is described here: https://docs.graylog.org/docs/query-language

Now that you have Graylog up and running with SolarThing, you can also use it for your docker containers. You can add this to your compose file:

.. code-block:: yaml

    # ...
        logging:
          driver: gelf  # https://docs.docker.com/config/containers/logging/gelf/
          options:
            gelf-address: "udp://localhost:12201"

You can also make more logging from rsyslog go to Graylog. Just add a Syslog input on port 1514.
Then, add this line to the end of ``/etc/rsyslog.conf``: ``*.* action(type="omfwd" target="localhost" port="1514" protocol="udp" template="RSYSLOG_SyslogProtocol23Format")``.
More details here: https://docs.graylog.org/docs/syslog.


