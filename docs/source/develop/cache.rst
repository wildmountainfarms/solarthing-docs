SolarThing Cache Database
===========================

The ``solarthing_cache`` database is a complicated, but can be broken down. This page aims to document
how it is currently used and how one can use it to cache data that may be expensive to calculate and query.


Database Structure
---------------------

Unlike other databases in SolarThing, ``solarthing_cache`` is not set up to be queried using a view.
It must be queried using the ID of the document. The documents are named like so: ``cache_<time start>_<duration>_<source ID>_<cache name>``.

Querying this data usually means making a `bulk get <https://docs.couchdb.org/en/stable/api/database/bulk-api.html?highlight=bulk#post--db-_bulk_get>`_ request.

Packet Structure
------------------

Although there are many different cache types, all documents in the database share a common base structure.

.. code-block:: json

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

Here's an example of data that would cause the following results:

.. code-block::

    # The following values are the timestamps of MX3 packets and the reading of MX3's kWh field
    12:59=3.3
    ----- 13:00
    13:01=3.3
    13:09=3.5
    13:14=3.6
    ----- 13:15
    ----- 13:30
    ----- 13:45
    13:46=4.0
    13:50=4.2
    13:55=4.3
    ----- 14:00

    Results:
    13:00-13:15 generationKWH=0.3, start=12:59, end=13:14, no unknown component
    13:15-13:30 unknown
    13:30-13:45 unknown
    13:45-14:00 generationKWH=0.3, start=13:46, end=13:55, unknownStart=13:14, unknownGeneration=0.4

You can now see that the unknown component represents the accumulation of data from previous intervals that were unknown all the way back to
the last "known" interval. This allows us to say "I know that 0.3 kWh was generated between 13:45 and 14:00",
and "I know that sometime between 13:14 and 13:46 0.4 kWh was generated.
I don't know if all of that 0.4 kWh came from one period or another, I just know that it happened."

Unknown components are necessary to prevent accumulation data from becoming lost if a device disconnects for an extended period of time.

Combining Intervals of Data
-----------------------------

In the cache database, data always goes in at fixed intervals. However, when you take that data out of the database (or calculate it yourself),
having a bunch of 15 minute intervals usually isn't that useful. Maybe you want hour long intervals or day long intervals.
Each cache type supports combining two intervals of data right next to each other. So, you can combine intervals 13:15-13:30 and 13:30-13:45
to make a 13:15-13:45 interval. You can keep combining intervals of data until you get a bunch of intervals that you want, or more commonly
combining all the intervals so you can get a single piece of data, such as the generation kWh for a single day.

Let's say that we combine a two ``chargeControllerAccumulation`` types of data.
``13:15-13:30 = 0.5 kWh generated`` and
``13:30-13:45 = 0.6 kWh generated``.
Combining them gives us a result of ``13:15-13:45 = 1.1 kWh generated``.

Now let's say that we have two intervals, both with unknown components.

.. code-block::

    14:00-15:00 generationKWH=1.3, unknownGenerationKWH=0.2
    15:00-16:00 generationKWH=0.9, unknownGenerationKWH=0.1

    Combined result:
    Interval: 14:00-16:00
    generationKWH=1.3+0.9+0.1 = 2.3
    unknownGenerationKWH=0.2

We see that to calculate the new ``generationKWH``, we add up both ``generationKWH``, then also add the later interval's unknown component.
The unkonwn component of the first interval remains in the resulting combining.

You can see this logic for yourself here:
:blob:`master/core/src/main/java/me/retrodaredevil/solarthing/type/cache/packets/data/ChargeControllerAccumulationDataCache.java`


``batteryRecord`` Cache Type
--------------------------------------------

The ``batteryRecord`` cache is one that keeps track of the minimum and maximum battery voltage, along with the
battery volt hours for an interval of time, for a single device. Minimum and maximum battery voltages are useful,
but battery volt hours is usually used to determine the average (integral over interval).

An example battery record's ``"data"`` object may look like this:

.. code-block:: json

    {
      "identifier": {
        "type": "outback",
        "address": 1
      },
      "firstDateMillis": 1655321348930,
      "lastDateMillis": 1655322224927,
      "unknownStartDateMillis": null,
      "record": {
        "minBatteryVoltage": 24.4,
        "minBatteryVoltageDateMillis": 1655321543926,
        "maxBatteryVoltage": 25.6,
        "maxBatteryVoltageDateMillis": 1655321447930,
        "unknownBatteryVoltageHours": 0,
        "unknownDurationMillis": 0,
        "batteryVoltageHours": 6.056228924143589,
        "knownDurationMillis": 875997
      }
    }

