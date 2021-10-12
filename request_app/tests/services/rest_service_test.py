import requests, json
from unittest.mock import MagicMock
from src.services.rest_service import RestService

def test_post_request_is_being_called_with_proper_parameters():
	requests.post = MagicMock()

	service = RestService('http://tmp.com')
	payload = {'name': 'raven', 'email': 'reyes@ark.com'}
	service.save(payload)

	requests.post.assert_called_with('http://tmp.com/user', json=json.dumps(payload))

def test_get_request_is_being_called_with_proper_parameters():
	requests.get = MagicMock()

	service = RestService('http://tmp.com')
	service.get()

	requests.get.assert_called_with('http://tmp.com/user')

def test_get_works_even_with_connection_problems():
	requests.get = MagicMock()
	requests.get.side_effect = requests.exceptions.ConnectionError()

	service = RestService('http://tmp.com')
	result = service.get()

	requests.get.assert_called_with('http://tmp.com/user')
	assert result == {'body': {'message': []}}
