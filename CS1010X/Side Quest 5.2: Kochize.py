#Side Quest 5.2: Kochize
#Nature hides many beauties, and one of these, as you have seen, are fractals. Grandmaster Ben now invites you to use your new-found skills to conjure up an image that is not quite so simple: the snowflake fractal, more commonly known as the Koch snowflake.

#This side quest contains two tasks. Complete sidequest05.2-template.py and paste the contents in the code box. You should test each function individually and only fill up the template file after you have confirmed your answer for each function. Upon successful completion of this side quest, you will earn the “Snowflake Catcher” achievement.

#Ans:


##########
# Task 1 #
##########
def kochize(level):
    if level == 0:
        return unit_line
    else:
        curve1 = kochize(level-1)
        return put_in_standard_position(connect_ends(connect_ends(connect_ends((curve1), rotate(pi/3)(curve1)), rotate(-pi/3)(curve1)), curve1))
def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))
    
##########
# Task 2 #
##########
def snowflake():
    curve1 = kochize(5)
    return connect_ends(connect_ends(curve1, rotate(-2*pi/3)(curve1)), rotate(2*pi/3)(curve1))
