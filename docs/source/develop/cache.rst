SolarThing Cache Database
===========================

The ``solarthing_cache`` database is a complicated, but can be broken down. This page aims to document
how it is currently used and how one can use it to cache data that may be expensive to calculate and query.


Database Structure
---------------------

Unlike other databases in SolarThing, ``solarthing_cache`` is not set up to be queried using a view. 
It must be queried using the ID of the document. The documents are named like so: ``cache_<time start>_<duration>_<source ID>_<cache name>``.

Querying this data usually means making a `bulk get <https://docs.couchdb.org/en/stable/api/database/bulk-api.html?highlight=bulk#post--db-_bulk_get>` request.

Packet Structure
------------------

Although there are many different cache types, all documents in the database share a common base structure.

.. code-block:: json5

    {
      "_id": "cache_2021-06-23T20:30:00Z_PT15M_default_chargeControllerAccumulation",
      "_rev": "31-1da15edb1b141b22d163a6fc8b7901d5",
      "periodStartDateMillis": 1624480200000,
      "periodDurationMillis": 900000,
      "sourceId": "default",
      "cacheName": "the cache name here",
      "nodes": [
        {
          "fragmentId": 1,
          "data": {
            // ... node data here
          }
        },
        // ... more nodes
      ]
    }

An entire packet represents one small interval (usually a 15 minute interval). Each node inside of the
packet represent the data for a SINGLE device for that interval.

Triggering Document Generation
---------------------------------

Packets are generated when a particular start time and interval are requested. If the document does not existing in the database
with the document ID corresponding to the start time, interval, source ID, and cache name, then that document will be generated.

Triggering Document Replacement
---------------------------------

Packets in the database are not replaced unless there is an error while trying to parse the data from that document.
When an error occurs, it is assumed that SolarThing has been updated in a way so that a particular cache document is no
longer valid. Maybe it doesn't have enough data anymore, or maybe it has too much data, or maybe an error was thrown by
SolarThing on purpose to indicate that the old cached data is bad and should not be used.

