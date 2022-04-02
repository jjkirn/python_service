# Python Flask - Nginx microservices with Docker

## The original authors' step by step guide is available on Medium
https://medium.com/@manos_fr/python-flask-scalable-microservices-using-docker-compose-and-nginx-load-balancer-e20d421b1ad6

## There were several changes made to the original project

1. Fixed issues with getting the project to run on Ubuntu 20.04 Desktop
2. Converted code to run under Python3 virtual environment (.venv)
3. Made changes to put all API keys into a .env file and excluded it from github (.gitignore), the API keys are read from the .env file via config.py

## After downloading the project using "git clone https://github.com/project", create the project's virtual environment

- Run the following in your project directory to create a Python3 .venv directory:
```
  $ python3 -m venv .venv
```
- To activate the virutal environment run:
```
  $ source .venv/bin/activate
```
- To deactivate the virutal environment run:
```
  $ deactivate
```
This will allow you to locally run parts of the project in the virtual environment.

## Both Dockerfile.news and Dockerfile.weather were modified use a virtual environment:
```
# Added by JJK to use virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
```

## Docker Engine Install - Ubuntu 20.04 Desktop

- [Install Docker Engine on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) :

```
  $ sudo apt-get update
  $ sudo apt install apt-transport-https ca-certificates curl software-properties-common
  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
  $ sudo apt install docker-ce
  $ sudo systemctl status docker
```
- Configure Docker Engine on Ubuntu 20.04 to run without sudo:

```
 $ sudo usermod -aG docker ${USER}
 $ su - ${USER}
```
## Docker Compose Install - Ubuntu 20.04 Desktop

- [Install Docker Compose on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04) :

```
  $ mkdir -p ~/.docker/cli-plugins/
  $ curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
  $ chmod +x ~/.docker/cli-plugins/docker-compose
  $ sudo chown $USER /var/run/docker.sock
  $ docker compose version
```

## Docker Compose - Run

- Run the microservices! (create 2 main API servers and use Nginx's load balancer)

```
$ docker compose up --build --scale master=2 

$ docker compose down (to kill and stop docker images)
```

- Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.

```
$ docker system prune -a
```

- Sample http requests in terminal

```
$ curl -XGET "localhost/weather?city=athens"
$ curl -XGET "localhost/news?country=gb"
```

- Architecture Overview:

![Arch](files/architecture.png)
