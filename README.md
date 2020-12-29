# Python Exercises

### Compilation of python exercises

##### *Guess the number:*
```
In this exercise, the aim of the game is to guess the number (between 1-20) by typing it in..
```
- feedback: I need to apply DRY (don't repeat yourself) more effectively.

###### Solution
```python
from random import randint

guessesTaken = 0

print("Hi, what's your name?")
name = input()

number = randint(1, 20)
print(f"Hi {name}! I'm thinking of a number between 1 and 20, take a guess?")

for guessesTaken in range(6):
    print("Take a guess!")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Too low!")

    if guess > number:
        print("Too high!")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f"Well done {name}! You guessed my number in {guessesTaken} guesses!")

if guess != number:
    number = str(number)
    print(f"Nope, better luck next time, I was thinking of {number}.")
```

##### *Chapt-6.py:*
``` 
This code is an extract from a Python Exercise book and the chapter covered Dictionaries
```
