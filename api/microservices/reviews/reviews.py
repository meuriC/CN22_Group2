from concurrent import futures

from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

import grpc
import pymongo  

# Connect to MongoDB
# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews.kqme2.mongodb.net/test"

# Create a connection using MongoClient. 
client = MongoClient(CONNECTION_STRING)
db = client["database"]  # Get database
db = db["reviews"] # Get column

# Second connection to another cluster cause free stuff now a days = not enough resources (RIP NO MORE 2GB IN FREE ACCOUNT)
secondClient = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews2.qwqeh.mongodb.net/test")
db2 = secondClient["database"]
db2 = db2["reviews"]

#print("ESTIMATED NUMBER OF ELEMENTS IN 1ST BD: ", db.estimated_document_count())
#print("\nESTIMATED NUMBER OF ELEMENTS IN 2ND BD: ", db2.estimated_document_count())

from reviews_pb2 import (
    ReviewByIdRequest,
    ReviewsByGameRequest,
    ReviewData,
    ReviewDataResponse,
)
import reviews_pb2_grpc


def review_by_id(result):
    review = ReviewData(
        app_id = result["app_id"],
        review_id = result["review_id"],
        language = result["language"],
        review = result["review"],
        timestamp_created = result["timestamp_created"],
        timestamp_updated = result["timestamp_updated"],
        recommended = result["recommended"],
        votes_helpful = result["votes_helpful"],
        author_steam_id = result["author.steamid"]
    )
    return review


class ReviewsService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        try:
            results = list(db.find({"review_id": request.review_id}).limit(1))
            if len(results) <= 0:
                results = list(db2.find({"review_id": request.review_id}).limit(1))

            if len(results) <= 0:
                print("Review not found ... Check if the id of the review is correct.")
                return ReviewData()
            return review_by_id(results[0])
        except:
            print("Review not found ... Check if the id of the review is correct.")
            return ReviewData()

    def GetGameReviews(self, request, context):
        results = list(db.find({"app_id": {"$all": [request.app_id]} }).limit(request.max_results))
        if len(results) < request.max_results:
            results += list(db2.find({"app_id": {"$all": [request.app_id] } }).limit((request.max_results - len(results))))
			
        results = [review_by_id(review) for review in results]
        return ReviewDataResponse(reviews = results)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )

    reviews_pb2_grpc.add_ReviewsServicer_to_server(
        ReviewsService(), server
    )

    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()
	
if __name__ == "__main__":
    serve()
