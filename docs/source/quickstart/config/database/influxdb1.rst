InfluxDB 1.X Setup
=====================

This will help you adjust your ``base.json`` so that SolarThing starts uploading to InfluxDB.

.. note:: For new users, please use :doc:`influxdb2` instead.

.. seealso:: :doc:`/software/influxdb`



Creating ``influxdb2.json``
-----------------------------


This file that you create can be called anything, but we will call it ``influxdb2.json``.
It can also be placed anywhere, but we will place it in the ``config`` directory that also contains our already created ``base.json``.

Lets get into the config directory we need.

.. code-block:: shell

    cd /opt/solarthing/program/<THE DIRECTORY YOU USED IN PREVIOUS STEPS>/config

OK, now our shell should look something like this (``custom_rover`` may be different):

.. code-block:: console

    pi@raspberrypi:/opt/solarthing/program/custom_rover/config$

And now we will create ``influxdb2.json``

.. code-block:: shell

    nano influxdb2.json

Paste this into your newly created file:


.. code-block:: json

    {
      "type": "influxdb",
      "config": {
        "url": "http://localhost:8086",
        "username": "root",
        "password": "root",
        "database": "default_database",
        "measurement": null,

        "status_retention_policies": [
          {
            "frequency": 120,
            "name": "autogen"
          }
        ],

        "event_retention_policy": {
          "name": "autogen"
        }
      }
    }

Adjust the username, password, and url settings to your need, then save the file.

Another page that I will add in the future will go over the other settings and what they do.

Jump to :doc:`../configuration-edit-base-json`
