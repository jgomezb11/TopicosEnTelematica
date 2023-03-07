from dotenv import load_dotenv
import os
from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc

load_dotenv(dotenv_path='../../config.env')

class StockService(Service_pb2_grpc.StockServiceServicer):
   def AddProduct(self, request, context):
      print("Request is received: " + str(request))
      channel = grpc.insecure_channel(os.environ.get("INVENTARY_IP"))
      client = Service_pb2_grpc.ProductInventaryStub(channel)
      request = Service_pb2.ProductExistRequest(name_product=request.name_product)
      response = client.ProductExist(request)
      status = 1
      if response.product_id == -1:
        client.WriteProduct(request)
        status = 2
      return Service_pb2.AddProductResponse(status_code=status)


def serve():
  host = os.environ.get("STOCK_IP")
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_StockServiceServicer_to_server(StockService(), server)
  server.add_insecure_port(host)
  print("Service is running... ")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    serve()
