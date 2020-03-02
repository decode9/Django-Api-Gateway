import grpc
from .utils.json_response import JsonResponse

class grpcClient(JsonResponse):

    def __init__(self, prot, protRPC, host):
        self.prototype = prot
        self.protoRPC = protRPC
        self.channel = grpc.insecure_channel(host)
    
    def save(self, **Data):

        try:

            request = self.prototype.Game(**Data)

            stub = self.protoRPC.VideogameStub(self.channel)

            response = stub.SaveVideogame(request)

            return response
    
        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throw400(status_code.name)
        except ValueError:
            
            self.throw400('value_error')

    def get(self):

        try:

            request = self.prototype.Empty()

            stub = self.protoRPC.VideogameStub(self.channel)

            response = stub.GetVideogame(request)

            return response
        except grpc.RpcError as e:
            print(e.details())
            status_code = e.code()
            self.throw400(status_code.name)
        except ValueError:
            
            self.throw400("value_error")
