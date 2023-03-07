from dotenv import load_dotenv
import os
from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc

load_dotenv(dotenv_path='../../config.env')

class ProductInventary(Service_pb2_grpc.ProductInventaryServicer):
  def ProductExist(self, request, context):
    print("Request is received: " + str(request))
    id = -1
    with open("inventary.txt", 'r') as inv:
      for line in inv:
        if line.split(",")[1].rstrip('\n') == request.name_product:
          id = int(line.split(",")[0])
    return Service_pb2.ProductExistResponse(product_id=id)

  def WriteProduct(self, request, context):
    print("Adding to the local database")
    with open('inventary.txt', 'r') as f:
      line_count = 0
      for line in f:
        line_count += 1
    with open("inventary.txt", "a") as f:
      f.write(f'{str(line_count+1)},{request.name_product}\n')

    return Service_pb2.ProductExistResponse(product_id=line_count+1)

def serve():
  host = os.environ.get("INVENTARY_IP")
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_ProductInventaryServicer_to_server(ProductInventary(), server)
  server.add_insecure_port(host)
  print("Service is running... ")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    serve()
