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
request = ActiveUsersRequest(user_num_reviews=47, max_results=2)

val = client.ActiveUsers(request)
print(val)