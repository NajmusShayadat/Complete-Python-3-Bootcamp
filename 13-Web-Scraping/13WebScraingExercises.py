# Web Scraping Exercises
# Complete the Tasks Below

# PROBLEM 1
# 1 TASK: Import any libraries you think you'll need to scrape a website.
# 2 TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text
# from the homepage.
# 3 TASK: Get the names of all the authors on the first page.
# 4 TASK: Create a list of all the quotes on the first page.
# 5 TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top
# right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath
# each quote, try to find a class only present in the top right tags, perhaps check the span.

# PROBLEM 2
# 6 TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all
# the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this,
# also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For
# debugging purposes, I will let you know that there are only 10 pages, so the last page is
# http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know
# the amount of pages beforehand, perhaps use try/except for this, its up to you!


# SOLUTION 1

import requests
import bs4

website = requests.get('http://quotes.toscrape.com')

authors1 = []
quotes1 = []

soup1 = bs4.BeautifulSoup(website.text, 'lxml')
all_q = soup1.select('.text')
all_a = soup1.select('.author')

for i in range(len(all_q)):
    authors1.append(all_a[i].getText())
    quotes1.append(all_q[i].getText())
authors1 = set(authors1)

print(authors1)
print(quotes1)

tag_item = soup1.select(".tag-item")

for txt in tag_item:
    print(txt.text)

# SOLUTION 2
# importing modules is already done in problem 1


page_base = 'http://quotes.toscrape.com/page/{}'
authors = set()

valid_page = True
i = 1

while valid_page:

    web_page = page_base.format(i)
    web_source = requests.get(web_page)

    soup = bs4.BeautifulSoup(web_source.text, 'lxml')
    page_authors = soup.select('.author')

    if page_authors:

        for author in page_authors:
            authors.add(author.getText())

        i += 1

    else:
        valid_page = False
authors = set(authors)
