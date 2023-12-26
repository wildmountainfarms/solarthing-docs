Remote Monitoring
====================

.. warning::

  This page is considered legacy because this page is not complete enough to fully explain how to set everything up, or why it should be set up.

There are many ways to remotely monitor your system. This page demonstrates how to setup a way to remotely monitor
your system if you cannot port forward on your router or ISP.

.. todo::

  This page needs to be updated. Many parts of this page are just notes that are not easy for the average user to follow.

Use SSH Port Forward Client to make your device available for remote monitoring
--------------------------------------------------------------------------------

If you cannot directly port forward port 22 on your device, but have another device (on another network) that you can port forward on,
you can use an ssh port forward client to make port 22 available through the other device.

The rest of this section helps you configure this using 2 docker images, although if you wanted to you could figure this out yourself without any reliance on these programs.
These 2 docker images just use the ssh command under the hood.

Install docker:

.. code-block:: shell

    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh

    # confirm installed with compose:
    docker compose version

    cd /opt/containers/
    mkdir ssh-forward-client
    cd ssh-forward-client

Edit ``docker-compose.yml`` in the ``ssh-forward-client`` directory and paste these contents into it:

.. code-block:: yaml

    version: '3.7'

    services:
      ssh-forward-client:
        image: 'davidlor/ssh-port-forward-client:0.4.1'
        restart: unless-stopped
        network_mode: host
        environment:
          - 'MAPPINGS=R0.0.0.0:9025:127.0.0.1:22'
          - 'SSH_HOST=your ip here'
          - 'SSH_PORT=2222'
          - 'SSH_USER=ssh'
        volumes:
          - './keys/id_rsa:/ssh_key:ro'

Make sure to replace ``your ip here`` with your IP that will host the SSH server.
Now run these commands to create your private and public SSH keys:

.. code-block:: shell

    mkdir keys
    cd keys
    ssh-keygen -t rsa -N "" -f ./id_rsa
    cat id_rsa.pub
    cd ..

The ``cat id_rsa.pub`` command gives some output that you will need later. Copy it to a notepad so you can copy it again later.
Now go ahead and start this service using ``sudo docker compose up -d``.

Setting up the SSH Forward Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sub-section assumes that you need a separate SSH server. This section is usually optional because most people
are already running SSHD server daemon on the device that is able to port forward. In the case you want to use that, ignore this section
and create a user and add the authorized public key (copied above) to ``/home/<user>/.ssh/authorized_keys``.
In the case you want to have a separate SSH server just for forwarding ports (recommended), keep reading.

Install docker on this machine just like you did on your client machine.

.. code-block:: shell

    # Install docker like the above section showed

    # confirm installed with compose:
    docker compose version

    cd /opt/containers/
    mkdir ssh-forward-server
    cd ssh-forward-server
    touch sshkey.pub  # this is basically the same as your authorized_keys file

Edit ``docker-compose.yml`` in the ``ssh-forward-server`` directory and paste these contents into it:

.. code-block:: yaml

    version: '3.7'

    services:
      ssh-forward-server:
        image: 'davidlor/ssh-port-forward-server:0.1.1'
        restart: unless-stopped
        environment:
          - 'SSH_PORT=2222'
        ports:
          - '2222:2222'
          - '9025:9025'  # notice the *second* 9025 is the same as the 9025 above. You can change this to 7045:9025 if you would like, just keep the second port the same as the one used above
        volumes:
          - './sshkey.pub:/ssh_pubkey:ro'
          - './ssh-folder:/etc/ssh'

Now take the text from the public key in the last second, and paste it into the ``sshkey.pub`` you created.
You can now use ``docker compose up -d`` to start this server. The port 9025 on this device should forward all traffic to port 22 on your client device!

Updated Way of setting up SSH Forward Server
-------------------------------------------------

.. code-block:: shell

    # Install docker like the above section showed

    # confirm installed with compose:
    docker compose version

    cd /opt/containers/
    mkdir ssh-forward-server
    cd ssh-forward-server
    touch sshkey.pub  # this is basically the same as your authorized_keys file

Forward an entire network
-----------------------------

.. note::

  This section assumes that you have a device that you can SSH into on a remote network. (You can optionally do this after you finish setting up port forwarding an SSH port)

.. note::

  This section is for advanced users


If you have a network with a unique range of IPs, you can use redsocks to forward a proxy server created by SSH. For instance:

.. code-block:: shell

    # In one terminal:
    ssh -D 8181 -N batterypi

    # In another
    sudo apt install redsocks

    sudo vi /etc/sysctl.conf
    # uncomment net.ipv4.ip_forward=1
    sudo sysctl -p

    sudo vi /etc/redsocks.conf
    # set local_ip=127.0.0.1
    # set local_port=12777
    # set ip=127.0.0.1 (the ip of your SOCKS proxy server)
    # set port=8181 (the port of your SOCKS proxy server)
    sudo systemctl restart redsocks.service

    sudo iptables -t nat -N REDSOCKS
    sudo iptables -t nat -A REDSOCKS -p tcp -d 192.168.10.0/24 -j REDIRECT --to-ports 12777

    sudo iptables -t nat -A OUTPUT -p tcp -j REDSOCKS

    # check results
    sudo iptables -L -v -n -t nat --line-numbers

    # The easiest way to reset iptables if you mess up is to restart your computer
