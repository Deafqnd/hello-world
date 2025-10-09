import random

number = random.randrange(1, 101)
guesses = 1

guess = int(input('First guess: '))
guesses += 1

while guess != number and guesses <= 7:
    if guess < number:
        print('Sorry, too low! Try again!')
        guess = int(input(f'Guess #{guesses}: '))
        guesses += 1
    elif guess > number: 
        print('Sorry, too high! Try again!')
        guess = int(input(f'Guess #{guesses}: '))
        guesses += 1

print('You guessed it! What are the odds?!?')
