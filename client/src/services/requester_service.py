class RequesterService:
    def __init__(self, restService, grpcService):
        self.restService = restService
        self.grpcService = grpcService
        self.lastComm = 'REST'

    def save(self, data):
        if data['comm'] == 'REST':
            self.restService.save(data)
            self.lastComm = 'REST'
        elif data['comm'] == 'GRPC':
            self.grpcService.save(data)
            self.lastComm = 'GRPC'
        else:
            raise Exception(
                f"Communication pattern not supported: {data['comm']}"
            )

    def show(self):
        if self.lastComm == 'REST':
            return self._getRestUsersList()
        elif self.lastComm == 'GRPC':
            return self._getGrpcUsersList()
        else:
            raise Exception(
                f"Communication pattern not supported: {self.lastComm}"
            )

    def _getRestUsersList(self):
        return self.restService.get()['body']['message']

    def _getGrpcUsersList(self):
        return self.grpcService.get().users
