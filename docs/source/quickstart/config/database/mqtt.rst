MQTT Uploading
============================

This will help you adjust your ``base.json`` so that SolarThing starts uploading to some MQTT broker.

.. note::

  The code behind MQTT functionality has had little testing. If you find issues with it, please report them on :issue-page:`our issue page <>`.


Creating ``mqtt.json``
--------------------------

This file that you create can be called anything, but we will call it ``mqtt.json``.
It can also be placed anywhere, but we will place it in the ``config`` directory that also contains our already created ``base.json``.

Lets get into the config directory we need.

.. code-block:: shell

  cd <THE DIRECTORY YOU USED IN PREVIOUS STEPS>

And now we will create ``mqtt.json``

.. code-block:: shell

  nano config/mqtt.json

Paste this into your newly created file:

.. code-block:: json

  {
    "type": "mqtt",
    "config": {
      "broker": "tcp://localhost:1883",
      "username": "admin",
      "password": "hivemq"
    }
  }

Adjust the settings as needed, then save the file.
