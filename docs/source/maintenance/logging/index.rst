Logging
==========

All the SolarThing programs are configured to log. By default, each program's systemd service is configured not to log to journalctl.
This saves disk space and allows SolarThing's Log4j configuration to compress or delete old log files.

By default, SolarThing writes 3 different types of log files, each with different information in them.
The "summary" log files have the least amount of text in them.
"info" log files are in the middle, and "debug" log files have the most information in them.


.. toctree::
  :maxdepth: 3
  :caption: Contents

  view
