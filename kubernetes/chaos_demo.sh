#!/bin/bash

kubectl create deployment nginx --image=nginx --replicas=2 --namespace=chaos-ns
sleep 5
kubectl get pods -n chaos-ns
kubectl apply -f chaos_pod_delete.yaml
sleep 5
kubectl get pods -n chaos-ns
kubectl describe chaosresult nginx-chaos-pod-delete -n chaos-ns
sleep 10
kubectl apply -f chaos_pod_scale.yaml
sleep 10
kubectl get pods -n chaos-ns
