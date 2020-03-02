from rest_framework.views import APIView
from .utils.json_response import JsonResponse
from .services import grpcClient

from .admin import ROUTING

from google.protobuf.json_format import MessageToDict

# Create your views here.
class gateway(APIView, JsonResponse):

    

    def operation(self, request):
        try: 
            url = request.path_info.split('/')

            for route in ROUTING:
                if route == url[2]:
                    client = grpcClient(ROUTING[route]['PROTO'], ROUTING[route]['PROTO_RPC'], ROUTING[route]['HOST'])
                    if request.method == 'GET':
                        response = client.get()
            
                    if request.method == 'POST':

                        form = ROUTING[route]['VALIDATOR'](request.data)

                        if not(form.is_valid()): self.throw400(form.errors)

                        response = client.save(**request.data)

                    return self.apiResponse(MessageToDict(response))
        except:
            raise

    def get(self, request):
        try: 
            return self.operation(request)
        except:
            raise

    def post(self, request):
        try:
            return self.operation(request)
        except:
            raise