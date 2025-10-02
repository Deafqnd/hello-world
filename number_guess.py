import random

number = random.randrange(1, 11)
guess = int(input('Im thinking of a number between 1 and 10! \n Your guess: '))

if guess == number:
    print(f'That\'s right! My secret number was {number}!')
else:
    print(f'Sorry, but I was really thinking of {number}.')
