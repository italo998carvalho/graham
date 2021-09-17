from concurrent import futures
import random, grpc
from users.users_pb2 import (
  SaveUserRequest,
  UserResponse,
  GetUsersRequest,
  GetUsersResponse
)
import users.users_pb2_grpc as users_pb2_grpc

class UsersService(users_pb2_grpc.UsersServicer):
  def Save(self, request, context):
    # logic to save payload on database

    return UserResponse(
      id = 123,
      name = "Italo",
      email = "italo@gmail.com"
    )

  def Get(self, request, context):
    # logic to get users from DB

    return GetUsersResponse(
      users = [
        UserResponse(
          id = 123,
          name = "Italo",
          email = "italo@gmail.com"
        ),
        UserResponse(
          id = 321,
          name = "Ester",
          email = "ester@gmail.com"
        )
      ]
    )

def serve():
  print('Starting server...')
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  users_pb2_grpc.add_UsersServicer_to_server(
    UsersService(), server
  )
  server.add_insecure_port("[::]:50051")
  print(f'Started on port {50051}')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
  serve()
