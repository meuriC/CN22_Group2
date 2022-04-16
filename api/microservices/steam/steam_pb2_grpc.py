# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import steam_pb2 as steam__pb2


class SteamStub(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecommendedGames = channel.unary_unary(
                '/Steam/RecommendedGames',
                request_serializer=steam__pb2.RecommendedGamesRequest.SerializeToString,
                response_deserializer=steam__pb2.GamesInfoResponse.FromString,
                )


class SteamServicer(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    def RecommendedGames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SteamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RecommendedGames': grpc.unary_unary_rpc_method_handler(
                    servicer.RecommendedGames,
                    request_deserializer=steam__pb2.RecommendedGamesRequest.FromString,
                    response_serializer=steam__pb2.GamesInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Steam', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Steam(object):
    """######################
    ###### SERVICES ###### 
    ######################

    """

    @staticmethod
    def RecommendedGames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Steam/RecommendedGames',
            steam__pb2.RecommendedGamesRequest.SerializeToString,
            steam__pb2.GamesInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
