# Iterators and Generators Homework

# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


# for problem number 2
import random


def gen_squares(n):
    for a in range(n):
        yield a * a


for x in gen_squares(10):
    print(x)

# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 2):
    print(num)

# Problem 3
# Use the iter() function to convert the string below into an iterator:

s = 'hello'

p = iter(s)
print(next(p))
