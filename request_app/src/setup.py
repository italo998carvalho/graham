from services.RestService import RestService
from services.GrpcService import GrpcService

restService = RestService('http://localhost:5001')
grpcService = GrpcService('localhost:50051')
