from concurrent import futures

import connexion as connexion
import grpc
import os
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
# 3rd party modules
from flask import make_response, abort
from flask import Flask, render_template
from games_pb2 import *
from games_pb2_grpc import GamesStub


recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")

games_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
games_client = GamesStub(games_channel)


app = connexion.App(__name__, specification_dir="./")


if __name__ == "__main__":

    print("Find game by ID: 203160")
    games_request = GameByIdRequest(
        app_id="203160"
    )
    games_response = games_client.SearchById(
        games_request
    )
    if(games_response is None):
        print("Game not found")
    else:
        print(games_response.game)

    print("Find game by name: Rocket League")
    games_request = GamesByNameRequest(
        app_name = "Rocket League"
    )
    games_response = games_client.SearchByName(
        games_request
    )
    if(games_response is None):
        print("Game not found")
    else:
        print(games_response.game)
    