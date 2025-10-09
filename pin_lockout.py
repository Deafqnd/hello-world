PIN = '090820'
tries = 0

print('WELCOME TO ANOTHER GUESSING GAME')
entry = input('ENTER YOUR GUESS: ')
tries += 1

while entry != PIN and tries < 4:
    print('\nINCORRECT PIN. TRY AGAIN.')
    entry = input('ENTER YOUR GUESS: ')
    tries += 1

if entry == PIN: 
    print('\nPIN ACCEPTED. YOU GUESSED IT RIGHT, CONGRATS!')
elif tries >= 3:
    print('\nYOU HAVE RUN OUT OF TRIES. BETTER LUCK NEXT TIME')
