Configuration Continued
==========================

.. tabs::

  .. group-tab:: Docker Install

    Since you are done configuring SolarThing and you know that it works, you can simply run it in the background like so:

    .. code-block:: shell

      sudo docker compose up -d

    If you have configuration changes and need to restart SolarThing, you can do so like this:

    .. code-block:: shell

      sudo docker compose restart

  .. group-tab:: Native Install

    Go to :doc:`/config/systemd` to see how to install the systemd service.
