# auth0-serverless-flask-app

This is a Serverless Flask web application with Auth0 authentication. I followed the [Auth0 python web-app quickstart](https://auth0.com/docs/quickstart/webapp/python) for guidance.

## Requirements

* Python 3.7+
* Set up an Auth0 app

Install requirements with `pip install -t requirements.txt` 

## Deploying with Docker Desktop

Build the image using `docker build -t auth0-flask-app .`

Run the image using `docker run -dp 5000:5000 auth0-flask-app`

## Deploying on AWS

Deploy the app using the [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/intro/)

TBD