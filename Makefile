DOCKER_COMPOSE_CMD=docker-compose -f docker/docker-compose.yml
DIR=$(shell pwd)

up:
	@$(DOCKER_COMPOSE_CMD) up -d

down:
	@$(DOCKER_COMPOSE_CMD) down

run\:client:
	python3 client/src/app.py

test\:client:
	pytest client/tests/

test\:client-cov:
	pytest --cov-config=.coveragerc --cov=client/ client/tests/
