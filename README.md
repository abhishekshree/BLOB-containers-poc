# BLOB-containers-poc

## Description

Client: Takes a file as input and uploads it to the `uploads` folder

Server:

- Lists all the files present in the `uploads` folder on `/`
- Can view a particular file on `/view/<name-of-file>`
- Zip and download the `uploads` folder on the `/download` endpoint.

To run all the services:
```
$ docker-compose up
```
