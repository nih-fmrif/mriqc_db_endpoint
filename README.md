# MRIQC Flask API Endpoint

This API server is used to upload and download records into the MRIQC database.
The database backend uses MongoDB.

## Prerequisites

To install MongoDB, follow the instructions on the official [MongoDB docs
site](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/).

To install Flask and other Python dependencies, run:

    sudo python setup.py install

## Running

To start the Flask app, run:

    FLASK_APP=mriqc flask run

