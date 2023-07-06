Welcome to SolarThing's documentation!
======================================

**SolarThing** is an application that can monitor data from a variety of solar charge controllers and inverters.
Code and issues available at https://github.com/wildmountainfarms/solarthing.

This documentation is targetted at people who have Raspberry Pis or any Debian based operating system.
However, SolarThing can run on any OS.

The primary purpose of SolarThing is to get data and upload it to a database. Using CouchDB allows for the best SolarThing
experience, but InfluxDB can also be used. CouchDB can run on Raspberry Pis >= 3, but using a separate computer or server for
CouchDB is recommended.

To install, checkout :doc:`quickstart/installation`.

If you do not have your Raspberry Pi setup yet, you can instead start at :doc:`setup/headless-rpi`.


Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Quickstart

   quickstart/installation
   quickstart/serial-port/index
   quickstart/config/index
   quickstart/data/index


.. toctree::
   :maxdepth: 1
   :caption: About

   about/index

.. toctree::
   :maxdepth: 1
   :caption: Maintaining SolarThing

   updating
   logging/index
   stability

.. toctree::
   :maxdepth: 1
   :caption: Configuration

   config/property-substitution
   actions/index
   config/base-json/index
   config/database/index
   config/analytics
   config/config-server
   config/commands/index
   docker/index
   legacy/index


.. toctree::
   :maxdepth: 1
   :caption: Other

   software/index
   setup/index
   other/remote-monitor
   other/security
   develop/index
   GitHub <https://github.com/wildmountainfarms/solarthing>
   Report an Issue <https://github.com/wildmountainfarms/solarthing/issues>
