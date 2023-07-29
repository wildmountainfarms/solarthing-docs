System Stability
==================

Once you get SolarThing running, you probably want it to stay running without any interference from you. Some of these can help your system stay stable.


Add Weekly Restarts
-----------------------

Reboots can help keep your system healthy. SolarThing comes with a script to add a weekly restart at 01:30 on Mondays:

.. code-block:: shell

    sudo /opt/solarthing/other/linux/add_weekly_restart.sh


Add a Watchdog
------------------

Watchdogs can help detect if your system is frozen, then restart the system.

I could go into detail on how to enable it on Raspberry Pis, but there are plenty better tutorials than I could make such as this one: 
https://medium.com/@arslion/enabling-watchdog-on-raspberry-pi-b7e574dcba6b or https://diode.io/raspberry%20pi/running-forever-with-the-raspberry-pi-hardware-watchdog-20202/


Use a good SD Card
----------------------

If you have a Raspberry Pi, you are either using a micro SD card or have set it up to boot off a USB Drive.
If you are using a micro SD card, you should do research to make sure it is a high quality SD card.
Low quality, cheap SD cards may fail after long periods of running. Using a SD card with more space
than you need is also a good way to prevent problems.


Serial Port Stability
----------------------

If you disconnect and reconnect your serial port, or if its connection isn't perfect, don't worry!
If SolarThing fails to communicate with your device enough times, it will attempt to reconnect the serial port.
