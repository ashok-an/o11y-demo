#!/bin/bash

kubectl create ns demo
kubectl create -f deploy-mongo.yaml -f deploy-redis.yaml
kubectl create -f svc-mongo.yaml -f svc-redis.yaml
kubectl create -f cm-notes.yaml
kubectl create -f cm-bugs.yaml
kubectl create -f deploy-notes.yaml
kubectl create -f svc-notes.yaml
kubectl create -f deploy-bugs.yaml

echo "Run:"
echo kubectl port-forward -n demo --address 0.0.0.0 deploy/deploy-mongo 27017:27017
echo python ../seed_bugs.py -c 25
echo kubectl port-forward -n demo --address 0.0.0.0 deploy/deploy-bugs 12345:12345
echo curl localhost:12345/bugs
echo "Note: if this does not work, try port-forward for the port (instead of deployment)"
