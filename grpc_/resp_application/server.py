import random, grpc
from concurrent import futures
from database import Base
from models.User import User
from users.users_pb2 import (
  SaveUserRequest,
  UserResponse,
  GetUsersRequest,
  GetUsersResponse
)
import users.users_pb2_grpc as users_pb2_grpc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://comm-tests:comm-tests@localhost:15432/comm-tests', echo=True)

class UsersService(users_pb2_grpc.UsersServicer):
  def __init__(self):
    Session = sessionmaker(bind = engine)
    self.session = Session()

  def Save(self, request, context):
    user = User(
      name = request.name,
      email = request.email
    )

    self.session.add(user)
    self.session.commit()

    return UserResponse(
      id = user.id,
      name = user.name,
      email = user.email
    )

  def Get(self, request, context):
    users_response = []
    for user in self.session.query(User).order_by(User.id):
      users_response.append(UserResponse(
        id = user.id,
        name = user.name,
        email = user.email
      ))
    
    return GetUsersResponse(users = users_response)

def serve():
  print('Starting server...')
  Base.metadata.create_all(engine)
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
