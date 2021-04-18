#!/bin/bash
docker run -d -p 27017:27017 --name test-mongo mongo
docker run -d -p 6379:6379 --name test-redis -e ALLOW_EMPTY_PASSWORD=yes bitnami/redis:latest
sleep 10
docker ps | grep "test-"
