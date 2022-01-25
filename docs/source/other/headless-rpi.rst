Headless Raspberry Pi Setup
=============================

If you want to use your Raspberry Pi without a monitor and have it automatically connect to your WiFi without
having to attach a keyboard and monitor, this'll help. You can do all SolarThing configuration either using a monitor and keyboard, or
"headless" over SSH without a monitor or keyboard.

If you are not familiar with Raspberry Pis at all, you may have a better experience using a monitor and keyboard rather than following the instructions below.

Download Image
----------------

If you haven't already flashed a micro SD card with Raspberry Pi OS, go here to download it: https://www.raspberrypi.com/software/operating-systems/

.. warning::

    No matter what, I do not recommend that you use "Raspberry Pi OS with desktop and recommended software" as
    it takes forever to update if you don't remove any of the software.

.. note::

    Since we are doing a headless install, you should use "Raspberry Pi OS Lite"

Flash Image
------------

Use software such as balenaEtcher to flash a micro SD card: https://www.balena.io/etcher/

Once flashed, you should remove, then reinsert your micro SD card into your computer so that the drives automatically mount.

Enable SSH
------------

SSH allows you to access your Raspberry Pi from a computer on the same network. When you reinserted your micro SD card,
one or two drives should have showed up. Navigate into the one called the "boot" drive.

Inside the boot drive, add a file named ``ssh`` with nothing in it. Note that there should be no file extension on it.

Adding a WiFi Network
----------------------

Unless you are using Ethernet, you'll want your Raspberry Pi to connect to WiFi as soon as you plug it in.
Once again, navigate to the "boot" drive.

Inside the boot drive, create and start editing a new file named ``wpa_supplicant.conf``.

.. note::
    
    You'll want to make sure that Windows or Mac OS isn't hiding the file extension as you do not want to end up with a file such as ``wpa_supplicant.conf.txt``

In the file, add the following content:

.. code-block::

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US
    network={
        ssid="YOUR SSID HERE"
        psk=YOUR PASSWORD HERE
    }

If you would like to use a program that does this automatically, take a look at this: https://github.com/retrodaredevil/headless-setup.
Note that it is a bit more work to set up as you have to have Python and pip installed on your system.

Plug in your Raspberry Pi and you're good to go!

Finding your Pi's IP Address
------------------------------

Once you plugged in your Raspberry Pi, it should connect to your WiFi network.
You can go to your router's webpage to try and figure out what IP it got.

Using SSH
-----------

If you set everything up correctly, you can ssh into your pi by using username: ``pi`` and password ``raspberry``.
On Linux or Mac OS, open a terminal and type ``ssh pi@<YOUR IP>``, then enter ``raspberry`` when it prompts for a password. 
On Windows, you can use something like Putty.

Updating your Raspberry Pi
----------------------------

Before installing SolarThing, it's a good idea to update everything on your system beforehand and install a few necessary tools.

.. code-block:: console

    pi@raspberrypi:~ $ sudo apt update
    pi@raspberrypi:~ $ sudo apt install git curl wget less zip
    pi@raspberrypi:~ $ sudo apt dist-upgrade -y
