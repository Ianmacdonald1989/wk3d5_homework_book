class Book():
	def __init__(self, title, author, genre):
		self.title = title
		self.author = author
		self.genre = genre


	
	
	
# 	def __repr__(self):
# 		return f"Book: {self.title} written by {self.author} Type of genre {self.genre}"

# old code above 



# from models.book import *
# from models.list_books import books



# book1 = Book("1984", "George Orwell", "Fiction")
# book2 = Book("You", "Caroline Kepnes", "Fiction")

# books = [book1, book2]


# def add_new_book(books):
#     books.append(books)

# def delete_book(book_title):
#     book_to_delete = None
#     for book in books:
#         if book.title == book_title:
#         event_to_delete = book
#         break

#     book.remove(book_to_delete)

# def delete_book_by_index(index):
#     books.pop(index)


