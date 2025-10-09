import random

number = random.randrange(1, 11)
guess = int(input('Try to guess the number between 1 and 10: '))

while guess != number:
    print('Incorrect! Try again!')
    number = random.randrange(1, 11)
    guess = int(input('Try to guess the number between 1 and 10: '))

print('Yay! You got it right!')
