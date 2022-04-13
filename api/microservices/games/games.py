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
    GameByNameRequest,
    GetMostReviewedGamesRequest,
    GetMostRecommendedGamesRequest, 
    DeletionResponse
)
import games_pb2_grpc


def games_response(result):

    game = GamesData (
        id = result["id"],
        name = result["name"],
        reviews_number = int(result["reviews_number"]),
        recommend_count = int(result["recommend_count"])
    )
    return game


def delete_game(result):
    deleted = DeletionResponse(deleted = True)
        
    return deleted


class GamesService(games_pb2_grpc.GamesServicer):

    def GetGames(self, request, context):
        results = list(db.find().sort("reviews_number", -1).limit(request.max_results))
        results = [ games_response(game) for game in results ]
        return GamesDataResponse( game = results )

    def GetRecommendedGames(self, request, context):
        results = list(db.find().sort("recommend_count", -1).limit(request.max_results))
        results = [ games_response(game) for game in results ]
        return GamesDataResponse( game = results )

    def GameByID(self, request, context):
        try:
            results = list(db.find({"id": request.id}).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_response(results[0])
        except:
            return GamesData()
        

    def GameByName(self, request, context):
        try:
            results = list(db.find({"name": request.name }).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_response(results[0])
        except:
            return GamesData()


    def CreateGame(self, request, context):

        result = db.insert({ 
             "id": "0", 
             "name": request.name,
             "reviews_number": 0, 
             "recommend_count": 0})

        resultFinal = db.find({"_id": result})
        db.update({ "_id" : resultFinal[0]["_id"] },{"$set": {  "id" : str(resultFinal[0]["_id"])}})
        return games_response(resultFinal[0])

    def DeleteGameByName(self, request, context):
        result = db.remove({"name": request.name})
        
        return delete_game(result)


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