FROM ubuntu:latest
FROM heroku/heroku:18-build AS builder

RUN apt-get -y update; \
    apt-get -y upgrade; \
    apt-get -y install apt-utils \
    vim \
    htop;

RUN apt-get -y install dstat
ARG RAILS_ENV=production
ARG FOO


CMD ["bash"]


