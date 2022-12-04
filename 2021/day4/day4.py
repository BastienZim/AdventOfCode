'''
up=Down
down = up


'''

from os import chdir

import numpy as np
from numpy.core.fromnumeric import argmax

dir = "/home/bastienzim/Documents/perso/adventOfCode/"
day = "day2/"


def check_numbers(sample, numbers):
    ##print(sample, numbers)
    for x in sample:
        if x not in numbers:
            return(False)
    #print(sum(sample))
    #print("!!!!!  We have a winner  !!!!!")
    return(True)

def check_board_status(board, numbers):
    for i in range(5):#rows
        sample_check = board[i,:]
        if(check_numbers(sample_check, numbers)): return True
    for j in range(5):#columns
        sample_check = board[:,j]
        if(check_numbers(sample_check, numbers)): return True
    return(False)

def fist_part(numbers_drawn, boards):
    game_won = False
    for draw_number in range(5, len(numbers_drawn)):
        if(not game_won):
            numbers = numbers_drawn[:draw_number]
            for i,board in enumerate(boards):
                if(check_board_status(board, numbers)):
                    game_won = True
                    score = numbers[-1]*sum(list(filter(lambda x: x not in numbers , list(np.ravel(board)))))
                    print("board number %d wins at the %d th number drawn\n SCORE = %d !!!!"%(i, draw_number, score))
                    print()
                    break

def get_win_index(board, numbers_drawn):
    '''
    Same code as part one, but we only check the winning rank.
    '''
    game_won = False
    for draw_number in range(5, len(numbers_drawn)):
        if(not game_won):
            numbers = numbers_drawn[:draw_number]
            if(check_board_status(board, numbers)):
                game_won = True
                return(draw_number)
                break
    return(-1)

def main():
    numbers_drawn, boards = get_input(False)
    #fist_part(numbers_drawn, boards)
       
    
    board_ranks = [get_win_index(board, numbers_drawn) for board in boards]
    worst_board_index = argmax(board_ranks)
    
    print(worst_board_index)
    fist_part(numbers_drawn, [boards[worst_board_index]])
    
    





def clean_board(dirty_boards):
    board = list(map(lambda x : x.replace("  "," ").split(" "), dirty_boards))
    board = [list(map(lambda x : int(x), filter(lambda elt : len(elt)!=0, row))) for row in board]
    return(np.array(board))

def get_input(exBOOL = False):
    if(exBOOL): path = "./day4/example_in.txt" 
    else: path = "./day4/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)
    input = list(map(lambda x: x.replace("\n",""), input))
    numbers_drawn = list(map(lambda x: int(x), input[0].split(",")))
    #print(numbers_drawn)
    dirty_boards = [input[i:i+5] for i in range(2, len(input),6)]
    boards = list(map(lambda x: clean_board(x), dirty_boards))


    return (numbers_drawn, boards)


if __name__ == "__main__":
    main()

