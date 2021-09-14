import requests, json
from rest.app_config import PORT

def post(payload):
  return requests.post(f"http://localhost:{PORT}/user", json = json.dumps(payload))

def get():
  return requests.get(f"http://localhost:{PORT}/user")
