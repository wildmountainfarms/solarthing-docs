Running for the first time
================================

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

