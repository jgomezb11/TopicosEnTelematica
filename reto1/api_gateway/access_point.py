from dotenv import load_dotenv
import os
from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
from flask import Flask, redirect, url_for, request, jsonify

load_dotenv(dotenv_path='../config.env')

app = Flask(__name__)

@app.route('/productExist', methods = ['GET'])
def productExist():
    if request.is_json:
      data = request.get_json()
      INVENTARY_IP = os.environ.get("INVENTARY_IP")
      channel = grpc.insecure_channel(INVENTARY_IP)
      client = Service_pb2_grpc.ProductInventaryStub(channel)
      req = Service_pb2.ProductExistRequest(name_product=data["name_product"])
      response = client.ProductExist(req)
      if response.product_id == -1:
        return jsonify({"name_product": data["name_product"], "exist": "False"})
      else:
        return jsonify({"name_product": data["name_product"], "exist": "True"})
    return "BAD REQUEST, TRY SENDING A VALID JSON IN THE BODY"

@app.route('/writeProduct', methods = ['POST'])
def writeProduct():
    if request.is_json:
      data = request.get_json()
      INVENTARY_IP = os.environ.get("INVENTARY_IP")
      channel = grpc.insecure_channel(INVENTARY_IP)
      client = Service_pb2_grpc.ProductInventaryStub(channel)
      req = Service_pb2.ProductExistRequest(name_product=data["name_product"])
      response = client.WriteProduct(req)
      return jsonify({"name_product": data["name_product"], "exist": "True", "product_id": response.product_id})
    return "BAD REQUEST, TRY SENDING A VALID JSON IN THE BODY"

@app.route('/addProduct', methods = ['POST'])
def addProduct():
    if request.is_json:
      data = request.get_json()
      STOCK_IP = os.environ.get("STOCK_IP")
      channel = grpc.insecure_channel(STOCK_IP)
      client = Service_pb2_grpc.StockServiceStub(channel)
      req = Service_pb2.ProductToAdd(name_product=data["name_product"])
      response = client.AddProduct(req)
      if response.status_code == 1:
        return jsonify({"name_product": data["name_product"], "exist": "True", "message": "This product already exists, so it can't be added again"})
      else:
        return jsonify({"name_product": data["name_product"], "exist": "False", "message": "This product was successfully added"})

    return "BAD REQUEST, TRY SENDING A VALID JSON IN THE BODY"

@app.route('/productSale', methods = ['POST'])
def productSale():
    if request.is_json:
      data = request.get_json()
      SALES_IP = os.environ.get("SALES_IP")
      channel = grpc.insecure_channel(SALES_IP)
      client = Service_pb2_grpc.ProductSaleStub(channel)
      req = Service_pb2.ProductSaleRequest(name_product=data["name_product"])
      response = client.SellProduct(req)
      if response.status_code == 1:
        return jsonify({"name_product": data["name_product"], "exist": "True", "message": "This product already exists, was successfully sold!"})
      else:
        return jsonify({"name_product": data["name_product"], "exist": "False", "message": "This product is sold out or doesn't exists"})

    return "BAD REQUEST, TRY SENDING A VALID JSON IN THE BODY"


if __name__ == '__main__':
   app.run(debug = True)
