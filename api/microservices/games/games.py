import os
import grpc
import pymongo

from concurrent import futures
from pymongo import MongoClient

from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from games_pb2 import *
import games_pb2_grpc

from reviews_pb2 import *
from reviews_pb2_grpc import ReviewsStub

reviews_host = os.getenv("REVIEWS_HOST", "localhost")
reviews_channel = grpc.insecure_channel(f"{reviews_host}:50053")
reviews_client = ReviewsStub(reviews_channel)

# connect to MongoDB
client = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@games.2gyca.mongodb.net/test")
db = client["database"]
db = db["games"]

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
    def GameReviews(self, request, context):
        rev_request = ReviewsByGameRequest(app_id = request.app_id, max_results = request.max_results)
        result = reviews_client.GetGameReviews(rev_request).reviews
		
        finalResult = [ReviewInfo(review_id=r.review_id, language=r.language, review=r.review, timestamp_created=r.timestamp_created, timestamp_updated=r.timestamp_updated, recommended=r.recommended, votes_helpful=r.votes_helpful, author_steam_id=r.author_steam_id) for r in result]
		
        return ReviewInfoResponse(reviews = finalResult)

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