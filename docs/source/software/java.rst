Install Java
============

So you need to install Java to your system?

* https://pi4j.com/documentation/java-installation/
* https://forums.raspberrypi.com//viewtopic.php?p=1308846


Required Version
----------------

SolarThing requires Java >= 11 and SolarThing Server requires Java >= 17. If you are able to install Java 17, you should do so, otherwise 11 is fine .


Install on Systems with Apt
---------------------------

The ``apt-get`` or ``apt`` command is used to install most software. To install Java 11, run this command:


.. code-block:: shell

    sudo apt-get update
    sudo apt-get install -y openjdk-11-jdk-headless

Raspberry Pi 1 and Raspberry Pi Zero
-------------------------------------

.. note::

  Because RPi 1 and RPi Zero have poor Java support and are slow devices in general, SolarThing does not officially support these devices.

Installing Java on a Raspberry Pi 1 and Raspberry Pi Zero is difficult because both of these devices have an ARMv6 architecture.
You will find that installing any version other than Java 8 does not work via ``apt-get``.
You can find Zulu's `list of OpenJDK builds here <https://www.azul.com/downloads/?architecture=arm-32-bit-hf&package=jdk#zulu>`_.
As you can see, Zulu provides ARMv6 support up to Java 11.
The simplest way to install these is to use SDKMAN, but currently there is no documentation for getting SolarThing to use an SDKMAN installation.


