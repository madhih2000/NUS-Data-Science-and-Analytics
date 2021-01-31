#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########
# (a)
# (Number) -> Curve
# (b)
# (Unit-Interval) -> Point
# (c)
def vertical_line(point, length):
    def func(t):
        return make_point(x_of(point), (length*t) + y_of(point))
    return func
# (d)
# (Number, Unit-Interval) -> Point
# (e)
# draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))


##########
# Task 2 #
##########
# (a)
# function should take curve type as argument and returns curve type
# the function logic should transform the point (x,y) as (-x, y) 
# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        point = curve(t)
        return make_point(-x_of(point), y_of(point))
    return reflected_curve
	
#draw_connected_scaled(200, arc)
#draw_connected_scaled(200, reflect_through_y_axis(arc))
