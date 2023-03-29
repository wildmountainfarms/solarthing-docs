Property Substitution
========================

Across SolarThing there are many different configuration files that you can use.
Depending on what kind of file you are configuring, SolarThing may support the ability for property substitution in that file.
Below we will describe the types of property substitution available, but before we do that, we will go over what documentation you should reference for a specific type of file.

If you are editing SolarThing configuration files that are JSON formatted such as ``base.json`` or a database configuration file,
you will be able to use SolarThing property substitution described here: :ref:`solarthing-property-substitution`.
If you are editing log4j configuration, you will be able to use Log4j property substitution described here: :ref:`log4j`.
If you are editing ``application.properties`` and are utilizing SolarThing Server, you will be able to use Spring's Property Placeholders described here: :ref:`spring`.

There are many reasons you would want to use property substitution in your config files, but normally only advanced users would choose to do this.
If you are running multiple instances of SolarThing on the same machine, you might find yourself typing the same constant in multiple spots.
Property substitution is especially great when you are utilizing Docker, as Docker makes it very easy to set environment variables that you can reference in configuration.


.. _solarthing-property-substitution:

SolarThing Property Substitution
------------------------------------

.. note:: SolarThing Server does not yet support any SolarThing Property Substitution.

SolarThing Property Substitution is a **feature added in SolarThing v2023.3.0**.
You can use this feature in most JSON configuration files except for ActionLang files described in raw JSON.
In any supported configuration file, if you put ``${something}`` inside of a JSON string or a JSON key (any value enclosed in quotes),
then (if it is valid) it will be replaced with its corresponding value.

For instance, let's take a CouchDB configuration that looks like this:

.. code-block:: yaml

  {
    "type": "couchdb",
    "config": {
      "protocol": "http",
      "host": "wmf-couchdb",
      "port": 5984,
      "connection_timeout": "${env:COUCH_CONNECTION_TIMEOUT}",
      "call_timeout": "${env:COUCH_CALL_TIMEOUT}"
    }
  }

``${env:COUCH_CONNECTION_TIMEOUT}`` will be replaced by the value of the environment variable "COUCH_CONNECTION_TIMEOUT" and
``${env:COUCH_CALL_TIMEOUT}`` will be replaced by the value of the environment variable "COUCH_CALL_TIMEOUT".
Setting environment variables is difficult for SolarThing instances that are not Dockerized,
but it is still possible with your own custom systemd configuration, or your own custom setup for running SolarThing.

Let's assume that the environment variable "ASDF" has a value of ``Hello there!`` and let's assume that the system property ``cool.text`` has a value of ``Awesome!``.
Let's assume today's date is 2023-03-28. Let's assume the Java version is 17.
Let's assume the file ``hello.txt`` has the content ``Hello!`` (with no new line).

.. csv-table:: Available Substitutions
  :header: "Name", "Example", "Result"

  "Environment", "``${env:ASDF}``", "Hello there!"
  "System Property", "``${sys:cool.text}``", "Awesome!"
  "System Property", "``${sys:user.dir}``", "/your/working/directory"
  "Base64 Decoder", "``${base64Encoder:SGVsbG9Xb3JsZCE=}``", "HelloWorld!"
  "Base64 Encoder", "``${base64Encoder:HelloWorld!}``", "SGVsbG9Xb3JsZCE="
  "Date", "``${date:yyyy-MM-dd}``", "2023-03-28"
  "Java", "``${java:version}``", "Java version 17.0.1"
  "Localhost", "``${localhost:canonical-name}``", "raspberrypi"
  "File content", "``${file:UTF-8:hello.txt}``", "Hello!"
  "URL Decoder", "``${urlDecoder:Hello%20World%21}``", "Hello World!"
  "URL Encoder", "``${urlEncoder:Hello World!}``", "Hello+World%21"


.. _log4j:

In ``log4j2.xml``
--------------------

Values present in ``log4j2.xml`` work very similar to how it is described above, but also have specific usages for Log4j.
For more information, go here: https://logging.apache.org/log4j/2.x/manual/configuration.html#PropertySubstitution.


.. _spring:

In Spring ``application.properties``
---------------------------------------

Values present in ``application.properties`` are handled differently than described above.
For more information, go here: https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.external-config.files.property-placeholders.
