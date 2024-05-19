#!/bin/bash
echo "========== Create Network =========="
docker network create frontend
docker network create web_network
echo "If networks are already exist, please skip those messages."
cd ./frontend || echo "Wrong Path...."
docker-compose up -d
cd -
docker-compose up -d
