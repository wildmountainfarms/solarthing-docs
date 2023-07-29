Setting up Graylog
====================

If you have many running SolarThing instances, it makes sense to send all of the logs to one place.
Graylog is an application to do just that. I recommend installing this in the same place you have CouchDB installed
(which should be a device that is OK to have lots of disk activity).

.. note::

  You can find more official documentation here: https://go2docs.graylog.org/4-x/downloading_and_installing_graylog/docker.html.
  However, I find that the documentation does not do a good job of describing what file permisisons each container can or cannot have.

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
        restart: unless-stopped
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
          #- "ES_JAVA_OPTS=-Dlog4j2.formatMsgNoLookups=true -Xms512m -Xmx512m -XX:+UseG1GC"
        restart: unless-stopped
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

.. note::

  The versions of the docker containers above were specifically chosen to work with the 4.X releases:
  https://go2docs.graylog.org/4-x/downloading_and_installing_graylog/installing_graylog.html

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

Graylog Message Retention
---------------------------

If you pour all of your logs into Graylog, you will likely want to automatically delete some of those logs after a period of time.
This is where Graylog's Indices & Index Sets come into play. It's official documentation is here: https://docs.graylog.org/docs/index-model.

There are numerous ways to configure this. The way I will describe is to make it so that debug logs are only retained for a week.

First, create a new Index Set. Name it ``SolarThing Debug Set`` and set its Index prefix to ``solarthing_debug``.
Use the defaults for Index Rotation Configuration. For Index Retention Configuration, set "Max number of indices" to 7
so that no more than 7 days of debug logs will be kept.

Now we have a set created, we need to create a stream that will filter only debut messages so that we can send it to our new set.
Call this ``SolarThing Debug Stream``. Go ahead and check "Remove matches from 'All messages' stream" so that
debug messages before making this stream are put into this stream.
Manage the rules of this stream. Select your GELF input.
Add a new stream rule with: Field: ``level``, Type: ``smaller than``, Value: ``7``, Inverted: ``Yes``.
The result of this is ``level must not be smaller than 7``.
Now you can start the stream.
