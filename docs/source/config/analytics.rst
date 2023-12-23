Analytics
==================

For SolarThing versions 2023.3.0 and earlier, analytics data is sent to Google Analytics to get usage data from users and is **enabled by default**.
For SolarThing version 2023.4.0 and until an unknown future version, SolarThing does not collect analytics data,
but may do so if a new SolarThing version re-enables this feature.

No matter what version you are using, you may choose to opt out to analytic collection (on earlier versions),
or opt out of future analytic collection in the future (on future versions of SolarThing).

Opt Out
----------
To opt out, add ``"analytics_enabled": false`` to your `config/base.json` (with a comma afterwards if necessary). Once you opt out, no data will be sent to Google.

To opt out, you can also set the ``ANALYTICS_DISABLED`` environment variable. (Run ``export ANALYTICS_DISABLED=``).
NOTE: **This is temporary** unless you make sure this environment variable gets set before running SolarThing. (Only works in versions >= 2020.3.1)

The status of Google Analytics should be sent as one of the first **log messages**. Such as:
``Google Analytics is disabled`` or ``Google Analytics is ENABLED``. Log messages look different for SolarThing 2023.4.0 and onwards.


Collected Data
----------------

This data may include the following:

* The type of program running (mate, rover)
* The language and region of the user
* (Mate)The devices connected to the mate (FX, MX, FM)
* (Mate)The operational mode of FX devices
* (Rover)The model of the CC ex: "RNG-CTRL-RVRPG40" or "RCC20RVRE-G1", etc

This data **cannot** be used to uniquely identify you or your system. The data is anonymous.

Resetting ID (SolarThing 2023.3.0 and earlier)
-------------------------------------------------

To uniquely identify each SolarThing instance, a UUID is used and is stored. If you have this repository cloned, you should
see the file ``.data/analytics_data.json`` in one of the ``/opt/solarthing/program/<your program>`` directories. You can delete this file
to reset the ID and if Google Analytics is enabled, the next time you start SolarThing a new ID will be generated.

There is no reason you should have to reset this, but it's there if you want to.

Policy for SolarThing to follow (SolarThing 2023.3.0 and earlier)
-------------------------------------------------------------------------

Because SolarThing uses Google Analytics and its Measurement Protocol, it must follow `this policy <https://developers.google.com/analytics/devguides/collection/protocol/policy>`_.
If you do not believe it follows this policy, please create an issue on :issue-page:`our issue page <>`.


