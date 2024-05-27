#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
poetry run celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler