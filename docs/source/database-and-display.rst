Supported Databases and Viewing Methods
=======================================

SolarThing supports multiple ways to export and upload data along with multiple ways to view that data.

CouchDB
-------
Using CouchDB allows for the most features. Used by SolarThing Android. Required for the ``automation`` and ``pvoutput`` programs.
Used alongside SolarThing GraphQL to get data into Grafana.


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



