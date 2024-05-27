#!/bin/bash

set -o errexit
set -o nounset

poetry run watchfiles \
  --filter python \
  'celery -A core worker --loglevel=info -Q high_priority,default'