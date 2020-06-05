# Numbers: Two types of numbers are in python environment.
# 1. Integers and 2. Floats
# Intergers are whole numbers without any decimal and Floats are numbers with decimals after it. 
# Examples: 1, 58 are integers. 4.0, 3.141658 are floats.

# Strings: Strings are an array of characters and can include numbers or characters as well. Strings should be written using within single or doubele qoutation marks "" or ''
# Examples: "Strings look like this." or '37 is a prime number'

# Lists: [1, 'asd', 4.0] is a list. List is indexed. List is mutable. supports indexing and slicing

# Tuples: ('a', 57.12, 7) is a list. List is immutable, indexed, static

# Dictionaries: {'k1': 5, 'k2': 'abc', 'k3': 4.2} is a dictionary. Dictionary is mutable, not indexed, created as key and value pair.


# Numbers

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
print(5*33-66+33/33+0.25)

# 44
# 29
# 34
# Floats
# Find Square
import math
math.pow(9,2)

# Find Square root
import math
math.sqrt(9)


# Strings

s = 'hello'

# Print out 'e' using indexing
print(s[1])

# Reverse the string 'hello' using slicing:
print(s[::-1])

# Print out the 'o'
# Method 1:
print(s[-1])
# Method 2:
print(s[4])


# Lists

# Build this list [0,0,0] two separate ways.
# Method 1:
L1 = [0,0,0]
# Method 2:
L2 = []
L2.append(0)
L2.append(0)
L2.append(0)
print(L2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)


# Dictionaries

# Grab 'hello' using keys and indexing.
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# No indexting hence no sorting.


# Tuples

# List is dynamic, tuple is static.
# Lists are mutable, Tuples are immutable
# Tuples: ('a', 57.12, 7)


# Sets

# Sets have unique values only.

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))


# Booleans

# What will be the resulting Boolean of the following pieces of code?
# 2 > 3, False
# 3 <= 2, False
# 3 == 2.0, False
# 3.0 == 3, True
# 4**0.5 != 2, False

# What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

# False
