Rover RS232 Port
================

So you have a Rover (or supported device) with an RS232 port?

Renogy is no longer supplying RS232 cables with their products that have RS232 ports.
RICH Solar used to sell a compatible cable undle `this link <https://richsolar.com/products/rs232-cable>`_, but it is no longer available.

That means that most people will have to create their own cable.

.. warning::
   Be careful when making your own DIY cable. Use a multimeter to isolate the 15V so you don't connect it to anything!


.. warning::
   **Don't** search amazon for RJ12 to RS232 USB. The cables you find here are **NOT** compatible with the rover.


Technical Details
-----------------

The RS232 port uses an RJ12 connector. This is commonly confused with RJ11 ports (phone lines). Although RJ11 cables are physically the same,
RJ11 cables only have 4 wires. RJ12 connectors have 6 wires. This is critcal as one of those extra wires is required.

The pin out of the cable is TX/RX/GND/GND/VCC/VCC. Note that is it possible the pin out is flipped (VCC/VCC/GND/GND/RX/TX), so you should use a multimeter to check.

There is a 15V potential across GND and VCC.


Creating your own cable
-----------------------

To create your own cable, you will need an RJ12 cable that you can strip to get the bare wires. You will also need an RS232 adapter.
Typically, an RS232 DB9 to USB cable is used. To make the connections easier to make with the DB9 port, a breakout board is recommended.

Once you know which wires on the RJ12 cable are RX, TX, and GND, you connect: 

* The RJ12's RX to the DB9's TX 
* The RJ12's TX to the DB9's RX
* GND to GND
