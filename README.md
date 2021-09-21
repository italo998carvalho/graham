# service-comm-tests

## Generate protobuf files

```shell
python3 -m grpc_tools.protoc -I grpc_/protobufs --python_out=grpc_/req_methods/users/ --grpc_python_out=grpc_/req_methods/users/ grpc_/protobufs/users.proto
```

```shell
python3 -m grpc_tools.protoc -I grpc_/protobufs --python_out=grpc_/resp_application/users/ --grpc_python_out=grpc_/resp_application/users/ grpc_/protobufs/users.proto
```
