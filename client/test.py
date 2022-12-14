
import sys
import unittest
sys.path.append('./service/')

from unittest.mock import MagicMock, Mock
import book_pb2
import get_book_titles
from inventory_client import InventoryClient

class TestGetBook(unittest.TestCase):

    def testGetBook(self):
        book = book_pb2.Book(ISBN=123, title="Hunger games", author="A", genre=2, year=20)
        client = Mock()
        client.get_book = MagicMock(return_value = book_pb2.GetBookResponse(book=book))
        result = get_book_titles.get_books([123], client)
        assert result == ['Hunger games']
        client.get_book.assert_called_with(123)

    def testGetBookWithServer(self):
        book = book_pb2.Book(ISBN=123, title="Hunger games", author="A", genre=2, year=20)
        client = InventoryClient()
        result = get_book_titles.get_books([123], client)
        assert result == ['Hunger games']


if __name__ == '__main__':
    unittest.main()