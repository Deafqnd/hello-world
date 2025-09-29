score = 0

ready = input('Are you ready for a quiz? Y/N: ')
if ready == 'Y':
    print('Okay, here it comes!')
    question1 = input('Q1) What is the capital of Alaska? \n     1) Melbourne     \n     2) Anchorage     \n     3) Juneau \n')
    if question1 == '3':
        print('Correct!')
        score += 1
    else:
        print('Sorry, the correct answer is 3) Juneau')
    question2 = input('Q2) In Python, the way you get a keyboard input is the keyboard_input function. \n     1) True \n     2) False \n')
    if question2 == '2':
        print('Correct!')
        score += 1
    else: 
        print('Sorry, in Python, you would use the "input" function to get keyboard input')
    question3 = input('Q3) What is the result of 9 + 6 / 3? \n      1) 5 \n     2) 11 \n     3) 15/3 \n')
    if question3 == '2':
        print('Correct!')
        score += 1
    else: 
        print('Sorry, the correct answer is 2')
    print(f'Overall, your score was {score} out of 3!')
    print('Thanks for playing!')
else: 
    print('See you later!')
