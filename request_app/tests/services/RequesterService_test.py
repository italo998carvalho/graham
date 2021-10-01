from src.services.requester_service import RequesterService

def test_something(restService, grpcService):
  requesterService = RequesterService(restService, grpcService)
  result = requesterService.save({'comm': 'REST'})

  assert result is True
