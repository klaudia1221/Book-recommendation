import requests
from bs4 import BeautifulSoup
import books_server as bs
import books as b

# b.add_column_to_table('books','description')
book_ids = bs.get_book_ids('description') #book_ids where there is no description
print(book_ids)
for book_reference_number in book_ids:
    page = requests.get('https://www.goodreads.com/book/show/' +str(book_reference_number[0]))
#
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        book_description = (soup.find(id="descriptionContainer").find(style="display:none").get_text())
        print(book_description)
        b.updateTable(book_reference_number[0],'description', book_description)
    except(Exception, AttributeError) as error:
        print(error)