CPU Temperature
=====================


For all the programs that upload to databases, they support the ability to add the device's CPU temperature as a packet. 
You just have to add this json to your ``base.json``:


.. code-block:: json5

  {
    //...
    "request": [
      { "type": "cpu-temp", "processors": 1 }
    ]
  }

Replace ``1`` with however many processors your device has.
The easiest way to see how many processors you have is to run ``ls /sys/class/thermal/thermal_zone*/temp | wc -l``.
Restarts your application, and you should see that CPU Temperature packets are being uploaded.


Required Docker Compose Configuration
----------------------------------------

If you are using Docker or Docker Compose, you must add the ``-v '/sys/class/thermal:/sys/class/thermal:ro'`` volume so that the container can read the necessary files.
If you are not using Docker, additional configuration is not required.

.. code-block:: yaml

  version: '3.7'

  services:
    solarthing-rover:
      image: 'ghcr.io/wildmountainfarms/solarthing:$SOLARTHING_VERSION'
      # ...
      volumes:
        # ...
        - '/sys/class/thermal:/sys/class/thermal:ro'
        # ...

