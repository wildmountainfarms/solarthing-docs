Tracer Clock Configuration
============================

The tracer has an internal clock. For SolarThing, this clock doesn't have any use. For the tracer itself, it's good to have the clock
accurate so that accumulating daily amounts (such as daily kWh) do not reset in the middle of the day.

Sync to system clock
-----------------------

Adding additional configuration to keep the clock in sync is easy:

Let's assume you had a config like this:

.. code-block:: json

  {
    "type": "request",
    "source": "default",
    "fragment": 5,
    "unique": 30,
    "databases_config": {
      "databases": [
      ]
    },
    "request": [
      {
        "type": "modbus",
        "io": "config/tracer_serial.json",
        "devices": {
          "1": {
            "type": "tracer"
          }
        }
      }
    ]
  }

To sync the Tracer's clock with the system clock, just do this:

.. code-block:: json

  {
    "type": "request",
    "source": "default",
    "fragment": 5,
    "unique": 30,
    "databases_config": {
      "databases": [
      ]
    },
    "request": [
      {
        "type": "modbus",
        "io": "config/tracer_serial.json",
        "devices": {
          "1": {
            "type": "tracer",
            "clock": {
              "threshold": "PT1M"
            }
          }
        }
      }
    ]
  }

Using a specific time zone
---------------------------

Sometimes you may want to use a timezone other than the one on the system, or maybe you just want to be explicit.

Changes this

.. code-block:: json

    {
      "threshold": "PT1M"
    }

To this:

.. code-block:: json

    {
      "threshold": "PT1M",
      "zone": "US/Mountain"
    }

Using a specific UTC offset
-----------------------------

If you don't want the tracer's clock to be set back or forward an hour each time daylight savings hits, you can use this configuration instead:

.. code-block:: json

    {
      "threshold": "PT1M",
      "offset": "-07:00"
    }

Adjusting the threshold
------------------------

You may have noticed the use of ``"threshold": "PT1M"``. That means that if the clock on the tracer is off by over 1 minute, it will be reset.
If you would like to make sure it is always within 5 seconds of the desired time, you can use ``"threshold": "PT5S"`` instead.
