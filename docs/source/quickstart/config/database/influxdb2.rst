InfluxDB 2.X Setup
=====================

This will help you adjust your ``base.json`` so that SolarThing starts uploading to InfluxDB.

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

    nano couchdb.json

Paste this into your newly created file:


.. code-block:: json

    {
      "type": "influxdb2",
      "config": {
        "url": "http://localhost:8086",
        "token": "token stuff",
        "org": "solarthing-org"
      }
    }

Adjust the url and token parameter to your need. You will have to go into your InfluxDB web interface to generate a token.
Documentation for generating a token is here: https://docs.influxdata.com/influxdb/latest/security/tokens/create-token/


Jump to :doc:`../configuration-edit-base-json`
