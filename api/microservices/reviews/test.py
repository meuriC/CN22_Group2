from reviews_pb2 import *
from reviews_pb2_grpc import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = ReviewsStub(channel)
request = ReviewByIdRequest(review_id=50463159)

client.GetReview(request)