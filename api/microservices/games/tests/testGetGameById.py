import sys
sys.path.append('../')

from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

print("Request - Find game by ID: 883710")

request = GameByIdRequest(id="883710")
response = client.GameByID(request)

print("Response: \n ",response)


