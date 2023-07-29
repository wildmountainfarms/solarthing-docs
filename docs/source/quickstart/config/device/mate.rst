MATE Configuration
==================

Documentation for configuring the ``mate`` program to monitor a MATE 1 or MATE 2.

.. tabs::

  .. code-tab:: shell Docker Install

    cd <your directory that contains docker-compose.yml>/<mate or main or whatever you called it>

  .. code-tab:: shell Native Install

    cd /opt/solarthing/program/mate


We will now begin editing a file called ``base.json`` in the ``config`` directory.

.. code-block::

  nano config/base.json

Paste this into the file:

.. code-block::

  {
    "type": "mate",
    "source": "default",
    "fragment": 1,
    "unique": 60,
    "databases_config": {
      "databases": [
      ]
    },
    "io": "config/mate_serial.json"
  }

Save the file. Now we need to create another file:


.. code-block:: shell

    nano config/mate_serial.json

You'll notice it has the same name as the ``"io"`` property in ``base.json``. We are now configuring the path to the serial port.

You can paste this into the file:


.. code-block:: json

  {
    "type": "serial",
    "port": "/dev/ttyUSB0"
  }

Depending on the path to your serial port, you may need to change ``"/dev/ttyUSB0"`` to something different.


Go to :doc:`../configuration-running`.
