import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

username_request = UsernameRequest(user_name = "CNGroup2")
val = client.GetUserByUsername(username_request)

if val:
    print("----------GetUserByUsername----------")
    print(val)
else :
    print("Empty")