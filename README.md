# PyAdder
Simple python app with multiple endpoints for demos.

## Build and run locally with Docker  
### Build
sudo docker build -t "pyadder:latest" .
### Run in foreground with shell:
docker run -it -p 80:80 pyadder:latest

## Use examples
### Locally browse or curl the following
For basic response: http://localhost:80/
For basic XML repsonse: http://localhost:80/xml
For basic addition of numbers: http://localhost:80/add?num1=444&num2=555

## Info
Forked from horvatca/PyAdder
Maintainer: chase.horvath@ibm.com