The data keeps track of the time when the battery was at a minimum, and the time it was at a maximum.

You'll notice that there is something called ``knownDurationMillis``. This is the total duration that the
``batteryVoltageHours`` integral has been calculated over. For a packet in the database ``lastDateMillis - firstDateMillis``,
is exactly the same as ``knownDurationMillis``. When we get into combining later, we will see how these two values may end up being different.


"Unknown" data is similar to that of a ``chargeControllerAccumulation`` cache. Unknown data represents data from
the last known period up to the start of this period. The main difference is the precision of the data.
Charge controllers report their power integral (energy), so even if a charge controller disconnects, the amount of energy
it generated can be reliably calculated. This is not the case for a ``batteryRecord``'s volt hours calculation.
An unknown component is always calculated using two data points: The last battery voltage from before the current period,
and the first battery voltage in this period. That means that while ``unknownBatteryVoltageHours`` does have the volt hours unit,
it can be an unreliable estimate of what actually happened during the (possibly multiple) unknown periods.

Combining ``batteryRecord``
------------------------------

Combining two battery record cache periods is relatively simple. The minimum of the minimums becomes the new minimum
and the maximum of the maximums becomes the new maximum. The battery voltage hours gets added up along with the known duration hours.
The tricky part, is what happens to unknown data. If we followed this exactly how the charge controller cache handles this,
the unknown component of the later period would be added to the known component of the resulting combination.
However, remember that an unknown component was calculated using two data points, and is extremely inprecise.
Because of this, a battery record cache also has a "gap" component, which represents unknown components
somewhere in the middle of the period. This allows someone to include or exclude the gap component in the calculation of an average.
This gives choice to the users of this data so they can either ignore the "gap" component, or just add it onto the known component.

You can see the logic of combining two battery record caches here:
:blob:`master/core/src/main/java/me/retrodaredevil/solarthing/type/cache/packets/data/BatteryRecordDataCache.java`


``IdentificationCacheNodeCreator``: generating data
-----------------------------------------------------

IdentificationCacheNodeCreator is an interface that is used for generating data for a single device.
You can view it here:
:blob:`master/core/src/main/java/me/retrodaredevil/solarthing/rest/cache/creators/IdentificationCacheNodeCreator/java`

The interface is pretty simple. ``getAcceptedType()`` should return the class of the type to accept.
For instance ``BatteryVoltage`` to get any type of device that provides the battery voltage.
``getCacheName()`` should return the name of the cache, which should be unique among all cache names. Some examples of names
already in use are ``batteryRecord``, ``chargeControllerAccumulation``, and ``fxAccumulation``.
New names should use camelCase, and should NOT be redundant by including "cache" in the name.

The most important method of this interface is the create method. The parameters taken are as follows:

* ``identifierFragment``: Represents the fragment and identifier for a given device
* ``packets``: The packets of the type given by ``getAcceptedType()``.
  Note that these packets may and will be out of the range of the given period.
  The implementation should filter for the given period or use the extra data for *smart* calculations.
  You can assume these are sorted in ascending order.
* ``periodStart``: The start time of the period that data will be returned for
* ``periodDuration``: The duration of the period that data will be returned for

One question one might have is why so much data is provided. The reason for this is because we want
and period to be able to calculate its "unknown" component by backtracking up to ~4 hours before the period even started.
In fact, any time this is called, it is expected that data should be provided for at least 4 hours before the start of the period.
Usually, much more data will be provided when calling this method, but it should not use all of that. By not using all of the data
provided, reproducible caches are possible so no matter how much data is provided in the ``packets`` list,
the same result should occur each time for a given cache and device.

The data returned is an ``IdentificationCacheNode``, which holds the fragment of the device and also the data, which is required to hold
the identifier of the device because the data is of the type of ``IdentificationCacheData``, which is the common type for data that can be combined.

So to recap, when calling the ``create`` method of a ``IdentificationCacheNodeCreator``, data for a single device is provided,
and the returned value is the data for that device for the given period. A ``IdentificationCacheNodeCreator`` only deals with a single
device and a single period at a time!

``CacheCreator``: generating data
----------------------------------

A ``CacheCreator`` is at a lower level of abstraction than a ``IdentificationCacheNodeCreator``. The result from a ``CacheCreator``
is what is stored right in the database. It has a single method: ``createFrom()``. This method takes a source ID,
a list of packets, and the period. This list of packets follows the same 4 hour rule that ``IdentificationCacheNodeCreator`` follows,
as its implementation directly calls ``IdentificationCacheNodeCreator``'s ``create()`` method.

