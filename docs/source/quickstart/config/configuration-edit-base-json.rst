Edit ``base.json`` for a database
===================================

.. note::

  See also :ref:`config-base-json-databases` if you need configuration documentation for older SolarThing versions.

Now that your database of choice is fully set up and we have a ``<some database>.json`` configuration file, let's add it to our ``base.json``.

Start editing ``base.json``. Right now, it should look something like:

.. code-block:: json5

    {
      //...
      "databases_config": {
        "databases": [
        ]
      }
      //...
    }

Let's change it to look like this:

.. code-block:: json5

    {
      //...
      "databases_config": {
        "databases": [
          {
            "external": "config/<some database>.json"
          }
        ]
      }
      //...
    }

Save the file. It is set up now!



Run it again
==============

Now that you have edited your ``base.json`` with a new database, give the program a run again:

.. code-block:: shell

    sudo -u solarthing ./run.sh

You should see similar output from before, but there may also be additional messages saying that data is being uploaded to a database.
