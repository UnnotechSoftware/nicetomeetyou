#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

poetry run python /app/manage.py collectstatic --noinput
poetry run python /app/manage.py migrate

/usr/local/bin/gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --chdir=/app