#!/bin/bash
docker run -d -p 27017:27017 --name test-mongo mongo

sleep 10
docker ps | grep "test-"
