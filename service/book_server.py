import book_pb2, book_pb2_grpc
from concurrent import futures
import grpc


class InventoryServer(book_pb2_grpc.InventoryServiceServicer):
    # Map of ISBN to book object 
    book_dict = {
        123: book_pb2.Book(
            ISBN = 123,
            title = 'Hunger games',
            author = 'idk',
            genre = 2,
            year = 2014
        ),
        124: book_pb2.Book(
            ISBN = 124,
            title = 'Hunger games II',
            author = 'idk',
            genre = 2,
            year = 2015
        )
    }


    # Create a new book and add to map if ISBN doesn't exist
    def createBook(self, request, context):
        book = self.book_dict.get(request.book.ISBN, None)
        if book:
            return book_pb2.CreateBookResponse(statusCode="400: ISBN already exists")

        self.book_dict[request.book.ISBN] = request.book
        return book_pb2.CreateBookResponse(statusCode="200: Added successfully")

    # Get book from ISBN number
    def getBook(self, request, context):
        book = self.book_dict.get(request.ISBN, None)
        print(book)
        if book:
            response = book_pb2.Book(ISBN=book.ISBN, title=book.title, genre=book.genre, year=book.year, author=book.author)
            return book_pb2.GetBookResponse(book=response, statusCode="200")

        return book_pb2.GetBookResponse(statusCode="400: No book found")
        


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server started!")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

