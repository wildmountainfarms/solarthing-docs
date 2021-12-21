Welcome to SolarThing's documentation!
======================================

**SolarThing** is an application that can monitor data from a variety of solar charge controllers and inverters.

This documentation is targetted at people who have Raspberry Pis or any Debian based operating system.
However, SolarThing can run on any OS.

The primary purpose of SolarThing is to get data and upload it to a database. Using CouchDB allows for the best SolarThing
experience, but InfluxDB can also be used. CouchDB can run on Raspberry Pis >= 3, but using a separate computer or server for
CouchDB is recommended.

To install, checkout :doc:`installation`.

.. note::

   This documentation is incomplete for the time being. Documentation is being migrated here from https://github.com/wildmountainfarms/solarthing


Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Start

   supported-products
   database-and-display
   installation
   serial-ports
   solarthing-check
   configuration
   faq
   updating


.. toctree::
   :maxdepth: 1
   :caption: External Installs
   
   external/install-java
   external/install-couchdb
