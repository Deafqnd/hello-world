team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins +=1
elif team_b_points > team_a_points:
    print('Team B wins!')
    team_b_wins += 1
else: 
    print('Tie')

if team_a_wins > team_b_wins:
    print('Team A has more wins than Team B')
if team_b_wins > team_a_wins:
    print('Team B has more wins than Team A')
else:
    print('Both Teams A and B have the same number of wins')

# This is because since Team A had more points than Team B,
# the if statement added another win to Team A. 
# This means that now both teams are tied on 16 wins.

# elif and else are there to tell the code what happens should Team B have more points, or both teams are tied
# this means that the elif and else statements are there to tell the code what happens if the initial if statement cannot be fulfilled

# This doesn't really make a difference here
