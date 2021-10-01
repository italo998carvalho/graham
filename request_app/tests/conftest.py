import pytest
from unittest.mock import MagicMock

class Object:
  pass

@pytest.fixture
def restService():
  service = Object()
  service.save = MagicMock(return_value={'body': {'message': 'XYZ'}})
  service.get = MagicMock(return_value={'body': {'message': [
    {'name': 'john'},
    {'name': 'mary'}
  ]}})

  return service

@pytest.fixture
def grpcService():
  class Response():
    def __init__(self):
      self.users = [
        {'name': 'john'},
        {'name': 'mary'}
      ]

  service = Object()
  service.save = MagicMock(return_value=Response())
  service.get = MagicMock(return_value=Response())

  return service
