Welcome to SolarThing's documentation!
======================================

**SolarThing** is an application that can monitor data from a variety of solar charge controllers and inverters.

This documentation is targetted at people who have Raspberry Pis or any Debian based operating system.
However, SolarThing can run on any OS.

The primary purpose of SolarThing is to get data and upload it to a database. Using CouchDB allows for the best SolarThing
experience, but InfluxDB can also be used. CouchDB can run on Raspberry Pis >= 3, but using a separate computer or server for
CouchDB is recommended.

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This documentation is incomplete for the time being. Documentation is being migrated here from https://github.com/wildmountainfarms/solarthing


Contents
--------

.. toctree::

   installation
   usage
   api
