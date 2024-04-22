Install CouchDB
===============

.. note::
   CouchDB cannot be installed on Raspberry Pi 1s or on a Raspberry Pi Zero


.. note::
   It is not recommended to run CouchDB on a Raspberry Pi. This is because databases use lots of I/O operations, which is not good for the Pi's SD card long term.


This documentation is not going to tell you exactly how to install CouchDB. Figuring that out for whatever device you install it on is up to you.

https://docs.couchdb.org/en/stable/install/index.html

.. _couchdb-docker-install:

CouchDB Docker Install
-------------------------

If you choose to use Docker, you can use docker compose.

.. note::

  The example file structure shown below assumes that you are installing CouchDB on a device different than what the uploader program is configured on.
  If that is not the case, you may append configuration to your existing ``docker-compose.yml`` file.

Here is an example file structure:

.. code-block::

  ~/Documents/containers/solarthing/
  ├── couchdb/
  │   ├── data/
  │   └── etc/
  └── docker-compose.yml

.. code-block:: shell

  mkdir -p ~/Documents/containers/solarthing/couchdb/{data,etc}
  cd ~/Documents/containers/solarthing
  mkdir couchdb
  cd couchdb
  touch docker-compose.yml
  vi docker-compose.yml

Then copy this into your ``docker-compose.yml``.

.. code-block:: yaml

  services:
    couchdb:
      image: 'apache/couchdb:3'
      restart: unless-stopped
      environment:
        - 'COUCHDB_USER=admin'
        - 'COUCHDB_PASSWORD=password'
      ports:
        - '5984:5984'
      volumes:
        - './couchdb/data:/opt/couchdb/data'
        - './couchdb/etc:/opt/couchdb/etc/local.d'
    # NOTE: You may put a SolarThing server service here later when you configure it.

You can login to your CouchDB instance with user ``admin`` and password ``password``. Please change your password when you login.

.. note::

  Although you could set your password in ``docker-compose.yml``, you should use ``docker-compose.yml`` to set a temporary password
  then change your password in the web interface. The reason for this is that it is bad practice to store your password in plain text,
  and setting your password in CouchDB's web interface will avoid your password being stored in plain text.

  Once you have changed your password, you may choose to remote the ``environment:`` section from your couchdb's service configuration in the ``docker-compose.yml`` file.


Basic CouchDB Setup
---------------------

Newer installs of CouchDB require some setup. Note this is different from the SolarThing setup required to use the database.
Make sure that these databases already exist or create them if they do not:

Create a database called ``_users`` and a database called ``_replicator``. The default options for creating these databases are fine.


Keep user logged in
---------------------

Sometimes you may want to keep users logged in for longer than the default. Go to the settings page: http://127.0.0.1:5984/_utils/#_config.
You will configure the ``timeout`` setting: https://docs.couchdb.org/en/3.2.2-docs/config/auth.html#chttpd_auth/timeout.
Add an option with section: ``chttpd_auth``, name: ``timeout``, and value in seconds. I recommend 3600 for 1 hour timeout.
