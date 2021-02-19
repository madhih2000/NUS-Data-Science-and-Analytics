##########
# Task 1 #
##########
def solve_trivial_2(table):
    a = get_table_state(table)
    if a == (1, 0):
        flip_coins(table, (0, 1))
    elif a == (0, 1):
        flip_coins(table, (1, 0))
    else:
        flip_coins(table, (1, 1))


##########
# Task 2 #
##########
def solve_trivial_4(table):
    a = get_table_state(table)
    b = ()
    for i in a:
        if i == 0:
            b += (1,)
        else:
            b += (0,)
    flip_coins(table, b)
    
    
 

##########
# Task 3 #
##########
def solve_2(table):
    if check_solved(table) == False:
        flip_coins(table, (1, 0))


##########
# Task 4 #
##########
def solve_4(table):
    A = (1, 0, 1, 0)
    B = (1, 1, 0, 0)
    C = (1, 0, 0, 0)
    algorithm = (A, B, A, C, A, B, A)
    for i in algorithm:
        if check_solved(table) == False:
            flip_coins(table, i)

##########
# Task 5 #
##########
def solve(table):
    x = get_table_size(table)
    y = get_table_size(table)
    power = 0
    while y > 1:
        y /= 2
        power += 1
            
    def creator(x):
        moves = ((1, 1), (1, 0))
        for i in range(power - 1):
            new_moves = ()
            for j in range(len(moves)):
                new_moves += (2 * moves[j],)
            for k in range(len(moves)):
                new_moves += (moves[k] + len(moves) * (0,),)
            moves = new_moves
        return moves
        
    turns = creator(x)
    def pattern(x):
        algorithm = ()
        if x == 1:
            algorithm += (x,)
        else:
            algorithm += pattern(x-1)
            algorithm += (x,)
            algorithm += pattern(x-1)
        return algorithm
    real_algorithm = pattern(x-1)
    for i in real_algorithm:
        if check_solved(table) == False:
            flip_coins(table, turns[i])
            
           
