SolarThing
============

.. only:: not latex

  |release| |stars|

  .. |stars| image:: https://img.shields.io/github/stars/wildmountainfarms/solarthing.svg?style=social
    :target: https://github.com/wildmountainfarms/solarthing/stargazers

  .. |release| image:: https://img.shields.io/github/v/release/wildmountainfarms/solarthing.svg
    :target: https://github.com/wildmountainfarms/solarthing/releases


**SolarThing** is an application that can monitor data from a variety of solar charge controllers and inverters.
SolarThing supports running in Docker and also supports a native install.
Code and issues available at https://github.com/wildmountainfarms/solarthing.

SolarThing targets monitoring off-grid solar installations.
The Renogy Rover and EPEver Tracer are typically used for smaller scale off-grid setups, so you will likely not use SolarThing on a larger install or residential install.
The Outback MATE 1/2 is also supported, but is far less common than the cheaper charge controllers.


To jump to installation, go to :doc:`quickstart/install/index`.

Intro
------

SolarThing is fully configurable.
Create a JSON configuration file to configure how and where data from your charge controller goes!
Once configured, charge controller data is continuously uploaded to a database for viewing in Grafana, or your choice of data visualization.

|pic_grafana| |pic_android|

.. |pic_grafana| image:: /images/2023-07-25-wmf_grafana_dashboard.png
  :width: 70%
  :alt: Screenshot of Grafana Dashboard for Wild Mountain Farms Taken around 21:00 CDT on July 25, 2023

.. |pic_android| image:: /images/2023-07-25-solarthing_android_notification.jpeg
  :width: 25%
  :alt: Screenshot of the SolarThing Android notification for Wild Mountain Farms Taken around 21:00 CDT on July 25, 2023

SolarThing allows you to monitor your battery voltage, incoming solar power, and power usage.
Each datapoint can be graphed over time. Grafana allows you to view historical data and current data.
SolarThing also supports 1-Wire temperature sensors, so you can record the indoor or outdoor temperatures.
With more advanced configurations of SolarThing, it can be used as an automation system.

SolarThing supports Outback MATE 1 and 2, Renogy Rover and similar devices, EPEver Tracer charge controllers.
For more information, check out :doc:`about/supported-products`.

This shows an example setup of SolarThing and the connections between each component.
You may make your setup however you would like, with or without all the features shown in the diagram.

.. only:: latex

  .. figure:: /images/solarthing_diagram.png
    :width: 100%

.. only:: not latex

  .. figure:: /images/solarthing_diagram.svg
    :width: 100%


To install, checkout :doc:`quickstart/install/index`.

If you do not have your Raspberry Pi setup yet, you can instead start at :doc:`setup/headless-rpi`.

About
------

.. toctree::
  :maxdepth: 1
  :caption: About

  about/supported-products
  about/database-and-display
  about/faq

Quickstart
-------------

.. toctree::
   :maxdepth: 3
   :caption: Quickstart

   quickstart/install/index
   quickstart/serial-port/index
   quickstart/config/index
   quickstart/data/index

Documentation
----------------

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   config/index
   maintenance/index
   software/index
   setup/index
   develop/index
   misc/index

.. only:: not latex

  References
  -------------

  .. toctree::
     :maxdepth: 3
     :caption: Links

     GitHub <https://github.com/wildmountainfarms/solarthing>
     Report an Issue <https://github.com/wildmountainfarms/solarthing/issues>
