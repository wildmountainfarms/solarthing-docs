Serial Ports
=============

SolarThing connects to the rover, mate, and tracer via serial connections. These are typically in the form of some sort of USB adapter.


Click on the type of port and device you have.

.. toctree::
   :maxdepth: 1
   :caption: Hardware

   rover/rs232-port
   rover/rs485-port
   tracer/rs485-port
   mate/rs232-port


.. _serial-ports-continued:

Finding the path to your serial port
---------------------------------------

Now that you have your serial port connected to your device, it's time to find the path. Most of the time the path is ``/dev/ttyUSB0``.
On Raspberry Pi 4s, it may be ``/dev/ttyAMA0``. You can try either of these possibilities on the next page, or you can run these commands to try
and figure out what it may be.


Running ``ls /dev/tty*``
--------------------------

.. code-block:: console

    joshua@batterypi:/opt/solarthing/program/custom_tracer $ ls /dev/tty*
    /dev/tty    /dev/tty19  /dev/tty3   /dev/tty40  /dev/tty51  /dev/tty62
    /dev/tty0   /dev/tty2   /dev/tty30  /dev/tty41  /dev/tty52  /dev/tty63
    /dev/tty1   /dev/tty20  /dev/tty31  /dev/tty42  /dev/tty53  /dev/tty7
    /dev/tty10  /dev/tty21  /dev/tty32  /dev/tty43  /dev/tty54  /dev/tty8
    /dev/tty11  /dev/tty22  /dev/tty33  /dev/tty44  /dev/tty55  /dev/tty9
    /dev/tty12  /dev/tty23  /dev/tty34  /dev/tty45  /dev/tty56  /dev/ttyAMA0
    /dev/tty13  /dev/tty24  /dev/tty35  /dev/tty46  /dev/tty57  /dev/ttyS0
    /dev/tty14  /dev/tty25  /dev/tty36  /dev/tty47  /dev/tty58  /dev/ttyUSB0
    /dev/tty15  /dev/tty26  /dev/tty37  /dev/tty48  /dev/tty59  /dev/ttyUSB1
    /dev/tty16  /dev/tty27  /dev/tty38  /dev/tty49  /dev/tty6   /dev/ttyXRUSB0
    /dev/tty17  /dev/tty28  /dev/tty39  /dev/tty5   /dev/tty60  /dev/ttyprintk
    /dev/tty18  /dev/tty29  /dev/tty4   /dev/tty50  /dev/tty61


In the above output you can see there are LOTS of devices. In my case, the only devices that are serial ports are
``/dev/ttyUSB0``, ``/dev/ttyUSB1``, and ``/dev/ttyXRUSB0``. This command doesn't tell you for sure which devices are serial ports,
but its output can be useful.


Running ``dmesg | grep tty``
-------------------------------

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
In the above output, you can see messages such as ``converter now attached to ttyUSB1``. In my case, ``/dev/ttyUSB1`` relates to that message.

You can check whether or not the port you have found is correct on the next page.
