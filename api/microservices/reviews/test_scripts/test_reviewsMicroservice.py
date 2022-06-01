import sys
#sys.path.append('../')
sys.path.append('api/microservices/reviews/')

from reviews_pb2 import *
from reviews_pb2_grpc  import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50053")
client = ReviewsStub(channel)
gameName = "Noddy"
def test_updateReviewNonExists():
    request = UpdateReviewByIdRequest(review_id="test", review="This is a test review by yours truly ren XD", recommended="True")
    response = client.PutReview(request)
    assert response.review=="", "test_updateReviewNonExists failed"

def test_updateReviews():
    request = UpdateReviewByIdRequest(review_id="50462588", review="This is a test review by yours truly ren XD", recommended="True")
    response = client.PutReview(request)
    assert response.review=="This is a test review by yours truly ren XD", "test_updateReviews failed"

def test_reviewByIdNonExists():
    request = ReviewByIdRequest(review_id="50463082")  #50463082
    response = client.GetReview(request)
    assert response.review_id=="",  "test_reviewByIdNonExists failed"

def test_reviewById():
    request = ReviewByIdRequest(review_id="50462588") 
    response = client.GetReview(request)
    assert response.review_id=="50463004", "test_reviewById"

def test_getgameReviews():
    request = ReviewsByGameRequest(app_id="883710", max_results=5)
    response =  client.GetGameReviews(request)
    assert len(response.reviews) == 5, "test_getgameReviews failded "


def test_putHelpfulReview():
    request = UpdateHelpfulOnReviewByIdRequest(review_id="50462588", votes_helpful=1)
    response = client.PutHelpfulReview(request)
    assert response.votes_helpful== 1, "test_PutHelpfulReview failed"

def test_deleteReviewNonExists():
    request = ReviewByIdRequest(review_id="test")
    response = client.DeleteReview(request)
    assert response.status== False, "test_deleteReviewNonExists failed"

def test_deleteReview():
    request = ReviewByIdRequest(review_id="50462567")
    response = client.DeleteReview(request)
    assert response.status== True, "test_DeleteReview failed"


def test_getReviewsByUser():
    request = ReviewsByUserIdRequest(author_steam_id="76561198054155096", max_results=5)
    response = client.GetReviewsByUser(request)
    assert len(response.reviews) < 0, "test_getReviewsByUser failed"
    assert len(response.reviews) >= 5, "test_getReviewsByUser failed"