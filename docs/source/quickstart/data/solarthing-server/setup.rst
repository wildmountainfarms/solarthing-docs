Setup
=======

This shows you how to setup SolarThing server.

.. note::

  It is recommended to configure SolarThing Server on the same device as the CouchDB database. If this device is different than the one
  you installed SolarThing on, you can install SolarThing on this device too, just skip to this configuration after installing.

Setting Up
-----------

Just like with whatever uploader program you configured, we're going to change our directory:

.. tabs::

  .. group-tab:: Docker Install

    Before we begin, setup a directory (or use part of an existing directory) to contain SolarThing Server configuration.

    .. code-block:: shell

      mkdir ~/Documents/solarthing-config/server/{config,logs}
      cd ~/Documents/solarthing-config/
      nano docker-compose.yml

    You should now be editing ``docker-compose.yml``.
    If it is the case that you already have a docker-compose file, you may append to it.
    If you do not already have this file, you may paste the contents below exactly as is:

    .. code-block:: yaml

      version: '3.7'

      services:
        solarthing-server:
          image: 'ghcr.io/wildmountainfarms/solarthing-server:latest'
          container_name: solarthing-server
          restart: 'unless-stopped'
          command: --spring.config.location=config/application.properties
          volumes:
            - './server/config:/app/config:ro'
            - './server/logs:/app/logs'

    Now let's edit ``application.properties``:

    .. code-block:: shell

      nano server/config/application.properties


  .. group-tab:: Native Install

    .. code-block:: shell

      cd /opt/solarthing/program/graphql
      nano config/application.properties

    .. note::

      SolarThing Server is different from the other SolarThing programs.
      This means that native installations must use the graphql directory or do custom scripting.

``application.properties``
--------------------------

Now we will start editing the configuration file:


.. code-block:: shell

  nano config/application.properties

Paste this into your file:

.. code-block:: ini

  solarthing.config.database=config/couchdb.json


With the above configuration, you must have a ``couchdb.json`` file in your ``config`` directory.
Since you already know how the ``couchdb.json`` file works, we will not go into detail on this here.

That's all the configuration you need. Just point it to your ``couchdb.json``. Now let's cd up a directory and run it:

.. tabs::

  .. code-tab:: shell Docker Install

    cd ..
    sudo docker compose up

  .. code-tab:: shell Native Install

    sudo -u solarthing ./run.sh

You should see a bunch of log messages. After about 5 seconds, you should see messages similar to those at the end:

.. code-block::

  2021-12-20 23:48:31.030  INFO 269837 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
  2021-12-20 23:48:31.042  INFO 269837 --- [           main] m.r.s.rest.SolarThingGraphQLApplication  : Started SolarThingGraphQLApplication in 3.846 seconds (JVM running for 4.88)

If you do, it's working as intended!

Running in background
----------------------

.. tabs::

  .. group-tab:: Docker Install

    Running any docker container in the background is trivial with docker compose:

    .. code-block:: shell

      sudo docker compose up -d

  .. group-tab:: Native Install

    Let's go ahead and install the systemd service, start it, then enable it so it starts across reboots:

    .. code-block:: shell

        sudo /opt/solarthing/other/systemd/install.sh graphql
        sudo systemctl start solarthing-graphql
        sudo systemctl enable solarthing-graphql

    Run ``systemctl status solarthing-server`` to make sure it is running.

Now that you have SolarThing Server running, you may continue to configuring Grafana,
or just enjoy your web interface that is hosted on port 8080.
