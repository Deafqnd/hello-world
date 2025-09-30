print('TWO QUESTIONS!')
print('Think of an object, and I\'ll try to guess it.')
print()
question1 = input('Question 1) Is it an animal, vegetable, or item? \n')
if question1 == 'animal':
    question2 = input('Question 2) Is it bigger than a breadbox? \n')
    if question2 == 'yes':
        print('My guess is you\'re thinking of a moose!')
    elif question2 == 'no':
        print('My guess is you\'re thinking of a mouse!')
    else:
        print('Something went wrong!')
elif question1 == 'vegetable':
    question2 = input('Question 2) Is it bigger than a breadbox? \n')
    if question2 == 'yes':
        print('My guess is you\'re thinking of a watermelon!')
    elif question2 == 'no':
        print('My guess is you\'re thinking of a carrot!')
    else:
        print('Something went wrong!')
elif question1 == 'item':
    question2 = input('Question 2) Is it bigger than a breadbox? \n')
    if question2 == 'yes':
        print('My guess is that you\'re thinking of a Camaro!')
    elif question2 == 'no':
        print('My guess is that you\'re thinking of a paperclip!')
    else:
        print('Something went wrong!')
