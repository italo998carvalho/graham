from sqlalchemy.orm import sessionmaker
from models.User import User
from users.users_pb2 import (UserResponse, GetUsersResponse)
import users.users_pb2_grpc as users_pb2_grpc


class UsersService(users_pb2_grpc.UsersServicer):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def Save(self, request, context):
        user = User(
            name=request.name,
            email=request.email
        )

        self.session.add(user)
        self.session.commit()

        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email
        )

    def Get(self, request, context):
        users_response = []
        for user in self.session.query(User).order_by(User.id):
            users_response.append(UserResponse(
                id=user.id,
                name=user.name,
                email=user.email
            ))

        return GetUsersResponse(users=users_response)
