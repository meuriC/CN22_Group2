
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB

db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test")
db = db['database']
db = db['users']

import users_pb2_grpc
from users_pb2 import (
    UserData,
    CreateUserResponse,
    UsersDataList
)

def marshalUserdbToUserService(result):
    user = UserData(
        nick_name = result["user_name"],
        num_reviews = result["user_num_reviews"],
        num_games_owned = result["user_num_games_owned"],
    )
    return user

def create_user(result):
    user = CreateUserResponse(
        user_name = result["user_name"],
        user_id = result["user_id"],
        user_num_games_owned = result["user_num_games_owned"],
        user_num_reviews = result["user_num_reviews"],
        user_playtime_forever = result["user_playtime_forever"],
        user_playtime_last_two_weeks = result["user_playtime_last_two_weeks"],
        user_playtime_at_review = result["user_playtime_at_review"],
        author_last_played = result["author_last_played"],
        user_pwd = result["user_pwd"],
    )
    return user
    

class UserService(users_pb2_grpc.UsersServicer):
    def GetUser(self, request, context):
        results = db.find({"_id": ObjectId(request.user_id)})
        #print(results[0])
        return marshalUserdbToUserService(results[0])

    def CreateUser(self, request, context):
        results = db.insert({ "user_name": request.user_name,
             "user_id": "0", 
             "user_num_games_owned": 0, 
             "user_num_reviews": 0, 
             "user_playtime_forever": 0,
             "user_playtime_last_two_weeks": 0,
             "user_playtime_at_review": 0,
             "author_last_played": 0,
             "user_pwd": "clear"})
        resultsFinal = db.find({"_id": results})
        #print(resultsFinal[0])
        return create_user(resultsFinal[0])

    def GetUsers(self, request, context):
        results = list(db.find().limit(request.max_result))
        usersList=[]
        for user in results:
            usersList.append(marshalUserdbToUserService(user))
        return UsersDataList(users=usersList)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    users_pb2_grpc.add_UsersServicer_to_server(
        UserService(), server
    )
    
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()