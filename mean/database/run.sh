# run the mongod with <db-dir>

docker run -d -p 27017:27017 -v ./:/data/db --name mongodb docker.io/library/mongo
