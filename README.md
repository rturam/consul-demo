# consul-demo

This is a sample demo of how consul, registrator work together to give auto service discovery.


This can be used as temporary test envirnment to test the web app with DB connectivity.

Just clone the repo and run docker compose command.

$  docker-compose up --build


Go to browser run http://127.0.0.1:8080/ , It will fetch the greeting message from the MYSQL DB and show as I web page.

Ex. Hello World!

The DB is loaded with MySQL dump file when docker is starting.

This code created and tested on Amazon Linux only. If you are using other OS specially OSX or windows, you have to 
make changes in docker file for consul registration IPS.

Also please note, To allow Docker Containers to use Docker bridge as the DNS IP address, we need to add the following to Docker start options. For Ubuntu 14.04, we need to specify the following options in “/etc/default/docker”.
Latest docker versions use /etc/docker/daemon.json file for same purpose. 

DOCKER_OPTS="--dns 172.17.0.1 --dns 8.8.8.8 --dns-search service.consul"
