#!/bin/bash

docker build -f Dockerfile.bugs -t ashoka007/test-bugs .

docker build -f Dockerfile.notes -t ashoka007/test-notes .
