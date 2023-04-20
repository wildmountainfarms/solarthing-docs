Docker Setup
==============

This page describes hwo to setup docker.

This page does not yet have documentation on how to run SolarThing in docker, but that documentation should be added soon.

Install Docker
----------------

https://docs.docker.com/engine/install/

Configure Docker
-------------------

Fix memory limit support on Raspberry Pi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you run ``docker info`` and get warnings shown below, then you may need to enable memory limit support.

.. code-block::

  ...
  WARNING: No memory limit support
  WARNING: No swap limit support
  WARNING: No kernel memory TCP limit support
  ...

To enable memory limit support edit ``/boot/cmdline.txt`` and add this:

.. code-block::

  cgroup_enable=memory swapaccount=1 cgroup_memory=1 cgroup_enable=cpuset

Now reboot your Rasbperry Pi. You can confirm the warnings go away when running ``docker info``.
You should now recreate your containers that you want to have memory limits and you can confirm they are working by running
``docker stats --no-stream``.

Related links:

* https://forums.raspberrypi.com/viewtopic.php?t=325521
* https://dalwar23.com/how-to-fix-no-memory-limit-support-for-docker-in-raspberry-pi/
