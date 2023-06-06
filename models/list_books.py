from models.book import * 



book1 = Book("1984", "George Orwell", "Fiction")
book2 = Book("You", "Caroline Kepnes", "Fiction")

books = [book1, book2]

def add_new_book(books):
    books.append(books)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = books
            break

    books.remove(book_to_delete)

def delete_book_by_index(index):
    books.pop(index)
