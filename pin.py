PIN = "090820"

print('WELCOME TO MY FUN THING')
entry = input('TRY TO GUESS THE PIN: ')

while entry != PIN: 
    print('\nINCORRECT PIN. TRY AGAIN')
    entry = input('ENTER YOUR PIN: ')

print('\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT :D')
