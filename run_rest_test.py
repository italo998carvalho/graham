import datetime
from test_config import POST_ITERACTIONS, GET_ITERACTIONS
from rest.req_methods.methods import post, get

users = []
for v in range(POST_ITERACTIONS):
  payload = {}
  payload['email'] = f"name-{v}@gmail.com"
  payload['name'] = f"name-{v}"

  users.append(payload)

starting = datetime.datetime.now()

for user in users:
  post(user)

print('Finished posting after: ' + str(datetime.datetime.now() - starting))

for v in range(GET_ITERACTIONS):
  get()

print('Finished getting after: ' + str(datetime.datetime.now() - starting))
