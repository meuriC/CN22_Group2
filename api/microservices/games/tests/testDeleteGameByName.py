from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Delete Game: Noddy")

request = GameByNameRequest(name = "Noddy")
response = client.DeleteGameByName(request)

print("Game deleted: \n ",response)

####################################

print("Request - Delete Game: Ruca")

request = GameByNameRequest(name = "Ruca")
response = client.DeleteGameByName(request)

print("Game deleted: \n ",response)