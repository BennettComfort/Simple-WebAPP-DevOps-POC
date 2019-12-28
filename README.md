# Simple-WebAPP-DevOps-POC
 This is a containerized web application project showcasing DevOps practices

> I am using Ubuntu 19.10 operating system and visual studio code to develop this web application FYI

This project builds a containerized web application using docker and flask. After building the docker image, running the image a page will be created on 0.0.0.0:41029 that returns a UUID in form a string

### Steps
> sudo docker build -t bennett/simple-webapp-devops-poc .

> sudo docker run -p 49160:8080 -d bennett/simple-webapp-devops-poc

enter 0.0.0.0:41029 in your browser

### Requirements
1. Docker installed on machine
2. Python
    - virtualenv
    - flask
    - waitress
    - httpd
    - apache2

