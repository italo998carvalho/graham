DOCKER_COMPOSE_CMD=docker-compose -f docker/docker-compose.yml
DIR=$(shell pwd)

up:
	@$(DOCKER_COMPOSE_CMD) up -d

down:
	@$(DOCKER_COMPOSE_CMD) down

run\:client:
	python3 client/src/app.py

run\:server\:rest:
	python3 servers/rest/app.py

run\:server\:grpc:
	python3 servers/grpc_/server.py

test\:client:
	pytest client/tests/

test\:client-cov:
	pytest --cov-config=.coveragerc --cov=client/ client/tests/
