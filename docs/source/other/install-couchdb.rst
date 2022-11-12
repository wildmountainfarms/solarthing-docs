Install CouchDB
===============

.. note::
   CouchDB cannot be installed on Raspberry Pi 1s or on a Raspberry Pi Zero


.. note::
   It is not recommended to run CouchDB on a Raspberry Pi. This is because databases use lots of I/O operations, which is not good for the Pi's SD card long term.


This documentation is not going to tell you exactly how to install CouchDB. Figuring that out for whatever device you install it on is up to you.

https://docs.couchdb.org/en/stable/install/index.html

Docker Compose Install
-------------------------

If you choose to use Docker, you can use docker compose.

.. code-block:: shell

   cd /opt/containers/
   mkdir couchdb
   cd couchdb
   touch docker-compose.yml
   vi docker-compose.yml

Then copy this into your ``docker-compose.yml``.

.. code-block:: yaml

    version: '3.7'

    services:
      wmf-couchdb:
        image: 'apache/couchdb:3'
        restart: unless-stopped
        environment:
          - 'COUCHDB_USER=admin'
          - 'COUCHDB_PASSWORD=password'
        ports:
          - '5984:5984'
        volumes:
          - './data:/opt/couchdb/data'
          - './etc:/opt/couchdb/etc/local.d'
    
You can login to your CouchDB instance with user ``admin`` and password ``password``. Please change your password when you login.

.. note:: 
   
   Althugh you could set your password in ``docker-compose.yml``, you should use ``docker-compose.yml`` to set a temporary password
   then change your password in the web interface. The reason for this is that it is bad practice to store your password in plain text,
   and setting your password in CouchDB's web interface will avoid your password being stored in plain text.


Basic CouchDB Setup
---------------------

Newer installs of CouchDB require some setup. Note this is different from the SolarThing setup required to use the database.

Create a database called ``_users`` and a database called ``_replicator``. The default options for creating these databases are fine.
