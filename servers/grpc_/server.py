import grpc
from sqlalchemy import create_engine
from concurrent import futures
from database import Base
import users.users_pb2_grpc as users_pb2_grpc
from services.UsersService import UsersService

engine = create_engine(
    'postgresql://comm-tests:comm-tests@localhost:15432/comm-tests', echo=True
)


def serve():
    print('Starting server...')
    Base.metadata.create_all(engine)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(
        UsersService(engine), server
    )
    server.add_insecure_port("[::]:50051")
    print(f'Started on port {50051}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
