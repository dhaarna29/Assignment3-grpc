from inventory_client import InventoryClient

# Call client to get book details from API for each ISBN
def get_books(list_of_ISBN, client):
    list_of_titles = []
    for isbn in list_of_ISBN:
        book = client.get_book(isbn)
        list_of_titles.append(book.book.title)
    
    return list_of_titles

if __name__ == '__main__':
    c = InventoryClient()
    books = get_books([123, 124], c)
    c.close()

