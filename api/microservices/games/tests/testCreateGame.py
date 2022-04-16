from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Create Game: Noddy")

request = CreateGameRequest(name = "Noddy")
response = client.CreateGame(request)

print("Create game: \n ",response)

####################################

print("Request - Create Game: Ruca")

request = CreateGameRequest(name = "Ruca")
response = client.CreateGame(request)

print("Create game: \n ",response)