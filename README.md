# Django Sandbox

## Prerequistis

One needs to install the docker application

## How to start an container

To build a container one needs to have a Dockerfile with an image.

Then one writes `docker build` that build the container. The flag -t means to tag it and one can then give it a name to make it easier to understand what container it is. The last part is the relative path to the folder of the dockerfile.

```bash
docker build -t welcome-to-docker .
```

After that one can start the container from the terminal with:

```bash
docker start welcome-to-docker
```

Then when entering the localhost:port one is greeted with:
![Alt text](docs/images/first_container.png)

For stopping the container from command line one can run:

```bash
docker kill welcome-to-docker
```

## Welcome-to-docker

This is the sample application from the good people at docker.
Original repository: https://github.com/docker/welcome-to-docker

### The python docker guild:

https://docs.docker.com/language/python/?uuid=9D25135B-2405-44D3-BB23-CCCA2D0BB0BE

### The GO lang docker guild:

https://docs.docker.com/language/golang/?uuid=9D25135B-2405-44D3-BB23-CCCA2D0BB0BE

### The Java docker guild:

https://docs.docker.com/language/java/?uuid=9D25135B-2405-44D3-BB23-CCCA2D0BB0BE

### The Rust docker guild:

https://docs.docker.com/language/rust/?uuid=9D25135B-2405-44D3-BB23-CCCA2D0BB0BE
