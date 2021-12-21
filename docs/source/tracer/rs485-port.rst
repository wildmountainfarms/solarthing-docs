Tracer RS485 Port
=================

The tracer has an RS485 Port. The cable used to connect to the tracer is typically bundled with the tracer.

If you do not have a cable, I recommend buying "EPEVER Remote Temperature Sensor and Communication Cable". It never hurts to also get a temperature sensor.



Installing Drivers
--------------------

For the time being, Raspberry Pis do not come installed with the necessary drivers to allow for RS485 communication.
You will need to install them using provided SolarThing scripts.

The awesome project `epsolar-tracer <https://github.com/kasbert/epsolar-tracer>`_ project is
responsible for the instructions to install this driver. I made a script that piggybacks off of the installation instructions. 
You can run it by:

.. code-block:: shell

    sudo apt-get update # not necessary if you've updated recently
    sudo apt-get install dkms # May already be installed
    sudo /opt/solarthing/other/linux/install_updated_serial_driver.sh

Once you have run these commands, you must restart your device.


Downsides to custom driver
---------------------------

The custom driver you just installed will have to be reinstalled every time you upgrade your Linux version. 
So sometimes after running ``sudo apt upgrade``, you may have to reinstall the driver. If you have to reinstall, simply run this again:

.. code-block:: shell

    sudo /opt/solarthing/other/linux/install_updated_serial_driver.sh


Path to serial port
--------------------

When you continue the configuration, you will see ``/dev/ttyUSB0`` being used for many of the example serial port paths.
With the custom driver you installed, the path will likely be ``/dev/ttyXRUSB0``.


Go to: :ref:`serial-ports-continued`.
