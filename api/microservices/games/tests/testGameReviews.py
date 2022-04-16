import sys
sys.path.append('../')

from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)
request = GameReviewsRequest(app_id="883710", max_results=2)

val = client.GameReviews(request)
print(val)