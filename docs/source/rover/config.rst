Rover Configuration
===================

Documentation for configuring SolarThing to monitor.

First, run these commands:


.. code-block:: console

    cd /opt/solarthing/program/
    ./create_custom.sh custom_rover
    cd custom_rover/config

That command will create a directory for you to put your configuration in. You may notice there are other directories in ``/opt/solarthing/program``.
In previous SolarThing versions, those were the recommended directories to place configuration files. This is no longer the case.

That you are in the ``/opt/solarthing/program/custom_rover/config/`` directory, it's time to create a configuration file. You can use your editor of choice.
For simplicity, the examples use ``nano``.

.. code-block:: console

    nano base.json

The name ``base.json`` is important. It is possible to use a different file name, but is not recommended.

You can now paste this into the file:


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


We will go over what all of this configuration means later, but for now let's focus on ``"1"``. That represents the address of the modbus device.
1 is typically the address, but it can sometimes be 10, 16, or a different number. The deprecated rover-setup program has a feature to scan for the address.
I will eventually add documentation for finding your Modbus address. `#26 <https://github.com/wildmountainfarms/solarthing/issues/26>`_ and `#29 <https://github.com/wildmountainfarms/solarthing/issues/29>`_ are cases of people having this issue.

Save the file. Now we need to create another file:


.. code-block:: console

    nano rover_serial.json

You'll notice it has the same name as the ``"io"`` property in ``base.json``. We are now configuring the path to the serial port.

You can paste this into the file:


.. code-block:: json

    {
      "type": "serial",
      "port": "/dev/ttyUSB0"
    }

Depending on the path to your serial port, you may need to change ``"/dev/ttyUSB0"`` to something different.

Now change your directory to continue to test your new configuration:

.. code-block:: console

    cd ..
    # OR
    cd /opt/solarthing/program/custom_rover/

