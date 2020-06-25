# Example Project - Working with Multiple Pages and Items Let's show a more realistic example of scraping a full
# site. The website: http://books.toscrape.com/index.html is specifically designed for people to scrape it. Let's try
# to get the title and price of every book that has a 2 star rating and at the end just have a Python dict with all
# their titles.
#
# We will do the following:
#
# Figure out the URL structure to go through every page
# Scrap every page in the catalogue
# Figure out what tag/class represents the Star rating and price
# Filter by that star rating using an if statement
# Store the results to a dict


import requests
import bs4

import re

page_url = "http://books.toscrape.com/catalogue/page-{}.html"
book_dict = {}
pat = r'\d+.\d+'

for n in range(1, 10):

    page = requests.get(page_url.format(n))
    soup = bs4.BeautifulSoup(page.text, 'lxml')
    books = soup.select('.product_pod')
    prices = soup.select('.price_color')

    for i in range(len(books)):

        book = books[i]
        price = prices[i]

        if len(book.select(".star-rating.Two")) != 0:
            two_star_title = book.select('a')[1]['title']
            book_price = float(re.findall(pat, price.get_text())[0])

            book_dict[two_star_title] = book_price
