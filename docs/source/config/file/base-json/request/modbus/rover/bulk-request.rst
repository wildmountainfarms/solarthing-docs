Rover Disable Bulk Request
=============================

The rover program has a feature enabled by default called ``bulk_request``.
This feature allows queries to the rover to be much faster than requesting each piece of data one at a time.

There are very few reasons to disable this option. One reason to disable it would be if you need to
debug errors or if you need to attempt to compare data using bulk requests and non-bulk requests to make sure they are the same.

Enabling
---------

Enabled by default, so no change is needed.

Disabling
----------

All you have to do is add ``"bulk_requeset": false`` at the same level that ``"type": "rover"`` is contained at in ``base.json``.

Let's assume you had a config like this:

.. code-block:: json

  {
    "type": "request",
    "source": "default",
    "fragment": 2,
    "unique": 30,
    "database_config": {
      "databases": [
      ]
    },
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
    "database_config": {
      "databases": [
      ]
    },
    "request": [
      {
        "type": "modbus",
        "io": "config/rover_serial.json",
        "devices": {
          "1": {
            "type": "rover",
            "bulk_request": false
          }
        }
      }
    ]
  }
