from games_pb2 import *
from games_pb2_grpc import GamesStub
import grpc

channel = grpc.insecure_channel("localhost:50051")
client = GamesStub(channel)

#request = GameByIdRequest(app_id=203160)
#client.GameByID(request)


request = GameByNameRequest(app_name="Rocket League")
client.GameByName(request)

