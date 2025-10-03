# Question 1: Rams Robotics Grade
latest_test = int(input('Please enter latest test mark: '))
if latest_test <= 49:
    print('Sorry, you are unable to attend this week\'s meeting.')
else:
    print('You are able to attend this week\'s meeting.')

# Question 2: Rams Robotics Sector & Name
name = input('Please enter your name: ')
sector = int(input('Please enter the sector of Robotics you are a part of: \n1) Design & Build \n2) Buisness \n3) Programming \n'))
if sector == 1:
    print(f'D/B: {name}')
elif sector == 2:
    print(f'B: {name}')
elif sector == 3:
    print(f'P: {name}')
else:
    print('Invalid Entry!')

# Question 3: Centering Camera

import random

ball_position = random.randrange(1, 501)
print(f'The ball\'s position is x = {ball_position}')

if ball_position <= 239:
    print('The ball is to the left')
elif ball_position >= 240 and ball_position <= 260:
    print('The ball is centered')
elif ball_position >= 261 and ball_position>= 500:
    print('The ball is to the right')

# Question 4: Picking up balls

detected = input('Is there a detected ball? ')
if detected == 'Y':
    holding = input('Are you already holding a ball? ')
    if holding == 'Y':
        print('Do not pick up the detected ball.')
    elif holding == 'N':
        print('You may pick up the detected ball.')
    else:
        print('Something went wrong!')
elif detected == 'N':
    print('Try scanning again.')
else: 
    print('Something went wrong!')

# Question 5: True & False

# T
# F
# T
# F
# T
# F
# F
# Dont Know
# T 
# T
