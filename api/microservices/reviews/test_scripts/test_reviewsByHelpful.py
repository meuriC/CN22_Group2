import sys
sys.path.append('../')

from reviews_pb2 import *
from reviews_pb2_grpc import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50053")
client = ReviewsStub(channel)
request = ReviewsByHelpfulRequest(votes_helpful=1, max_results=5)

val = client.GetReviewsByHelpful(request)
print(val)