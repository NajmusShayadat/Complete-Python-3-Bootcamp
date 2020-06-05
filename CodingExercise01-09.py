# Exercise 01
# Numbers and operators
# Problem statement:
# Write an expression that equals to 100 and print it. No variables.

print(5*33-66+33/33)


# Exercise 02
# Print 
# Problem statement:
# Print "Hello World". No variables.

print ('Hello World')


# Exercise 03
# String Indexing
# Problem statement:
# Write a string index just returns the letter 'r' from 'Hello world'
# Use one line of code. No variables.

print('Hello World'[-3])


# Exercise 04
# String Slicing
# Problem statement:
# Use slicing to grab the wowrd 'ink' from inside 'tinker'
# Use one line of code. No variables.

print('tinker'[1:4])


# Exercise 05
# Print Formatting
# Problem statement:
# Write 'Python rules!' using string formatting
# Use one line of code. No variables.

print('Python {}'.format('rules!'))


# Exercise 06
# Lists
# Problem statement:
# Create a list containing one string, one integer and one float. Order of the variables doesn't matter.
# Use one line of code. No variables.

print(["zero", 1, 2.7])


# Exercise 07
# Dictionaries
# Problem statement:
# Create a dictionary where key are strings and values are integers.
# Use one line of code. No variables.

price = {'apple': 2, 'oranges': 1, 'milk': 4}


# Exercise 08
# Sets
# Problem statement:
# Write an expression that would turn the string "Mississippi" into a set of unique letters.
# Use one line of code. No variables.

print(set("Mississippi"))


# Exercise 09
# SFile I/O
# Problem statement:
# Write a script that opens a file named 'test.txt', writes 'Hello wworld' to the file and closes it
# Use one line of code. No variables.

nfile = open('test.txt','w+')
nfile.write('Hello world')
nfile.close()
