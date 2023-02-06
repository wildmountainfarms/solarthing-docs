CouchDB Develop
================

This page aims to document some best practices when testing and setting up CouchDB while developing.

Running
------------

While developing, this is a good way to create a temporary instance with a login of ``admin/relax``.
You can change the password once the instance is running, but there should be no need to.

.. code-block:: shell

  docker run -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=relax -d couchdb:3
