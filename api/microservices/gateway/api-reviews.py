import os
import re

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from reviews_pb2_grpc import ReviewsStub
from reviews_pb2 import *

reviews_host = os.getenv("REVIEWS_HOST", "localhost")
reviews_channel = grpc.insecure_channel(f"{reviews_host}:50053")
reviews_client = ReviewsStub(reviews_channel)

def getReviewById(id):
    request = ReviewByIdRequest(review_id = id)  
    response = reviews_client.GetReview(request)
    return {"user_id": response.author_steam_id, 
    "app_id": response.app_id, 
    "review": response.review, 
    "recommended": response.recommended, 
    "votes_helpful": response.votes_helpful,
    "language": response.language,
    "timestamp_created": response.timestamp_created,
    "timestamp_updated": response.timestamp_updated}

def updateReview(id, ReviewsItem):
    request = UpdateReviewByIdRequest(review_id = id, review = ReviewsItem["review"], recommended = ReviewsItem["recommended"])
    response = reviews_client.PutReview(request)
    return {"user_id": response.author_steam_id, "app_id": response.app_id, "review": response.review, "recommended": response.recommended}

def deleteReview(id):
    request = ReviewByIdRequest(review_id = id)
    return reviews_client.DeleteReview(request).status

def setReviewHelpful(id):
    request = UpdateHelpfulOnReviewByIdRequest(review_id = id, votes_helpful = "1")
    response = reviews_client.PutHelpfulReview(request)
    return {"user_id": response.author_steam_id, 
    "app_id": response.app_id, 
    "review": response.review, 
    "recommended": response.recommended, 
    "votes_helpful": response.votes_helpful,
    "language": response.language,
    "timestamp_created": response.timestamp_created,
    "timestamp_updated": response.timestamp_updated}

def getGameReviewsByLanguage(id, language):
    request = GameReviewsByLanguageRequest(app_id = id, language = language, max_results = 5)
    reviewsList = []
    for r in reviews_client.GetGameReviewsByLanguage(request).reviews:
        object = {"user_id": r.author_steam_id, "app_id": r.app_id, "review": r.review, "recommended": r.recommended}
        reviewsList.append(object)
    return reviewsList

def userReviews(user_id):
    request = ReviewsByUserIdRequest(author_steam_id = user_id, max_results = 5)
    reviewsList = []
    for r in reviews_client.GetReviewsByUser(request).reviews:
        object = {"user_id": r.author_steam_id, "app_id": r.app_id, "review": r.review, "recommended": r.recommended}
        reviewsList.append(object)
    return reviewsList