Configuration
=====================

Now that you know the path to your serial port and the modbus address, it's time to get configuring!

Click on the configuration below for whichever type of device you have.

.. toctree::
   :caption: Configuration

   rover/config
   mate/config
   tracer/config

Running for the first time
--------------------------

Now that you have some configuration, it's time to run it. The above configuration should have had you either create a directory
or use a particular directory for configuration. Let's change our directory to that now if you aren't already there.


.. code-block:: shell

    cd /opt/solarthing/program/<THE DIRECTORY YOU USED IN PREVIOUS STEPS>

OK, now our shell should look something like this (``custom_rover`` may be different):

.. code-block:: console

    pi@raspberrypi:/opt/solarthing/program/custom_rover$ 

Now, all we have to do is run this:

.. code-block:: shell
    
    sudo -u solarthing ./run.sh

.. note:: The ``sudo -u solarthing`` is optional, but recommended. You can simply do ``./run.sh`` if you would like.

The program should start up and it will start outputting lots of messages to your screen. If you configured it correctly, after a second you will see
data from your device in a JSON format. Press ``CTRL+C`` to stop the program.


Configuring a database
-------------------------

OK, now the program is working! However, right now the only thing the program is doing is showing us data. We want to upload the data to a database.

If you don't already know which database you want to set up, take a look at :doc:`database-and-display`.

.. toctree::
   :maxdepth: 1
   :caption: Databases

   config/couchdb


.. _configuration-continued:

Configuration Continued
-------------------------

Now that you have edited your ``base.json`` with a new database, give the program a run again:

.. code-block:: shell
    
    sudo -u solarthing ./run.sh

You should see similar output from before, but there may also be additional messages saying that data is being uploaded to a database.


Install systemd service
-------------------------

Running ``./run.sh`` ourselves is great and all, but we want SolarThing to run if the device restarts or if we logout.

To install the systemd service, run this command:

.. code-block:: shell

    sudo /opt/solarthing/other/system/install.sh <NAME OF YOUR DIRECTORY HERE>

If you configured a rover, you can likely replace ``<NAME OF YOUR DIRECTORY HERE>`` with ``custom_rover`` like so:

.. code-block:: shell

    sudo /opt/solarthing/other/system/install.sh custom_rover

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