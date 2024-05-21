#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

poetry run python3 manage.py migrate
poetry run python3 manage.py runserver 0.0.0.0:8000