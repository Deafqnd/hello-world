import random

print('WELCOME TO DEAFQND\'S TINY ADVENTURE.')
name = input('Before we start your first race, let\'s get your name! ')
if name == 'Max Verstappen':
    print(f'Well then, let\'s see if you\'re really all of that, {name}!')
elif name == 'Charles Leclerc':
    print(f'Well, at least this time you get to choose your own strategy, {name}!')
elif name == 'Oscar Piastri':
    print(f'Omg u literally my favourite driver Ocsar!')
elif name == 'Lando Norris':
    print(f'Well, its go, go, go, for Lando Norris!')
else:
    print(f'Wonderful! Now, let\'s begin, {name}!')

position = 22
points = 0

print()
r1 = input('You are starting a go-kart race from last! You need to make up places quickly. \nAre you more of a "patient" person, or "impatient" person? ')
if r1 == 'patient':
    position -= 6
    print()
    r2 = input('Great! You\'re now in 16th! Your tyres are wearing quickly, however. \nWould you like to pit "sooner" or try to survive and pit "later"? ')
    if r2 == 'sooner':
        position -= 5
        print()
        r4 = input('Wonderful! You\'re now 11th! So close to points! Last decision! \nDo you want to "push" and try for more places, or "conserve" and let the race come to you? ')
        if r4 == 'push':
            position -= 4
            print()
            print(f'Great job! You finished in 7th! Congrat\'s {name}! That\'s 6 points to your tally! Amazing finish!')
        elif r4 == 'conserve':
            position -= 2
            print()
            print(f'Good job! You finished in 9th! You definetly could\'ve finished higher, but you were smart and played it safe! \nYou scored 2 points, {name}!')
    elif r2 == 'later':
        position -= 4
        print()
        r5 = input('Good management, you\'re now in 12th! The other\'s have worn their tyres and are so close! \nDo you want to "push" now, or "let" them take each other out? ')
        if r5 == 'push':
            position -= 7
            print()
            print(f'Incredible job, {name}, thats P5! Unbelievable stuff! That was magic, enjoy this moment!')
        elif r5 == 'let':
            position -= 6
            print()
            print(f'Wow! They did take each other out! You\'re P6, P6! Great judgement, {name}!')
elif r1 == 'impatient':
    position -= 7
    print()
    r3 = input('Great, you\'re now in 15th. You\'ve still got a ways to go but you can do it! \nYour tyres are wearing quickly, though, would you like to pit for "medium" tyres, or "hard" tyres? ')
    if r3 == 'medium':
        position -= 5
        print()
        r6 = input('Awesome job, those mediums are working wonders! You\'re in 10th now! These tyres might not last you to the end, however! \nWould you like to pit "again" and try to regain positions, or try to "stay" out \'till the end? ')
        if r6 == 'again':
            position -= 2
            print()
            print(f'Nice work! You\'re P8, {name}! You tried your best and let your pace do the talking. Good work!')
        elif r6 == 'stay':
            position += 14
            print()
            print(f'Oh no! You\'ve got a puncture and you\'re now out of the race. You tried your best, but the tyres couldn\'t go the distance. Better luck next time!')
    elif r3 == 'hard':
        position -= 1
        print()
        r7 = input('Great! Your tyres feel great, and you feel you have enough pace that you can make it into some higher places. \nDo you want to push "flat", or do you want to push with "restraint"? ')
        if r7 == 'flat':
            position -= 5
            print()
            print(f'Incredible job! Your pace was unmatchable today! If you hadn\'t had to start from last, you probably would\'ve finished on the podium! Great job, {name}!')
        elif r7 == 'restraint':
            position -= 4
            print()
            print(f'Awesome! You definetly had more pace in you, but those tyres might not\'ve gone the distance! Great work and smart management! P5, P5! See ya back in the pitlane, {name}!')
elif r1 == 'divebomb':
    position -= 10
    print()
    rs1 = input('Wow! A secret section??? Anyways, good job with that divebomb, you\'re now in P12! \nDo you want to keep "pushing", or "let off" a little bit and go with the flow? ')
    if rs1 == 'pushing':
        position -= 6
        print()
        print('Awesome! You\'re up to P7! \nBox, box, it\'s time for some new tyres.')
        print('Great, you\'ve done well and kept 9th! You\'ll make up more places as the others start to pit too.')
        print('It\'s now time for your final push; you can win this!')
        final_push_value = random.randrange(1, 8)
        fpguess = int(input('Just get the number right from 1-7, and you\'ll win this race!'))
        if fpguess == final_push_value:
            positon -= 5
            print('YEEEEESSSSSS!!! YOU\'VE DONE IT!!! YOU\'VE WON FROM LAST!!! INCREDIBLE JOB MATE, YOU DESERVE THIS ONE!!!')
        else:
            position -= 4
            print('Awesome job man! Not nearly a win, but you\'ve finished P2, still an incredible job from last on the grid! \nYou should be proud of yourself!')
    elif rs1 == 'let off':
        position -= 5
        print()
        print('Awesome! Your tyres should last the entire race now because of your good management!')
        print('You\'ve got an immense lead to the people behind, so we\'re gonna pit you for softs and you can blast it \'till the end! Box, box!')
        print('Great! You\'re in P3, so worst you can do is finish on the podium! Let\'s push to the end now!')
        final_push_value = random.randrange(1, 4)
        fpguess = int(input('Just get the number right from 1-3, and you\'ll win this race!'))
        if fpguess == final_push_value:
            position -= 6
            print('YEEEEESSSSSS!!! YOU\'VE DONE IT!!! YOU\'VE WON FROM LAST!!! INCREDIBLE JOB MATE, YOU DESERVE THIS ONE!!!')
        else:
            position -= 5
            print('Awesome job man! Not nearly a win, but you\'ve finished P2, still an incredible job from last on the grid! \nYou should be proud of yourself!')

print(f'Congrats, {name}! You\'ve done well to finish P{position} in your first ever race! I hope to see you again later down the line!')

if position == 1:
    points += 25
    print(f'You scored {points} points on this run! You left nothing on the table this time!')
elif position == 2:
    points += 18
    print(f'You scored {points} points on this run! So close to the win, yet so far away! Better luck next time!')
elif position == 3:
    points += 15
    print(f'You scored {points} points on this run! Great job finishing on the podium!')
elif position == 4:
    points += 12
    print(f'You scored {points} points on this run! That\'s a great points haul for your first time!')
elif position == 5:
    points += 10
    print(f'You scored {points} points on this run! That\'s a great points haul for your first time!')
elif position == 6:
    points += 8
    print(f'You scored {points} points on this run! That\'s a great points haul for your first time!')
elif position == 7:
    points += 6
    print(f'You scored {points} points on this run! Great job for your first race!')
elif position == 8:
    points += 4
    print(f'You scored {points} points on this run! Great job for your first race!')
elif position == 9:
    points += 2
    print(f'You scored {points} points on this run! Great job for your first race!')
elif position == 10:
    points += 1
    print(f'You scored {points} points on this run! Great job for your first race!')
else:
    print('Great job on your first race! You didn\'t score any points this time, but you\'ve done good to keep it out of the wall! \nHope to see you again!')
