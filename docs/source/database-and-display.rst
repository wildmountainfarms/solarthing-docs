Databases and Viewing Data
=======================================

SolarThing supports multiple ways to export and upload data along with multiple ways to view that data.

CouchDB
-------
Using CouchDB allows for the most features. Used by SolarThing Android. Required for the ``automation`` and ``pvoutput`` programs.
Used alongside SolarThing Server to get data into Grafana.


InfluxDB
--------
People use InfluxDB if they want to get data into Grafana and design their own queries against their data.


--------


PVOutput
--------

With a CouchDB database, SolarThing's ``pvoutput`` program can be set up to upload data to PVOutput at regular intervals.


GraphQL and Grafana
-------------------

With a CouchDB database, SolarThing's GraphQL program can be set up to serve data to Grafana. This is used alongside https://github.com/fifemon/graphql-datasource


SolarThing Android
------------------

The Android application is available on the Google Play Store and uses the CouchDB database directly.

https://play.google.com/store/apps/details?id=me.retrodaredevil.solarthing.android


SolarThing Automation
---------------------

The SolarThing ``automation`` program can do many things. It can send Slack messages to alert you of potential problems.
It can upload data to Solcast.

This program can be configured using SolarThing's Action Language. Many features of the ``automation`` program are advanced and usually undocumented.
