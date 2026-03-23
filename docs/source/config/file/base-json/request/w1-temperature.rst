1-Wire Temperature Sensors
==============================

Temperature sensors such as the DS18B20 use the 1-Wire protocol. SolarThing can be configured to monitor these sensors.


Configuring your Raspberry Pi
------------------------------

The tutorial here: https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-temperature-sensor provides a great walkthrough of the necessary steps to
wire the sensor correctly and to enable the necessary drivers.

.. code-block::

  echo w1-gpio >> /etc/modules
  echo w1-therm >> /etc/modules
  # Note: if you don't have an external pull up resistor, you may replace w1-gpio with w1-gpio-pullup (not recommended)
  # If /boot/firmware/confix.txt exists, run this
  echo "dtoverlay=w1-gpio,gpiopin=4" | sudo tee -a /boot/firmware/config.txt
  # If /boot/config.txt exists, run this instead
  echo "dtoverlay=w1-gpio,gpiopin=4" | sudo tee -a /boot/config.txt
  reboot



Editing ``base.json``
----------------------

You just have to add this json to your ``base.json``:


.. code-block:: json

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
