Question 1

Consider the following functions:
foo = lambda x: lambda a, b: a * x + b
bar = foo(5)
What's the value of bar(2, 3)?

Ans:

13

Question 2

Given function
def thrice(f):
    return lambda x: f(f(f(x)))
and add1 = lambda x: x + 1.

What would be the result of the following two expressions?

thrice(thrice(add1))(0)
thrice(thrice)(add1)(0)

Ans:
9,27

Question 3: *Hard* Basic Morphology - Part 1

We have previously learnt about numbers and how they can be easily converted from one base to another.

Recall that binary numbers are represented with only two symbols, and as such, the non-negative integers form the following sequence.

0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 10000, 10001

Their decimal counterparts would be 0 to 17. Write a function decimal_to_binary, that takes a non-negative decimal integer, and converts it into its binary representation, a string.

Ans:

def decimal_to_binary(number):
    B_Number = 0
    cnt = 0
    while (number != 0): 
        rem = number % 2
        c = 10 ** cnt  
        B_Number += rem * c  
        number //= 2
        cnt += 1
    B_str = str(B_Number)
    return B_str 
    
Question 4

plus is a function that takes in two numbers and return the sum. Given the following functions:

add1 = lambda x: x + 1

def compose(f, g):
    return lambda x: f(g(x))


def repeated(f, n):
    if n == 0:
        return lambda x: x
    else:
        return compose(f, repeated(f, n - 1)) 

Can you implement plus using repeated and add1? You may assume that the two input numbers are both non-negative.
Hint: x + y may be considered as x + 1 for y times.

Ans:

def plus(x, y):
    return repeated(add1, y)(x)


Question 5: *Hard* Basic Morphology - Part 2

Other than just binary and decimal, we can have numbers of any base. Common bases that we work with include octal, hexadecimal and base64.

Here is a table of numbers from 0 to 15 in each of the above mentioned bases except base64.

https://web.archive.org/web/20190714220120/http://www.themathwebsite.com/TogglerNumbers/Octal.GIF

Write a function make_decimal_to_n_ary_converter that accepts a number n where 1 < n < 17, and returns a number converter that converts a given decimal number into that of base n.


Ans:


def make_decimal_to_n_ary_converter(n):
    def converter(x):
        if x==0 or x==1:   
            return str(x)
        i=x
        b=('A','B','C','D','E','F')
        result = ""
        while i>0:
            a=i%n         
            if a<10:
                result = str(i%n)+result
            else:
                d=a-10
                result = b[d] + result
            i=i//n
        return result
    return converter
decimal_to_binary = make_decimal_to_n_ary_converter(2)
decimal_to_octal = make_decimal_to_n_ary_converter(8)
decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)


Question 6: *Hard* Basic Morphology - Part 3

Now, converting from decimal to other bases is useful, but we need to be able to convert back too!

Write a function hexadecimal_to_decimal that takes a string representation of a hexadecimal number and converts it into a decimal number.

Ans:


def hexadecimal_to_decimal(hex_number):
    res = int(hex_number, 16) 
    return res
    
Question 7: *Hard* Basic Morphology - Part 4

To step things up, now, we want to be able to convert a number from any base to decimal.

Write a function make_n_ary_to_decimal_converter that takes a number n where 1 < n < 17 and returns a number converter that converts string representations of numbers of base n into decimal numbers.

Ans:

def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent
    def converter(number):
    #split number in figures
        figures = [int(i,n) for i in number]
        #invert oder of figures (lowest count first)
        figures = figures[::-1]
        result = 0
        #loop over all figures
        for i in range(len(figures)):
            #add the contirbution of the i-th figure
            result += figures[i]*n**i
        return result
    return converter
        
binary_to_decimal = make_n_ary_to_decimal_converter(2)
octal_to_decimal = make_n_ary_to_decimal_converter(8)
hexadecimal_to_decimal = make_n_ary_to_decimal_converter(16)

Question 8: *Hard* Basic Morphology - Part 5

Finally, we want to be able to convert numbers from any base, to any other base!

Write a function make_p_ary_to_q_ary_converter that takes two numbers p and q, and returns a converter that takes a string representation of a number in base p, and returns the string representation of the number in base q.
Note that make_decimal_to_n_ary_converter and make_n_ary_to_decimal_converter have already been defined for you.

As usual, assume 1 < p, q < 17.

Ans:


def compose(f, g):
    return lambda x: f(g(x))
def make_p_ary_to_q_ary_converter(p, q):
    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q
    return compose(make_decimal_to_n_ary_converter(q),make_n_ary_to_decimal_converter(p))
binary_to_octal = make_p_ary_to_q_ary_converter(2, 8)
hexadecimal_to_binary = make_p_ary_to_q_ary_converter(16, 2)
octal_to_hexadecimal = make_p_ary_to_q_ary_converter(8, 16)
octal_to_binary = make_p_ary_to_q_ary_converter(8, 2)
