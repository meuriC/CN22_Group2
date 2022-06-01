import sys
sys.path.append('../')

from reviews_pb2 import *
from reviews_pb2_grpc  import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50053")
client = ReviewsStub(channel)
request = UpdateReviewByIdRequest(review_id="test", review="This is a test review by yours truly ren XD", recommended="True")

val = client.PutReview(request)
print(val)