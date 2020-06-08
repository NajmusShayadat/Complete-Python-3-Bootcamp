# Functions and Methods Homework

# PROBLEM 1
# Write a function that computes the volume of a sphere given its radius.

import math
import string  # for problem number 7


def vol(rad):
    """
    DOCSTRING: computes the volume of a sphere given its radius.
    :param rad: radius (number)
    :return: Volume of sphere (number)
    """
    return round((4 / 3) * math.pi * rad ** 3, 2)


# Check
vol(2)


# PROBLEM 2
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    """
    DOCSTRING: checks whether a number is in a given range
    :param num: input number to check
    :param low: lower range
    :param high: higher range
    :return: string
    """
    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is NOT in the range between {low} and {high}'


def ran_bool(num, low, high):
    """
    DOCSTRING: another version of the previous function which checks whether a number is in a given range
    :param num: input number to check
    :param low: lower range
    :param high: higher range
    :return: Boolean
    """
    return num in range(low, high + 1)


# Check
ran_check(5, 2, 7)
ran_bool(3, 1, 10)


# PROBLEM 3
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


def up_low(str3):
    """
    DOCSTRING: a function that accepts a string and calculates the number of upper case letters and lower case letters.
    :param str3: Any string
    """
    uc = 0
    lc = 0
    for c in str3:
        if c.isupper():
            uc += 1
        elif c.islower():
            lc += 1
        else:
            pass
    print(f'Original String : {str3}')
    print(f'No. of Upper case characters :  {uc}')
    print(f'No. of Lower case characters :  {lc}')


st = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(st)


# PROBLEM 4
# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(lst):
    """
    DOCSTRING: a function that takes a list and returns a new list with unique elements of the first list.
    :param lst: any list
    :return:
    """
    return list(set(lst))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6])


# PROBLEM 5
# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24


def multiply(numbers):
    """
    DOCSTRING: a function to multiply all the numbers in a list.
    :param numbers: list
    :return: number
    """
    out = 1
    for n in numbers:
        out *= n
    return out


multiply([1, 1, 1])


# PROBLEM 6
# Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(s):
    """
    DOCSTRING: a function that checks whether a passed in string is palindrome or not.
    :param s: any string
    :return: Boolean
    """
    s = s.replace(" ", "")
    return s == s[::-1]


palindrome('nurses run')


# PROBLEM 7
# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


def ispangram(str1, alphabet=string.ascii_lowercase):
    """
    DOCSTRING: a function to check whether a string is pangram or not.
    :param str1: any string
    :param alphabet: another set of alphabet, default value is set to be "string.ascii_lowercase"
    :return: Boolean
    """
    alphaset = set(alphabet)
    if alphaset <= set(str1):
        return True
    else:
        return False


ispangram("The quick brown fox jumps over the lazy dog")
# print (string.ascii_lowercase)
# output = 'abcdefghijklmnopqrstuvwxyz'
