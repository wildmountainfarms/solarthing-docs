Frequently Asked Questions
==========================


Can SolarThing run on an Arduino?
---------------------------------

No. SolarThing uses Java, which does not run on an Arduino.

Is there an ISO image I can install to my Pi to have everything set up?
------------------------------------------------------------------------

No. See enhancement issue: :issue:`79`.


Rover Questions
---------------

Can SolarThing communicate over Bluetooth?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. There is a possibility of support in the future, but it is unlikely. See :issue:`125`.


Can a Bluetooth module be connected while SolarThing is running?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Most renogy devices have a single comm port. When the comm port is connected to the device SolarThing is running on, the Bluetooth module cannot be connected.
It is unknown if this holds true for the few Renogy devices that have two comm ports.

Is my hybrid inverter/solar charge controller supported?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. See :issue:`137`.

Where can I buy a serial adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There's not a good place to buy a cable.
You will likely have to make a cable: :doc:`/quickstart/serial-port/hardware/rover/rs232-port` or :doc:`/quickstart/serial-port/hardware/rover/rs485-port`.

I have the config server set up. I set the battery type to user. Why can't I change some parameters?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The rover's battery type is a little bit weird.
In my experience, you cannot programmatically set the battery type to user/self-customized and have it be in an "unlocked state".
To get this "unlocked state", you must physically change the battery type on your charge controller,
then you should be able to programmatically change parameters via the configuration server.

Tracer Questions
-------------------

I have the config server set up. Why can't I change some parameters?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In my experience, the tracer does not allow its charging parameters to be changed.
You are likely out of luck.


