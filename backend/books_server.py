from flask import Flask, jsonify, request
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
    df2=b.get_books_from_db("SELECT book_id, title, image_url FROM books ORDER BY 1 fetch first 10 rows only")
    result = {}
    for index, row in df2.iterrows():
        result[index] = dict(row)
    return jsonify(result)

@app.route("/")
def home():
    return jsonify("Hello, World!")

#
# @app.route("/books",methods=["GET"])
# def get_books():
#     # print(books)
#     books = b.get_books_from_db("SELECT array_to_json(array_agg(books_basic2)) FROM books_basic2 ");
#     # books = b.get_books_from_db("SELECT array_to_json(array_agg(select * from books_basic2)) FROM books_basic2 ");
#     return jsonify(books)


# @app.route("/books",methods=["GET"])
# def get_books():
#
#     args = request.args
#     offset = args.get('offset') if 'offset' in args else 0
#     limit = args.get('limit') if 'limit' in args else 10000
#     search="\'%"+args.get('search')+"%\'" if 'search' in args else '\'%\''
#     # search='\'%John%\''
#     books = b.get_books_from_db("SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from (select * from books order by id LIMIT {} OFFSET {}) s where s.authors like {}) t ".format(limit,offset,search));
#     print(books)
#     return jsonify(books)

@app.route("/books",methods=["GET"])
def get_books():
    args = request.args
    page = args.get('page') if 'page' in args else 1
    limit = args.get('limit') if 'limit' in args else 10000
    offset=(int(page)-1)*int(limit)
    print(offset)
    search="\'%"+args.get('search')+"%\'" if 'search' in args else '\'%\''
    # search='\'%John%\''
    books = b.get_books_from_db("SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from (select * from books order by id LIMIT {} OFFSET {}) s where s.authors like {} or s.title like {}) t ".format(limit,offset,search,search));
    print(books)
    return jsonify(books)

@app.route("/bookdetails",methods=["GET"])
def get_book_details():
    args = request.args
    book_id = args.get('book_id')
    print(book_id)
    books = b.get_books_from_db("SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from (select * from books order by id )s where s.book_id={})t".format(book_id))
    return jsonify(books)





if __name__ == "__main__":
    app.run(debug=True)
