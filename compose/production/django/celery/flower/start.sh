#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
    poetry run celery -A core inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

exec poetry run celery -A core \
    --broker="${CELERY_BROKER}" \
    flower \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"