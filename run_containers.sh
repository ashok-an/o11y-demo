#!/bin/bash
echo "Removing containers "
docker run -d -p 27017:27017 --name test-mongo mongo

docker run -d -p 6379:6379 --name test-redis -e ALLOW_EMPTY_PASSWORD=yes bitnami/redis:latest

docker run -d -p 23456:23456 \
  -e MONGODB_URI=mongodb://mongo:27017/db0 -e REDIS_HOST=redis -e REDIS_PORT=6379 \
  --link test-redis:redis --link test-mongo:mongo \
  --name test-notes ashoka007/test-notes

docker run -d -p 12345:12345 \
  -e MONGODB_URI=mongodb://mongo:27017/db0 -e REDIS_HOST=redis -e REDIS_PORT=6379 -e NOTES_BASE_URL=http://notes:23456 \
  --link test-redis:redis --link test-mongo:mongo --link test-notes:notes\
  --name test-bugs ashoka007/test-bugs

sleep 10
docker ps | grep "test-"
