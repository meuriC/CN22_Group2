import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

createUserRequest = CreateUserRequest(user_language = "portuguese", user_name = "CNGroup2")
res = client.CreateUser(createUserRequest)

createUserRequest2 = CreateUserRequest(user_language = "portuguese", user_name = "CompNuvem")
res2 = client.CreateUser(createUserRequest2)

if res:
    print("----------CreateUser----------")
    print(res)
    print(res2)
else :
    print("Empty")