# MRIQC Flask API Endpoint

This API server is used to upload and download records into the MRIQC database.
The database backend uses MongoDB.

## Prerequisites

To install MongoDB, follow the instructions on the official [MongoDB docs
site for Centos](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
or [Digital Ocean docs for Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04). After installing, start the mongodb service. If it fails to start, you may need to reboot the server.

To install Flask and other Python dependencies, run:

    sudo python setup.py install

## Running

To start the Flask app, run:

    FLASK_APP=mriqc flask run

