import sys
sys.path.append('../')

from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)
gameName = "Noddy"
def test_createGame():
    request = CreateGameRequest(name = gameName)
    response = client.CreateGame(request)
    assert response.name == gameName, " test createGame failed"

def test_getGameByName ():
    request = GameByNameRequest(name= gameName)
    response = client.GameByName(request)
    assert response.name == gameName, " test gameByName failed"

'''
def test_getRecommendedGames():
    request = GetMostRecommendedGamesRequest(max_results=5)
    response = client.GetRecommendedGames(request)
    assert len(response) == 5, " test getRecommendedGames failed"
'''