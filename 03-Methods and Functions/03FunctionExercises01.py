# Function Practice Exercises
# Problems are arranged in increasing difficulty:
#
# Warm-up - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# WARM-UP SECTION:
# NUMBER 1
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5


def lesser_of_two_evens(a, b):
    """
    DOCSTRING: a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
    :param a: input 1
    :param b: input 2
    :return: lesser of the evens or greater of the other combinattion
    """
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    elif a > b:
        return a
    else:
        return b


# Check
lesser_of_two_evens(2, 4)
# Check
lesser_of_two_evens(2, 5)


# NUMBER 2
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(text):
    """
    DOCSTRING: a function takes a two-word string and returns True if both words begin with same letter
    :param text: Two word string
    :return: Boolean
    """
    t = list(text.lower().split())
    return t[0][0] in t[1][0]


# Check
animal_crackers('Levelheaded Llama')

# Check
animal_crackers('Crazy Kangaroo')


# NUMBER 3
# MAKES TWENTY: Given two integers,
# return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False.
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False


def makes_twenty(n1, n2):
    """
    DOCSTRING: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    :param n1: input 1 (whole number)
    :param n2: input 2 (whole number)
    :return: Boolean
    """
    if n1 == 20 or n2 == 20 or (n1 + n2) == 20:
        return True
    else:
        return False


# Check
makes_twenty(20, 10)
# Check
makes_twenty(2, 3)
