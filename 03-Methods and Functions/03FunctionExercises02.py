# Function Practice Exercises
# Problems are arranged in increasing difficulty:
#
# Warm-up - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# LEVEL 1 PROBLEMS:

# NUMBER 1
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald


def old_macdonald(name):
    """
    DOCSTRING: a function that capitalizes the first and fourth letters of a name.
    :param name: Any name, basically a set of strings
    :return: Formatted Name
    """
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Too short name'


# Check
old_macdonald('macdonald')


# NUMBER 2
# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here.
# The .join() method allows you to join together strings in a list with some connector string.
# For example, some uses of the .join() method:
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence,
# you could just join them with a single space string:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"


def master_yoda(text):
    """
    DOCSTRING: a function that capitalizes the first and fourth letters of a name.
    :param text: Any sentence. (set of words)
    :return: reversed order of the words of the sentence
    """
    t = ' '.join(text.split()[::-1])
    return t


# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')

# NUMBER 3
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True


def almost_there(n):
    """
    DOCSTRING: Given an integer n, return True if n is within 10 of either 100 or 200
    :param n: any integer
    :return: Boolean
    """
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


# Check
almost_there(94)
# Check
almost_there(150)
# Check
almost_there(209)
