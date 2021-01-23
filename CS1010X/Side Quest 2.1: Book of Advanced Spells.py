#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, picture):
    result = picture #if n = 1, must return original pic
    for i in range(2,n+1):  #for the remaining layers
        result = overlay_frac(1/i, scale((n-i+1)/n, picture), result)
    return result


# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

from math import sin, cos, pi
def helix(picture, n):
    R = 1/2 - 1/n
    A = 2 * math.pi/n
    def small_picture(i):
        return translate(R * math.cos(math.pi/2 + i * A),
                         R * math.sin(math.pi/2 + i * A),
                         scale(2/n, picture))
    result = small_picture(1)
    for i in range(2, n+1):
        result = overlay_frac(1/i, small_picture(i), result)
    return result
    

# Test
#show(helix(make_cross(rcross_bb), 9))
