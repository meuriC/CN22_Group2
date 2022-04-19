import os
import re

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from games_pb2_grpc import GamesStub
from games_pb2 import *

games_host = os.getenv("GAMES_HOST", "localhost")
games_channel = grpc.insecure_channel(f"{games_host}:50051")
games_client = GamesStub(games_channel)

def gameReviews (id):
    request = GameReviewsRequest(app_id = id, max_results = 5)
    gamesList = []

    for r in games_client.GameReviews(request).reviews:
        object = {"user_id": r.author_steam_id, "review": r.review, "recommended": r.recommended, "language": r.language }
        gamesList.append(object)
    return gamesList


def getGameByName (name):

    request = GameByNameRequest(name = name)
    response = games_client.GameByName(request)
    return {"id" : response.id, 
    "name": response.name, 
    "reviews_number": response.reviews_number,
    "recommend_count":response.recommend_count}

def createGame (GamesItem):
    request = CreateGameRequest (name = GamesItem["name"])
    return games_client.CreateGame(request).name 


def deleteGameByName (name):
    request = GameByNameRequest(name = name)
    return games_client.DeleteGameByName(request).deleted

def getReviewByGame(id):
    request = GameReviewsRequest(app_id = id, max_results = 5)
    gameReviewsList = []
    for r in games_client.GameReviews(request).reviews:
        object = {"user_id": r.author_steam_id, "recommended": r.recommended, "language": r.language, "votes_helpful": r.votes_helpful, "timestamp_created": r.timestamp_created, "timestamp_updated": r.timestamp_updated, "review": r.review}
        gameReviewsList.append(object)
    return gameReviewsList