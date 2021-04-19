# About
  This is a demo of kubernetes using 2 web applications (implemented with *flask*) 
 with *mongodb* backend and *redis* as cache

# Architecture
```
[ client ]  -> [ bugs:12345 ] ->  |-> [ redis:6379 ]
                     v            |
               [ notes:23456 ] -> |-> [ mongo:27017 ] 

```

# To access from client, expose the port:
`kubectl port-forward --address 0.0.0.0 deploy/deploy-bugs 12345:12345`

# Injecting linkerd (my linkerd version is 2.9):
0. Install linkerd (https://linkerd.io/2.9/getting-started/)
1. `linkerd check --pre`
2. `linkerd install | kubectl apply -f -`
3. `linkerd check`
4. Inject side-car: `cat deployment.yaml | linkerd inject - | kubectl apply -f -` (for each deployment)
5. `linkerd dashboard &`

# Seeding data:
1. Forward *mongodb* port
2. `python seed_data.py -c <whatever>`

# Accessing notes:
0. port forward `23456`
- health check: `curl localhost:23456/ping`
- bug list: `curl localhost:23456/_bugs`
- notes: `curl localhost:23456/notes/<bug-id>`


# Accessing bugs:
0. port forward `12345`
- health check: `curl localhost:12345/ping`
- bug list by user: `curl localhost:12345/bugs?user_id=sandy`
- bug details by bug: `curl localhost:12345/bugs?bug_id=BUG1234`

# TODO:
- Liveness probe
- Fault injection
- Circuit breaker (with `pyhysterix`)
