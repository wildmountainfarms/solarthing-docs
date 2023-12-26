SolarThing Server GraphQL Queries and Mutations
================================================

In SolarThing there is a whole package dedicated to defining GraphQL endpoints for the SolarThing Server here:
:tree:`master/server/src/main/java/me/retrodaredevil/solarthing/rest/graphql/service`

The ``/graphql`` endpoint is used to make GraphQL requests. There are many different possible queries to choose from.
The structure of many of the queries are designed in such a way to make them easily usable with `graphql-datasource <https://github.com/fifemon/graphql-datasource>`.

.. note::

  Documentation for setting up the GraphQL datasource is outdated. See :issue:`190` for more information.

The cool thing about GraphQL, is that you can tell it to query something, then only ask for some of the result.
By asking for only some of the result, it may not have to do all the calculations.
In the case of SolarThing, we can ask it to query all the status packets in a time period,
then we can sort and calculate data using that data that has been queried.
A good example of this is the ``queryStatus`` query defined in ``SolarThingGraphQLService``.
This query will get some data, then return a ``SolarThingStatusQuery``, where we can then ask for very specific data
in a specific format and get the exact data that we want. That particular format is very accessible in graphql-datasource.

GraphQL Usage in ``web`` module
---------------------------------

The ``web`` module contains the code for SolarThing Web that is bundled with SolarThing Server.
This website is completely backed by GraphQL queries and mutations that define how the website works and functions.
You can see the directory containing the queries here:
:tree:`master/web/src/graphql`.

You will notice that all of the queries are named, and many of them take in query variables. Each query can be tested to be
correct against the schema, and each query has its own function automatically generated for it.
At the low level, some ``npm`` command is run to generate code based on these queries.
For our purposes, all we need to know is that running ``./gradlew web:generateCode`` will generate the code for us.
When running that, it will also generate the GraphQL schema for us so it knows that our queries are correct,
and so that it can provide the generated code with rich type information, which is very important because
it gives us the same typing that the Java code has.

The ``web`` module uses React, so most of the time it doesn't look like you are querying the GraphQL endpoint,
as much of the boilerplate is taken away from you so you can deal with the result.
Much of the time, the use of a query will look like this:

.. code-block:: typescript

    const {data, error, isLoading, isSuccess} = useHomeQuery(graphQLClient, { sourceId, currentTimeMillis: "" + timeMillisRounded});


Testing GraphQL Endpoint on Command Line
------------------------------------------

https://github.com/Urigo/graphql-cli

