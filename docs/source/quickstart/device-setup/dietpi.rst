DietPi Setup
========================

This page is for setting up DietPi without a keyboard and monitor attached to your Raspberry Pi (or other single board computer).
This page may also be useful to gain remote access to a DietPi system that is not operating headless (headful system).

.. note::

  DietPi supports a "testing" Raspberry Pi 5 image.
  I have been able to get this to work on a Raspberry Pi 5, but at the time of writing (2025-01-05)
  Raspberry Pi 5s do not have the best support across a range of software designed to run on Raspberry Pi devices.
  If you are considering a new Raspberry Pi, I recommend a Raspberry Pi 4 for the time being.


Flashing DietPi
-----------------

Download DietPi here: https://dietpi.com/#download

.. note::

  If you are choosing a DietPi version for your Raspberry Pi 2, you should likely choose the ARMv8 image, as it is unlikely that you have a Raspberry Pi 2 v1.1.
  (It's worth checking to see if you have the v1.1 revision, though)

Once you have your DietPi image downloaded, you can choose a tool to flash your SD card such as `balenaEtcher <https://dietpi.com/docs/install/#2-flash-the-dietpi-image>`_.
If you need more thorough instructions, navigate to https://dietpi.com/docs/install/#2-flash-the-dietpi-image.

.. note::

  https://dietpi.com/docs/install/#2-flash-the-dietpi-image
  **is the official documentation and will always be more up to date than this page. If you get stuck setting up your device, refer to that page!**

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

Edit ``dietpi.txt`` in the boot partition of the SD card.

.. code-block::

  AUTO_SETUP_NET_WIFI_ENABLED=1
  AUTO_SETUP_NET_WIFI_COUNTRY_CODE=US

Now edit ``dietpi-wifi.txt``:

.. code-block::


  aWIFI_SSID[0]='YOUR SSID'
  aWIFI_KEY[0]='YOUR WiFi PASSWORD'
  aWIFI_KEYMGR[0]='WPA-PSK'

Now plug your device in, and it should connect to your WiFi network!

Other (Optional) Recommended Settings
--------------------------------------

``dietpi.txt`` has some other settings that I recommend you set as follows. (Make sure to find and replace the entries in the file, rather than appending this block of text).

You may alter these settings as you see fit, this is a simple list of settings that I find useful that I've put here so you don't have to read through all of the settings.

.. code-block::

  AUTO_SETUP_LOCALE=en_US.UTF-8
  AUTO_SETUP_KEYBOARD_LAYOUT=us
  AUTO_SETUP_TIMEZONE=America/Chicago


  AUTO_SETUP_NET_ETHERNET_ENABLED=1
  AUTO_SETUP_NET_WIFI_ENABLED=1
  # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
  AUTO_SETUP_NET_WIFI_COUNTRY_CODE=US


  AUTO_SETUP_NET_HOSTNAME=solarthingpi

  # -2 represents OpenSSH. I actually recommend leaving this as default and changing to OpenSSH LATER
  AUTO_SETUP_SSH_SERVER_INDEX=-2


  # Optionally, include the contents of your public SSH key here. To get these contents, run `cat ~/.ssh/id_rsa.pub` or `cat ~/.ssh/id_ed25519.pub`
  AUTO_SETUP_SSH_PUBKEY=ssh-rsa aaaYOUR_ACTUAL_KEY_HEREaaa yourname@yourhost

  # -2 is "RAMlog hourly save to disk + clear" - This writes to your SD card more frequently than the default, but allows you to actually have logs when you need them
  AUTO_SETUP_LOGGING_INDEX=-2

  # 3 is "boot + hourly" - this makes sure your system's clock is never out of sync for more than an hour
  CONFIG_NTP_MODE=3

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

Initial Configuration (Optional)
--------------------------------

You have just logged into your DietPi system!
You're going to see a bunch of messages on the screen.
DietPi is now doing its initial updates and configuration prompts.
Go through the prompts normally, and check this list of bullet points for anything to look out for:

* On the install screen

  * I recommend installing OpenSSH to replace Dropbear
  * Set the logging to "hourly save + clear" so that you have logs

After the initial configuration, run ``dietpi-config`` and change these settings:

* Performance Options

  * ARM Temp Limit = 60C - We really don't want our Raspberry Pi to get super hot. This is usually only necessary if your Raspberry Pi does not have any heat syncs or coolers on it

* Security

  * Set the hostname to something like ``solarpi`` or whatever name you'd like.

* Language/Regional Options

  * Optionally set Locale to en_US.UTF-8
  * Set your timezone

* Network Options: Adapters

  * WiFi - Set up WiFi if necessary. Make sure to enable "Onboard WiFi". Going through the configuration here allows DietPi to have both Ethernet and WiFi connections if desired.


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

User Setup (Optional)
----------------------

Optionally, create your own personal user, and lock the root account for security reasons:

.. code-block:: shell

  # NOTE: Run these commands with sudo if you are not currently using the root user

  # Add the user
  useradd --create-home --user-group --shell /usr/bin/bash --groups sudo,tty,dialout,video,docker,input yourname
  # Set the password
  passwd yourname

Now SSH into your device as ``yourname`` (replace with the user name you created).
Confirm you have ``sudo`` access, then lock the root account and the dietpi account so they can not be logged into

.. code-block:: console

  yourname@solarthingpi:~$ sudo echo hi
  yourname@solarthingpi:~$ sudo passwd -l root
  yourname@solarthingpi:~$ sudo passwd -l dietpi


Install SolarThing
--------------------

Now that you have your device setup, head on over to :doc:`/quickstart/install/index`!
