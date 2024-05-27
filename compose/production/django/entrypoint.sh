#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
poetry run python3 << END
import sys

import psycopg2

try:
    psycopg2.connect(
        dbname="${SQL_DATABASE}",
        user="${SQL_USER}",
        password="${SQL_PASSWORD}",
        host="${SQL_HOST}",
        port="${SQL_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'


rabbitmq_ready() {
    echo "Waiting for rabbitmq..."

    while ! nc -z rabbitmq 5672; do
      sleep 1
    done

    echo "rabbitmq started"
}

rabbitmq_ready

exec "$@"