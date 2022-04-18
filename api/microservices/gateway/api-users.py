import os
import re

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from users_pb2_grpc import UsersStub
from users_pb2 import *

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)


def createUser(UserItem):
    request = CreateUserRequest(user_language = UserItem["language"], user_name = UserItem["username"])  
    return users_client.CreateUser(request).user_name

def getUser(username):
    request = UsernameRequest(user_name = username)
    response = users_client.GetUserByUsername(request)
    return {"user_name": response.user_name, "user_id": response.user_id}

def deleteUserAccount(username):
    request = UsernameRequest(user_name = username)
    return users_client.DeleteUserByUsername(request).deleted 

def createReview(user_id, app_id, ReviewsItem):
    request = CreateReviewRequest(app_id = app_id, review = ReviewsItem["review"], recommended = ReviewsItem["recommended"], user_id = user_id)
    response = users_client.PostReview(request)
    return {"user_id": response.author_steam_id, "app_id": response.app_id, "review": response.review, "recommended": response.recommended}