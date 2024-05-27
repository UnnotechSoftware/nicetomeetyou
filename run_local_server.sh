#!/bin/bash
docker-compose up -d  --build
cd ./frontend || echo "Wrong Path...."
docker-compose up -d  --build
