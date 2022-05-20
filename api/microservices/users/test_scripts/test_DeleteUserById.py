import sys
sys.path.append('../')

import grpc
from users_pb2 import * 
from users_pb2_grpc import UsersStub

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

UserCompNuvemId = ""
user_request = IdRequest(user_id = UserCompNuvemId)
val = client.DeleteUserById(user_request)

if val:
    print("----------DeleteUserById----------")
    print("Deleting CompNuvem")
    print(val)
else :
    print("Empty")