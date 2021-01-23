#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
from runes import *
###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
    return beside(pic, stackn(2, fractal(pic, n-1)))
    
# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here
