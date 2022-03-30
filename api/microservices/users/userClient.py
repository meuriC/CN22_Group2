import sys
sys.path.append('../')

import grpc

from users_pb2 import UsernameRequest
from users_pb2 import GetUsersRequest
from users_pb2 import CreateUserRequest
from users_pb2_grpc import UsersStub



channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

#Test GetUser by ID
"""user_request = UsernameRequest(user_id="62439da17e360515056f336b")
val = client.GetUser(user_request)
if val:
    print("Database Flag")
    print(val)
else :
    print("Empty")"""

#Test GetUsers
"""users_request = GetUsersRequest(max_result=2)
val = client.GetUsers(users_request)
if val:
    print("Database Flag")
    print(val)
else :
    print("Empty")"""

#Test CreateUser
"""createUserRequest = CreateUserRequest(user_name="miguelfsilva")
res = client.CreateUser(createUserRequest)
if res:
    print("Database Flag")
    print(res)
else :
    print("Empty")"""
