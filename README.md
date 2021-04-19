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
4. Inject: `cat deployment.yaml | linkerd inject - | kubectl apply -f -` (for each deployment)
5. `linkerd dashboard &`
