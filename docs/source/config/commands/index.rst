Configuring Commands
=====================

The ``mate`` and ``request`` program have the ability to accept commands from CouchDB.
Commands can be sent from SolarThing Android and from the Slack chatbot.

.. note::

    Documentation for setting up commands is lacking. You will likely have to ask on :issue-page:`our issue page <>` for help.

Setting up commands requires a few things:

* Configurating in the ``mate`` or ``request`` programs
* SolarThing Android or Slack chatbot to be setup
* Editing the ``authorized`` document in the ``solarthing_closed`` database in CouchDB

This page only helps you with configuration in the ``mate`` or ``request`` programs, so it is incomplete in that regard.

Creating a basic action
------------------------

Commands are requests from a client that, once authenticated and validated, trigger the execution of an action.
Actions can do any number of things (the JSON configuration for actions is turing complete), but for now we'll focus on a very basic action.

For a rover, let's use this action:

.. code-block:: json

    {
      "type": "roverload",
      "on": true
    }

For a Tracer or Mate, you can look here: :tree:`master/config_templates/actions` for examples.

Go ahead and save that JSON to a file in a directory such as ``/opt/solarthing/program/<YOUR DIRECTORY>/config/`` named something like ``load_on.json``.
(Choose a more appropriate name if it does something different).

Now in your ``base.json`` file, edit it like so (add the ``commands`` field):

.. code-block:: json5

    {
      //...
      "commands": [
        {
          "name": "ROVER LOAD ON",
          "display_name": "Rover Load On",
          "description": "Turns the load on the rover",
          "action": "config/load_on.json",
        }
      ]
    }

We also need to edit another part of our ``base.json`` to tell the command what rover it belongs to.

.. note::

    This is not necessary for the ``mate`` program, as there is always only a single MATE


.. code-block:: json5

    {
      //...
      "request": [
        {
          "type": "modbus",
          "io": "config/rover_serial.json",
          "devices": {
            "1": {
              "type": "rover",
              "commands": "ROVER LOAD ON"
            }
          }
        }
      ],
      //...
    }

Now the rover and the command are "linked" together.


Now restart the program and make a request! (Yeah I still need to add documentation on that).
