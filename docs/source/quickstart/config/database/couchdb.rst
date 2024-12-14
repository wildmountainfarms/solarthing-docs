CouchDB
====================

This will help you adjust your ``base.json`` so that SolarThing starts uploading to CouchDB.

First, this assumes that you have installed CouchDB: :doc:`/software/couchdb`. After installing, we need to run the SolarThing CouchDB setup program.
This adds databases to CouchDB that SolarThing needs. In order to run the setup program, we first need to create our own database configuration file.

Creating ``couchdb.json``
--------------------------

This file that you create can be called anything, but we will call it ``couchdb.json``.
It can also be placed anywhere, but we will place it in the ``config`` directory that also contains our already created ``base.json``.

Lets get into the config directory we need.

.. code-block:: shell

    cd <THE DIRECTORY YOU USED IN PREVIOUS STEPS>

And now we will create ``couchdb.json``

.. code-block:: shell

  nano config/couchdb.json

Paste this into your newly created file:

.. code-block:: json

  {
    "type": "couchdb",
    "settings": {
      "packet_upload": {
        "throttle_factor": 3,
        "initial_skip": 1
      },
      "command_download": {
        "throttle_factor": 3,
        "initial_skip": 4
      }
    },
    "config": {
      "url": "http://localhost:5984",
      "username": "admin",
      "password": "relax",
      "connection_timeout": 1.5,
      "call_timeout": 10
    }
  }

You may ignore the ``"settings"`` object for now. Let's focus on the ``"config"`` part.
Let's understand how to update the ``"url"`` to correctly refer to your database.

* If CouchDB is installed on a different device (recommended)

  * Set ``"url"`` to refer to the IP address of that device. For example, ``http://192.168.1.250:5984`` if the device's IP address is 192.168.1.250

* If CouchDB is installed on the device SolarThing is running on

  * If SolarThing is running in Docker

    * If CouchDB is installed in Docker

      * CouchDB must be in the same docker compose file as SolarThing
      * Set ``"url"`` to refer to the service name of the CouchDB container or its container name. For instance, ``http://couchdb:5984`` if ``couchdb`` is the name of the service or is the ``container_name``.

    * CouchDB is not installed in Docker, set its URL to either of these

      * ``http://172.17.0.1:5984``  (recommended)
      * ``http://<IP address of your device on the LAN>:5984`` (not recommended, prone to errors if your device's LAN IP address changes)

  * If SolarThing is a native install

    * Set ``"url"`` to be ``http://localhost:5984``

.. warning::

  Remember that you should not be running CouchDB on a Raspberry Pi, or any device whose filesystem uses an SD card.
  SD cards are prone to failure if lots of data is written to them.
  This is generally not a big deal unless you are running something like a database that has data being constantly written to it.

.. note::

  The ``settings`` object provided in the example configuration above is a reasonable default.
  To understand it better or customize it to your liking, you will find more information about it at :ref:`config-database-settings`.


While installing CouchDB, it likely had you set up an admin account. You can change the username and password to be the same as that.
It is important that this user has admin permissions for the setup program to work.


Running the setup program
----------------------------

Now that you have a ``couchdb.json`` file, it's time to run the setup program.

CD up one directory using ``cd ..``. The end result should be similar to below:

Now let's run the setup program:


.. tabs::

  .. code-tab:: shell Docker Install

    sudo docker run --rm -it -v $(pwd)/config:/app/config ghcr.io/wildmountainfarms/solarthing run --couchdb-setup config/couchdb.json

  .. code-tab:: shell Native Install

    solarthing run --couchdb-setup config/couchdb.json

.. note:: ``config/couchdb.json`` is relative to the directory we are currently in.

You should see output in the terminal saying that it is creating a bunch of databases. If it ends with no errors, you have successfully run the setup program.


Jump to :doc:`../configuration-edit-base-json`
