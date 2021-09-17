import grpc
from .users.users_pb2 import (
  SaveUserRequest,
  UserResponse,
  GetUsersRequest,
  GetUsersResponse
)
from .users.users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50051")
client = UsersStub(channel)

def post(payload):
  request = SaveUserRequest(
    name = payload['name'],
    email = payload['email']
  )

  return client.Save(request)

def get():
  request = GetUsersRequest()
  return client.Get(request)
