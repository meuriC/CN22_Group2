import sys
from urllib import response
#sys.path.append('../')
sys.path.append('api/microservices/users/')

from users_pb2 import * 
from users_pb2_grpc import UsersStub
import grpc

channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

def test_getUsers():
    users_request = GetUsersRequest(max_result = 2)
    response = client.GetUsers(users_request)
    assert len(response.users) == 2, "test_getUsers failed"

def test_CreateUser():
    createUserRequest2 = CreateUserRequest(user_language = "portuguese", user_name = "CompNuvem")
    response = client.CreateUser(createUserRequest2)
    assert response.user_name == "CompNuvem", "test_CreateUser failed"

def test_DeleteUser():
    username_request = UsernameRequest(user_name = "CNGroup2")
    response = client.DeleteUserByUsername(username_request)
    assert response.deleted == True, "test_CreateUser failed"

def test_GetActiveUsers():
    users_request = GetUsersRequest(max_result = 5)
    response = client.GetActiveUsers(users_request)
    assert len(response.users) == 5 , "test_GetActiveUsers failed"