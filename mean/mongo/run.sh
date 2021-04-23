#!/usr/bin/env bash

# run the mongod with <db-dir>
# @NOTE we are running podman here NOT docker
# we use podman instead SAME just replace docker with podman 
docker run -d -p 27017:27017 -v $1:/data/db --name mongodb docker.io/library/mongo
