Frequently Asked Questions
==========================


Can SolarThing run on an Arduino?
---------------------------------

No. SolarThing uses Java, which does not run on an Arduino.


(Rover) Can SolarThing communicate over Bluetooth?
--------------------------------------------------

No. There is a possiblity of support in the future, but it is unlikely. See :issue:`125`.


(Rover) Can a Bluetooth module be connected while SolarThing is running?
------------------------------------------------------------------------

No. Most renogy devices have a single comm port. When the comm port is connected to the device SolarThing is running on, the Bluetooth module cannot be connected.
It is unknown if this holds true for the few Renogy devices that have two comm ports.


