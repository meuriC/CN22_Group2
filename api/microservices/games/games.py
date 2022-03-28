from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient

# connect to MongoDB

db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test")
db = db["database"]
db = db["games"]

from games_pb2 import (
    GamesData,
    GamesDataList,
    GameByIdRequest,
    GamesByNameRequest
)
import games_pb2_grpc

class GamesService(games_pb2_grpc.GamesServicer):

    def GetGames(self, request, context):
        page = request.page * request.max_results
        results = list(db.find().skip(page).limit(request.max_results))
        results = [ games_to_proto(games) for games in results ]
        return GamesDataList( games = results )

    def SearchById(self, request, context):
        try:
            results = list(db.find({ "app_id": request.app_id }).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_to_proto(results[0])
        except:
            return GamesData()
        

    def SearchByName(self, request, context):
        try:
            results = list(db.find({ "app_name": request.app_name }).limit(1))

            if len(results) <= 0:
                return GamesData()
            return games_to_proto(results[0])
        except:
            return GamesData()


def games_to_proto(result):
    game = GamesData (
        app_id = str(result["app_id"]),
        app_name = result["app_name"],
        games_reviews_number = str(result["games_reviews_number"])
    )
    
    return game


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