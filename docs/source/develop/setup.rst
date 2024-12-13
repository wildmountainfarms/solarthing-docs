Developer Setup
==================

Developing SolarThing does not require an IDE, but it is highly recommended.
Typically IntelliJ Idea is used. To install it, you should first install JetBrains Toolbox
to make its installation and updating easier: https://www.jetbrains.com/toolbox-app/.

When compiling the majority of SolarThing, the only thing that is required is Java 11 or higher to be installed.
Installing Java on your developer machine is the same as installing it on the machine that is running SolarThing.
You can go here to learn how to install it: doc:`/software/java`.
Alternatively, you can use SDKMAN to install Java only for developing SolarThing: https://sdkman.io/install.

Cloning SolarThing
--------------------

When SolarThing is installed on a device such as a Raspberry Pi, it is typically installed in the ``/opt`` directory.
When developing SolarThing, you should install it in a different directory. Typically you can do something like this:

.. code-block:: console

    $ mkdir ~/workspace/
    $ cd ~/workspace/
    $ git clone https://github.com/wildmountainfarms/solarthing

If you want to make commits, I recommend that you `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_ it
and clone your own, forked, repository instead of cloning ``https://github.com/wildmountainfarms/solarthing``.

To see if you can compile the main SolarThing jar, you can run this in your terminal:

.. code-block:: shell

    ./compile_and_move.sh

Open in IntelliJ
---------------------

File -> Open, then navigate to the place where you cloned ``solarthing``.

Installing Java
------------------

You need Java 21 to build SolarThing. You may install it however you please. I recommend the following:

.. code-block:: shell

  # Install Eclipse Temurin 21
  sdk install java 21-tem

Further Setup for server and web module
------------------------------------------

The server module depends on the ``web`` module, which contains a React application.
This React application requires ``npm`` and ``node`` to be installed on your system. A tool commonly used to install and
manage the these commands command is nvm, which can be installed here: https://github.com/nvm-sh/nvm#install--update-script.
Once ``nvm`` is installed, you can use it to install like so:

.. code-block:: shell

    # Install Node 16 (which will automatically install a recent npm version as well)
    nvm install 16

Then you can check the versions of the tools you just installed. You should get outputs similar to these:

.. code-block:: console

    $ node --version
    v16.15.1
    $ npm --version
    8.11.0

Now you must install the ``web`` module's dependencies before being able to compile it:

.. code-block:: shell

    cd web/
    npm install
    cd ../

You can now compile SolarThing Server:

.. code-block:: shell

    ./server_compile_and_move.sh

.. note::

    If you already have a gradle daemon running, you need to kill using ``./gradlew --stop`` before compiling.
    If you don't, you may get an error such as ``> A problem occurred starting process 'command 'npm''``, which indicates
    that gradle cannot find the ``npm`` command.

Running SolarThing Server from IntelliJ
---------------------------------------------------------------------------------

Once the above steps are completed, it is typically easier to run straight from IntelliJ, rather
than running the jar file that is generated using ``./server_compile_and_move.sh``.
You can do this by going to the right side of IntelliJ and opening up the Gradle tab.
Under the ``server`` module, expand ``Tasks``, expand ``application``, then double click ``bootRun``.

Configuring SolarThing Server
--------------------------------------------------------

No matter how you run Solarthing Server, you must configure it. You might have a ``couchdb.json`` file already created.
If you don't already have that file placed in ``program/config``, you can place it there.
Then, create a new file in ``program/graphql/config`` named ``application.properties``. Paste this line in:

.. code-block::

    solarthing.config.database=../config/couchdb.json

You should now be able to run SolarThing Server without errors by running the ``bootRun`` task.
Navigate to http://localhost:8080 to see if it successfully connects to your CouchDB instance and shows some data.

Testing the Main SolarThing Program
-------------------------------------

Running the main SolarThing program should be done just like normal when developing.
You will compile it using ``./compile_and_move.sh``. If you want to run it on your computer, great, go for it!
If you want to run it on another device, you can use the ``./copy_jar.sh`` command like: ``./copy_jar.sh pi@myipaddress``.
It will prompt for a password unless you have SSH Public Key authentication set up on your device.
