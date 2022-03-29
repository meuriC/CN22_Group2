from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Find game by name: Rocket League")

request = GameByNameRequest(app_name="Rocket League")
response = client.GameByName(request)

print(response)

