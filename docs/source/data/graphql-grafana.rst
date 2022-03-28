GraphQL and Grafana
====================

If you have a CouchDB database, using SolarThing GraphQL is a great way to expose data to be used with https://github.com/fifemon/graphql-datasource.

.. note:: 

   It is recommended to configure the GraphQL program on the same device as the CouchDB database. If this device is different than the one
   you installed SolarThing on, you can install SolarThing on this device too, just skip to this configuration after installing.


.. note:: CouchDB is the only database that the GraphQL program works with

.. note:: This page assumes you have installed Grafana

Just like with whatever uploader program you configured, we're going to change our directory:


.. code-block:: shell

    cd /opt/solarthing/program/graphql/config

.. note:: The GraphQL program is different from the other SolarThing programs. This means that you must use the graphql directory, or it will not work.

Now we will start editing the configuration file:


.. code-block:: shell

    nano application.properties

Paste this into your file:

.. code-block:: ini

    solarthing.config.database=config/couchdb.json


With the above configuration, you must have a ``couchdb.json`` file in ``/opt/solarthing/program/graphql/config/``.
Since you already know how the ``couchdb.json`` file works, we will not go into detail on this here.

That's all the configuration you need. Just point it to your ``couchdb.json``. Now let's cd up a directory and run it:

.. code-block:: shell

    cd /opt/solarthing/program/graphql
    # OR
    cd ..

    # Now run it:
    sudo -u solarthing ./run.sh

You should see a bunch of log messages. After about 5 seconds, you should see messages similar to those at the end:

.. code-block:: log

    2021-12-20 23:48:31.030  INFO 269837 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
    2021-12-20 23:48:31.042  INFO 269837 --- [           main] m.r.s.rest.SolarThingGraphQLApplication  : Started SolarThingGraphQLApplication in 3.846 seconds (JVM running for 4.88)

If you do, it's working as intended!

Installing and starting systemd service
----------------------------------------

Let's go ahead and install the systemd service, start it, then enable it so it starts across reboots:


.. code-block:: shell

    sudo /opt/solarthing/other/systemd/install.sh graphql
    sudo systemctl start solarthing-graphql
    sudo systemctl enable solarthing-graphql

Run ``systemctl status solarthing-graphql`` to make sure it is running. If it is, you're ready to configure the GraphQL Datasource.

Install GraphQL Datasource to Grafana
---------------------------------------

Go here to learn how to install the data source: https://grafana.com/grafana/plugins/fifemon-graphql-datasource/?tab=installation


Configuring GraphQL Datasource
--------------------------------

Navigate to "Add data source" in Grafana.  Choose "GraphQL Data Source".

Feel free to change the name to something other than "GraphQL Data Source".

If you have Grafana installed on the same machine that the GraphQL program is running, set the URL to ``http://localhost:8080/graphql``. 
If you do not, use ``http://<my ip here>:8080/graphql`` where ``<my ip herer>`` is the ip address of the machine running the GraphQL program.

Keep all the other defaults, then click "Save & Test". You should see a green box pop up indicating success.


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

This doesn't mean you should blindly start trying to make queries. If you want to create more queries, I recommend you install GraphQL playground: https://github.com/graphql/graphql-playground.
You can then utilize the autocompletion and see the documentation of all the available queries (There are a lot, many of which you will not use!)


