#!/bin/bash

docker rmi -f consuldemo_web
rm -rf data/*
docker-compose down

