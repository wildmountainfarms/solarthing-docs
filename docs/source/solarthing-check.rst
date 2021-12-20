Running solarthing check command
================================

If you would like, you can jump straight into configuring the program. However, if you are new, it's a good idea to know
that your setup works before spending the time to craft your SolarThing configuration.

Run ``solarthing check -h`` to see usage of the command


.. code-block:: console

    pi@raspberrypi:/opt/solarthing$ solarthing check -h
    The options available are:
            [--help -h]
            [--modbus value] : The modbus address if using the rover or tracer type. Defaults to 1 if not set
            [--port value] : The path to the serial port
            [--scan] : Set this flag if you want to scan multiple modbus addresses. Starts at the value set from --modbus
            [--type /mate|rover|tracer/] : The type of device to look for [mate|rover|tracer]


Ok, that's a lot of options. First, we need to know what our serial port is. For a simple USB to RS232 adapter,
it is likely ``/dev/ttyUSB0``. So if we have a rover, we can run a command like so:

.. code-block:: shell   

    solarthing check --port /dev/ttyUSB0 --type rover

If you have a tracer or mate instead, simply replace ``rover`` with ``tracer`` or ``mate`` and run the command.

If the command was successful, continue on to configuring SolarThing.


Wrong serial port
-----------------

If you got a message like ``Could not open serial port``, then it might be worth running this command to see what its output is:

.. code-block:: console

    joshua@batterypi:/opt/solarthing/program/custom_rover $ dmesg | grep tty
    [    0.000000] Kernel command line: coherent_pool=1M 8250.nr_uarts=1 snd_bcm2835.enable_compat_alsa=0 snd_bcm2835.enable_hdmi=1 bcm2708_fb.fbwidth=656 bcm2708_fb.fbheight=416 bcm2708_fb.fbswap=1 vc_mem.mem_base=0x3ec00000 vc_mem.mem_size=0x40000000  console=ttyAMA0,115200 console=tty1 root=PARTUUID=74d263f2-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
    [    0.001171] printk: console [tty1] enabled
    [    3.154007] 3f201000.serial: ttyAMA0 at MMIO 0x3f201000 (irq = 114, base_baud = 0) is a PL011 rev2
    [    4.236312] printk: console [ttyAMA0] enabled
    [    6.798820] systemd[1]: Created slice system-serial\x2dgetty.slice.
    [    9.238515] cdc_xr_usb_serial 1-1.4:1.0: ttyXR_USB_SERIAL0: USB XR_USB_SERIAL device
    [    9.447000] usb 1-1.3: pl2303 converter now attached to ttyUSB0
    [    9.451726] usb 1-1.2.4.2: pl2303 converter now attached to ttyUSB1

OK, so the above output is likely more than what you would see. When I ran the above command, I had 3 serial port adapters. 
In the above output, you can see messages such as ``converter now attached to ttyUSB1``. 
If you see a message like that, it means your adapter is on ``/dev/ttyUSB1``. Awesome! You found the right port!


.. _devices-not-detected:

Devices not detected
--------------------

If you tried checking for a rover or tracer and got that no devices were detected, don't worry! 
It is common for these devices to use Modbus Addresses other than ``1``. We can try detecting using an address other than ``1`` like so:

.. code-block:: shell   

    solarthing check --port /dev/ttyUSB0 --type rover --modbus 10

The above command checks for a rover at address ``10``. If that doesn't work I recommend you try ``16``. If that also does not work, you can scan:

.. code-block:: shell   

    solarthing check --port /dev/ttyUSB0 --type rover --modbus 1 --scan

The above command scans addresses starting at address ``1``.


Still not working
-----------------

If it is still not working, there could be any number of things wrong. The most likely of which is that your serial adapter is not working properly.
This could be because the adapter is bad, or because the wiring is bad if you created a custom cable.