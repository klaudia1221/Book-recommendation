from flask import Flask, jsonify
import books as b
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:books@localhost/books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)


CORS(app,resources={r'/*': {'origins': '*'}})
@app.route("/ping",methods=['GET'])
def ping():
    df2=b.get_books_from_db("SELECT book_id, title, small_image_url FROM books ORDER BY 1 fetch first 10 rows only")
    result = {}
    for index, row in df2.iterrows():
        result[index] = dict(row)
    return jsonify(result)

@app.route("/")
def home():
    return jsonify("Hello, World!")


@app.route("/books",methods=["GET"])
def get_books():
    books=b.get_books_from_db("SELECT book_id, title, small_image_url FROM books ORDER BY 1 fetch first 10 rows only")
    print(books)
    return jsonify(books)


if __name__ == "__main__":
    app.run(debug=True)
