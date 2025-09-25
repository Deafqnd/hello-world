robot_location = 40
ball_location = 45
goal_location = 30
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")
if robot_location > goal_location:
    print("You are beyond the goal.")
if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
# The if statements instruct each piece of code underneath it as to whether or not it should run. Once the if condition is fulfilled, it runs the code beneath it
# The purpose of the indent is to tell the computer what code falls under the if statement and which does not. 
# This also helps tell us what the fulfilled if statement is supposed to do
