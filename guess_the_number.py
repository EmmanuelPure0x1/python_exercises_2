from random import randint
import time

# In this exercise, the aim of the game is to guess the number (between 1-20) by typing it in..

#def guessMe():

secret = int(randint(1, 3))
tries = 0
left = 6

while tries < 6:

    play_or_not = input("Play? Y/N > ")

    if play_or_not.lower() == 'n':
        print("Ok, bye")
        break

    else:
        guess = int(input("Give me a number > "))

        if guess < secret:
            print("Higher!")
            tries += 1
            left -= 1
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

#guessMe()

