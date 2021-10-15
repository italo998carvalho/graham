# **Graham**
The goal of this project is to study a few different communication patterns between services. The repository consists of a client application that saves and lists users, and a few server applications, each one responding to a different pattern.

---
### **Project name**
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Alexander_Graham_Bell.jpg" height="350" />
</p>
This project was named after Alexander Graham Bell, considered the father of modern communication and creator of the telephone, so I thought it might be a good idea, also the first name was "service-comms-test", so I prefer the current one.

---
### **Requirements**
- python 3
- docker 20.10+ (didn't test in older versions)
- docker-compose 1.25+ (didn't test in older versions)

---
### **Supported patterns until now**
- REST
- gRPC

---
### **Generate protobuf files**
To generate the gRPC files this project uses a lib called `grpcio`, but after running the commands to generate the files, they are created with a wrong import statement from python2, which causes an error in python3 applications like this one. To solve this problem, we need to manually fix the imports of `servers/grpc_/users/users_pb2_grpc.py` and `client/src/proto_users/users_pb2_grpc.py` files in the line 5 from `import users_pb2 as users__pb2` to `from . import users_pb2 as users__pb2`. More discussions about this problem [here](https://github.com/grpc/grpc/issues/11041) and [here](https://github.com/grpc/grpc/issues/9450). 

##### Client files
```shell
$ python3 -m grpc_tools.protoc -I protobufs --python_out=client/src/proto_users/ --grpc_python_out=client/src/proto_users/ protobufs/users.proto
```

##### Server files
```shell
$ python3 -m grpc_tools.protoc -I protobufs --python_out=servers/grpc_/users/ --grpc_python_out=servers/grpc_/users/ protobufs/users.proto
```

---
### **Running**
As we have one client application and multiple servers application, each one needs to be ran separatelly in a different terminal.

**Note:** All of the following instructions should be executed from the repository root

#### **Preparing the environment (Run this steps just once) :**
1. Create python virtual env  
`$ python3 -m venv venv`

2. Enter in the virtual env  
`$ source venv/bin/activate`

3. Install the dependencies  
`$ pip install -r requirements.txt`

4. Generate grpc files | [Read here](#generate-protobuf-files)  
`$ make up:grpc`

5. Build the database containers  
`$ docker-compose -f docker/docker-compose.yml up -d`

#### **Running the applications (Run this steps in every terminal that applications will run)**:
1. Create python virtual env  
`$ python3 -m venv venv`

2. Enter in the virtual env  
`$ source venv/bin/activate`

3. Install the dependencies  
`$ pip install -r requirements.txt`

4. Run the applications  
`$ make run:client`  
`$ make run:server:rest`  
`$ make run:server:grpc`  

5. Access client application in `http://localhost:5000/`

**Really important note:** I got the Front-end code from somewhere in [this list](https://uicookies.com/beautiful-css-forms/), it's not responsive or very detailed, but does its job, and also this is not the purpose of this study case, so... ¯\\_(ツ)_/¯