``DefaultIdentificationCacheCreator``: ``CacheCreator`` implementation
--------------------------------------------------------------------------------------------------

A ``CacheCreator`` doesn't have to necessarily deal with ``IdentificationCacheNodeCreator`` s.
The main (and only) implementation of ``CacheCreator`` is ``DefaultIdentificationCacheCreator``,
which takes a ``IdentificationCacheNodeCreator``.

This implementation is the lowest level of abstraction for data generation. Any lower and we'll start getting into
the logic for determining what periods to generate, cache, and store in the database.

``BatteryRecordCacheNodeCreator`` implementation
--------------------------------------------------

``BatteryRecordCacheNodeCreator`` implements ``IdentificationCacheNodeCreator`` and has the main logic for generating
``batteryRecord`` caches. View it here: :blob:`master/core/src/main/java/me/retrodaredevil/solarthing/rest/cache/creators/BatteryRecordCacheNodeCreator.java`

Cache Logic
-------------

The actual logic for generating caches and storing them in the database is present here:
:blob:`master/server/src/main/me/retrodaredevil/solarthing/rest/cache/CacheHandler.java`

Usages of caches
--------------------

Currently, the SolarThing Server program exposes a REST API for querying cache data, which then will call
methods provided by ``CacheHandler``. You can see this here:
:blob:`master/server/src/main/me/retrodaredevil/solarthing/rest/cache/CacheController.java`

Currently, nothing actually uses that REST endpoint, but there are usages of ``CacheController`` in some of the GraphQL queries.
Typically, a GraphQL query that needs to use cache data will be provided a ``CacheController`` object. You can see an example here:
:blob:`master/server/src/main/me/retrodaredevil/solarthing/rest/graphql/service/SolarThingGraphQLLongTermService.java`

Creating your own cache
-------------------------

If you would like to make your own cache, then you first need to decide a couple of things.
We will assume that you would like to make a cache that is based around data for each device of a certain type.
In this case, we will be implementing the ``IdentificationCacheData`` interface, or more likely, we will be extending an
abstract implementation of that called ``BaseAccumulationDataCache``. Now, let's come up with some sort of name for our cache such as
"cheese sandwich cache".

We will create a class called ``CheeseSandwichDataCache``, which will extend ``BaseAccumulationDataCache``.
This class should be created in the ``core`` module under the ``me.retrodaredevil.solarthing.type.cache.packets.data`` package.
We should create a field like so: ``public static final String CACHE_NAME = "cheeseSandwich";``.
We should annotate our class with ``@JsonExplicit``, and create a constructor annotated with ``@JsonCreator``.
You can see an example here: :blob:`master/core/src/main/java/me/retrodaredevil/solarthing/type/cache/packets/data/BatteryRecordDataCache.java`

You should populate your newly created class with useful data and implement the ``combine()`` method.

Now, we need to create our class to generate the data. We will create a class called ``CheeseSandwichCacheNodeCreator``
in the ``graphql`` module under the ``me.retrodaredevil.solarthing.rest.cache.creators`` package.
This should implement ``IdentificationCacheNodeCreator<CheeseSandwichDataCache, CheeseSandwichStatusPacket>``.
Note that you can replace ``CheeseSandwichStatusPacket`` with whatever type of class that you need to use to generate data.
Note that class must implement the ``Identifiable`` interface AND, the identifier returned must be serializabe and deserializable to and from JSON.
Please make sure you check to make sure that the type of identifiable used by that class is present in the ``@JsonSubTypes`` in the ``Identifier`` interface.
You can see an example here: :blob:`master/server/src/main/java/me/retrodaredevil/solarthing/rest/cache/creators/BatteryRecordCacheNodeCreator.java`.

Now that you have your class created, it's time to implement the required methods. The ``getAcceptedType()`` method can return
the class of what you replaced ``CheeseSandwichStatusPacket`` with. ``getCacheName()`` returns ``CheeseSandwichDataCache.CACHE_NAME``.
Now it's time to implement the create method. This is where you may have to get creative to create the perfect algorithm to
generate your data, or you can look at one of the many implementations of this method for other types of cache data.

Once you are done, go into the ``CacheHandler`` class, and add an entry similer to the other entries under the ``CACHE_CREATORS`` field.
Now go to ``CacheController`` and add a method similer to the other methods already present, but for your data types.
To test it, use something to hit the newly created endpoint that you have made, and see if it works.
