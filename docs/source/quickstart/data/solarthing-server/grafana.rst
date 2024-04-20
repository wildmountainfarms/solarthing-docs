Grafana and the GraphQL Datasource
===================================

With SolarThing Server fully setup and a Grafana instance installed on your system, you are ready to configure Grafana with the GraphQL Datasource!


Install Wild GraphQL Datasource to Grafana
--------------------------------------------

Go here to learn how to install the data source: https://grafana.com/grafana/plugins/retrodaredevil-wildgraphql-datasource/?tab=installation

.. note::

  If you search around Grafana plugins, you may notice `fifemon-graphql-datasource <https://grafana.com/grafana/plugins/fifemon-graphql-datasource/>`_.
  Note that this plugin is deprecated and does not work on newer version of Grafana.
  Additionally, the documentation on this page is not compatible with that data source.


Configuring Wild GraphQL Datasource
-------------------------------------

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


Simple Battery Voltage Graph
-----------------------------

Create a new panel on Grafana with the visualization of your choosing. Paste this into the query:

.. code-block:: graphql

  query ($from: Long!, $to: Long!) {
    queryStatus(from: $from, to: $to) {
      batteryVoltage {
        dateMillis
        packet {
          batteryVoltage
        }
      }
    }
  }


Once you have the query written, you can start configuring "Parsing Option 1" as such:


+------------+-------------------------------------------+
| Data path  |  ``queryStatus.batteryVoltage``           |
+------------+-------------------------------------------+
| Time path  |  ``dateMillis``                           |
+------------+-------------------------------------------+

You should get the above query to work before attempting other queries, as the above query is one of the most simple queries you can have.

(Advanced) Battery Voltage Graph with Multiple Devices
--------------------------------------------------------

If you have a SolarThing instance with multiple devices, you may want to change your battery voltage query to correctly identify each device.

.. code-block:: graphql

  query ($from: Long!, $to: Long!, $sourceId: String!) {
    queryStatus(from: $from, to: $to, sourceId: $sourceId) {
      batteryVoltage {
        dateMillis
        fragmentIdString
        packet {
          batteryVoltage
          identifier {
            representation
          }
          identityInfo {
            displayName
          }
        }
      }
    }
  }

The first difference you'll notice is we now have fields ``fragmentIdString``, ``packet.identifier.representation`` and ``packet.identityInfo.displayName`` at our disposal.
You may also notice that this query includes a ``$sourceId: String!`` variable.
The inclusion of the Source ID is not required, but is recommended if you ever want to have different systems using the same SolarThing CouchDB database.
Before we use the additional fields, let's first pass in a ``sourceId`` variable that we define in Grafana. Create a Constant or Custom variable: https://grafana.com/docs/grafana/latest/variables/variable-types/
Once the variable is created within Grafana, you need to pass it to the query by adding it to the variables section of the GraphiQL editor:

.. code-block:: json

  {
    "sourceId": "$sourceId"
  }

Now that we have written the query and passed in the necessary variables, it's time to configure "Parsing Option 1":

+------------+-------------------------------------------+
| Data path  |  ``queryStatus.batteryVoltage``           |
+------------+-------------------------------------------+
| Time path  |  ``dateMillis``                           |
+------------+-------------------------------------------+

Initially, it looks just the same as before, but now we need to add some labels.
Let's create a label called ``displayName`` by typing ``displayName`` into the "Create label" box, and then pressing enter.
Under the time path in Parsing Option 1, you should see a new entry with the label: ``Label: "displayName"``.
Configure this to be a "Field" label, rather than a "Constant" label by clicking the first dropdown.
Now, set its value to ``packet.identityInfo.displayName``.
You may set "If absent" to "Error" if you would like, because we never expect that field to be absent from the response.
For completeness's sake, let's also add labels for the fragment ID, and the representation of the identifier.
The table below shows recommended label names and values for these.

+---------------------------+------------+-------------------------------------------+-------------+
| (Recommended) Label name  | Label type |  Label value                              | If absent   |
+===========================+============+===========================================+=============+
| ``displayName``           | Field      |  ``packet.identityInfo.displayName``      | Error       |
+---------------------------+------------+-------------------------------------------+-------------+
| ``fragmentId``            | Field      |  ``fragmentIdString``                     | Error       |
+---------------------------+------------+-------------------------------------------+-------------+
| ``identifier``            | Field      |  ``packet.identifier.representation``     | Error       |
+---------------------------+------------+-------------------------------------------+-------------+

The query is now fully configured. Click the refresh dashboard button to confirm that the battery voltages are graphed correctly.
As it is now, you should see different data points for each device, however, these data points do not yet have labels on them.
(Currently the legend is cluttered with illegible names).
To fix this, navigate to the right side of the screen and scroll until you find the "Standard Options" section.
Expand the Standard options section if necessary.
Within this section, there is a field called "Display name" that you can change.
We want to set its value to ``${__field.labels.displayName}`` or ``${__field.labels["displayName"]}``.
Either one will work, although the second one is required if the name of your label is not ``displayName`` AND it has spaces in it.

With this configuration, your graph should now have a legend labeled by the display name of the device,
and the graph should show battery voltages of each device!


More queries
--------------

There is a lack of documentation for more queries. For the time being, the answer to "How do I add more queries?" is figure it out yourself.

This doesn't mean you should blindly start trying to make queries. If you want to create more queries, I recommend you use the ``/graphiql`` endpoint of the SolarThing web interface.
You can then utilize the autocompletion and see the documentation of all the available queries (There are a lot, many of which you will not use!)

