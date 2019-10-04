#!/usr/bin/env bash

COMPOSE_HTTP_TIMEOUT=200
docker-compose -p lifehacker_test build
docker-compose -p lifehacker_test up
