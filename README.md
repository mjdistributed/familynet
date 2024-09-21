# Development

Package dependencies are installed in a virtualenv located at /Users/matt/workplace/familynet/.virtualenv

Activate the vitrualenv prior to running the app or installing any new packages by running `$ source .virtualenv/bin/activate`

See "Appendix" for a list of required packages.

## Running the app locally

`$ python server/main.py`

## Running the app locally in a container

1. Update working directory to ./server: `$ cd server`
1. Build the Docker image: `$ docker build -t familynet-dev .`
1. Run a container of the image: `$ docker run -p 5000:5000 familynet-dev`

## Unit Testing

TODO

# Deployment

To deploy the server to cloud run:

## One-time setup

### Initialize the gcloud CLI

1. Run `$ gcloud init`
1. Select the "familynet" configuration.

## For each new deployment

TODO

# Appendix

## Log of Installed Packages:

* Flask: `$ python -m pip install Flask`
