import random
choice = random.randrange(1, 21)
response = ''

if choice == 1:
    response = 'It is certain'
elif choice == 2:
    responce = 'It is decidedly so'
elif choice == 3:
    response = 'Without a doubt'
elif choice == 4: 
    response = 'Yes - definetly'
elif choice == 5:
    response = 'You may rely on it'
elif choice == 6:
    response = 'As I see it, yes'
elif choice == 7: 
    response = 'Most likely'
elif choice == 8: 
    response = 'Outlook good'
elif choice == 9: 
    response = 'Signs point to yes'
elif choice == 10:
    response = 'Yes'
elif choice == 11:
    response = 'Reply hazy, try again'
elif choice == 12:
    response = 'Ask again later'
elif choice == 13:
    response = 'Better not tell you now'
elif choice == 14:
    response = 'Cannot predict now'
elif choice == 15:
    response = 'Concentrate and ask again'
elif choice == 16: 
    response = 'Maybe, hard to tell'
elif choice == 17:
    response = 'If you\'re good enough'
elif choice == 18:
    response = 'In the future, near or far, I\'m not gonna tell ya'
elif choice == 19:
    response = 'So close, but try again next time'
elif choice == 20:
    response = 'When pigs fly brochacho'
else:
    response = '8-BALL ERROR!'

print('MAGIC 8-BALL SAYS: ' + response)
