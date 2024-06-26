PVOutput Uploader
==================

If you have a CouchDB database, you can create a system on https://pvoutput.org and upload your output data.

.. note:: CouchDB is the only database that the PVOutput program works with

.. note::

   It is recommended to configure SolarThing PVOutput on the same device as the CouchDB database. If this device is different than the one
   you installed SolarThing on, you can install SolarThing on this device too, just skip to this configuration after installing.

Setting up
-------------

Now we'll change our directory to the pvoutput directory and start editing its config:

.. tabs::

  .. group-tab:: Docker Install

    Before we begin, setup a directory (or use part of an existing directory) to contain pvoutput configuration.


    Here is an example file structure incorporating the CouchDB container we set up and the SolarThing server container we set up:

    .. code-block::

      ~/Documents/containers/solarthing/
      ├── couchdb/
      │   ├── data/
      │   └── etc/
      ├── server/
      │   ├── config/
      │   │   ├── application.properties
      │   │   └── couchdb.json
      │   └── logs/
      ├── pvoutput/
      │   ├── config/
      │   │   ├── base.json
      │   │   └── couchdb.json
      │   └── logs/
      └── docker-compose.yml

    .. code-block:: shell

      mkdir -p ~/Documents/containers/solarthing/pvoutput/{config,logs}
      cd ~/Documents/containers/solarthing/
      nano docker-compose.yml

    You should now be editing ``docker-compose.yml``.
    If it is the case that you already have a docker-compose file, you may append to it.
    If you do not already have this file, you may paste the contents below exactly as is:

    .. code-block:: yaml

      services:
        couchdb:
          # ...
        server:
          # ...
        # You may have other services defined here already
        #   If that is the case, just append the following configuration to your file:
        pvoutput:
          image: 'ghcr.io/wildmountainfarms/solarthing:latest'
          container_name: solarthing-pvoutput
          restart: 'unless-stopped'
          command: run --base config/base.json
          volumes:
            - './pvoutput/config:/app/config:ro'
            - './pvoutput/logs:/app/logs'

    Now let's edit ``base.json``:

    .. code-block:: shell

      nano pvoutput/config/base.json


  .. code-tab:: shell Native Install

    cd /opt/solarthing/program/pvoutput
    nano config/base.json

``base.json``
-------------

Paste this into your ``base.json`` file:

.. code-block:: json

  {
    "type": "pvoutput-upload",
    "system_id": 100,
    "api_key": "<YOUR API KEY>",
    "database": "config/couchdb.json",
    "source": "default"
  }

.. note::

  Make sure the ``couchdb.json`` file you refer to exists in a location that is accessible to SolarThing via the path you provide.

  You may copy the config file from ``server/config/couchdb.json`` to ``pvoutput/config/couchdb.json`` if you already have a configuration file in that location.

In the above example, ``100`` is the system id. You should replace this with whatever your system id is.

Replace ``<YOUR API KEY>`` with your API key.


``couchdb.json``
------------------

Here's an example ``couchdb.json`` file to put in ``pvoutput/config/couchdb.json``:

.. tabs::

  .. code-tab:: json Docker Install

    {
      "type": "couchdb",
      "config": {
        "url": "http://couchdb:5984"
      }
    }

  .. code-tab:: json Native Install

    {
      "type": "couchdb",
      "config": {
        "url": "http://localhost:5984"
      }
    }

.. note::

  The PVOutput program only reads from the database, so assuming you set up CouchDB using SolarThing's CouchDB Setup tool,
  then you don't need to specify a username and password.

Running the program
---------------------

Now let's run it:

.. tabs::

  .. code-tab:: shell Docker Install

    cd ..
    sudo docker compose up

  .. code-tab:: shell Native Install

    # Now run it:
    sudo -u solarthing ./run.sh

You should see a bunch of log messages. Some of the log messages should indicate success in uploading to PVOutput.

Running in background
----------------------------------------

.. tabs::

  .. group-tab:: Docker Install

    Running any docker container in the background is trivial with docker compose:

    .. code-block:: shell

      sudo docker compose up -d

  .. group-tab:: Native Install

    Let's go ahead and install the systemd service, start it, then enable it so it starts across reboots:

    .. code-block:: shell

        sudo /opt/solarthing/other/systemd/install.sh pvoutput
        sudo systemctl start solarthing-pvoutput
        sudo systemctl enable solarthing-pvoutput

    Run ``systemctl status solarthing-pvoutput`` to make sure it is running.

Now you're done! Navigate to your system on PVOutput and you should see one data point.
SolarThing will upload every 5 minutes, so after some time it'll be a cool graph!
