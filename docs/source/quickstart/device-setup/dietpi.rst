DietPi Setup
========================

This page is for setting up DietPi without a keyboard and monitor attached to your Raspberry Pi (or other single board computer).
This page may also be useful to gain remote access to a DietPi system that is not operating headless (headful system).


Flashing DietPi
-----------------

Download DietPi here: https://dietpi.com/#download

.. note::

  If you are choosing a DietPi version for your Raspberry Pi 2, you should likely choose the ARMv8 image, as it is unlikely that you have a Raspberry Pi 2 v1.1.
  (It's worth checking to see if you have the v1.1 revision, though)

Once you have your DietPi image downloaded, you can choose a tool to flash your SD card such as `balenaEtcher <https://dietpi.com/docs/install/#2-flash-the-dietpi-image>`_.
If you need more thorough instructions, navigate to https://dietpi.com/docs/install/#2-flash-the-dietpi-image.

Configuring DietPi SD Card to Connect to WiFi
-------------------------------------------------

Since the goal is to be able to put the SD card in our Raspberry Pi, then boot up the Pi and gain SSH access,
we first need to configure DietPi to automatically connect to the WiFi network.

.. note::

  If you are using Ethernet, you may skip this step

Plug the SD card into your computer, or unplug and plug it back in if you just flashed it (this makes sure it is mounted).
Now, navigate to the boot partition using your file explorer, or a terminal if you prefer.
You will know it is the boot partition when you see that it contains ``dietpi`` and ``overlays`` folders.
In that same directory, there should be a file named ``dietpi.txt``.

Edit ``dietpi.txt`` with your editor of choice.
Find the line that has ``AUTO_SETUP_NET_WIFI_ENABLED=0`` and change it to ``AUTO_SETUP_NET_WIFI_ENABLED=1``.
Save the file.

Edit ``dietpi-wifi.txt``.
Begin editing Entry 0.

* Change ``aWIFI_IDENTITY[0]=''`` to ``aWIFI_IDENTITY[0]='YourSSID'`` and replace ``YourSSID`` with your WiFi's SSID
* Change ``aWIFI_PASSWORD[0]=''`` to ``aWIFI_PASSWORD[0]='YourPassword'`` and replace ``YourPassword`` with your WiFi network's password.
* Leave the other settings unchanged
* Save the file

Now plug your device in, and it should connect to your WiFi network!

.. _dietpi-gain-remote-access:

Finding IP address and gaining remote access
-----------------------------------------------

Now that your device is connected to your local network, it has an IP address assigned by your router.
The easiest way to find what that IP address is is to log into your router and find what IP address your device got (if you can't find it, try looking at DHCP leases).

Now that you have the IP address, it's time to SSH into your device.
Choose the option that best describes your setup.

.. tabs::

  .. tab:: PuTTY on Windows

    If you are using Windows, one option is PuTTY, which has a nice GUI interface to connect to a device.
    Download it here: https://putty.org/

    After opening PuTTY, connect to your device's IP address and configure the user as ``root`` and the password as ``dietpi``.

  .. tab:: ``ssh`` command on Windows

    If you would like to use the ``ssh`` command directly, you may do so as long as you have it installed.
    The recommended way to use the ``ssh`` command on Windows is to install `Git <https://git-scm.com/downloads>`_ and choose the default options while going through the installer to also install Git Bash.
    To install this more quickly, you may instead run this in command prompt/PowerShell: ``winget install --id=Git.Git -e``.

    Run this command and replace ``192.168.X.X`` with your device's IP address.

    .. code-block:: shell

      ssh root@192.168.X.X

    When prompted for a password, enter ``dietpi``. Note that you will not see your password as you type it. This is normal.

  .. tab:: ``ssh`` command on Linux or Mac OS

    If you are running Linux or Mac OS and want to SSH into your device from Linux or Mac OS,
    you can simply open a terminal to run the ``ssh`` command.

    Run this command and replace ``192.168.X.X`` with your device's IP address.

    .. code-block:: shell

      ssh root@192.168.X.X

    When prompted for a password, enter ``dietpi``. Note that you will not see your password as you type it. This is normal.

Now you should have shell access to DietPi.
Since this is the first time logging into the system, it will prompt you to configure and install software.
Most of the default options are fine, but feel free to change them if you know what you are doing.


Installing Docker
--------------------

During the initial installation, or after the initial installation, you should install Docker (if that's how you choose to run SolarThing - it's the recommended way to run SolarThing, after all).
On most systems, you should follow `install docker engine on Debian <https://docs.docker.com/engine/install/debian/>`_,
however on a DietPi system, you can simply use ``dietpi-software`` to install ``162 Docker`` and ``134 Docker Compose`` (you need to install both).
Or, you can simply run:

.. code-block:: shell

  # install Docker
  sudo dietpi-software install 162

  # Install Docker Compose
  sudo dietpi-software install 134

For more information relating to Docker on DietPi, go here: https://dietpi.com/docs/software/programming/#docker


Install SolarThing
--------------------

Now that you have your device setup, head on over to :doc:`/quickstart/install/index`!
