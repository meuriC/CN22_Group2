from concurrent import futures
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from users_pb2 import *
from users_pb2_grpc import UsersStub

from games_pb2 import *
from games_pb2_grpc import GamesStub

from steam_pb2 import *
import steam_pb2_grpc

from pymongo import MongoClient
from bson.objectid import ObjectId

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)

games_host = os.getenv("GAMES_HOST", "localhost")
games_channel = grpc.insecure_channel(f"{games_host}:50051")
games_client = GamesStub(games_channel)




class SteamService(steam_pb2_grpc.SteamServicer):
    def ActiveUsers(self, request, context):
       
        active_users_request = ActiveUsersRequest(max_results = request.max_results)
        results = users_client.GetActiveUsers(active_users_request).users
        finalResult = [UserInfo(user_name=r.user_name, num_reviews=r.num_reviews, num_games_owned=r.num_games_owned, user_id=r.user_id, user_language=r.user_language) for r in results]
        
        return ActiveUsersResponse(users = finalResult)

    def RecommendedGames(self, request, context):
        game_request = RecommendedGamesRequest(max_results = request.max_results)
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
	