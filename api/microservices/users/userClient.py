import sys
sys.path.append('../')

import grpc

"""from users_pb2 import UsernameRequest
from users_pb2 import GetUsersRequest
from users_pb2 import CreateUserRequest
from users_pb2 import IdRequest"""
from users_pb2 import * 
from users_pb2_grpc import UsersStub





channel = grpc.insecure_channel("localhost:50052")
client = UsersStub(channel)

"""users_request = CreateReviewRequest(app_id="883710", review="Test made by the boyz", recommended="True", user_id="76561198054155096")
val = client.PostReview(users_request)
print(val)"""

#Test CreateUser
"""createUserRequest = CreateUserRequest(user_language = "portuguese",user_name="CNGroup2")
res = client.CreateUser(createUserRequest)
createUserRequest2 = CreateUserRequest(user_language = "portuguese",user_name="CompNuvem")
res2 = client.CreateUser(createUserRequest2)
if res:
    print("----------CreateUser----------")
    print(res)
    print(res2)
else :
    print("Empty")"""

#Test GetUser by Username
"""username_request = UsernameRequest(user_name="CNGroup2")
val = client.GetUserByUsername(username_request)
if val:
    print("----------GetUserByUsername----------")
    print(val)
else :
    print("Empty")"""

#Test DeleteUser by Username
username_request = UsernameRequest(user_name="CNGroup2")
val = client.DeleteUserByUsername(username_request)
if val:
    print("----------DeleteUserByUsername----------")
    print("Deleting CNGroup2")
    print(val)
else :
    print("Empty")

"""#Test DeleteUser by Id
UserCompNuvemId = ""
user_request = IdRequest(user_id=UserCompNuvemId)
val = client.DeleteUserById(user_request)
if val:
    print("----------DeleteUserById----------")
    print("Deleting CompNuvem")
    print(val)
else :
    print("Empty")"""

#Test GetUser by ID
"""user_request = IdRequest(user_id="625ca6e44b01279a30c8cf5d")
val = client.GetUserById(user_request)
if val:
    print("----------GetUserByID----------")
    print(val)
else :
    print("Empty")"""

#Test GetUsers
"""users_request = GetUsersRequest(max_result=2)
val = client.GetUsers(users_request)
if val:
    print("----------GetUsers----------")
    print(val)
else :
    print("Empty")"""
	

	

