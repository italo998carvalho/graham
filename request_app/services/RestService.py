import requests, json

class RestService:
  def __init__(self, host):
    self.host = host

  def save(self, form):
    payload = {}
    payload['name'] = form['name']
    payload['email'] = form['email']
    return requests.post(f"{self.host}/user", json = json.dumps(payload))

  def get(self):
    return requests.get(f"{self.host}/user").json()
