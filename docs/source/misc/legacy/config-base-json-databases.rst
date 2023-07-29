.. _config-base-json-databases:

Config ``databases`` property of ``base.json`` (Version 2023.3.0 and before)
=================================================================================

If you are using SolarThing version 2023.4.0 or later

Now that your database of choice is fully set up and we have a ``<some database>.json`` configuration file, let's add it to our ``base.json``.

Start editing ``base.json``. Right now, it should look something like:

.. code-block:: json

    {
      //...
      "databases": [ ],
      //...
    }

Let's change it to look like this:

.. code-block:: json

    {
      //...
      "databases": [
        "config/<some database>.json"
      ],
      //...
    }

Save the file. It is set up now!
