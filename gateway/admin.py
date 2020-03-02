from .protos import videogame_pb2, videogame_pb2_grpc
from .validators.videogamesValidator import VideogameValidation

ROUTING = {
    'videogames': {
        'PROTO': videogame_pb2,
        'PROTO_RPC': videogame_pb2_grpc,
        'VALIDATOR': VideogameValidation,
        'HOST': 'localhost:50051' 
    }
}