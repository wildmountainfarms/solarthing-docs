Installation
============

Run these commands to install SolarThing. The script will install to ``/opt/solarthing``.


.. code-block:: console

   curl https://raw.githubusercontent.com/wildmountainfarms/solarthing/master/other/linux/clone_install.sh | sudo bash
   sudo usermod -a -G solarthing,dialout,tty,video $USER


Now SolarThing has been installed. That does not mean that ``java`` or CouchDB have been installed. Let's check to see if ``java`` is installed now.

.. code-block:: console

   java -version


If you got an unknown command, you need to install Java.
