import sys
#sys.path.append('../')
sys.path.append('api/microservices/games/')

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


def test_getRecommendedGames():
    request = GetMostRecommendedGamesRequest(max_results=5)
    response = client.GetRecommendedGames(request)
    assert len(response.game) == 5, " test getRecommendedGames failed"

def test_deleteGame():
    request = GameByNameRequest(name = "Noddy")
    response = client.DeleteGameByName(request)
    assert response.deleted == True, "test_deleteGame failed"

def test_GetMostReviewedGames():
    request = GetMostReviewedGamesRequest(max_results=5)
    response = client.GetGames(request)
    assert len(response.game) == 5, " test_GetMostReviewedGames failed"

def test_gameReviews():
    request = GameReviewsRequest(app_id="883710", max_results=2)
    response = client.GameReviews(request)
    assert len(response.game) == 5, " test_gameReviews failed"
