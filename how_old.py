name = input('Hey! What\'ts your name? ')
age = int(input(f'Ok, {name}, how old are you? '))
print()
if age < 16:
    print(f'You can\'t drive just yet, {name}.')
if age < 18: 
    print(f'Looks like you can\'t vote, {name}.')
if age < 21:
    print(f'No drinking for you, {name} (probably for the best)')
if age > 21:
    print(f'You can do anything that\'s legal, since you\'re old enough! Enjoy life, {name}')
