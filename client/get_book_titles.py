from inventory_client import InventoryClient

def get_books(list_of_ISBN, client):
    list_of_books = []
    for isbn in list_of_ISBN:
        book = client.get_book(isbn)
        list_of_books.append(book.book.title)
    
    return list_of_books

if __name__ == '__main__':
    c = InventoryClient()
    books = get_books([123, 124], c)
    c.close()

