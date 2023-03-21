Updating
==========

SolarThing gets updates every once in a while, and when it does, you will want to update. You can see updates here: https://github.com/wildmountainfarms/solarthing/releases

If you notice an update, run these commands to get it:

.. code-block:: shell

    cd /opt/solarthing
    git pull
    program/download_solarthing.sh
    # Or instead use this if you are running SolarThing Server
    program/graphql_download_solarthing.sh

Once you have done that, you can restart SolarThing. One would typically restart SolarThing like so:


.. code-block:: shell

    sudo systemctl restart solarthing-<NAME OF YOUR DIRECTORY HERE>

If you have multiple SolarThing instances running, or don't remember the name of the ones you have running, you can run this to restart all of them:

.. code-block:: shell

    sudo systemctl restart solarthing-*

It's a good idea to make sure they are all running:

.. code-block:: shell

    systemctl status solarthing-*


Permission Issues
--------------------

If you got errors while trying to update, run these commands:

.. code-block:: shell

    sudo other/linux/create_user.sh
    sudo other/linux/update_perms.sh
    sudo usermod -a -G solarthing,dialout,tty,video,gpio $USER
    # Or use this if you don't need the gpio (if your system doesn't have the gpio group)
    sudo usermod -a -G solarthing,dialout,tty,video $USER
