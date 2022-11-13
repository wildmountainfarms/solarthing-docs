Remote Monitoring
====================

There are many ways to remotely monitor your system. This page demonstrates how to setup a way to remotely monitor
your system if you cannot port forward on your router or ISP.

On the device to monitor
--------------------------

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

Forward an entire network
-----------------------------

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
