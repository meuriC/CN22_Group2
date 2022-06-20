import sys
sys.path.append('../')

from steam_pb2 import *
from steam_pb2_grpc  import SteamStub
import grpc

channel = grpc.insecure_channel("localhost:50050")
client = SteamStub(channel)
request = RecommendedGamesRequest(max_results=3)

val = client.RecommendedGames(request)
print(val)