import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

users_request = GetUsersRequest(max_result = 2)
val = client.GetUsers(users_request)

if val:
    print("----------GetUsers----------")
    print(val)
else:
    print("Empty")