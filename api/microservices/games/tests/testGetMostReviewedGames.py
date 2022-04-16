from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Get top 5 reviewed games")

request = GetMostReviewedGamesRequest(max_results=5)
response = client.GetGames(request)

print("Response: \n ",response)