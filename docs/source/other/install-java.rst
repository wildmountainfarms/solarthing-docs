Install Java
============

So you need to install Java to your system?

* https://pi4j.com/documentation/java-installation/
* https://forums.raspberrypi.com//viewtopic.php?p=1308846


Required Version
----------------

SolarThing requires Java >= 8 and SolarThing GraphQL requires Java >= 11. If you are able to install Java 11, you should do so.


Install on Systems with Apt
---------------------------

The ``apt-get`` or ``apt`` command is used to install most software. To install Java 11, run this command:


.. code-block:: shell

    sudo apt-get update
    sudo apt-get install -y openjdk-11-jdk-headless

