Alternatives to SolarThing
=============================

SolarThing isn't perfect. You might be able to find what you're looking for elsewhere.

.. note::

  I have not personally tested any of these libraries, so use and rely on them at your own risk.

Renogy Rover Alternatives
---------------------------

These alternatives are for Renogy Rover (SRNE like) charge controllers.
At the time of writing, these do not appear to support inverters or hybrid inverter charge controllers.

* https://github.com/corbinbs/solarshed

  * The most complete Python library for communicating with a Renogy Rover

* https://github.com/Olen/solar-monitor

  * Designed to work WITH a Bluetooth Module, rather than a USB to serial cable

* https://github.com/logreposit/renogy-rover-reader-service

  * Written in Kotlin
  * Available `on Dockerhub <https://hub.docker.com/r/logreposit/renogy-rover-reader-service/tags>`_

* https://github.com/menloparkinnovation/renogy-rover

  * Written in JavaScript

* https://github.com/floreno/renogy-rover-modbus

  * Written in JavaScript

* https://github.com/CyberRad/CoopSolar

  * Simple Python script

* https://github.com/amigadad/SolarDataCollection

  * Based off of solarshed, but supports more parameters

Tracer Alternatives
---------------------

* https://github.com/kasbert/epsolar-tracer

Outback MATE Alternatives
----------------------------

These alternatives are for the Outback MATE 1 and MATE 2.

* https://github.com/jorticus/pymate

  * `matecom.py <https://github.com/jorticus/pymate/blob/master/pymate/matecom.py>`_ does a similar thing to SolarThing
  * Most of this library is designed to emulate an Outback MATE to communicate with devices using Outback proprietary protocol.

    * If you use these features of this library, a MATE is not actually required.
