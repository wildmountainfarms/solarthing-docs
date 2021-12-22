MATE Configuration
==================

Documentation for configuring the ``mate`` program to monitor a MATE 1 or MATE 2.

Let's `cd` into `/opt/solarthing/program/mate/config` and begin configuring!

.. code-block::

    cd /opt/solarthing/program/mate/config

We will now begin editing a file called ``base.json``.

.. code-block::

    nano base.json

Paste this into the file:

.. code-block::

    {
      "type": "mate",
      "source": "default",
      "fragment": 1,
      "unique": 60,
      "databases": [ ],
      "io": "confif/mate_serial.json"
    }

Save the file. Now we need to create another file:


.. code-block:: shell

    nano mate_serial.json

You'll notice it has the same name as the ``"io"`` property in ``base.json``. We are now configuring the path to the serial port.

You can paste this into the file:


.. code-block:: json

    {
      "type": "serial",
      "port": "/dev/ttyUSB0"
    }

Depending on the path to your serial port, you may need to change ``"/dev/ttyUSB0"`` to something different.

Now change your directory to continue to test your new configuration:

.. code-block:: shell

    cd ..
    # OR
    cd /opt/solarthing/program/mate



Go to :doc:`../configuration-running`.
