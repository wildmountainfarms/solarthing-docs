Headless Armbian Setup
==========================

.. warning::

  This page may be outdated.
  For up to date documentation and for a more consistent experience across different single board computers, we recommend to instead setup :doc:`/quickstart/device-setup/dietpi`.

Armbian is an operating system that runs on many boards including but not limited to:

* Orange Pi
* Odroid

This document focuses on the setup without using a monitor or keyboard.


Downloading Armbian
--------------------

You can go here to download Armbian for your specific device https://armbian.hosthatch.com/archive/.


Connecting to a network
------------------------------------

Many devices do not have built in WiFi, so you will have to connect them to Ethernet.
Even if it does have built in WiFi, there is not a way that I know of to set up a WiFi connection without a keyboard and monitor.
You can setup WiFi later.


Using SSH
-------------

Armbian enables SSH by default, so as long as you know your IP from your router, you can SSH into it.

.. code-block:: shell

    ssh root@YOUR IP

The password is by default, ``1234``. It will ask you to change it on first login.

Connect to WiFi
----------------

If you have a USB adapter or your device has built in WiFi, use the ``armbian-config`` command to configure the WiFi.
Once WiFi is setup, you can unplug your Ethernet connection.

