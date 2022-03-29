
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
user = "CN_Grupo11"
password = "jcAUsQouhCddO0xW"
credentials = user + ":" + password

db = MongoClient("mongodb+srv://" + credentials + "@users.lastb.mongodb.net/test")
db = db["users"] #TODO : alterar o nome para database
db = db["users"]

import users_pb2_grpc
from users_pb2 import (
    UserData,
)

def marshalUserdbToUserService(result):
    UserData = UserData(
        nick_name = result["username"],
        num_reviews = result["author.num_reviews"],
        num_games_owned = result["author.num_games_owned"],
    )
    return UserData

class UserService(users_pb2_grpc.UsersServicer):
    def GetUser(self, request, context):
        try:
            results = list(db.find({"id": ObjectId(request.user_id)}).limit(1))
            if len(results) <= 0:
                return UserData()
            return marshalUserdbToUserService(results[0])
        except:
            return UserData()

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