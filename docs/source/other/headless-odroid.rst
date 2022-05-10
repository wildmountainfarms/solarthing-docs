Headless Odroid Setup
======================

Odroids primarily run most Linux distributions but can also run Android as an operating system.
SolarThing has not been tested with Android, so you should use the provided Ubuntu image.

More info on headless setup here: https://wiki.odroid.com/odroid-xu4/application_note/software/headless_setup


Download Image
----------------

Go to https://wiki.odroid.com/getting_started/os_installation_guide#tab__odroid-xu4 (and select something other than UX4 if you have something different) to download the image. I recommend the "Ubuntu Minimal" image.

If you use the wrong image, your Odroid will not boot.

Connecting Odroid to a network
--------------------------------

Odroids do not have built in WiFi, but WiFi can be added using a USB adapter.
If you want to configure WiFi, you will first either have to set it up using Ethernet, or will have to plug in a monitor

Connecting to Ethernet
--------------------------

All you have to do is hook your Odroid up to Ethernet and it will connect automatically.
Now navigate to your router's homepage to find the IP of the Odroid device

Using SSH
-----------

The provided Ubuntu images have SSH enabled by default, so you simply have to ssh into your Odroid like so:

.. code-block:: shell

    # If you did a minimal install
    ssh root@YOUR IP

    # If you did a full install, you can also do this instead
    ssh odroid@YOUR IP

.. note::

    The minimal install does not create a user named ``odroid`` like the full install does.
    So for the minimal install you will have to use the ``root`` user initially.

The password is ``odroid`` in both cases.

Configure WiFi
---------------

If you have a WiFi adapter, you can easily configure the WiFi though the command line. 
Configuring the WiFi network on an Odroid running Ubuntu is just like configuring WiFi on any Ubuntu through the command line.

You can follow instructions here: https://wiki.odroid.com/odroid_go_advance/application_note/sdio_wifi#configuring_wifi_station_mode_2_-_using_command_line.

The two main commands you will be running are here:

.. code-block:: shell

    nmcli dev wifi list
    nmcli dev wifi con 'SSID_1' password 'password_of_ssid1'

.. note:: 
    
    If your WiFi network is not currently online, the command will fail. In that case, you can manually create a file in ``/etc/NetworkManager/system-connections/`` named ``MYSSID.nmconnection``.

You can then check to make sure you are connected with this:

.. code-block:: shell

    ip addr
    # And
    ping 8.8.8.8

.. note::
    
    If you have the Odroid connected via Ethernet to the same network, it may not work at the same time as it could try to assign similar IP addresses
    to your Odroid. If it doesn't work, try disconnecting the Ethernet and going to your router's homepage to find the new IP address of your Odroid.

Once you are connected to WiFi, you can unplug your Ethernet cable (or monitor) you were using to configure it.
You should have already gotten your new IP address above. You can now use the new IP address to SSH into your Odroid device.


Other Notes
------------

* Hostname: ``odroid``
* Password: ``odroid``
  * Password for ``root`` user and password for ``odroid`` user.
* ``odroid`` user is only setup on full installs
* ``cat /sys/devices/virtual/thermal/thermal_zone*/temp`` to view temperature data
