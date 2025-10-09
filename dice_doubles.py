import random

dice1 = random.randrange(1, 21)
dice2 = random.randrange(1, 21)
total = dice1 + dice2

print('HERE COMES THE DICE!')
print(f'Roll 1: {dice1}')
print(f'Roll 2: {dice2}')
print(f'The total is {total}!')

while dice1 != dice2:
    dice1 = random.randrange(1, 21)
    dice2 = random.randrange(1, 21)
    total = dice1 + dice2
    print(f'Roll 1: {dice1}')
    print(f'Roll 2: {dice2}')
    print(f'The total is {total}!')
