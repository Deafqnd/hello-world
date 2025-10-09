total = 0

print('I will add up the numbers you give me.')
number = int(input('Number: '))
total += number
print(f'The total so far is {total}')

while number != 0:
    number = int(input('Number: '))
    total += number
    print(f'The total so far is {total}')   

print(f'The total is {total}')
