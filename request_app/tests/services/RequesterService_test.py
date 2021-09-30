from src.services.RequesterService import RequesterService

def test_something(restService, grpcService):
  requesterService = RequesterService(restService, grpcService)
  result = requesterService.save({'comm': 'REST'})

  assert result is True
