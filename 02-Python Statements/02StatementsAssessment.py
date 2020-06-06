# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for w in st.split():
    if w[0] == 's':
        print(w)

# Use range() to print all the even numbers from 0 to 10.
for n in range(0, 11, 2):
    print(n)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
t = [a for a in range(50) if a % 3 == 0]
print(t)


# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for lst in st.split():
    if len(lst) % 2 == 0:
        print(lst + " <-- is even length!")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the
# number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print
# "FizzBuzz".
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
L = [s[0] for s in st.split()]
print(L)
