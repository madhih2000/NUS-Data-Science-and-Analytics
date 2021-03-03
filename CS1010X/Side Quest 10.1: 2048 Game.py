#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    "Your answer here"
    mat = []
    for i in range(n):
        a = [0]
        mat += [a * n]
    return mat
        

#print(new_game_matrix(4))
            

def has_zero(mat):
    "Your answer here"
    x = flatten(mat)
    if 0 in x:
        return True
    else:
        return False
            

def add_two(mat):
    "Your answer here"
    if not 0 in flatten(mat):
        return mat
    else:
        zero_list = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    zero_list.append([i,j])
        chosen_zero = zero_list[randint(0, len(zero_list)-1)]
        mat[chosen_zero[0]][chosen_zero[1]] = 2
        return mat
                

#print(new_game_matrix(4))
#print(has_zero(new_game_matrix(5)))
#print(has_zero([[5]]))
#print(add_two(new_game_matrix(6)))
#print(add_two([[2, 4, 8, 16], [0, 2, 4, 8], [4, 0, 16, 32], [0, 8, 16, 64]]))
#print(add_two([[4, 8], [16, 0]]))
#print(add_two([[4, 8], [16, 2]]))


###########
# Task 2  #
###########

def game_status(mat):
    "Your answer here"
    counter = 0
    flatten_mat = flatten(mat)
    x = len(mat)
    for i in range((len(flatten_mat)-x)):
        if flatten_mat[i] == flatten_mat[i+x]:
            counter += 1
    for j in range(len(flatten_mat)-1):
        if flatten_mat[j] == flatten_mat[j+1] and (j+1) / x == 0:
            print(j)
            counter += 1
    if 2048 in flatten_mat:
        return "win"
    elif 0 in flatten_mat or counter > 0:
        return "not over"
        return counter
    else:
        return "lose"
        
#print(game_status(new_game_matrix(5)))
#print(game_status([[3, 1, 2, 4], [4, 4, 4, 5], [5, 9, 10, 11], [12, 13, 14, 15]]))   
#print(game_status([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]))


###########
# Task 3a #
###########

def transpose(mat):
    "Your answer here"
    flatten_mat = flatten(mat)
    transposed_mat = []
    x = 0
    while x < len(mat[0]):
        temp_mat = []
        for i in mat:
            temp_mat.append(i[x])
        transposed_mat.append(temp_mat)
        x += 1
    return transposed_mat

#print(transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
#print(transpose([[1, 2, 3], [4, 5, 6]]))
#print(transpose([[0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]))

###########
# Task 3b #
###########

def reverse(mat):
    "Your answer here"
    reversed_mat = [list(x) for x in mat]
    for i in reversed_mat:
        i.reverse()
    return reversed_mat

#print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

############
# Task 3ci #
############

def merge_left(mat):
    new_mat = new_game_matrix(len(mat))
    test_mat = [list(y) for y in mat]
    increment = []

    def helper(row, slot, from_mat, to_mat):
        for l in range(len(from_mat)):
            if to_mat[row][l] == 0:
                to_mat[row][l] = from_mat[row][slot]
                break
        
    for i in range(len(test_mat)):
        for j in range(len(test_mat)):
            if test_mat[i][j] == 0:
                continue
            elif j == len(test_mat) - 1 and test_mat[i][j] > 0:
                helper(i, j, test_mat, new_mat)
            else:
                a = j+1
                for k in range(len(test_mat)-a):
                    if test_mat[i][a] == 0:
                        if a < len(test_mat) - 1:
                            a += 1
                            continue
                        else:
                            helper(i, j, test_mat, new_mat)
                            break
                    elif test_mat[i][a] != test_mat[i][j]:
                        helper(i, j, test_mat, new_mat)
                        break
                    elif test_mat[i][a] == test_mat[i][j]:
                        for l in range(len(test_mat)):
                            if new_mat[i][l] == 0:
                                new_mat[i][l] = (test_mat[i][j] + test_mat[i][a])
                                increment.append(test_mat[i][j] + test_mat[i][a])
                                test_mat[i][a] = 0
                                break
                        break

    return (new_mat, new_mat != mat, sum(increment))          

                
mat = [[2, 0], [0, 0]]
#new_mat = merge_left(mat)
#print(new_mat)

mat2 = [[2, 0, 2, 2], [0, 0, 0, 4], [4, 0, 8, 4], [2, 0, 0, 0]]
#new_mat2 = merge_left(mat2)
#print(new_mat2)

# LEFT
# if no tile on right: add tile of equal value to left most empty cell
# if tile on right is same value: add tile of combined value to left most empty cell
    # - tile now becomes empty
    # - move on to cell to the right of the right cell
# if tile on right is diff value: add current tile value to left most empty cell
    # - tile now becomes empty
    # - process tile on right


#############
# Task 3cii #
#############

def merge_right(mat):
    result = merge_left(reverse(mat))
    return (reverse(result[0]), result[0] != mat, result[2])
    "Your answer here"

mat3 = [[2, 0, 2, 2], [0, 0, 0, 4], [4, 0, 8, 4], [2, 0, 0, 0]]
#new_mat3 = merge_right(mat3)
#print(new_mat3)

# RIGHT
# if no tile on left: add tile of equal value to right most empty cell
# if tile on left is same value: add tile of combined value to right most empty cell
    # - move on to cell to the left of the left cell
# if tile on left is diff value: add current tile value to right most empty cell
    # - process tile on left


def merge_up(mat):
    "Your answer here"
    result = merge_left(transpose(mat))
    return (transpose(result[0]), result[0] != transpose(mat), result[2])

mat4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 0]]
new_mat4 = merge_up(mat4)
print(new_mat4)

def merge_down(mat):
    "Your answer here"
    result = merge_right(transpose(mat))
    return (transpose(result[0]), result[0] != transpose(mat), result[2])

mat5 = [[2, 2, 0, 0], [0, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
new_mat5 = merge_down(mat5)
print(new_mat5)


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    #mat = add_two(add_two([[0, 0, 1024, 1024], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    "Your answer here"
    return (matrix, total_score)

def get_matrix(state):
    "Your answer here"
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    "Your answer here"
    return make_state(add_two(add_two(new_game_matrix(n))), 0)

def adder(result, state):
    if result[1] == True:
        return (make_state(add_two(result[0]), get_score(state) + result[2]), result[1])
    else:
        return (make_state(result[0], get_score(state) + result[2]), result[1])   

def left(state):
    "Your answer here"
    result = merge_left(get_matrix(state))
    return adder(result, state)            

def right(state):
    "Your answer here"
    result = merge_right(get_matrix(state))
    return adder(result, state)

def up(state):
    "Your answer here"
    result = merge_up(state[0])
    return adder(result, state)

def down(state):
    "Your answer here"
    result = merge_down(state[0])
    return adder(result, state)

# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    "Your answer here"

def get_record_matrix(record):
    "Your answer here"

def get_record_increment(record):
    "Your answer here"

############
# Task 5ii #
############

def make_new_records():
    "Your answer here"

def push_record(new_record, stack_of_records):
    "Your answer here"

def is_empty(stack_of_records):
    "Your answer here"

def pop_record(stack_of_records):
    "Your answer here"

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    "Your answer here"

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"

def undo(state):
    "Your answer here"


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)
