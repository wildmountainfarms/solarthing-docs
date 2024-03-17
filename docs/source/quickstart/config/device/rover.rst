Rover Configuration
===================

Documentation for configuring SolarThing to monitor a Renogy Rover (or supported product).

First, run these commands:

.. tabs::

  .. code-tab:: shell Docker Install

    cd <your directory that contains docker-compose.yml>/<rover or main or whatever you called it>

  .. code-tab:: shell Native Install

    cd /opt/solarthing/program/
    ./create_custom.sh custom_rover
    cd custom_rover/

Now it's time to create a configuration file. You can use your editor of choice.
For simplicity, the examples use ``nano``.

.. code-block:: shell

  nano config/base.json

The name ``base.json`` is important. It is possible to use a different file name, but is not recommended.

You can now paste this into the file:


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


We will go over what all of this configuration means later, but for now let's focus on ``"1"``. That represents the address of the modbus device.
If the address is not ``1``, you should know the correct address from :ref:`devices-not-detected`.

Save the file. Now we need to create another file:


.. code-block:: shell

  nano config/rover_serial.json

You'll notice it has the same name as the ``"io"`` property in ``base.json``. We are now configuring the path to the serial port.

You can paste this into the file:


.. code-block:: json

  {
    "type": "serial",
    "port": "/dev/ttyUSB0"
  }

Depending on the path to your serial port, you may need to change ``"/dev/ttyUSB0"`` to something different.

Go to :doc:`../configuration-running`.
