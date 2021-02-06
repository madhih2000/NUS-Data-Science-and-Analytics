#Question 1: Task 1

#Write down the difference between unit_circle and alternative_unit_circle.

#You should also point out why this difference exists by examining the code of both unit_circle and alternative_unit_circle in hi_graph.py.

#Answer:

#There is no visible difference when using draw_connected for unit_circle and alternative_unit_circle since the points are all connected.

#When draw_points is used, draw_points(200, unit_circle), the points are evenly spaced out from the start of the arc. However, when draw_points(200, alternative_unit_circle) is used, the points are clustered together at the start of the arc before moving on to being evenly spaced out for the rest for the arc.

#unit_circle has got the arguments 2*pi*t while alternative_unit_circle has got arguments 2*pi*t*t. Therefore, there is an increase in frequency of the number of points in the arc for alternative_unit_circle.

#t increases linearly while t**2 increases more slowly at first but becomes faster.

#t**2 increases more slowly which means there is less distance between each point, which leads to the clustering at the beginning.

#Question 2: Task 2

#(a) Using the definition of the unit_circle as a reference, define a new curve spiral that draws a ‘circle’ which mimics a spiral.

def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))
# draw_connected_scaled(1000, spiral)

#(b) Define a new curve heart that draws a curve by connecting 2 spirals. You should make use of your spiral function to produce the curve.

def heart(t):
    # your answer here
    if t < 0.5:
        return spiral(2 * t)
    else:
        return scale_xy(-1, 1)(spiral)(2 * t - 1)
