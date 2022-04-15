from concurrent import futures
import os

from flask import Flask, render_template
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from users_pb2 import *
from users_pb2_grpc import UsersStub

from steam_pb2 import *
import steam_pb2_grpc

from pymongo import MongoClient
from bson.objectid import ObjectId

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)


"""from pymongo import MongoClient
from bson.objectid import ObjectId

db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test")
db = db['database']
db = db['users']

#app = Flask(__name__)

"""

def mostActive_users(result):
    user = UserInfo(
        user_name = result["user_name"],
        num_reviews = result["num_reviews"],
        num_games_owned = result["num_games_owned"],
        steamid = result["steamid"]      
    )
    return user

class SteamService(steam_pb2_grpc.SteamServicer):
    def ActiveUsers(self, request, context):
        db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test")
        db = db['database']
        db = db['users']
        #active_users_request = ActiveUsersRequest(request.max_results)
        #results = users_client.GetUsers(active_users_request).users
        results = list(db.find().sort("num_reviews", -1).limit(request.max_results))
        results = [mostActive_users(user) for user in results]
        
        return ActiveUsersResponse(user = results)
 
   
def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    steam_pb2_grpc.add_SteamServicer_to_server(
        SteamService(), server
    )
    
    server.add_insecure_port("[::]:50050")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()


"""
@app.route("/")
def render_homepage():
    users_request = ActiveUsersRequest(max_result=3)
    users_response = users_client.GetUsers(users_request)
	
    return render_template(
        "homepage.html",
        users = users_response.users,
    )
"""

"""from concurrent import futures
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

import sys
sys.path.insert(0, '../users')

from users_pb2 import *
from users_pb2_grpc import UsersStub

sys.path.insert(0, '../')

from steam_pb2 import *
import steam_pb2_grpc

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)
"""

