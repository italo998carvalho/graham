DIR=$(shell pwd)

test\:requester:
	pytest request_app/tests/

test\:requester-cov:
	pytest --cov-config=.coveragerc --cov=request_app/ request_app/tests/
