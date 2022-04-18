import sys
sys.path.append('../')

from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Get top 5 recommended games")

request = GetMostRecommendedGamesRequest(max_results=5)
response = client.GetRecommendedGames(request)

print("Response: \n ",response)