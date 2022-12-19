Configuration Server
=====================

The rover and tracer programs have the ability to host a small server that can be accessed using a tool such as netcat (``nc``).
These servers are by default bound to ``localhost``, so only those on the device itself can access it.
Enabling this feature can allow you to set parameters on your charge controller and read parameters, all while SolarThing is running normally.

Enabling
-----------

Let's assume you had a config like this:

.. code-block:: json

    {
      "type": "request",
      "source": "default",
      "fragment": 2,
      "unique": 30,
      "databases": [ ],
      "request": [
        {
          "type": "modbus",
          "io": "config/rover_serial.json",
          "devices": {
            "1": {
              "type": "rover"
            }
          }
        }
      ]
    }

You can simply change it to:

.. code-block:: json

    {
      "type": "request",
      "source": "default",
      "fragment": 2,
      "unique": 30,
      "databases": [ ],
      "request": [
        {
          "type": "modbus",
          "io": "config/rover_serial.json",
          "devices": {
            "1": {
              "type": "rover",
              "server": { "port": 5051 }
            }
          }
        }
      ]
    }

The above configuration will create a server that listens on port ``5051``.


Connecting using netcat
--------------------------

If you have a server configured to run on port ``5051``, simply run this command:

.. code-block:: shell

    nc localhost 5051

Once you run that command, you should be able to start typing commands. You can type the battery voltage command, and you should get a response back within 5 seconds like so:

.. code-block:: console

    pi@raspberrypi:/opt/solarthing/program/custom_rover $ nc localhost 5051
    batteryVoltage
    24.5

Rovers and Tracers support different fields to query.

Changing paramters of a rover
------------------------------

If you have a rover, here is an example of some of the fields you can change and some values you might change them to:

.. code-block::

    underVoltageWarningLevelRaw     112
    dischargingLimitVoltageRaw      110
    overDischargeRecoveryVoltageRaw 112
    overDischargeTimeDelaySeconds   120

    boostChargingVoltageRaw         149
    boostChargingRecoveryVoltageRaw 120
    boostChargingTimeMinutes        110

    equalizingChargingVoltageRaw    151
    equalizingChargingTimeMinutes   130
    equalizingChargingIntervalDays    0

    floatingChargingVoltageRaw      136

    chargingVoltageLimitRaw         154
    overVoltageThresholdRaw         156

You can see all the methods with the ``@JsonSetter`` annotation to see other possibilities here: :blob:`master/core/src/main/java/me/retrodaredevil/solarthing/solar/renogy/rover/RoverWriteTable.java`.

Changing parameters of a tracer
---------------------------------

If you have a tracer, here is an example of some of the fields you can change and some values you might change them to:

.. code-block::

    equalizationChargingCycleDays 0

    batteryTemperatureWarningUpperLimit 35.0
    batteryTemperatureWarningLowerLimit 3.0

    insideControllerTemperatureWarningUpperLimit 60.0
    insideControllerTemperatureWarningUpperLimitRecover 55.0

    powerComponentTemperatureWarningUpperLimit 60.0
    powerComponentTemperatureWarningUpperLimitRecover 55.0

    nightPVVoltageThreshold 18.0
    dayPVVoltageThreshold 20.0

    isLoadOnByDefaultInManualMode false
    equalizeDurationMinutes 120
    boostDurationMinutes 90


You can see all the methods with the ``@JsonSetter`` annotation to see other possibilities here: :blob:`master/core/src/main/java/me/retrodaredevil/solarthing/solar/tracer/TracerWriteTable.java`.
Note that many of the fields relating to the battery setpoints are not configurable on many models.
