Docker Install
===============

If you are doing a Docker install, you can choose where you would like to place your configuration files.
You must also have `docker installed <https://docs.docker.com/desktop/install/linux-install/>`_.

Throughout the tutorials here, you will find yourself running many ``docker run`` commands.
When you finally are ready to configure SolarThing, you will end up writing a ``docker-compose.yml`` file.

Testing ``docker run``
-----------------------

To make sure you are ready for future steps in the tutorial, run this command:

.. code-block:: shell

  docker run ghcr.io/wildmountainfarms/solarthing version

You should get output similar to:

.. code-block:: console

  pi@solarpi:~$ docker run ghcr.io/wildmountainfarms/solarthing version
  SolarThing made by Lavender Shannon
  Jar: solarthing.jar
  Jar last modified: 2023-07-02T18:21:48Z
  Java version: 19.0.2

Creating your configuration directory
--------------------------------------

To make sure you can configure SolarThing easily, you should determine what directory you would like to use to contain your configuration.
You may choose to put SolarThing config in a place such as ``~/Documents/solarthing-config`` or even in a place like ``/opt/solarthing-config``.
It is recommend to put SolarThing configuration somewhere in your home directory so that your user has permission to edit the configuration without sudo.

For the purpose of this tutorial, I will choose ``~/Documents/solarthing-config``.
Since we are choosing that location, it should also have a folder named config nested inside it.
We will now create a ``docker-compose.yml`` file so that when we configure SolarThing in future steps we can easily run and test it.

.. note::

  In this example we are creating a subfolder of ``solarthing-config`` called main.
  This ``main`` folder should house the all of the files for a given SolarThing instance.
  If you would like, you can use a name other than ``main`` such as ``rover`` or ``mate``,
  as long as it makes sense to you and the program you plan to run.

.. code-block:: shell

  mkdir -p ~/Documents/solarthing-config/main/{config,logs}
  cd ~/Documents/solarthing-config/
  nano docker-compose.yml

At this point you should be editing ``docker-compose.yml``.
Place this inside your file:

.. code-block::

  version: '3.7'

  services:
    solarthing-main:
      image: 'ghcr.io/wildmountainfarms/solarthing:latest'
      container_name: solarthing-main
      restart: 'unless-stopped'
      command: run --base config/base.json
  #    group_add: # this is only necessary if you are using a user other than root
  #      - dialout
  #    cap_add:
  #      - SYS_RAWIO
  #    devices:
  #      - '/dev/ttyUSB0:/dev/ttyUSB0'
      volumes:
        - './main/config:/app/config:ro'
        - './main/logs:/app/logs'

.. note::

  When running this, SolarThing will write logs files to the log directory using root:root permission
  (unless you change the user running SolarThing or do not mount the logs directory).

.. TODO we should link to a place talking about how to set the user that runs SolarThing here

Now run ``sudo docker compose up``.
The program should crash with output similar to this:

.. code-block::

  solarthing  | 2023-07-12 04:32:40.939 [main] INFO  me.retrodaredevil.solarthing.program.SolarMain - [LOG] Beginning main. Jar: Jar: solarthing.jar Last Modified: 2023-07-12T04:29:54Z Java version: 19.0.2
  solarthing  | [stdout] Beginning main. Jar: Jar: solarthing.jar Last Modified: 2023-07-12T04:29:54Z Java version: 19.0.2
  solarthing  | [stderr] Beginning main. Jar: Jar: solarthing.jar Last Modified: 2023-07-12T04:29:54Z Java version: 19.0.2
  solarthing  | 2023-07-12 04:32:40.990 [main] INFO  me.retrodaredevil.solarthing.program.SolarMain - Using base configuration file: config/base.json
  solarthing  | 2023-07-12 04:32:40.990 [main] ERROR me.retrodaredevil.solarthing.program.SolarMain - (Fatal)Base configuration file does not exist!
  solarthing exited with code 0

Now you are ready to continue!
Head over to :ref:`after-install`.
