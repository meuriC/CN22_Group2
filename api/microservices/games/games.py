from concurrent import futures

from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

import grpc
import pymongo

# connect to MongoDB

client = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test")
db = client["database"]
db = db["games"]

from games_pb2 import (
    GamesData,
    GamesDataResponse,
    GameByIdRequest,
    GameByNameRequest
)
import games_pb2_grpc


def games_response(result):

    game = GamesData (
        app_id = result["id"],
        app_name = result["name"],
        games_reviews_number = result["reviews_number"]
    )
    return game

class GamesService(games_pb2_grpc.GamesServicer):

    def GetGames(self, request, context):
        page = request.page * request.max_results
        results = list(db.find().skip(page).limit(request.max_results))
        results = [ games_response(games) for games in results ]
        return GamesDataResponse( games = results )

    def GameByID(self, request, context):
        try:
            results = list(db.find({"id": request.app_id}).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_response(results[0])
        except:
            return GamesData()
        

    def GameByName(self, request, context):
        try:
            results = list(db.find({"name": request.app_name }).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_response(results[0])
        except:
            return GamesData()


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )

    games_pb2_grpc.add_GamesServicer_to_server(
        GamesService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
	
if __name__ == "__main__":
    serve()