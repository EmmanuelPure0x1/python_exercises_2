# Modules Import
from random import randint
import time

# secret variable is the random integer generator.
secret = int(randint(1, 21))

# Tries variable is the counter variable keeping us informed and the 'point of ref' for the while loop
tries = 0

# Left variable is letting us know how many guesses we have left
left = 6

# While loop is true while certain condition is not met.
while tries < 6:

    play_or_not = input("Play? Y/N > ")

    # below if statement evaluates the input response and quits if input is 'n'
    if play_or_not.lower() == 'n':
        print("Ok, bye")
        break

    else:

        guess = int(input("Give me a number > "))

        # 'guess' evaluated as 'if less than' against 'secret'
        if guess < secret:
            print("Higher!")
            tries += 1
            left -= 1
            # statements printed
            print(f"try: {tries}")
            print(f"guesses left: {left}")

        if guess > secret:
            print("Lower!")
            tries += 1
            left -= 1
            print(f"try: {tries}")
            print(f"guesses left: {left}")

        if guess == secret:
            print("Well done pal, you got it!")
            tries += 1
            left -= 1
            time.sleep(.1)

            print(f"It took you {tries} guess(s).")
            break