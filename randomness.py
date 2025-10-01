import random

x = random.randrange(10) 
# 0-9
print(f'My random number is {x}.')

print()
print('Here are some random numbers from 1 to 5...')
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6))

print()
print('Here are some random numbers from 1 to 100...')
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print('Will these next two random numbers be the same?')
a = random.randrange(10)
b = random.randrange(10)

if a == b:
    print(f'Wow! Both numbers were {a}!')
else:
    print('The two random numbers were different. Not too surprising.')

# If we change the random.randrange from (1, 6) to (1, 5) instead, it will show a random number from 1-4, rather than 1-5, since we are stating that the number cannot be larger or equal to 5. 
# This number is the maximum number that the random generator can pick, with no numbers ever going over this value. 
# They change based on the maxumum value that we give it.
# I think that they can use this to simulate random movement or other random actions that characters or NPC's can do.
