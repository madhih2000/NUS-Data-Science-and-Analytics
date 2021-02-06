##########
# Task 1 #
##########

def dragonize(order, curve):
    pattern = curve
    for _ in range(order):
        pattern = connect_ends(revert(rotate(-pi/2)(pattern)), pattern)
    return put_in_standard_position(pattern)
