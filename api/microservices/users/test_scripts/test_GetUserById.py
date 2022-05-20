import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

user_request = IdRequest(user_id = "625ca6e44b01279a30c8cf5d")
val = client.GetUserById(user_request)
if val:
    print("----------GetUserByID----------")
    print(val)
else :
    print("Empty")