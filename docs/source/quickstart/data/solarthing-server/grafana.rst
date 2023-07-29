Grafana and the GraphQL Datasource
===================================

With SolarThing Server fully setup and a Grafana instance installed on your system, you are ready to configure Grafana with the GraphQL Datasource!


Install GraphQL Datasource to Grafana
---------------------------------------

Go here to learn how to install the data source: https://grafana.com/grafana/plugins/fifemon-graphql-datasource/?tab=installation


Configuring GraphQL Datasource
--------------------------------

Navigate to "Add data source" in Grafana.  Choose "GraphQL Data Source".

Feel free to change the name to something other than "GraphQL Data Source".

If you have Grafana installed on the same machine that SolarThing Server is running, set the URL to ``http://localhost:8080/graphql``.
If you do not, use ``http://<my ip here>:8080/graphql`` where ``<my ip here>`` is the ip address of the machine running SolarThing Server.

Keep all the other defaults, then click "Save & Test". You should see a green box pop up indicating success.

.. note::

  If you are using Grafana inside of a docker container, then you will likely have to use ``http://172.17.0.1:8080/graphql`` instead.
  That particular IP address is used inside of docker containers to refer to the "real" host machine. If you are not using Docker, ignore this.

  If you are running SolarThing server inside of docker, you can either expose the port 8080, or you make sure your Grafana container
  and your SolarThing server container are on the same Docker network. Once you do that, you can refer to the GraphQL endpoint via
  ``http://solarthing-server:8080/graphql`` where ``solarthing-server`` is the name of your container.


Graph battery voltages
-----------------------

Create a new panel on Grafana with the visualization of your choosing. Paste this into the query:

.. code-block:: graphql

    {
        data:queryStatus(from:"$__from", to:"$__to", sourceId:"$sourceId") {
            batteryVoltage {
                Time:dateMillis
                packet {
                    batteryVoltage
                    identifier { representation }
                    identityInfo { displayName }
                }
            }
        }
    }

That might work right off the bat, but you should also change ``Data path``, ``Group by``, and ``Alias by`` like so:


+------------+-------------------------------------------+
| Data path  |  ``data.batteryVoltage``                  |
+------------+-------------------------------------------+
| Group by   |  ``packet.identifier.representation``     |
+------------+-------------------------------------------+
| Alias by   |``$field_packet.identityInfo.displayName`` |
+------------+-------------------------------------------+

The ``Data path`` is the path to get into the structure containing the ``Time`` variable.
``Group by`` is useful for advanced SolarThing installations that have multiple devices.
``Alias by`` Will make each device have a human friendly name.
The other parameters can be left blank or default.

.. note::
    The above query and other queries on this page use ``$sourceId`` to represent the source ID.

    You can instead use ``default`` if you do not want to create a ``$sourceId`` variables in Grafana.
    If you would like to create a variables, you can go here to create a Constant or Custom variable: https://grafana.com/docs/grafana/latest/variables/variable-types/

You should get the above query to work before attempting other queries, as the above query is one of the most simple queries you can have.


More queries
--------------

There is a lack of documentation for more queries. For the time being, the answer to "How do I add more queries?" is figure it out yourself.

This doesn't mean you should blindly start trying to make queries. If you want to create more queries, I recommend you use the ``/graphiql`` endpoint of the SolarThing web interface.
You can then utilize the autocompletion and see the documentation of all the available queries (There are a lot, many of which you will not use!)

