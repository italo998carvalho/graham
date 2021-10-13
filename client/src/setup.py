from services.rest_service import RestService
from services.grpc_service import GrpcService

restService = RestService('http://localhost:5001')
grpcService = GrpcService('localhost:50051')
