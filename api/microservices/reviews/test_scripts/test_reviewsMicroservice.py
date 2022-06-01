import sys
#sys.path.append('../')
sys.path.append('api/microservices/reviews/')

from reviews_pb2 import *
from reviews_pb2_grpc  import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50053")
client = ReviewsStub(channel)
gameName = "Noddy"
def test_updateReview():
    request = UpdateReviewByIdRequest(review_id="test", review="This is a test review by yours truly ren XD", recommended="True")
    response = client.PutReview(request)
    assert response.review=="This is a test review by yours truly ren XD", " test test_updateReview failed"

def test_reviewById():
    request = ReviewByIdRequest(review_id="50463082")  #50463082
    response = client.GetReview(request)
    assert response.review_id=="50463082"

def test_getgameReviews():
    request = ReviewsByGameRequest(app_id="883710", max_results=5)
    response =  client.GetGameReviews(request)
    assert len(response) == 5, "test_getgameReviews failded "


def test_putHelpfulReview():
    request = UpdateHelpfulOnReviewByIdRequest(review_id="test", votes_helpful="1")
    response = client.PutHelpfulReview(request)
    assert response.votes_helpful== 1, "test_PutHelpfulReview failed"

def test_deleteReview():
    request = ReviewByIdRequest(review_id="test")
    response = client.DeleteReview(request)
    assert response.status== True, "test_DeleteReview failed"


def test_getReviewsByUser():
    request = ReviewsByUserIdRequest(author_steam_id="76561198054155096", max_results=5)
    response = client.GetReviewsByUser(request)
    assert len(response) == 5, "test_getReviewsByUser failed"