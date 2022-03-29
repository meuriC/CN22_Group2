from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB https://www.mongodb.com/languages/python
user = "CN_Grupo11"
password = "jcAUsQouhCddO0xW"
credentials = user + ":" + password

db = MongoClient("mongodb+srv://" + credentials + "@reviews.kqme2.mongodb.net/test")
db = db["database"]
db = db["reviews"]

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
        review = result["review"],
        timestamp_created = result["timestamp_created"],
        timestamp_updated = result["timestamp_updated"],
        author_steam_id = result["author.steamid"]
    )
    review.language.extend(result["language"])
    review.recommended.extend(result["recommended"])
    review.votes_helpful.extend(result["votes_helpful"])
    return review


class ReviewsService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        try:
            results = list(db.find({"review_id": ObjectId(request.review_id)}).limit(1))
            if len(results) <= 0:
                return ReviewData()
            return review_by_id(results[0])
        except:
            return ReviewData()

    def GetGameReviews(self, request, context):
        results = list(db.find({ "app_id": {"$all": [request.app_id]} }).limit(request.max_results))
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

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
	
if __name__ == "__main__":
    serve()
