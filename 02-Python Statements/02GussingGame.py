# Guessing Game Challenge
# Let's use while loops to create a guessing game.
#
# The Challenge:
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!


# Generating a random number between 1 and 100.
from random import randint

p = randint(1, 100)

# Printing instruction and asking for an input
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# Guess Numbers are stored in variable gns, counting the number of guesses using variable gns and i
gns = []
i = 0
while True:
    # Asking for an input
    gn = int(input("\nPlease enter your guess! "))
    # Count of the number of input
    i += 1

    # Checking the input is within the limit or not, if not, asking for input again
    if gn < 1 or gn > 100:
        print('\nOUT OF BOUNDS! Please try again!')
        continue

    # Checking if the number guessed correctly, if guessed correctly, the loop breaks.
    elif gn == p:
        print(f'\n*** Congratulations ***\n\nThe number is {gn}.\n\nYou have guessed correctly.\nYou have taken {i} guesses')
        break

    # appending new inputs in a list to compare later for warmer or colder!
    gns.append(gn)

    # if there are more than one guess latest guess is compared with the previous one
    # for only one input len(gns) > 1 returns False. and the condition moves to else section
    if len(gns) > 1:
        if abs(p - gn) < abs(p - gns[-2]):
            print('\nyou are getting WARMER!')
        else:
            print('\nyou are getting COLDER!')

    # The first guess is compared with the actual number to check the difference is bigger than 10 or not
    else:
        if abs(p - gn) < 10:
            print('\nWARM!')
        else:
            print('\nCOLD!')
