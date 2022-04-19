from concurrent import futures

from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

import time
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

# Third connection, mainly for new created reviews
thirdClient = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews3.keyxx.mongodb.net/test")
db3 = thirdClient["database"]
db3 = db3["reviews"]

#print("ESTIMATED NUMBER OF ELEMENTS IN 1ST BD: ", db.estimated_document_count())
#print("\nESTIMATED NUMBER OF ELEMENTS IN 2ND BD: ", db2.estimated_document_count())
#print("\nESTIMATED NUMBER OF ELEMENTS IN 3RD BD: ", db3.estimated_document_count())

from reviews_pb2 import (
    ReviewDetails,
    ReviewDetailsResponse,
	DeleteReviewResponse
)
import reviews_pb2_grpc


def review_by_id(result):
    review = ReviewDetails(
        app_id = result["app_id"],
        review_id = result["review_id"],
        language = result["language"],
        review = result["review"],
        timestamp_created = result["timestamp_created"],
        timestamp_updated = result["timestamp_updated"],
        recommended = result["recommended"],
        votes_helpful = result["votes_helpful"],
        author_steam_id = result["author_steamid"]
    )
    return review


class ReviewsService(reviews_pb2_grpc.ReviewsServicer):
    def GetReview(self, request, context):
        try:
            # Search on the 1st database
            results = list(db.find({"review_id": request.review_id}))
            if len(results) <= 0:
                # Search on the 2nd database
                results = list(db2.find({"review_id": request.review_id}))
				
            if len(results) <= 0:
                # Search on the 3rd database
                results = list(db3.find({"review_id": request.review_id}))

            if len(results) <= 0:
                print("Review not found ... Check if the id of the review is correct.")
                return ReviewDetails()
            return review_by_id(results[0])
        except:
            print("Review not found ... Check if the id of the review is correct.")
            return ReviewDetails()

    def GetGameReviews(self, request, context):
        # Search on the 1st database
        results = list(db.find({"app_id": {"$all": [request.app_id]} }).limit(request.max_results))
        if len(results) < request.max_results:
            # Search on the 2nd database
            results += list(db2.find({"app_id": {"$all": [request.app_id] } }).limit((request.max_results - len(results))))
			
        if len(results) < request.max_results:
            # Search on the 3rd database
            results += list(db3.find({"app_id": {"$all": [request.app_id] } }).limit((request.max_results - len(results))))
			
        results = [review_by_id(review) for review in results]
        return ReviewDetailsResponse(reviews = results)

    def PutReview(self, request, context):
        try:
            # Search on the 1st database
            results = list(db.find({"review_id": request.review_id}))
            database = db
			
            if len(results) <= 0:
                # Search on the 2nd database
                results = list(db2.find({"review_id": request.review_id}))
                database = db2
				
            if len(results) <= 0:
                # Search on the 3rd database
                results = list(db3.find({"review_id": request.review_id}))
                database = db3

            if len(results) <= 0:
                print("Try: Review not found.")
                return ReviewDetails()

            database.update_one({"review_id": request.review_id}, {"$set": {"review": request.review}})
            database.update_one({"review_id": request.review_id}, {"$set": {"recommended": request.recommended}})
            database.update_one({"review_id": request.review_id}, {"$set": {"timestamp_updated": str(int(time.time()))}})
            results = list(database.find({"review_id": request.review_id}))
            return review_by_id(results[0])
        except:
            print("Except: Review not found.")
            return ReviewDetails()

    def DeleteReview(self, request, context):
        try:
            # Search on the 1st database
            results = list(db.find({"review_id": request.review_id}))
            database = db
			
            if len(results) <= 0:
                # Search on the 2nd database
                results = list(db2.find({"review_id": request.review_id}))
                database = db2
				
            if len(results) <= 0:
                # Search on the 3rd database
                results = list(db3.find({"review_id": request.review_id}))
                database = db3

            if len(results) <= 0:
                print("Try: Review not found, thus not deleted.")
                return DeleteReviewResponse(status=False)

            database.delete_one({"review_id": request.review_id})
            return DeleteReviewResponse(status=True)
        except:
            print("Except: Review not found, thus not deleted.")
            return DeleteReviewResponse(status=False)
			
    def PutHelpfulReview(self, request, context):
        try:
            # Search on the 1st database
            results = list(db.find({"review_id": request.review_id}))
            database = db
			
            if len(results) <= 0:
                # Search on the 2nd database
                results = list(db2.find({"review_id": request.review_id}))
                database = db2
				
            if len(results) <= 0:
                # Search on the 3rd database
                results = list(db3.find({"review_id": request.review_id}))
                database = db3

            if len(results) <= 0:
                print("Try: Review not found.")
                return ReviewDetails()
            
            totalVotes = str(int(results[0]["votes_helpful"]) + int(request.votes_helpful))
            database.update_one({"review_id": request.review_id}, {"$set": {"votes_helpful": totalVotes}}) #request.votes_helpful
            results = list(database.find({"review_id": request.review_id}))
            return review_by_id(results[0])
        except:
            print("Except: Review not found.")
            return ReviewDetails()
    
    def GetGameReviewsByLanguage(self, request, context):
        # Search on the 1st database
        results = list(db.find({"app_id": {"$all": [request.app_id]}, "language": {"$all": [request.language]}}).limit(request.max_results))
        if len(results) < request.max_results:
            # Search on the 2nd database
            results += list(db2.find({"app_id": {"$all": [request.app_id]}, "language": {"$all": [request.language]}}).limit((request.max_results - len(results))))
			
        if len(results) < request.max_results:
            # Search on the 3rd database
            results += list(db3.find({"app_id": {"$all": [request.app_id]}, "language": {"$all": [request.language]}}).limit((request.max_results - len(results))))
        results = [review_by_id(review) for review in results]
        return ReviewDetailsResponse(reviews = results)
		
    def GetReviewsByUser(self, request, context):
        # Search on the 1st database
        results = list(db.find({"author_steamid": {"$all": [request.author_steam_id]}}).limit(request.max_results))
        if len(results) < request.max_results:
            # Search on the 2nd database
            results += list(db2.find({"author_steamid": {"$all": [request.author_steam_id]}}).limit((request.max_results - len(results))))
			
        if len(results) < request.max_results:
            # Search on the 3rd database
            results += list(db3.find({"author_steamid": {"$all": [request.author_steam_id]}}).limit((request.max_results - len(results))))
        results = [review_by_id(review) for review in results]
        return ReviewDetailsResponse(reviews = results)
		
    def GetReviewsByHelpful(self, request, context):
        # Search on the 1st database
        results = list(db.find({"votes_helpful": {"$all": [request.votes_helpful]}}).limit(request.max_results))
        if len(results) < request.max_results:
            # Search on the 2nd database
            results += list(db2.find({"votes_helpful": {"$all": [request.votes_helpful]}}).limit((request.max_results - len(results))))
			
        if len(results) < request.max_results:
            # Search on the 3rd database
            results += list(db3.find({"votes_helpful": {"$all": [request.votes_helpful]}}).limit((request.max_results - len(results))))
        results = [review_by_id(review) for review in results]
        return ReviewDetailsResponse(reviews = results)

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
