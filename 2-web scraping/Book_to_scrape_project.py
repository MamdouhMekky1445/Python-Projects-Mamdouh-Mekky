import requests
from bs4 import BeautifulSoup


response = requests.get('https://books.toscrape.com/')
#print(response)

soup = BeautifulSoup(response.content,"html.parser")
#print(soup)

books = soup.find_all("article")
#print(books)
title=''
for book in books:
    title = book.find('h3').find('a')['title']
    rating = book.find('p', class_='star-rating')['class'][1]
    price = book.find('div', class_='product_price').find('p').text
    print(f'The title of the book is {title} and its rating is {rating} stars with price of {price}')


