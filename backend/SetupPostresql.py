import books as b

class SetupPostgresql:
    def __init__(self):
        #load data from csv files to postgresql
        b.create_table_from_csv('data/book_tags.csv','book_tags')
        b.create_table_from_csv('data/ratings.csv','ratings')
        b.create_table_from_csv('data/tags.csv','tags')
        b.create_table_from_csv('data/to_read.csv','to_read')

