import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from users_pb2_grpc import UsersStub
from users_pb2 import *

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)


def createUser(body):
    request = CreateUserRequest(user_language = body["language"], user_name = body["username"])  
    return users_client.CreateUser(request).user_name

def getUser(username):
    request = UsernameRequest(user_name = username)
    response = users_client.GetUserByUsername(request)
    return {"username": response.user_name, "id": user_id}

def deleteUser(username):
    request = UsernameRequest(user_name = username)
    return users_client.DeleteUserByUsername(request).deleted 