FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/docker
WORKDIR /code

RUN \
  apk add --no-cache \
  musl-dev \
  gcc \
  postgresql-dev && \
  apk add --no-cache \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
  openssl \
  gdal-dev \
  geos-dev \
  proj4-dev

COPY . /code/
RUN python3 -m pip install gunicorn --no-cache-dir
RUN python3 -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT /code/docker/docker-entrypoint.prod.sh
