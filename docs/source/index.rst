Welcome to SolarThing's documentation!
======================================

**SolarThing** is an application that can monitor data from a variety of solar charge controllers and inverters.
Code and issues available at https://github.com/wildmountainfarms/solarthing.

This documentation is targetted at people who have Raspberry Pis or any Debian based operating system.
However, SolarThing can run on any OS.

The primary purpose of SolarThing is to get data and upload it to a database. Using CouchDB allows for the best SolarThing
experience, but InfluxDB can also be used. CouchDB can run on Raspberry Pis >= 3, but using a separate computer or server for
CouchDB is recommended.

To install, checkout :doc:`installation`.

If you do not have your Raspberry Pi setup yet, you can instead start at :doc:`other/headless-rpi`.


Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Quickstart

   installation
   serial-ports
   solarthing-check
   configuration
   view-data


.. toctree::
   :maxdepth: 1
   :caption: About

   supported-products
   database-and-display
   faq

.. toctree::
   :maxdepth: 1
   :caption: Maintaining SolarThing

   updating
   logging
   stability

.. toctree::
   :maxdepth: 1
   :caption: More Configuration

   actions/index
   config/property-substitution
   config/cpu-temperature
   config/w1-temperature
   config/analytics
   config/config-server
   tracer/clock
   config/commands
   rover/bulk-request
   docker/index


.. toctree::
   :maxdepth: 1
   :caption: Other

   other/install-java
   other/install-couchdb
   other/install-influxdb
   other/headless-rpi
   other/headless-odroid
   other/headless-armbian
   other/remote-monitor
   other/security
   develop/index
   GitHub <https://github.com/wildmountainfarms/solarthing>
   Report an Issue <https://github.com/wildmountainfarms/solarthing/issues>
