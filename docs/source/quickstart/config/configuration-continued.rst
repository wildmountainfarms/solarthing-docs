Configuration Continued
==========================


Install systemd service
-------------------------

Running ``./run.sh`` ourselves is great and all, but we want SolarThing to run if the device restarts or if we logout.

To install the systemd service, run this command:

.. code-block:: shell

    sudo /opt/solarthing/other/systemd/install.sh <NAME OF YOUR DIRECTORY HERE>

If you configured a rover, you can likely replace ``<NAME OF YOUR DIRECTORY HERE>`` with ``custom_rover`` like so:

.. code-block:: shell

    sudo /opt/solarthing/other/systemd/install.sh custom_rover

If it was successful, you should see a message ``Reloaded systemctl``.

Starting systemd service
-------------------------

You have now installed the systemd service. The name of that service is the format: ``solarthing-<NAME OF YOUR DIRECTORY HERE>``. So to start it, you may run:

.. code-block:: shell

    sudo systemctl start solarthing-custom_rover

That starts SolarThing in the background. It should be running now! If you restart your device, SolarThing won't start running.
To enable it so that it starts on reboot, run this:

.. code-block:: shell

    sudo systemctl enable solarthing-custom_rover


Next, you probably want to view your data: :doc:`/quickstart/data/index`.
