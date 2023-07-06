Raspberry Pi CPU Temperature
==============================

.. note::

  This documentation is deprecated in favor of :doc:`/config/base-json/request/cpu-temperature`.


For all the programs that upload to databases, they support the ability to add the Raspberry Pi's CPU temperature
as a packet. You just have to add this json to your ``base.json``:


.. code-block:: json5

    {
      //...
      "request": [
        { "type": "rpi-cpu-temp" }
      ]
    }

Restarts your application, and you should see that CPU Temperature packets are being uploaded.


It's not working
------------------

.. note::

  This only applies to versions 2023.2.1 and before. 2023.3.0 and above is not affected by permission issues for CPU temperature measurements.

First, if you are using the systemd service, make sure that you installed it correctly and did not try to install it yourself.
If you are running SolarThing using ``./run.sh``, you should instead do ``sudo -u solarthing ./run.sh``. This is because the ``solarthing`` user
should be set up to have the group ``video``. You can make sure this is the case by running ``groups solarthing``.

