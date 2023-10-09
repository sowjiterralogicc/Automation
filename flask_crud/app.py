# from flask import Flask, request, jsonify
# app = Flask(__name__)
# book_list = [
#     {"id" : 1,
#      "book" : "sowji",
#      "name" : "sowjiname",
#      "author" : "sowjiaut"
#      },
#     {"id": 2,
#      "book": "sowji2",
#      "name": "sowjiname2",
#      "author": "sowjiaut2"
#      },
#     {"id": 3,
#      "book": "sowji3",
#      "name": "sowjiname3",
#      "author": "sowjiaut3"
#      },
#     {"id": 4,
#      "book": "sowji4",
#      "name": "sowjiname4",
#      "author": "sowjiaut4"
#      }
# ]
# @app.route('/books', methods = ['GET','POST'])
# def books():
#     if request.method == 'GET':
#         if (len(book_list) > 0):
#             return jsonify(book_list)
#         else:
#             'nothing found', 404
#     if request.method == 'POST':
#         new_book = request.form['book']
#         new_name = request.form['name']
#         new_author = request.form['author']
#         id = book_list[-1]['id']+1
#         new_obj = {
#             'id' :id,
#             'book': new_book,
#             'name': new_name,
#             'author' : new_author,
#         }
#         book_list.append(new_obj)
#         return jsonify(book_list), 201
# @app.route('/book/<int:id>',methods = ['GET','PUT','DELETE'])
# def single_book():
#     if request.method == 'GET':
#         for book in book_list:
#             if book['id'] == id:
#                 return jsonify(book)
#             pass
#     if request.method == 'PUT':
#         for book in book_list:
#             if book['id'] == id:
#                 book['book'] = request.form['book']
#                 book['name'] = request.form['name']
#                 book['author'] = request.form['author']
#                 updated_book = {
#                     'id' : id,
#                     'book' : book['book'],
#                     'name' : book['name'],
#                     'author' : book['author']
#
#                 }
#                 return jsonify(updated_book)
#     if request.method == 'DELETE':
#         for index, book in enumerate(book_list):
#             if book['id'] == id:
#                 book_list.pop(index)
#                 return jsonify(book_list)
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Load initial data from JSON file
with open('books.json', 'r') as file:
 books = json.load(file)
# Get all books
@app.route('/books', methods=['GET'])
def get_books():
 return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
 book = next((book for book in books if book['id'] == book_id), None)
 if book is not None:
     return jsonify(book)
 return jsonify({'message': 'Book not found'}), 404

@app.route('/books',methods=['POST'])
def create_book():
    if request.method=='POST':
        data = request.get_json() # Access JSON data sent in the request body

        id=len(books)+1
        title = data.get('title')
        author = data.get('author')
        published_date = data.get('published_date')
        data['id']=str(id)

        books.append(data)

        with open('books.json', 'w') as file:
            json.dump(books, file, indent=4)
        return jsonify(data), 201
# Update a book by ID using PUT
# Update a book by ID using PUT or Delete a book by ID using DELETE
@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE'])
def update_or_delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        if request.method == 'PUT':
            data = request.get_json()
            book['title'] = data.get('title')
            book['author'] = data.get('author')
            book['published_date'] = data.get('published_date')

            with open('books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return jsonify(book)
        elif request.method == 'DELETE':
            books.remove(book)

            with open('books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run()