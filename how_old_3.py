name = input('Hey man! What\'s your name? ')
age = int(input(f'Ok, {name}, how old are you? '))

if age <= 16:
    print(f'You can\'t drive just yet, {name}.')
if age <= 17 and age >= 16:
    print(f'You can drive, but you can\'t vote just yet, {name}.')
if age >= 18 and age <= 20:
    print(f'You can vote now, but you can\'t drink just yet. Keep waiting!')
if age >= 20:
    print(f'You can do pretty much anyhting, {name}, as long as it\'s legal!')
