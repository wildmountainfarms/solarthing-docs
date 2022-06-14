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

Unless a particular cache type is being actively developed, it is likely that for most cache types, they will be generated once
and left in the database forever.

Cache Cleanup
--------------

Currently SolarThing does not have a way to remove old cache data. There is no way to tell if a particular
document is actively being used, so there is no perfect solution to this. The cache database does not
take up much space, so this is not a concern.


``chargeControllerAccumulation`` Cache Type
--------------------------------------------

The ``chargeControllerAccumulation`` cache type is one that keeps track of the amount of energy generated
by a charge controller over a certain interval.

An example ``data`` object looks like this:

.. code-block:: json

    {
      "identifier": {
        "type": "outback",
        "address": 3
      },
      "generationKWH": 0.099999905,
      "firstDateMillis": 1624480199471,
      "lastDateMillis": 1624481099437,
      "unknownGenerationKWH": 0,
      "unknownStartDateMillis": null
    }

The data is pretty easy to understand, but there are some important things to know. 
You have an identifier object, which represents what device this data was generated from.

You have a ``firstDateMillis`` and ``lastDateMillis``, which represent the timestamps of the first and last status packets that
were used to generate this data. Those status packets belong to the device identified by that identifier. There may be any number of
packets in between the first and last packets, but that information is irrelevant. It is also possible for there to be 0 packets in between
the first and last packets used for generation, and it is possible that the first packet IS the last packet.

Almost always, ``firstDateMillis`` is actually outside of the interval for this document. It is usually the last packet of the previous interval.
The reason for this is because let's say that we have two intervals right next to each other. 
13:15-13:30 and 13:30-13:45. The first interval has data from 13:14 to 13:29 and the second interval has data from 13:29 to 13:44.
Let's say that during the first interval 1.0 kWh was reported and during the second interval 1.0 kWh was reported. 
Let's say that the device read these values at these times: ``13:14=4.5kWh``, ``13:29=5.5kWh``, ``13:31=5.6kWh``, ``13:44=6.5kWh``.
Now, between 13:14 and 13:44, you can see that a total of 2.0 kWh was generated. However, if the generation of this data used 13:31 as the
start packet for the second interval, the generated values would end up being 1.0 kWh and 0.9 kWh respectively.
For this reason, the last packet from the previous interval is used for the start packet to make sure no data is "left behind" when
generating the data.

In this case we have a ``generationKWH`` which represents the energy generated during this period.

"Unknown" Data in ``chargeControllerAccumulation`` 
-----------------------------------------------------

In the above section, that particular piece of data is "known" because ``startDateMillis`` and ``endDateMillis`` are not null.
"Known" pieces of data can have unknown components to them, which represents the accumulation of preceding periods where data in those periods
for that particular device were "unknown".

A particular piece of data is completely unknown if ``startDateMillis`` is null and ``endDateMillis`` is null. If that is the case,
then that "unknown" data does not have an "unknown" component to it. It is only "unknown".

In the above section, there is an example ``data`` object that has ``unknownGenerationKWH`` = 0 and ``unknownStartDateMillis`` = null.
This means that particular piece of data is "known", and it has no "unknown" component.


