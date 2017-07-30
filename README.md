# consul-demo

This is a sample demo of how consul, registrator work together to give auto service discovery.


This can be used as temporary test envirnment to test the web app with DB connectivity.

Just clone the repo and run docker compose command.

$  docker-compose up --build


Go to browser run http://127.0.0.1:8080/ , It will fetch the greeting message from the MYSQL DB and show as I web page.

Ex. Hello World!

The DB is loaded with MySQL dump file when docker is starting.
