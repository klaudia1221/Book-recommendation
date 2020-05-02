import requests
from bs4 import BeautifulSoup
import books_server as bs
import books as b

# b.add_column_to_table('books','book_cover_url')
book_ids = bs.get_book_ids('book_cover_url') #book_ids where there is no link to cover img
print(book_ids)
for book_reference_number in book_ids:
    page = requests.get('https://www.goodreads.com/book/show/' +str(book_reference_number[0]))
#
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        book_cover_url = (soup.find(id="coverImage").attrs['src'])
        print(book_cover_url)
        b.updateTable(book_reference_number[0],'book_cover_url', book_cover_url)
    except(Exception, AttributeError) as error:
        print(error)