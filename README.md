# Development

Package dependencies are installed in a virtualenv located at /Users/matt/workplace/familynet/.virtualenv

Activate the vitrualenv prior to running the app or installing any new packages by running `$ source .virtualenv/bin/activate`

See "Appendix" for a list of required packages.

## Running the app locally

`$ python server/main.py`

## Running the app locally in a container

1. Build the Docker image: `$ docker build -t familynet-dev:head server/`
1. Run a container of the image: `$ docker run -p 8080:8080 familynet-dev:head`

## Unit Testing

TODO

# Deployment

To deploy the server to cloud run:

## One-time setup

### Initialize the gcloud CLI

1. Run `$ gcloud init`
1. Select the "familynet" configuration.

## For each new deployment

### Build & Push the image to Artifact Registry

1. Build the Docker image you'd like to deploy (see "Running the app locally in a container")
1. Tag the image with the Artifact Registry Repository name:
    ```
    $ docker tag familynet-dev:head \
    us-docker.pkg.dev/familynet-434915/familynet-docker/familynet-dev:head
    ```
1. Push the image to Artifact Registry:
    ```
    $ docker push us-docker.pkg.dev/familynet-434915/familynet-docker/familynet-dev:head
    ```

### Deploy the image to Cloud Run

TODO

# Appendix

## Log of Installed Packages:

* Flask: `$ python -m pip install Flask`
