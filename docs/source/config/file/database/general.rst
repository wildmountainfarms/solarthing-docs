General Database Configuration
===============================

This page documents the common format of database configurations such as the ``settings`` object that is part of a database configuration.

.. todo::

  Complete this page

.. _config-database-settings:

``settings``
------------

The settings object of a database configuration has a couple of properties that help determine how frequently data should be uploaded to this database.

* ``inherit`` (boolean) (default true) - This property determines whether the settings should be inherited from the ``external`` database configuration (if provided)
* ``packet_upload`` (frequency settings) - Determines how often packets should be uploaded to this database
* ``command_download`` (frequency settings) - Determines how often commands should be downloaded from this database (This configuration will be ignored for all non-CouchDB database types)

Frequency Settings
^^^^^^^^^^^^^^^^^^

A frequency settings object has parameters that determine how often the database should be used for a particular task.

* ``throttle_factor`` (integer) (default 1)
* ``initial_skip`` (integer) (default 0)
