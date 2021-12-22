1-Wire Temperature Sensors
==============================

Temperature sensors such as the DS18B20 use the 1-Wire protocol. SolarThing can be configured to monitor these sensors.


Configuring your Raspberry Pi
------------------------------

The tutorial here: https://www.deviceplus.com/raspberry-pi/raspberrypi_entry_018/ provides a great walkthrough of the necessary steps to
wire the sensor correctly and to enable the necessary drivers.


Editing ``base.json``
----------------------

You just have to add this json to your ``base.json``:


.. code-block:: json5

    {
      //...
      "request": [ 
        {
          "type": "w1-temperature",
          "directory": "/sys/bus/w1/devices/28-000006470bec",
          "data_id": 1
        }
      ]
    }

You will have to change the ``28-000006470bec`` to something else.

Restarts your application, and you should see that CPU Temperature packets are being uploaded.
