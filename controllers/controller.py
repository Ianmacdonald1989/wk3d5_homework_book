# from flask import render_template, request
# from app import app 
# from models.book import *
# from models.list_books import books



# @app.route("/books")
# def show_books():
#     return render_template("index.html", book = books)




# @app.route('/books/', methods =['post'])
# def show_books(index):
#     index = int(index)
#     book = book[index]
#     return render_template("base.html", book=book)

# @app.route("/books")
# def add_book():
# 	title = request.form['title']
# 	author = request.form['author']
# 	genre = request.form['genre']

#old above 


from flask import render_template, request, redirect
from app import app
from models.list_books import books, add_new_book, delete_book, delete_book_by_index
from models.book import *




@app.route("/books")
def index():
    return render_template("index.html", title="Books", book = books)


@app.route("/books", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]



    title = request.form["titleName"]
    author = request.form["author"]
    genre = request.form["genre"]
    newbook = books(
        title=title,
        author=author,
        genre=genre)
    
    add_new_book(newbook)
    return redirect("/books")


@app.route("/books/del/<index>", methods=["POST"])
def delete_by_index(index):
    delete_book_by_index(int(index))
    return redirect("/books")


@app.route("/books/delete/<name>", methods=["POST"])
def delete(title):
    delete_book(title)
    return redirect("/books")

	

