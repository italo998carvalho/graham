import pytest
from src.services.requester_service import RequesterService


def test_rest_service_is_being_called_properly_on_save(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    requesterService.save(
        {'comm': 'REST', 'name': 'John', 'email': 'john@email.com'}
    )

    restService.save.assert_called_with(
        {'comm': 'REST', 'name': 'John', 'email': 'john@email.com'}
    )
    grpcService.save.assert_not_called()


def test_grpc_service_is_being_called_properly_on_save(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    requesterService.save(
        {'comm': 'GRPC', 'name': 'John', 'email': 'john@email.com'}
    )

    grpcService.save.assert_called_with(
        {'comm': 'GRPC', 'name': 'John', 'email': 'john@email.com'}
    )
    restService.save.assert_not_called()


def test_exception_is_being_thrown_if_wrong_communication_name_is_sent_on_save(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    with pytest.raises(Exception) as excinfo:
        requesterService.save(
            {'comm': 'ANY_NAME', 'name': 'John', 'email': 'john@email.com'}
        )

    assert str(excinfo.value) == "Communication pattern not supported: ANY_NAME"
    grpcService.save.assert_not_called()
    restService.save.assert_not_called()


def test_rest_service_is_being_called_properly_on_show(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    requesterService.lastComm = 'REST'
    result = requesterService.show()

    assert result == [{'name': 'john'}, {'name': 'mary'}]
    restService.get.assert_called_once()
    grpcService.get.assert_not_called()


def test_grpc_service_is_being_called_properly_on_show(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    requesterService.lastComm = 'GRPC'
    result = requesterService.show()

    assert result == [{'name': 'john'}, {'name': 'mary'}]
    grpcService.get.assert_called_once()
    restService.get.assert_not_called()


def test_exception_is_being_thrown_if_wrong_communication_name_is_sent_on_get(restService, grpcService):
    requesterService = RequesterService(restService, grpcService)
    requesterService.lastComm = 'ANY_NAME'
    with pytest.raises(Exception) as excinfo:
        requesterService.show()

    assert str(excinfo.value) == "Communication pattern not supported: ANY_NAME"
    grpcService.get.assert_not_called()
    restService.get.assert_not_called()
