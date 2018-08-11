FROM python:3.7-alpine3.8
LABEL author="Marcus Mann"

WORKDIR /usr/src/app
COPY requirements.txt ./

# install gcc
RUN apk add --no-cache --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache --update postgresql-dev && \
    pip install psycopg2==2.7.1

RUN pip install --no-cache-dir  -r requirements.txt 

COPY . .