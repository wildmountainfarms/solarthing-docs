Graylog 4
===========

I have had problems with this setup multiple times in the past.
This page serves to hold the documentation I wrote before updating it to Graylog 5.


.. code-block:: shell

    cd /opt/containers
    mkdir graylog
    cd graylog
    apt-get install -y pwgen  # need this to generate a good password_secret
    pwgen -N 1 -s 96  # copy this output, you will paste it below
    (read -s PASS && printf $PASS | sha256sum)  # type your password here and copy the SHA-256 output to paste later

    mkdir es_data/
    sudo chown -R 1000:root es_data  # es_data requires certain permissions for the elasticsearch image to like it

    mkdir mongo_data/
    sudo chown -R 2000:2000 mongo_data  # mongo allows any uid:gid combination, so we will use 2000 for both here

    mkdir -p graylog_data/config/
    wget https://raw.githubusercontent.com/Graylog2/graylog-docker/4.3/config/graylog.conf
    mv graylog.conf graylog_data/config/
    sudo chown -R 1100:1100 graylog_data  # graylog_data requires certain permissions for the graylog image to like it


Edit ``docker-compose.yml`` in the ``graylog`` directory and paste these contents into it:

.. code-block:: yaml

    # This example based on the combination of examples on https://docs.graylog.org/docs/docker
    version: '3'
    services:
      # MongoDB: https://hub.docker.com/_/mongo/
      mongo:
        image: mongo:4.2
        volumes:
          - ./mongo_data:/data/db
        user: "2000:2000"
        restart: unless-stopped
      # Elasticsearch: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/docker.html
      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
        volumes:
          - ./es_data:/usr/share/elasticsearch/data
        #user: "2000:2000" Specifying user does not work
        environment:
          - http.host=0.0.0.0
          - transport.host=localhost
          - network.host=0.0.0.0
          - "ES_JAVA_OPTS=-Dlog4j2.formatMsgNoLookups=true -Xms512m -Xmx512m"
          #- "ES_JAVA_OPTS=-Dlog4j2.formatMsgNoLookups=true -Xms512m -Xmx512m -XX:+UseG1GC"
        restart: unless-stopped
        ulimits:
          memlock:
            soft: -1
            hard: -1
        deploy:
          resources:
            limits:
              memory: 1g
      # Graylog: https://hub.docker.com/r/graylog/graylog/
      graylog:
        image: graylog/graylog:4.3
        container_name: graylog
        volumes:
          - ./graylog_data:/usr/share/graylog/data
        environment:
          # CHANGE ME (must be at least 16 characters)! https://docs.graylog.org/docs/manual-setup password_secret. Generated using pwgen
          - GRAYLOG_PASSWORD_SECRET=forpasswordencryption
          # Password: admin
          - GRAYLOG_ROOT_PASSWORD_SHA2=8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
          #- GRAYLOG_HTTP_EXTERNAL_URI=http://127.0.0.1:9000/
          - GRAYLOG_HTTP_EXTERNAL_URI=http://192.168.10.251:9100/
        entrypoint: /usr/bin/tini -- wait-for-it elasticsearch:9200 --  /docker-entrypoint.sh
        restart: unless-stopped
        depends_on:
          - mongo
          - elasticsearch
        ports:
          # Graylog web interface and REST API
          - 9100:9000
          # Syslog TCP
          - 1514:1514
          # Syslog UDP
          - 1514:1514/udp
          # GELF TCP
          - 12201:12201
          # GELF UDP
          - 12201:12201/udp

    #networks: # only uncomment this if you specify $DOCKER_MY_NETWORK in .env file
    #  default:
    #    name: $DOCKER_MY_NETWORK

.. note:: 

  The versions of the docker containers above were specifically chosen to work with the 4.X releases:
  https://go2docs.graylog.org/4-x/downloading_and_installing_graylog/installing_graylog.html

