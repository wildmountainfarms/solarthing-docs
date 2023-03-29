Actions
===========

Actions are a part of SolarThing's more advanced configuration.
Actions can be configured using ActionLang, which can be specified using NotationScript or raw JSON (legacy).

NotationScript
----------------

Before you can understand how ActionLang works, you need to understand what NotationScript is.
NotationScript, in its simplest form, is a format to describe data, similar to JSON.
Using NotationScript to program ActionLang is preferred over JSON because NotationScript is designed to be shorthand for JSON.

.. code-block:: json

  {
    "type": "print",
    "message": "Hello there"
  }

In NotationScript you could instead have something like this:

.. code-block::

  print "Hello there"

In the above example, ``print "Hello there"`` is a node. ``print`` is the name of the node and ``"Hello there"`` is an argument of that node.
In the case of the ``print`` node, ActionLang is configured to use the node's first argument as the argument to ``"message"``.

In other words, you can effectively "compile" NotationScript to JSON.
In fact, that's what it's designed for at its core.
NotationScript is just shorthand for writing JSON.

.. note:: 

  The above is an example that is specific to ActionLang, but NotationScript itself is just a format.
  The behavior for a node ``print "Hello there"`` is not strictly defined to result in the JSON shown above.


ActionLang
------------

ActionLang is usually described in NotationScript format, but can also be described using raw JSON (deprecated).
Before explaining how to write ActionLang programs, we need to explain the concept of actions.

An action does something when it is run. Some actions may finish immediately, other actions may take time until they are "done".
For instance, the ``print`` and ``log`` actions are done immediately after running, but a ``wait`` action does not finish immediately.

ActionLang has many built-in actions to help describe the order actions are executed in or if they are executed in parallel.
Maybe one action ending will cause the start of another.
Here are some examples that **are not specific to SolarThing** that show how ActionLang can be used.

A simple program
^^^^^^^^^^^^^^^^^^

This program aims to show how simple ActionLang can be.

.. code-block::

  // queue is a type of action that takes a list of actions and executes those actions in sequence.
  queue {
    print "Hello there"
    // These are the same
    print("Hello there")

    // When passing an argument to a node without parenthesis, if you do not quote that argument it will be interpreted as a string.
    print Hello

    // parallel is a type of action that takes a list of actions and executes those actions in parallel
    parallel {
      queue {
        // The wait action takes an ISO-8601 duration as its argument. 
        //   The action is effectively a timer, and becomes done once the given duration is up
        wait PT5S
        print "5 seconds are up!"
      }
      queue {
        wait PT10S
        print "10 seconds are up!"
      }
    }
  }


Notice that in the outer most block, there is only a single action: ``queue``.
Inside of the ``queue`` action are other actions.
As you see above, depending on the action, you can nest actions inside of actions to get the behavior you want.

You can run this simple program using ``solarthing action file_name.ns``. 
(Or docker: ``cat config_templates/actions-ns/simple_program.ns | docker run -i --rm ghcr.io/wildmountainfarms/solarthing action -``)
The result is this:

.. code-block::

  Hello there
  Hello there
  Hello
  5 seconds are up!
  10 seconds are up!

Normally you won't ever use the ``solarthing action`` command, but it can be a useful tool for understanding ActionLang.
If you run the program on your own machine, you would see that the line ``x seconds are up!`` are run after 5 and 10 seconds respectively.
The simplicity of ActionLang allows for simple and complicated sequences of instructions over time.

The race action
^^^^^^^^^^^^^^^^

The ``race`` action is one of the most powerful actions in ActionLang.
It can be used like an if statement, or as a statement to only do one thing depending on what action is done first.

.. code-block::

  race {
    racer(wait PT5S) : print "5 seconds won!"
    racer(wait PT10S) : print "10 seconds won!"
  }

In the above example, you have two actions competing to "win" the race (``wait PT5S`` and ``wait PT10S``).
The ``wait PT5S`` action will finish first so its corresponding action (``print "5 seconds won!"``) will be executed.
There are many creative uses for the ``race`` action that you might not think of initially. Take this example:

.. code-block:: 

  race {
    racer(perform-some-action-that-takes-time) : pass
    racer(PT30S) : print "Timed out!"
  }

In the above example, ``perform-some-action-that-takes-time`` takes some time to complete, 
and there is a chance that performing that action may never finish.
If the action finishes within 30 seconds, the ``pass`` action will be run, which is a placeholder for doing nothing and being done immediately.
If the action does not finish within 30 seconds, the action will be forcefully ended and the ``print "Timed out!"`` action will be run.

You can also use the race action as an if statement.

.. code-block::

  race {
    racer(is-complete) : do-something
    racer(pass) : do-something-else
  }

In the above example, we assume that ``is-complete`` is either done or is not done.
If ``is-complete`` is done (true), then ``do-something`` is executed.
If ``is-complete`` is not done, then ``pass`` is checked to see if it is done.
Since ``pass`` is always done immediately, ``do-something-else`` would be run in this case.
