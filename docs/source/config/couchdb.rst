Configuring CouchDB
====================

This will help you adjust your ``base.json`` so that SolarThing starts uploading to CouchDB.

First, this assumes that you have installed CouchDB: :doc:`../external/install-couchdb`. After installing, we need to run the SolarThing CouchDB setup program.
This adds databases to CouchDB that SolarThing needs. In order to run the setup program, we first need to create our own database configuration file.

Creating ``couchdb.json``
--------------------------

This file that you create can be called anything, but we will call it ``couchdb.json``. 
It can also be placed anywhere, but we will place it in the ``config`` directory that also contains our already created ``base.json``.

Lets get into the config directory we need.

.. code-block:: shell

    cd /opt/solarthing/program/<THE DIRECTORY YOU USED IN PREVIOUS STEPS>/config

OK, now our shell should look something like this (``custom_rover`` may be different):

.. code-block:: console

    pi@raspberrypi:/opt/solarthing/program/custom_rover/config$ 

And now we will create ``couchdb.json``

.. code-block:: shell

    nano couchdb.json

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
        "protocol": "http",
        "host": "localhost",
        "port": 5984,
        "username": "admin",
        "password": "relax",
        "connection_timeout": 1.5,
        "call_timeout": 10
      }
    }

OK, so the first part of that you can ignore for now, but the ``"config"`` part isn't too hard to understand. 
If you did not install CouchDB on this device, then you will likely have to change ``"host"`` to something different. 
You will likely change it to ``"host": "192.168.1.250"`` or something similar.

While installing CouchDB, it likely had you set up an admin account. You can change the username and password to be the same as that.
It is important that this user has admin permissions for the setup program to work.


Running the setup program
----------------------------

Now that you have a ``couchdb.json`` file, it's time to run the setup program.

CD up one directory using ``cd ..``. The end result should be similar to below:

.. code-block:: console

    pi@raspberrypi:/opt/solarthing/program/custom_rover$ 

Now let's run the setup program:

.. code-block:: shell

    solarthing run --couchdb-setup config/couchdb.json

.. note:: ``config/couchdb.json`` is relative to the directory we are currently in.

You should see output in the terminal saying that it is creating a bunch of databases. If it ends with no errors, you have successfully run the setup program.


Jump to :doc:`../configuration-edit-base-json`