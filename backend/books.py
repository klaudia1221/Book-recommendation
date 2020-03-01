import pandas as pd
import psycopg2
from config import config
from sqlalchemy import create_engine

def get_book_data_from_csv(path):
    # ../backend/data/books.csv
    books=pd.read_csv(path, delimiter=',')
    return books

def create_table(path_to_csv,table_name):
    engine = create_engine('postgresql://postgres:books@localhost/books')
    a = get_book_data_from_csv(path_to_csv)
    a.to_sql(table_name, engine)


def get_data_from_db(query):
    """ "SELECT book_id, title, small_image_url FROM books ORDER BY 1 fetch first 10 rows only" """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        print("The number of parts: ", cur.rowcount)
        all_data = cur.fetchall()

        # while row is not None:
        #     # print(row)
        #     row = cur.fetchone()

        cur.close()
        return all_data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateTable(book_id, description):
    conn = None
    try:
        params = config()
        connection = psycopg2.connect(**params)


        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from books where book_id = %s"""
        cursor.execute(sql_select_query, (book_id, ))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update books set description = %s where book_id = %s"""
        cursor.execute(sql_update_query, (description, book_id))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from books where book_id = %s"""
        cursor.execute(sql_select_query, (book_id,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")