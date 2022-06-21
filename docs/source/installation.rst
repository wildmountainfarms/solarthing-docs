Installation
============

If you choose to do so, you can install SolarThing to a different location than ``/opt``. If you do, just realize that this documentation
will refer to ``/opt/solarthing/`` instead of whatever custom location you use.


Installing
-----------

Run these commands to install SolarThing. The script will install to ``/opt/solarthing`` and will create a new ``solarthing`` user.


.. code-block:: shell

    curl https://raw.githubusercontent.com/wildmountainfarms/solarthing/master/other/linux/clone_install.sh | sudo bash
    sudo usermod -a -G solarthing,dialout,tty,video $USER

.. note::

    If you do not have ``curl`` installed, you can instead use ``wget -O - https://raw.githubusercontent.com/wildmountainfarms/solarthing/master/other/linux/clone_install.sh | sudo bash``.
    Make sure to also run the ``usermod`` command above.

.. note::

    You must have ``git`` installed on your system before running the install.

After installing and running the ``usermode`` command, you should log out and back in, for your user to have full access to the ``/opt/solarthing`` directory.

Checking if java is installed
-----------------------------

Now SolarThing has been installed. That does not mean that ``java`` has been installed. Let's check to see if ``java`` is installed now.

.. code-block:: shell

    java -version


If you got an unknown command, you need to go to :doc:`other/install-java`.


The solarthing command
----------------------

Throughout the documentation, you may see the use of the ``solarthing`` command. Even though we ran the above installation command,
it did not add the ``solarthing`` command to your ``PATH``. Adding the ``solarthing`` command to your ``PATH`` is optional, but recommended.

If you decide not to add the ``solarthing`` command to your path, just know that these are equivalent:

.. code-block:: shell

    solarthing version
    # These are equivalent
    /opt/solarthing/program/.bin/solarthing version


Adding solarthing command to your PATH
--------------------------------------

To add ``solarthing`` to your path **temporarily**, run

.. code-block:: shell

    source /opt/solarthing/other/linux/path_update.sh

To add ``solarthing`` to your PATH for your user only, edit ``~/.bash_profile`` like so:

.. code-block:: shell

    nano ~/.bash_profile
    # or if you do not have a .bash_profile
    nano ~/.bashrc

Now go to the bottom of the file and add the above command to the end of the file. Save the file.


Testing the solarthing command
------------------------------

Now that you have the ``solarthing`` command in your ``PATH``. Run

.. code-block:: shell

    solarthing version

You should get output such as 

.. code-block:: console

    pi@raspberrypi:/opt/solarthing$ solarthing version
    SolarThing made by Joshua Shannon
    Jar: solarthing-SNAPSHOT.jar
    Jar last modified: 2021-12-20T08:28:27.040Z
    Java version: 11.0.11

If you got *similar* output, continue on! The installation was successful!
