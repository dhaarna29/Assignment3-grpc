import sys
sys.path.append('./service/')

import book_pb2
import book_pb2_grpc
import grpc

class InventoryClient:
    # Initialize server
    def __init__ (self):
        self.server = 'localhost'
        self.port = '50051'
        self.channel = grpc.insecure_channel(self.server + ":" + self.port)
        self.stub = book_pb2_grpc.InventoryServiceStub(self.channel)
        print("Started!!")

    # Call get book API from service stub
    def get_book(self, isbn):
        request = book_pb2.GetBookRequest(ISBN=isbn)
        return self.stub.getBook(request)

    # Close the client channel
    def close(self):
        self.channel.close()