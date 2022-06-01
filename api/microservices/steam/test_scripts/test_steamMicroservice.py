import sys
#sys.path.append('../')
sys.path.append('api/microservices/steam/')

from steam_pb2 import *
from steam_pb2_grpc  import SteamStub
import grpc

channel = grpc.insecure_channel("localhost:50050")
client = SteamStub(channel)
request = ActiveUsersRequest(max_results = 5)

def test_activeUsers():
    request = ActiveUsersRequest(max_results = 5)
    response = client.ActiveUsers(request)
    assert len(response.users) == 5, " test_activeUsers failed"

def test_recommendedGames():
    request = RecommendedGamesRequest(max_results=3)
    response = client.RecommendedGames(request)
    assert len(response.games) == 3, " test_recommendedGames failed"
