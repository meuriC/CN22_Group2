import os
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from steam_pb2 import *
from steam_pb2_grpc import SteamStub

from games_pb2 import *
from users_pb2 import *

steam_host = os.getenv("STEAM_HOST", "localhost")
steam_channel = grpc.insecure_channel(f"{steam_host}:50050")
steam_client = SteamStub(steam_channel)


def getRecommendedGames():
    request = RecommendedGamesRequest(max_results = 10)
    
    gamesList = []
    for r in steam_client.RecommendedGames(request).games:
        object = {"id": r.id, "name": r.name}
        gamesList.append(object)
    return gamesList
	
def getActiveUsers():
    request = ActiveUsersRequest(max_results = 10)
	
    activeUsersList = []
    for r in steam_client.ActiveUsers(request).users:
        object = {"user_id": r.user_id, "user_name": r.user_name}
        activeUsersList.append(object)
    return activeUsersList
