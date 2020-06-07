# Function Practice Exercises
# Problems are arranged in increasing difficulty:
#
# Warm-up - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# LEVEL 2 PROBLEMS:

# NUMBER 1
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(nums):
    """
    DOCSTRING: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    :param nums: a list of integers.
    :return: Boolean
    """
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


# Check
has_33([1, 3, 3, 3, 2, 3])
# Check
has_33([1, 3, 1, 3])
# Check
has_33([3, 1, 3])


# NUMBER 2
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    """
    DOCSTRING: Given a string, return a string where for every character in the original there are three characters
    :param text: any word
    :return: formatted string
    """
    out = ''
    for c in text:
        out += (c * 3)
    return out


# Check
paper_doll('Hello')
# Check
paper_doll('Mississippi')


# NUMBER 3
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(a, b, c):
    """
    DOCSTRING: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
    :param a: integer
    :param b: integer
    :param c: integer
    :return: integer below 21 of 'BUST'
    """
    n = a + b + c
    if n <= 21:
        return n
    elif n <= 31 and 11 in (a, b, c):
        return n - 10
    else:
        return 'BUST'


# Check
blackjack(5, 6, 7)
# Check
blackjack(9, 9, 9)
# Check
blackjack(9, 9, 11)


# NUMBER 3
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(arr):
    """
    DOCSTRING: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 9 (every 6 will be followed by at least one 9).
    :param arr: an array
    :return: formatted selective sum
    """
    cont = True
    s = 0
    for i in range(len(arr)):
        while cont:
            if arr[i] != 6:
                s += arr[i]
                break
            else:
                cont = False
                break
        while not cont:
            if arr[i] == 9:
                cont = True
                break
            else:
                break
    return s


# Check
summer_69([0, 1, 6, 9, 4, 5])
# Check
summer_69([4, 5, 6, 7, 8, 9])
# Check
summer_69([2, 1, 6, 7, 9, 11, 2])
