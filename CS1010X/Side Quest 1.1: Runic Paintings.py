
#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
from runes import *
##########
# Task 1 #
##########
def draw_column(pic, n):
    return stackn(n-2, pic)
def draw_row(pic, n):
    return quarter_turn_right(stackn(n, quarter_turn_left(pic)))
def draw_center(pic, n):
    right = quarter_turn_right(draw_column(pic, n))
    left = quarter_turn_right(draw_column(pic, n))
    center = quarter_turn_right(pic)
    stack_center_on_right = stack_frac((n-2)/(n-1), center, right)
    stack_left_on_center_and_right = stack_frac(1/n, left, stack_center_on_right)
    return quarter_turn_left(stack_left_on_center_and_right)
def egyptian(pic, n):
    top = draw_row(pic, n)
    bottom = draw_row(pic, n)
    middle = draw_center(pic, n)
    stack_middle_on_bottom = stack_frac((n-2)/(n-1), middle, bottom)
    stack_top_on_middle_and_bottom = stack_frac(1/n, top, stack_middle_on_bottom)
    return stack_top_on_middle_and_bottom
