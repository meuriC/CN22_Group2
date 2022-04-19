
from concurrent import futures

import grpc
import time
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB

db = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@users.lastb.mongodb.net/test")
db = db['database']
db = db['users']

import users_pb2_grpc
from users_pb2 import (
    UserData,
    CreateUserResponse,
    UsersDataList,
    DeletionResponseUser, 
	ReviewData
)

def marshalUserdbToUserService(result):
    user = UserData(
        user_name = result["user_name"],
        user_num_reviews = result["user_num_reviews"],
        user_num_games_owned = result["user_num_games_owned"],
        user_id = result["user_id"],
        user_language = result["user_language"]
    )
    return user

def create_user(result):
    user = CreateUserResponse(
        user_language = result["user_language"],
        user_id = result["user_id"],
        user_num_games_owned = result["user_num_games_owned"],
        user_num_reviews = result["user_num_reviews"],
        user_name = result["user_name"],
        user_pwd = result["user_pwd"]
    )
    return user
    
def delete_user(result):
    deleted = DeletionResponseUser(
        deleted = True
    )
    return deleted
	
def create_review(result):
    review = ReviewData(
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

class UserService(users_pb2_grpc.UsersServicer):
    def GetUserById(self, request, context):
        #results = db.remove({"_id": ObjectId(request.user_id)})
        results = db.remove({"user_id": request.user_id})
        return marshalUserdbToUserService(results[0])
    
    def GetUserByUsername(self, request, context):
        results = db.find({"user_name": request.user_name})
        return marshalUserdbToUserService(results[0])
    
    def DeleteUserByUsername(self, request, context):
        results = db.remove({"user_name": request.user_name})
        return delete_user(results)
    
    def DeleteUserById(self, request, context):
        #results = db.remove({"_id": ObjectId(request.user_id)})
        results = db.remove({"user_id": request.user_id})
        return delete_user(results)

    def CreateUser(self, request, context):
        results = db.insert({ "user_language" : request.user_language,
             "user_id": "0", 
             "user_num_games_owned": 0, 
             "user_num_reviews": 0,
             "user_name": request.user_name, 
             "user_pwd": "clear"})
        resultsFinal = db.find({"_id": results})
        db.update({ "_id" : resultsFinal[0]["_id"] },{"$set": {  "user_id" : str(resultsFinal[0]["_id"])}})
        #print(resultsFinal[0])
        return create_user(resultsFinal[0])

    def GetUsers(self, request, context):
        results = list(db.find().limit(request.max_result))
        usersList=[]
        for user in results:
            usersList.append(marshalUserdbToUserService(user))
        return UsersDataList(users=usersList)

    def GetActiveUsers(self, request, context):
        results = list(db.find().sort("user_num_reviews", -1).limit(request.max_result))
        results = [ marshalUserdbToUserService(user) for user in results ]
        return UsersDataList( users = results )

    def PostReview(self, request, context):
        thirdClient = MongoClient("mongodb+srv://CN_Grupo11:jcAUsQouhCddO0xW@reviews3.keyxx.mongodb.net/test")
        db3 = thirdClient["database"]
        db3 = db3["reviews"]
		
        findUser = db.find({"user_id": request.user_id})
        results = db3.insert({
             "app_id": request.app_id,
             "review_id": "0",			 
             "language": findUser[0]["user_language"],
             "review": request.review, 
             "timestamp_created": str(int(time.time())),
             "timestamp_updated": str(int(time.time())),
             "recommended": request.recommended,
             "votes_helpful": "0",
		     "author_steamid": request.user_id})

        resultsFinal = db3.find({"_id": results})
        db3.update_one({"_id": resultsFinal[0]["_id"]},{"$set": {"review_id": str(resultsFinal[0]["_id"])}})
        return create_review(resultsFinal[0])

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    users_pb2_grpc.add_UsersServicer_to_server(
        UserService(), server
    )
    
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()