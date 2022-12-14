
import sys
sys.path.append('./service/')

from unittest.mock import MagicMock, Mock
import book_pb2
import get_book_titles
from inventory_client import Client

def testGetBook():
    book = book_pb2.Book(ISBN=123, title="Hunger games", author="A", genre=2, year=20)
    client = Mock()
    client.get_book = MagicMock(return_value = book_pb2.GetBookResponse(book=book))
    result = get_book_titles.get_books([123], client)
    assert result == ['Hunger games']

def testGetBookWithServer():
    book = book_pb2.Book(ISBN=123, title="Hunger games", author="A", genre=2, year=20)
    client = Client()
    result = get_book_titles.get_books([123], client)
    assert result == ['Hunger games']

if __name__ == '__main__':
    testGetBook()
    testGetBookWithServer()