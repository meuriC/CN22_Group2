# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import games_pb2 as games__pb2


class GamesStub(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GameReviews = channel.unary_unary(
                '/Games/GameReviews',
                request_serializer=games__pb2.GameReviewsRequest.SerializeToString,
                response_deserializer=games__pb2.ReviewInfoResponse.FromString,
                )
        self.GetGames = channel.unary_unary(
                '/Games/GetGames',
                request_serializer=games__pb2.GetMostReviewedGamesRequest.SerializeToString,
                response_deserializer=games__pb2.GamesDataResponse.FromString,
                )
        self.GetRecommendedGames = channel.unary_unary(
                '/Games/GetRecommendedGames',
                request_serializer=games__pb2.GetMostRecommendedGamesRequest.SerializeToString,
                response_deserializer=games__pb2.GamesDataResponse.FromString,
                )
        self.GameByID = channel.unary_unary(
                '/Games/GameByID',
                request_serializer=games__pb2.GameByIdRequest.SerializeToString,
                response_deserializer=games__pb2.GamesData.FromString,
                )
        self.GameByName = channel.unary_unary(
                '/Games/GameByName',
                request_serializer=games__pb2.GameByNameRequest.SerializeToString,
                response_deserializer=games__pb2.GamesData.FromString,
                )
        self.CreateGame = channel.unary_unary(
                '/Games/CreateGame',
                request_serializer=games__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=games__pb2.GamesData.FromString,
                )
        self.DeleteGameByName = channel.unary_unary(
                '/Games/DeleteGameByName',
                request_serializer=games__pb2.GameByNameRequest.SerializeToString,
                response_deserializer=games__pb2.DeletionResponse.FromString,
                )


class GamesServicer(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    def GameReviews(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecommendedGames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GameByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GameByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGameByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GamesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GameReviews': grpc.unary_unary_rpc_method_handler(
                    servicer.GameReviews,
                    request_deserializer=games__pb2.GameReviewsRequest.FromString,
                    response_serializer=games__pb2.ReviewInfoResponse.SerializeToString,
            ),
            'GetGames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGames,
                    request_deserializer=games__pb2.GetMostReviewedGamesRequest.FromString,
                    response_serializer=games__pb2.GamesDataResponse.SerializeToString,
            ),
            'GetRecommendedGames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecommendedGames,
                    request_deserializer=games__pb2.GetMostRecommendedGamesRequest.FromString,
                    response_serializer=games__pb2.GamesDataResponse.SerializeToString,
            ),
            'GameByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GameByID,
                    request_deserializer=games__pb2.GameByIdRequest.FromString,
                    response_serializer=games__pb2.GamesData.SerializeToString,
            ),
            'GameByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GameByName,
                    request_deserializer=games__pb2.GameByNameRequest.FromString,
                    response_serializer=games__pb2.GamesData.SerializeToString,
            ),
            'CreateGame': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGame,
                    request_deserializer=games__pb2.CreateGameRequest.FromString,
                    response_serializer=games__pb2.GamesData.SerializeToString,
            ),
            'DeleteGameByName': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGameByName,
                    request_deserializer=games__pb2.GameByNameRequest.FromString,
                    response_serializer=games__pb2.DeletionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Games', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Games(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    @staticmethod
    def GameReviews(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/GameReviews',
            games__pb2.GameReviewsRequest.SerializeToString,
            games__pb2.ReviewInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/GetGames',
            games__pb2.GetMostReviewedGamesRequest.SerializeToString,
            games__pb2.GamesDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecommendedGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/GetRecommendedGames',
            games__pb2.GetMostRecommendedGamesRequest.SerializeToString,
            games__pb2.GamesDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GameByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/GameByID',
            games__pb2.GameByIdRequest.SerializeToString,
            games__pb2.GamesData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GameByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/GameByName',
            games__pb2.GameByNameRequest.SerializeToString,
            games__pb2.GamesData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/CreateGame',
            games__pb2.CreateGameRequest.SerializeToString,
            games__pb2.GamesData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGameByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Games/DeleteGameByName',
            games__pb2.GameByNameRequest.SerializeToString,
            games__pb2.DeletionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
