#!/bin/bash

docker build -t api_tests
docker run --name my_run api_tests
docker system prune
