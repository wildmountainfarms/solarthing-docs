Installation
============

Run these commands to install SolarThing. The script will install to ``/opt/solarthing``.


.. code-block:: console

   curl https://raw.githubusercontent.com/wildmountainfarms/solarthing/master/other/linux/clone_install.sh | sudo bash
   sudo usermod -a -G solarthing,dialout,tty,video $USER
