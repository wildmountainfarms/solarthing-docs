History of SolarThing
=========================

This program started in the summer of 2017.
This page talks about the history of SolarThing and has some anecdotes about design decisions that were made.


Inspiration
--------------

`@eidolon1138 <https://github.com/eidolon1138>`_ is the one who originally came up with the idea to collect data from his Outback Mate device.
He helped set up the database and `@retrodaredevil <https://github.com/retrodaredevil>`_ did the rest.
Eventually `@retrodaredevil <https://github.com/retrodaredevil>`_ created an android app making it much more convenient than a website.

`@retrodaredevil <https://github.com/retrodaredevil>`_ came up with the idea of the outhouse status when she walked all the way out to the outhouse only to find that it was occupied!
She walked all the way back inside, then went back out a few minutes later.
She knew that something had to be done about this first world problem.
The outhouse status is no more, but it was a fun little experiment.

SolarThing looks a lot different from its first fully functional version in 2018, but it's fun to look back on what it looked like years ago.

Timeline
---------

2017
^^^^^

* A perl script was created in a single day to collect data from an Outback Mate serial port
* The terrible perl script was ditched to start on the Java program. The program allowed packets to be added to a CouchDB database

2018
^^^^

* This continued in the summer of 2018. The formatting of the packets was completely rethought. The web application was created and completed in less than a week.
* An Android app was created to see the data continuously updated in a status notification

2019
^^^^

* Outhouse status was added
* Renogy rover support was added
* To maintain compatibility with the previous packet structure, Source and Fragment packets types were added to have the ability to have multiple instances uploading packets to a single database
* InfluxDB support was added allowing for easy configuration of a Grafana dashboard
* Raspberry Pi running the outhouse program didn't survive the freezing temperatures (RIP outhousepi 2019-2019)

2020
^^^^

* PVOutput was setup
* Outhouse code was completely removed from SolarThing codebase
* "Events Display" was added to the Android application
* RoverPi became corrupt, but was eventually re-flashed and set up again
* MatePi finally became corrupt. It was re-flashed, worked, then became corrupt again. (Need new SD card).
* Google Analytics were added
* Did a huge rebase to remove all solarthing.jar files, restructured program directory
* Added ability to read from DS18B20 temperature sensors
* Added GraphQL program
* Added message sending abilities for push notifications (Mattermost and eventually Slack)
* Added automation program that can help automate sending of commands and eventually became the base program for the message-sender program and other general 'actions'
* Added home assistant upload action
* Added ability to send data to Solcast along with GraphQL queries for Solcast
* message-sender program usable through automation program (removed message-sender program)


2021
^^^^

* InfluxDB 2.0 Support
* DCDC Controller monitoring bug fixed
* Pzem Shunt Support Added
* MQTT Support added
* Switched from Ektorp to custom CouchDB library
* Started to make some aspects of SolarThing use their own thread
* The buried cable connecting the MATE2 failed. MATE was moved into the Battery Room. The RPi0 was set up to monitor it, but soon the RPi0 died for an unknown reason and was replaced by an RPi3. Now most monitoring runs off that RPi3.


Anecdotes
-----------


Legacy Perl Script
^^^^^^^^^^^^^^^^^^^^

:blob:`c9069b8993b783c664705a36fd6c30965d7748f4/other/legacy/helloworld.pl` is a legacy program. It was the program that started SolarThing.
After learning perl for a day. I went straight back to Java, which I am more familiar with.

Moving from Gson to Jackson
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project started out with Gson, but as of 2019.12.24, I have started to move to Jackson. I originally chose Gson for its
simplicity. It has served this project very well and is very user friendly. However, I got tired of writing custom
deserializing functions to deserialize advanced packets. Jackson is very annotation orientated and is very
feature rich. The added complexity of Jackson is worth the speed of development it brings.

Configuration in the Early Days
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When developing SolarThing, I didn't want to hard code values everywhere in the code, so I decided to
go with command line arguments. For this, I decided to use `JCommander <https://github.com/cbeust/jcommander>`_.

JCommander was a great option until I wanted to use inheritance to define which types of programs can have
certain options. JCommander did not work with interfaces an `JewelCli <http://jewelcli.lexicalscope.com/>`_ did. JewelCli
is like the Retrofit of command line parsers. Defining options in interfaces gives you many options for how to structure
your configuration. If SolarThing or another one of my projects needs command line parsing again, JewelCli will be my go to library.

At this point, the command line arguments were pretty crazy. Plus, swapping out different configs meant changing the
file that actually ran the ``java -jar`` command. I knew it was time to move to JSON configuration. This allowed for a lot of
flexibility. While GSON was used to start with, the JSON configuration code was one of the reasons I felt like I needed to rewrite a lot
of the stuff that used JSON. I wasn't utilizing Gson's deserialization features, so I decided to switch
to Jackson altogether as explained above.

Currently the configuration is very easy to change. I can swap out what configuration I'm using easily and can
use the same CouchDB or InfluxDB configuration on multiple devices running SolarThing.


Getting Data into Grafana
^^^^^^^^^^^^^^^^^^^^^^^^^^

When support for InfluxDB was added in late 2019, it became easy to make a Grafana dashboard to display data.
However, this was not perfect. I had to maintain two different databases. CouchDB for nicely structured JSON
data, and InfluxDB for easy to query data. In 2020, I decided I wanted to be able to query data from CouchDB
without InfluxDB. After some searching, I found the graphql-datasource for Grafana. It was perfect. I did some
research on how to do a code first approach for a GraphQL program and ran into graphql-spqr. Now my schema was
already created without additional setup because of how awesome Java is. Now I could query CouchDB from Grafana
and even add additional data calculations that weren't in the packets to begin with.

