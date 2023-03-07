# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class ProductInventaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProductExist = channel.unary_unary(
                '/ProductInventary/ProductExist',
                request_serializer=Service__pb2.ProductExistRequest.SerializeToString,
                response_deserializer=Service__pb2.ProductExistResponse.FromString,
                )
        self.WriteProduct = channel.unary_unary(
                '/ProductInventary/WriteProduct',
                request_serializer=Service__pb2.ProductExistRequest.SerializeToString,
                response_deserializer=Service__pb2.ProductExistResponse.FromString,
                )


class ProductInventaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProductExist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductInventaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProductExist': grpc.unary_unary_rpc_method_handler(
                    servicer.ProductExist,
                    request_deserializer=Service__pb2.ProductExistRequest.FromString,
                    response_serializer=Service__pb2.ProductExistResponse.SerializeToString,
            ),
            'WriteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteProduct,
                    request_deserializer=Service__pb2.ProductExistRequest.FromString,
                    response_serializer=Service__pb2.ProductExistResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductInventary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductInventary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProductExist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductInventary/ProductExist',
            Service__pb2.ProductExistRequest.SerializeToString,
            Service__pb2.ProductExistResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductInventary/WriteProduct',
            Service__pb2.ProductExistRequest.SerializeToString,
            Service__pb2.ProductExistResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StockServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddProduct = channel.unary_unary(
                '/StockService/AddProduct',
                request_serializer=Service__pb2.ProductToAdd.SerializeToString,
                response_deserializer=Service__pb2.AddProductResponse.FromString,
                )


class StockServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=Service__pb2.ProductToAdd.FromString,
                    response_serializer=Service__pb2.AddProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StockService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StockService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/StockService/AddProduct',
            Service__pb2.ProductToAdd.SerializeToString,
            Service__pb2.AddProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ProductSaleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SellProduct = channel.unary_unary(
                '/ProductSale/SellProduct',
                request_serializer=Service__pb2.ProductSaleRequest.SerializeToString,
                response_deserializer=Service__pb2.ProductSaleResponse.FromString,
                )


class ProductSaleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SellProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductSaleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SellProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.SellProduct,
                    request_deserializer=Service__pb2.ProductSaleRequest.FromString,
                    response_serializer=Service__pb2.ProductSaleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductSale', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductSale(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SellProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductSale/SellProduct',
            Service__pb2.ProductSaleRequest.SerializeToString,
            Service__pb2.ProductSaleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)