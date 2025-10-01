print('WELCOME TO DEAFQND\'S TINY ADVENTURE.')
name = input('Before we start your first race, let\'s get your name!')
print(f'Wonderful! Now, let\'s begin, {name}!')
position = 22
print()
r1 = input('You are starting a go-kart race from last! You need to make up places quickly. \n Are you more of a "patient" person, or "impatient" person? ')
if r1 == 'patient':
    position == 16
    r2 = input('Great! You\'re now in 16th! Your tyres are wearing quickly, however. \n Would you like to pit "sooner" or try to survive and pit "later"? ')
    if r2 == 'sooner':
        position == 11
        r4 = input('Wonderful! You\'re now 11th! So close to points! Last decision! \n Do you want to "push" and try for more places, or "conserve" and let the race come to you? ')
        if r4 == 'push':
            position == 7
            print(f'Great job! You finished in 7th! Congrat\'s {name}! That\'s 6 points to your tally! Amazing finish!')
        elif r4 == 'conserve':
            position == 9
            print(f'Good job! You finished in 9th! You definetly could\'ve finished higher, but you were smart and played it safe! \n You scored 2 points, {name}!')
    elif r2 == 'later':
        position == 12
        r5 = input('Good management, you\'re now in 12th! The other\'s have worn their tyres and are so close! \n Do you want to "push" now, or "let" them take each other out? ')
        if r5 == 'push':
            position == 5
            print(f'Incredible job, {name}, thats P5! Unbelievable stuff! That was magic, enjoy this moment!')
        elif r5 == 'let':
            position == 6
            print(f'Wow! They did take each other out! You\'re P6, P6! Great judgement, {name}!')
elif r1 == 'impatient':
    position == 15
    r3 = input('Great, you\'re now in 15th. You\'ve still got a ways to go but you can do it! \n Your tyres are wearing quickly, though, would you like to pit for "medium" tyres, or "hard" tyres? ')
    if r3 == 'medium':
        position == 10
        r6 = input('Awesome job, those mediums are working wonders! You\'re in 10th now! These tyres might not last you to the end, however! \n Would you like to pit "again" and try to regain positions, or try to "stay" out \'till the end? ')
        if r6 == 'again':
            position == 8
            print(f'Nice work! You\'re P8, {name}! You tried your best and let your pace do the talking. Good work!')
        elif r6 == 'stay':
            position == 22
            print(f'Oh no! You\'ve got a puncture and you\'re now out of the race. You tried your best, but the tyres couldn\'t go the distance. Better luck next time!')
    elif r3 == 'hard':
        position == 9
        r7 = input('Great! Your tyres feel great, and you feel you have enough pace that you can make it into some higher places. \n Do you want to push "flat", or do you want to push with "restraint"? ')
        if r7 == 'flat':
            position == 4
            print(f'Incredible job! Your pace was unmatchable today! If you hadn\'t had to start from last, you probably would\'ve finished on the podium! Great job, {name}!')
        elif r7 == 'restraint':
            position == 5
            print(f'Awesome! You definetly had more pace in you, but those tyres might not\'ve gone the distance! Great work and smart management! P5, P5! See ya back in the pitlane!')
