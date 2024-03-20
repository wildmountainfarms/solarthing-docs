Tracer RS485 Port
=================

The tracer has an RS485 Port. The cable used to connect to the tracer is typically bundled with the tracer.

If you do not have a cable, I recommend buying "EPEVER Remote Temperature Sensor and Communication Cable". It never hurts to also get a temperature sensor.



Installing Drivers
--------------------

.. note::

  You **do not need to install drivers if your Linux kernel version is 6.6 or greater**.
  At the time of writing, most Linux distributions that you run on a Raspberry Pi (such as DietPi or Raspberry Pi OS),
  are not running Linux 6.6. This means that most of the time, it is necessary to follow these steps.


The awesome project `epsolar-tracer <https://github.com/kasbert/epsolar-tracer>`_ project is responsible for the instructions to install this driver.
SolarThing contains a script to piggyback off of their work.

First, install dependencies for the script:

.. code-block:: shell

  sudo apt-get update
  # NOTE: If you do not have a Raspberry Pi, instead install the kernel headers for your device
  sudo apt-get install dkms initramfs-tools rapsberrypi-kernel-headers
  # alternatively, you may install
  sudo apt-get install dkms initramfs-tools rapsberrypi-kernel-headers

Download and run the script:

.. code-block:: shell

  wget https://raw.githubusercontent.com/wildmountainfarms/solarthing/master/other/linux/install_tracer_serial_driver.sh
  chmod +x install_tracer_serial_driver.sh
  sudo ./install_tracer_serial_driver.sh

Once you have run these commands, you must restart your device.


Downsides to custom driver
---------------------------

The custom driver you just installed will have to be reinstalled every time you upgrade your Linux version.
So sometimes after running ``sudo apt upgrade``, you may have to reinstall the driver. If you have to reinstall, simply follow the above steps again.


Path to serial port
--------------------

When you continue the configuration, you will see ``/dev/ttyUSB0`` being used for many of the example serial port paths.
With the custom driver you installed, the path will likely be ``/dev/ttyXRUSB0``.


Go to: :ref:`serial-ports-continued`.
