
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
import users_pb2_grpc
from users_pb2 import (
    User,
)

class UserService(users_pb2_grpc.UsersServicer):
    def GetUserByName(self, request, context):
        return User(username = "ola", userid="")

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    users_pb2_grpc.add_UsersServicer_to_server(
        UserService(), server
    )

    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()