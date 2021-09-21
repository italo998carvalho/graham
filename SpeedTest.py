from test_config import POST_ITERACTIONS, GET_ITERACTIONS

class SpeedTest():
  def __init__(self, post, get):
    self.post = post
    self.get = get

  def runPost(self):
    users = []
    for v in range(POST_ITERACTIONS):
      payload = {}
      payload['email'] = f"name-{v}@gmail.com"
      payload['name'] = f"name-{v}"

      users.append(payload)

    for user in users:
      self.post(user)

  def runGet(self):
    for v in range(GET_ITERACTIONS):
      self.get()