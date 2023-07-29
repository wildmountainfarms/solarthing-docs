Databases and Viewing Data
=======================================

SolarThing supports multiple ways to export and upload data along with multiple ways to view that data.
This page can help you choose which database to use and setup as you configure SolarThing.

Databases
---------

CouchDB
^^^^^^^
Using CouchDB allows for the most features. Used by SolarThing Android. Required for the ``automation`` and ``pvoutput`` programs and for SolarThing Server.


InfluxDB
^^^^^^^^
People use InfluxDB if they want to get data into Grafana and design their own queries against their data.


Viewing Data
-------------

SolarThing Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All SolarThing Server configurations require CouchDB to be setup.

GraphQL and Grafana
"""""""""""""""""""

With a CouchDB database, SolarThing's Server program can be set up to serve data to Grafana. This is used alongside https://github.com/fifemon/graphql-datasource

SolarThing Web
""""""""""""""""""

SolarThing Server comes with a simple web interface ready to use out of the box.
Just navigate to the IP and port where it is being hosted and

InfluxDB and Grafana
""""""""""""""""""""""

If you are using an InfluxDB database, you may configure Grafana yourself to query data from InfluxDB.
Just know that SolarThing's maintainers are not well versed in InfluxDB, so do not expect much support.

PVOutput
^^^^^^^^

With a CouchDB database, SolarThing's ``pvoutput`` program can be set up to upload data to PVOutput at regular intervals.


SolarThing Android
^^^^^^^^^^^^^^^^^^

The Android application is available on the Google Play Store and uses the CouchDB database directly.

https://play.google.com/store/apps/details?id=me.retrodaredevil.solarthing.android


SolarThing Automation
^^^^^^^^^^^^^^^^^^^^^

The SolarThing ``automation`` program can do many things. It can send Slack messages to alert you of potential problems.
It can upload data to Solcast.

This program can be configured using SolarThing's Action Language.
Many features of the ``automation`` program are advanced and usually undocumented.
This is not for beginners.
