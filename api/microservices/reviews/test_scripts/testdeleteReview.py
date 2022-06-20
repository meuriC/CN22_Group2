import sys
sys.path.append('../')

from reviews_pb2 import *
from reviews_pb2_grpc  import ReviewsStub
import grpc

channel = grpc.insecure_channel("localhost:50053")
client = ReviewsStub(channel)
request = ReviewByIdRequest(review_id="50463159")

val = client.DeleteReview(request)
print(val)