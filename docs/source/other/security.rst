Security
=========

Security is important on any system, even if it is not running SolarThing software.
This page will help you harden your system and make it more secure.


Secure your SSH server
------------------------

.. note:: 

    This section is not for securing the ssh-port-forward-* containers. It is for securing/hardening SSHD daemons running on any of your devices.

If you have your SSH server exposed directly or indirectly (by using ssh port forwarding), your server will eventually start to be hit
with many login attempts from bots. You can secure your server by requiring a publickey to be used, rather than a password.
Before you make these optional but recommended changes, you should create an SSH key and use ``ssh-copyid`` command to authorize yourself
on your device. (See: https://www.ssh.com/academy/ssh/copy-id)

Typically one would just disable password authentication completely, but I prefer to only allow password authentication on local networks.
Edit ``/etc/ssh/sshd_config`` and add this at the bottom:

.. code-block::
    PasswordAuthentication no
    Match Address 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
      PasswordAuthentication yes

You can also install ``fail2ban`` on your system to automatically block spammers who attempt to login many times.

.. code-block:: sh
    sudo apt-get install -y fail2ban
    cd /etc/fail2ban
    cp jail.conf jail.local
    vi jail.local
    systemctl restart fail2ban

Secure Your Server With Firewall
-----------------------------------

You can use a firewall to block (or allow specific IPs) from connecting to certain ports.
This can be useful if you notice unknown IPs attempting to connect to your SSH port

.. note::
    Using ``ufw`` or ``/etc/hosts.deny`` without additional configuration will not block connections to docker containers 
    (that use bridge networks--the default when exposing ports) because of how docker modifies iptables.

.. code-block::

    sudo apt-get install -y ufw
    sudo ufw default allow incoming

    # These IPs are malicious. Feel free to create your own list, these are the ones I have gathered.
    sudo ufw deny from 91.212.166.22 # ssh bot with users: Admin, user, telnet, support
    sudo ufw deny from 91.240.118.172 # ssh bot with user: admin
    sudo ufw deny from 200.29.117.156 # ssh bot with user: rkz
    sudo ufw deny from 51.91.78.31 # ssh bot with user: teste
    sudo ufw deny from 188.166.188.181 # ssh bot with user: ahmed
    sudo ufw deny from 13.71.46.226 # ssh bot with user: rpms
    sudo ufw deny from 51.250.5.16 # ssh bot with user: rebecca
    sudo ufw deny from 200.70.56.204 # ssh bot with user: test
    sudo ufw deny from 62.204.41.176 # ssh bot with user: admin
    sudo ufw deny from 192.241.210.224 # ssh bot with user: hasmtpuser
    sudo ufw deny from 189.216.40.170 # ssh bot with user: hadoop
    sudo ufw deny from 134.209.69.41 # ssh bot with user: bbj
    sudo ufw deny from 200.75.16.212 # ssh bot with user: tomecat4
    sudo ufw deny from 157.230.53.66 # ssh bot with user: losif
    sudo ufw deny from 2.234.152.80 # ssh bot with user: mass
    sudo ufw deny from 82.196.113.78 # ssh bot with user: paulj
    sudo ufw deny from 60.51.38.237 # ssh bot with user: admin
    sudo ufw deny from 45.80.64.230 # ssh bot with user: cable
    sudo ufw deny from 117.79.226.120 # ssh bot with user: user
    sudo ufw deny from 154.68.39.6 # ssh bot with user: docm

    # To remove a rule
    sudo ufw delete deny from <ip address>

    sudo ufw reload
    sudo ufw enable
    sudo ufw logging medium

    # View log
    sudo less /var/log/ufw.log

To make this apply to docker containers, view this repository: https://github.com/chaifeng/ufw-docker.
Note that messing up the iptables configuration can mess up who can access your server.

A simpler method can be to edit ``/etc/hosts.deny`` if you don't want to install ufw. Note that this may not work with the ufw-docker
iptables update to apply to docker containers.

.. code-block::
    ALL : 91.212.166.22
    # You can add more from above

To learn more about ``/etc/hosts.deny``, you can view a tutorial such as https://linuxconfig.org/hosts-deny-format-and-example-on-linux.