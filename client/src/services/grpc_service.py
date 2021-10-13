import grpc, logging
from proto_users.users_pb2 import (
  SaveUserRequest,
  GetUsersRequest
)
from proto_users.users_pb2_grpc import UsersStub

class GrpcService:
  def __init__(self, host):
    channel = grpc.insecure_channel(host)
    self.client = UsersStub(channel)

  def save(self, form):
    request = SaveUserRequest(
      name = form['name'],
      email = form['email']
    )

    return self.client.Save(request)

  def get(self):
    request = GetUsersRequest()
    try:
      return self.client.Get(request)
    except grpc._channel._InactiveRpcError as e:
      logging.error(f'Error trying to get users list: {str(e)}')
      class Object:
        def __init__(self):
          self.users = []

      return Object()
