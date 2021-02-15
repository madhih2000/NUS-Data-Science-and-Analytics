#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
from diagnostic import *
from hi_graph_connect_ends import *
# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:
    
def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))
def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize
# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########
# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)
# Choose a significant level for testing for all three sets of functions.
def average_of_five(function):
    sum = 0
    for i in range(0, 5):
        a = function
        print(a)
        sum += a
    return sum / 5
# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below
print(profile_fn ( lambda : gosper_curve(10)(0.1), 10))
print('average: ' + str(average_of_five(profile_fn ( lambda : gosper_curve(10)(0.1), 10))))
# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below
print(profile_fn ( lambda : gosper_curve_with_angle(10, lambda lvl : pi/4)(0.1), 10))
print('average: ' + str(average_of_five(profile_fn ( lambda : gosper_curve_with_angle(10, lambda lvl : pi/4)(0.1), 10))))
#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below
print(profile_fn ( lambda : your_gosper_curve_with_angle(10, lambda lvl : pi/4)(0.1), 10))
print('average: ' + str(average_of_five(profile_fn ( lambda : your_gosper_curve_with_angle(10, lambda lvl : pi/4)(0.1), 10))))
# Conclusion:
# (Time below are to 2 decimal places)
# When the angle is fixed, there would be no significant advantage in speed for the functions that are customized more.
# gosper_curve takes 1.58s but gosper_curve_With angle which is more customized takes 1.99s which is similar. There is no significant difference.
# gosper_curve_with_angle and your_gosper_curve_with_angle are customizable to a great extent but there is significant difference in time (1.99s and 18.26s)
# Customized functions run faster than customizable functions.



##########
# Task 2 #
##########
#  1) Yes. curve(t) gives the output to pt and hence both are the same.
#  2) joe_rotate runs curve(t) every time it is being called out as seen it is twice in joe_rotate. For rotate
#     the program just calls it out once, stores it in pt and uses the stored value when pt is called out.    
#     stores it in the variable pt and uses the stored value when pt is called.
#     When repeated, gosper_curve calls gosperize in a recusrive manner whole gosperize calls rotate twice.
#     For every increase in level of a binary tree, the complexity becomes exponential.
#     Hence, we can conclude that the time complexity for joe_rotate is exponential instead of linear.
