# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.


try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print('wrong input')

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'


x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("Can't divide by Zero (0)")
finally:
    print('All Done.')


# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.


def ask():
    while True:
        try:
            inp = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print(f'Thank you, your number {inp} square is: {inp ** 2}')
            break


ask()
