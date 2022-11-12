Configure Grafana Login
============================

To make your Grafana instance easy to access for all the users that want to
look at dashboards without being logged in, you can configure 
these settings.

Allow Anonymous User
---------------------------
Allowing the anonymous user allows people to view dashboards without looging in.

TODO link the documentation to configure this setting

Keep Users Logged in Longer
-------------------------------

https://grafana.com/docs/grafana/next/setup-grafana/configure-security/configure-authentication/grafana/

You can set ``login_maximum_inactive_lifetime_duration`` to be a larger value than ``7d``.

.. note::

    This does not always seem to work

Disable basic auth
---------------------

You may consider disabling basic auth if you are using the basic auth from a reverse proxy that is different from your Grafana login.
https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/grafana/#basic-authentication
