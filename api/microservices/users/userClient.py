import sys
sys.path.append('../')

import grpc

from users_pb2 import UsernameRequest
from users_pb2 import CreateUserRequest
from users_pb2_grpc import UsersStub



channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

user_request = UsernameRequest(user_id="6241bf85fc6ffe00ae5c4809")
val = client.GetUser(user_request)
if val:
    print("Foi a BD, mas deu coco")
    print(val)
else :
    print("Empty")

createUserRequest = CreateUserRequest(user_name="miguelfsilva")
res = client.CreateUser(createUserRequest)
if res:
    print("Database Flag")
    print(res)
else :
    print("Empty")
