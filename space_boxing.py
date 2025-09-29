venus = 0.78
mars = 0.39
jupiter = 2.65
saturn = 1.17
uranus = 1.05
neptune = 1.23

earth_weight = int(input('Please enter your current Earth weight: '))

v_weight = earth_weight * venus
m_weight = earth_weight * mars
j_weight = earth_weight * jupiter
s_weight = earth_weight * saturn
u_weight = earth_weight * uranus
n_weight = earth_weight * neptune

print('I have information on the following planets: ')
print('     1. Venus      2. Mars      3. Jupiter ')
print('     4. Saturn     5. Uranus    6. Neptune ')

planet = input('Which planet are you visiting? ')
if planet == '1':
    print(f'Your weight would be {v_weight} pounds on that planet.')
elif planet == '2':
    print(f'Your weight would be {m_weight} pounds on that planet.')
elif planet == '3':
    print(f'Your weight would be {j_weight} pounds on that planet.')
elif planet == '4':
    print(f'Your weight would be {s_weight} pounds on that planet.')
elif planet == '5':
    print(f'Your weight would be {u_weight} pounds on that planet.')
elif planet == '6':
    print(f'Your weight would be {n_weight} pounds on that planet')
else:
    print('Invalid input')
