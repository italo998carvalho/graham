from flask import render_template

class RequesterService:
  def __init__(self, restService, grpcService):
    self.restService = restService
    self.grpcService = grpcService
    self.lastComm = 'REST'

  def save(self, data):
    if data['comm'] == 'REST':
      self.restService.save(data)
      self.lastComm = 'REST'
      return self._renderIndex(
        self._getRestUsersList()
      )
    elif data['comm'] == 'GRPC':
      self.grpcService.save(data)
      self.lastComm = 'GRPC'
      return self._renderIndex(
        self._getGrpcUsersList()
      )
    else:
      raise Exception(f"Communication pattern not supported: {data['comm']}")

  def show(self):
    if self.lastComm == 'REST':
      return self._renderIndex(
        self._getRestUsersList()
      )
    elif self.lastComm == 'GRPC':
      return self._renderIndex(
        self._getGrpcUsersList()
      )
    else:
      raise Exception(f"Communication pattern not supported: {self.lastComm}")

  def _renderIndex(self, usersList):
    return render_template('index.html', users=usersList)

  def _getRestUsersList(self, ):
    return self.restService.get()['body']['message']

  def _getGrpcUsersList(self, ):
    return self.grpcService.get().users
