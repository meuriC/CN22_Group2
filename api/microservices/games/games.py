from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to MongoDB

db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test")
db = db["database"]
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
        app_id = result["app_id"],
        app_name = result["app_name"],
        games_reviews_number = result["games_reviews_number"]
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
            results = list(db.find({ "app_id": ObjectId(request.app_id)}).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_response(results[0])
        except:
            return GamesData()
        

    def GameByName(self, request, context):
        try:
            results = list(db.find({ "app_name": request.app_name }).limit(1))

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

    # with open("games.key", "rb") as fp:
        # games_key = fp.read()
    # with open("games.pem", "rb") as fp:
        # games_cert = fp.read()
    # with open("ca.pem", "rb") as fp:
        # ca_cert = fp.read()
    
    # creds = grpc.ssl_server_credentials(
        # [(games_key, games_cert)],
        # root_certificates=ca_cert,
        # require_client_auth=True,
    # )
    
    # server.add_secure_port("[::]:50051", creds)
  
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()