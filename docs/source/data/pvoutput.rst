PVOutput Uploader
==================

If you have a CouchDB database, you can create a system on https://pvoutput.org and upload your output data.


.. note:: CouchDB is the only database that the PVOutput program works with

Now we'll change our directory to the pvoutput config directory and start editing its config:


.. code-block:: shell

    cd /opt/solarthing/program/pvoutput/config
    nano base.json

Paste this into your ``base.json`` file:

.. code-block:: json

    {
      "type": "pvoutput-upload",
      "system_id": 100,
      "api_key": "<YOUR API KEY>",
      "database": "config/couchdb.json",
      "source": "default"
    }

This assumes you have a ``couchdb.json`` file located in ``/opt/solarthing/program/pvoutput/config/couchdb.json``. 
If you do not, either change the path or create a new ``couchdb.json`` file to put in that location.

In the above example, ``100`` is the system id. You should replace this with whatever your system id is.

Replace ``<YOUR API KEY>`` with your API key.

Now let's cd up a directory and run it:

.. code-block:: shell

    cd /opt/solarthing/program/graphql
    # OR
    cd ..

    # Now run it:
    sudo -u solarthing ./run.sh

You should see a bunch of log messages. Some of the log messages should indicate success in uploading to PVOutput.



Installing and starting systemd service
----------------------------------------

Let's go ahead and install the systemd service, start it, then enable it so it starts across reboots:


.. code-block:: shell

    sudo /opt/solarthing/other/system/install.sh pvoutput
    sudo systemctl start solarthing-pvoutput
    sudo systemctl enable solarthing-pvoutput

Run ``systemctl status solarthing-pvoutput`` to make sure it is running. 

Now you're done! Navigate to your system on PVOutput and you should see one data point. 
SolarThing will upload every 5 minutes, so after some time it'll be a cool graph!