import grpc
import sys
import os

sys.path.append('../')

#sys.path.insert(0, '../../users')
#print(sys.path)
#sys.path.insert(0, '../')
#print(sys.path)

from users_pb2 import *

from steam_pb2 import *
from steam_pb2_grpc import SteamStub

host = os.getenv("STEAM_HOST", "localhost")
channel = grpc.insecure_channel(f"{host}:50050")
client = SteamStub(channel)

#user={"user_nick_name": "<built-in function new>", "num_reviews": 47, "num_games_owned": 887},


request = ActiveUsersRequest(max_results=5)

val = client.ActiveUsers(request)

print(val)