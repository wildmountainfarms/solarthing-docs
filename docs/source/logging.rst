Logging
==========

All the SolarThing programs are configured to log. By default, each program's systemd service is configured not to log to journalctl.
This saves disk space and allows SolarThing's Log4j configuration to compress or delete old log files.


Viewing Logs
----------------

Viewing SolarThing's log files is a good way to see if anything is going wrong, or to just view debug information to see data.

Let's assume that we have a program configured in the ``/opt/solarthing/program/custom_rover`` directory. To view logs, go ahead and ``cd``:

.. code-block:: shell

    cd /opt/solarthing/program/custom_rover/logs
    ls -l

You will now see all of the logs in the directory. You may see lots of files with a ``.log.gz`` extension. Those files are the old log files.
There should also be three files that have the current logs: ``log_summary.log``, ``log_info.log`` and ``log_debug.log``.

To view info logs:

.. code-block:: shell

    less -R log_info.log

.. note:: 
    
    While you can use ``nano`` to view log files, it is not recommended because it will not view colors well and is not good at opening large files.
    ``vi`` and ``vim`` are also not good for viewing log files containing color.


Now you can browse around.

You can also look at the logs "live", by using this command:

.. code-block:: shell

    tail -f log_debug.log

.. note:: 
    
   By default the debug log output is not "flushed" immediately. That means that while viewing it data will be cut off.
   This is to reduce the amount of time spent writing to disk, which is critical in maintaining a stable system on Raspberry Pis.

If you do not want to switch between ``less -R`` and ``tail -f``, you can just use ``less -R`` by itself. 
When you want to start "tailing" a file, just press Shift+F. When you want to go back to browsing the file, just press CTRL+C.

If you want to reload the file while inside of ``less -R``, just type Shift+R (``R``). ``less`` is such a useful tool!


Types of logs
---------------

You've seen above that there are three log files. The "summary" log files have the least amount of text in them. 
"info" log files are in the middle, and "debug" log files have the most information in them.


Decompressing logs
---------------------

As mentioned earlier, old log files have a ``.log.gz`` extension. If you need to view these log files, you must first decompress them.

Here is an example of how to decompress a particular log file:

.. code-block:: shell

    
