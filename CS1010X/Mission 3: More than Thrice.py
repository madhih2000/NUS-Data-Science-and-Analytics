#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation:
# 27 + 6 = 33
# - compose => f . f
# - thrice => f . f . f
# - thrice(thrice) => thrice(f . f . f) => f . 27 times

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation:
# Returns function equivalent to compose

# (iii) print(thrice(thrice)(sq)(1))
# Explanation:
# (1**2)**27 = 1

# (iv) print(thrice(thrice)(sq)(2))
# Explanation:
# (2**2)**27 = 18014398509481984


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 1:
            return 1
        else:
            return 2*(x**2)

    def op(x, y):
        return x + y

    n  = t+1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def new_fib(n):
    def f(x):
        if x == 0 or x == 1:
            return x
        else:
            return f(x-1) + f(x-2)
    
    def op(x, y):
        return y

    return combine(f, op, n+1)


"""
Or provide an explanation why this can't be done.

# answer here




"""
