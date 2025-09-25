name = input('Hey! What\'ts your name? ')
age = int(input(f'Ok, {name}, how old are you? '))
print()
if age < 16:
    print('You can\'t drive just yet.')
if age < 18: 
    print('Looks like you can\'t vote man.')
if age < 21:
    print('No drinking for you (probably for the best)')
if age > 21:
    print('You can do anything that\'s legal, since you\'re old enough!')
