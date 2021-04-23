# MEAN

This is an example build with M(ongodb)E(xpress)A(ngular)N(ode.js)

They are separate in different directory, because we have different Dockerfile for each,
and want to show each one on their own.

## Mongo

You can use the script we create in the `mean/mongo` folder, and run mongo on your computer (need docker or podman instead first)

```sh
$ cd /mean/mongo
$ chmod +x run.sh
$ ./run.sh /path/to/where/you/store/your/data
```

Its important that you pass the `/path/to/where/you/store/your/data` because the script mount that path as a volume for the mongodb

## Express

This is a super simple REST API, and we are going to re-use this in several other examples.

```sh
$ cd /mean/express
$ npm start
```

It will start on port 3000, you could change it at start up time

```sh
$ PORT=[port_you_want] npm start
```
