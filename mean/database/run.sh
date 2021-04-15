# run the mongod with <db-dir>
# @NOTE we are running podman here NOT docker

podman run -d -p 27017:27017 -v ./:/data/db --name mongodb docker.io/library/mongo
