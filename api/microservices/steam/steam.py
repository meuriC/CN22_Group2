import os

from flask import Flask, render_template
import grpc

from users_pb2 import *
from users_pb2_grpc import UsersStub

app = Flask(__name__)

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)


@app.route("/")
def render_homepage():
    users_request = GetUsersRequest(max_result=3)
    users_response = users_client.GetUsers(users_request)
	
    return render_template(
        "homepage.html",
        users = users_response.users,
    )

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

class SteamService(steam_pb2_grpc.SteamServicer):
    def ActiveUsers(self, request, context):
        active_users_request = ActiveUsersRequest(request.user, request.max_results)
        results = users_client.ActiveUsers(active_users_request).users
        return results
    
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
    serve()"""
