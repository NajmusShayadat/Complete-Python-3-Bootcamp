# PDFs and Spreadsheets Puzzle Exercise
# Let's test your skills, the files needed for this puzzle exercise
#
# You will need to work with two files for this exercise and solve the following tasks:
#
# TASK 1: Use Python to extract the Google Drive link from the .csv file. (HINT: Its along the diagonal from top
# left to bottom right).

import csv
import PyPDF2
import re  # Import for the TASK 2

# folder location
csv_address = 'C:\\Users\\User\\PycharmProjects\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files' \
              '\\find_the_link.csv '


# Opening and reading the csv file
doc = open(csv_address, encoding='utf-8')
all_csv = list(csv.reader(doc))

link = ''
# Row number and element index in that row for the address is the same.
# for example: first item (row 0, index 0) next item (row 1, index 1)..etc
for row, data in enumerate(all_csv):
    link += data[row]

# Closing the file
doc.close()
print(link)

# TASK 2: Download the PDF from the Google Drive link (we already downloaded it for you just
# in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are
# different ways of formatting a phone number!

# folder location
pdf_address = 'C:\\Users\\User\\PycharmProjects\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files' \
              '\\Find_the_Phone_Number.pdf '

# Opening and reading the pdf file, binary mode
doc2 = open(pdf_address, 'rb')
reader = PyPDF2.PdfFileReader(doc2)

# The pattern is a 3 segmented number for this case.

pattern = '[0-9]+[.]?[0-9]+[.]?[0-9]+'

# get the page number to run the loop
for n in range(reader.getNumPages()):

    page = reader.getPage(n)
    page_text = page.extractText()

    # find the pattern in each page
    for match in re.finditer(pattern, page_text):

        # returns number only if the number is above minimum phone number length of 8
        if len(match.group()) > 8:
            print(match.group())
doc2.close()
