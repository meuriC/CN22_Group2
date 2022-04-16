from concurrent import futures
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from games_pb2 import *
from games_pb2_grpc import GamesStub

from steam_pb2 import *
import steam_pb2_grpc

from pymongo import MongoClient
from bson.objectid import ObjectId

games_host = os.getenv("GAMES_HOST", "localhost")
games_channel = grpc.insecure_channel(f"{games_host}:50051")
games_client = GamesStub(games_channel)


"""def mostActive_users(result):
    user = UserInfo(
        user_name = result["user_name"],
        num_reviews = result["num_reviews"],
        num_games_owned = result["num_games_owned"],
        steamid = result["steamid"]      
    )
    return user"""

class SteamService(steam_pb2_grpc.SteamServicer):
    """def ActiveUsers(self, request, context):
        db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test")
        db = db['database']
        db = db['users']
        #active_users_request = ActiveUsersRequest(request.max_results)
        #results = users_client.GetUsers(active_users_request).users
        results = list(db.find().sort("num_reviews", -1).limit(request.max_results))
        results = [mostActive_users(user) for user in results]
        
        return ActiveUsersResponse(user = results)"""
    def RecommendedGames(self, request, context):
        game_request = GetMostRecommendedGamesRequest(max_results = request.max_results)
        result = games_client.GetRecommendedGames(game_request).game
		
        finalResult = [GameInfo(id=r.id, name=r.name, reviews_number=r.reviews_number, recommend_count=r.recommend_count) for r in result]
        return GamesInfoResponse(games = finalResult)
 
   
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
	