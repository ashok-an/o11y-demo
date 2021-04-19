## Steps
1. k create -f deploy-mongo.yaml -f deploy-redis.yaml
1a. kubectl port-forward --address 0.0.0.0 deploy/deploy-mongo 27017:27017
1b. python ../seed_bugs.py -c 25
2. k create -f svc-mongo.yaml -f svc-redis.yaml
3. k create -f cm-notes.yaml
4. k create -f deploy-notes.yaml
5. k create -f svc-notes.yaml
6. k create -f deploy-bugs.yaml
7. kubectl port-forward --address 0.0.0.0 deploy/deploy-bugs 12345:12345
7a. curl localhost:12345/bugs
Note: if this does not work, try port-forward for the port (instead of deployment)
