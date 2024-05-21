#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

poetry run python3 manage.py migrate
#poetry run python3 manage.py runserver 0.0.0.0:8000
/usr/local/bin/gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --chdir=/app