#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


exec poetry run celery -A core beat -l INFO