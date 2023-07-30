Running solarthing check command
================================

If you would like, you can jump straight into configuring the program. However, if you are new, it's a good idea to know
that your setup works before spending the time to craft your SolarThing configuration.

Run ``solarthing check -h`` to see usage of the command

.. tabs::

  .. code-tab:: console Docker Install

    pi@raspberrypi:/opt/solarthing$ sudo docker run ghcr.io/wildmountainfarms/solarthing check -h
    The options available are:
            [--help -h]
            [--modbus value] : The modbus address if using the rover or tracer type. Defaults to 1 if not set
            [--port value] : The path to the serial port
            [--scan] : Set this flag if you want to scan multiple modbus addresses. Starts at the value set from --modbus
            [--type /mate|rover|tracer/] : The type of device to look for [mate|rover|tracer]

  .. code-tab:: console Native Install

    pi@raspberrypi:/opt/solarthing$ solarthing check -h
    The options available are:
            [--help -h]
            [--modbus value] : The modbus address if using the rover or tracer type. Defaults to 1 if not set
            [--port value] : The path to the serial port
            [--scan] : Set this flag if you want to scan multiple modbus addresses. Starts at the value set from --modbus
            [--type /mate|rover|tracer/] : The type of device to look for [mate|rover|tracer]


Ok, that's a lot of options. First, we need to know what our serial port is. For a simple USB to RS232 adapter,
it is likely ``/dev/ttyUSB0``. So if we have a rover, we can run a command like so:

.. tabs::

  .. code-tab:: shell Docker Install

    sudo docker run --privileged -v /dev:/dev ghcr.io/wildmountainfarms/solarthing check --port /dev/ttyUSB0 --type rover
    # or if you would prefer not to use --privileged
    sudo docker run --cap-add=SYS_RAWIO --device "/dev/ttyUSB0:/dev/ttyUSB0" ghcr.io/wildmountainfarms/solarthing check --port /dev/ttyUSB0 --type rover

  .. code-tab:: shell Native Install

    solarthing check --port /dev/ttyUSB0 --type rover

If you have a tracer or mate instead, simply replace ``rover`` with ``tracer`` or ``mate`` and run the command.

If the command was successful, continue on to configuring SolarThing.


Wrong serial port
-----------------

If you got a message like ``Could not open serial port``, jump back over to :ref:`serial-ports-continued`.

There's also the possibility that another application on your computer is using the same serial port.
If you have not configured an application to use the serial port, this likely is *not* the problem.



.. _devices-not-detected:

Devices not detected
--------------------

If you tried checking for a rover or tracer and got that no devices were detected, don't worry!
It is common for these devices to use Modbus Addresses other than ``1``. We can try detecting using an address other than ``1`` like so:

.. tabs::

  .. code-tab:: shell Docker Install

    sudo docker run --privileged -v /dev:/dev ghcr.io/wildmountainfarms/solarthing check --port /dev/ttyUSB0 --type rover --modbus 10

  .. code-tab:: shell Native Install

    solarthing check --port /dev/ttyUSB0 --type rover --modbus 10

The above command checks for a rover at address ``10``. If that doesn't work I recommend you try ``16``. If that also does not work, you can scan:

.. tabs::

  .. code-tab:: shell Docker Install

    sudo docker run --privileged -v /dev:/dev ghcr.io/wildmountainfarms/solarthing check --port /dev/ttyUSB0 --type rover --modbus 1 --scan

  .. code-tab:: shell Native Install

    solarthing check --port /dev/ttyUSB0 --type rover --modbus 1 --scan

The above command scans addresses starting at address ``1``.


Still not working
-----------------

If it is still not working, there could be any number of things wrong. The most likely of which is that your serial adapter is not working properly.
This could be because the adapter is bad, or because the wiring is bad if you created a custom cable.
