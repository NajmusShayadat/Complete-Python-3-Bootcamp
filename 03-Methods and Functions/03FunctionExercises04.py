# Function Practice Exercises
# Problems are arranged in increasing difficulty:
#
# Warm-up - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve

# CHALLENGING PROBLEMS:
# NUMBER 1
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False


def spy_game1(nums):
    """
    DOCSTRING: a function that takes in a list of integers and returns True if it contains 007 in order
    :param nums: an array containing integers
    :return: Boolean
    """
    count = 0
    for i in nums:
        while count == 0:
            if i == 0:
                count += 1
                break
            else:
                break
        while count == 1:
            if i == 0:
                count += 1
                break
            else:
                break

        while count == 2:
            if i == 7:
                count += 1
                break
            else:
                break
    if count == 3:
        return True
    else:
        return False


def spy_game(nums):
    """
    DOCSTRING: a function that takes in a list of integers and returns True if it contains 007 in order
    :param nums: an array containing integers
    :return: Boolean
    """
    count = [0, 0, 7, 'a']
    for i in nums:
        if i == count[0]:
            count.pop(0)  # count.remove(num) also works
    return 1 == len(count)


# Check
spy_game1([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 2, 4, 0, 0, 7, 5])
# Check
spy_game1([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 0, 2, 4, 0, 5, 7])
# Check
spy_game1([1, 7, 2, 0, 4, 5, 0])
spy_game([1, 7, 2, 0, 4, 5, 0])


# NUMBER 2
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):
    """
    DOCSTRING: a function that returns the number of prime numbers that exist up to and including a given number
    :param num: integer
    :return: list and number of primes up to the input
    """
    c = 0
    numbers = []
    if num < 2:
        return 0

    for i in range(2, num + 1):
        if i == 2:
            c += 1
            numbers.append(i)
        elif i > 2 and i % 2 == 0:
            pass
        elif i < 9:
            c += 1
            numbers.append(i)
        else:
            d = range(3, (int(i ** 0.5) + 1), 2)
            for n in d:
                if i % n == 0:
                    break
                elif i % n != 0 and n == d[-1]:
                    c += 1
                    numbers.append(i)
                else:
                    continue
    print(numbers)
    return c


# Check
count_primes(20)
# Check
count_primes(1000)
