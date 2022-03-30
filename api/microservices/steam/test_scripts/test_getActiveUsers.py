import grpc

import sys
sys.path.insert(0, '../../users')
print(sys.path)

from users_pb2 import *

sys.path.insert(0, '../')
print(sys.path)
from steam_pb2 import *
from steam_pb2_grpc import SteamStub

channel = grpc.insecure_channel("localhost:50050")
client = SteamStub(channel)
request2 = ActiveUsersRequest(max_results=2)
#user={"user_nick_name": "<built-in function new>", "num_reviews": 47, "num_games_owned": 887},

val = client.ActiveUsers(request=request2)
print(val)