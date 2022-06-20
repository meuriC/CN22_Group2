import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

username_request = UsernameRequest(user_name = "usn76561198182228313")
val = client.DeleteUserByUsername(username_request)

if val:
    print("----------DeleteUserByUsername----------")
    print("Deleting usn76561198182228313")
    print(val)
else :
    print("Empty")