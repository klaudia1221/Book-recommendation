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
    df2=b.get_data_from_db("SELECT book_id, title, image_url FROM books ORDER BY 1 fetch first 10 rows only")
    result = {}
    for index, row in df2.iterrows():
        result[index] = dict(row)
    return jsonify(result)

@app.route("/books",methods=["GET"])
def get_books():
    args = request.args
    page = args.get('page') if 'page' in args else 1
    limit = args.get('limit') if 'limit' in args else 10000
    offset=(int(page)-1)*int(limit)
    print(offset)
    search="\'%"+(args.get('search')).lower()+"%\'" if ('search' in args ) and (len((args.get('search')))>1) else '\'%\''
    # search='\'%John%\''
    books = b.get_data_from_db("SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from (select * from books order by id LIMIT {} OFFSET {}) s where LOWER(s.authors) like {} or LOWER(s.title) like {}) t ".format(limit,offset,search,search));
    print(books)
    return jsonify(books)

@app.route("/bookdetails",methods=["GET"])
def get_book_details():
    args = request.args
    book_id = args.get('book_id')
    print(book_id)
    books = b.get_data_from_db("SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from (select * from books order by id )s where s.book_id={})t".format(book_id))
    return jsonify(books)

@app.route("/bookgenres",methods=["GET"])
def get_book_genres():
    args=request.args
    book_id=args.get('book_id')
    book_genres=b.get_data_from_db("SELECT genre FROM public.books_genres g where g.goodreads_book_id={} order by g.count desc LIMIT 5".format(book_id))
    return jsonify(book_genres)

@app.route("/userbookrating",methods=["GET"])
def get_user_book_rating():
    args = request.args
    book_id=args.get('book_id')
    user_id=args.get('user_id')
    user_book_rating= b.get_data_from_db("select rating from user_ratings where user_id={} and book_id={}".format(user_id,book_id,))

    return jsonify(user_book_rating)

@app.route("/userbooks",methods=["GET"])
def get_user_books():
    args = request.args
    book_id=args.get('book_id')
    user_id=args.get('user_id')
    user_book_rating= b.get_data_from_db("select rating from user_ratings where user_id={} and book_id={}".format(user_id,book_id,))

    return jsonify(user_book_rating)

@app.route("/newbookrating",methods=["GET"])
def add_new_user_book_rating():
    args = request.args
    user_id = args.get('user_id')
    rating = args.get('rating')
    print(user_id)
    # book_id=args.get('book_id')
    # rating= args.get('rating')
    # user_id=args.get('user_id')
    print(args)
    return jsonify(args)


def get_book_ids(column):
    book_ids=b.get_data_from_db("""SELECT cast(book_id as INTEGER) FROM books where {} is null""".format(column))
    return book_ids

def get_book_cover_urls():
    book_cover_urls=b.get_data_from_db("""SELECT cast(book_id as INTEGER), image_url FROM books where book_cover_url is null and image_url like 'https://images.gr-assets.com/books/%'""")
    return book_cover_urls

@app.route("/coldbooks", methods=["GET"])
def get_cold_books():
        books = b.get_data_from_db( "SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from books order by ratings_count desc limit 20) t ");
        print(books)
        return jsonify(books)

@app.route("/getrecommendations", methods=["GET"])
def get_recommendations():
        args=request.args
        ratings = args.get('ratings')
        to_read=args.get('to_read')
        not_interested=args.get('not_interested')

        books = b.get_data_from_db( "SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from books order by average_rating desc offset 102 limit 20) t ");
        print("ratings"+str(ratings))
        print("not_interested"+str(not_interested))

        print("to_read"+str(to_read))
        return jsonify(books)

@app.route("/toprated", methods=["GET"])
def get_top_rated():
    # args=request.args
    # book_ratings = args.get('book_ratings')

        books = b.get_data_from_db( "SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from books order by average_rating desc limit 100) t ");
        print(books)
        return jsonify(books)

@app.route("/toppopular", methods=["GET"])
def get_top_popular():
    # args=request.args
    # book_ratings = args.get('book_ratings')

        books = b.get_data_from_db( "SELECT array_to_json(array_agg(row_to_json(t))) FROM (select * from books order by ratings_count desc limit 100) t ");
        print(books)
        return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)
