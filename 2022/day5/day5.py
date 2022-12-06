'''
@author: BastienZim

'''

import os
import numpy as np

path = "/home/bastienzim/Documents/perso/adventOfCode/2022/"
#path = "/home/bastien/Documents/AdventOfCode/2022/"


example = False


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    #print(input)
    input = sanitize_input(input)
    split_index = input.index("")
    positions = input[:split_index]
    moves = input[split_index+1:]
    moves = list(map(lambda x: x[5:].split(" from "), moves))
    moves = list(map(lambda x: [x[0]] + x[1].split(" to "), moves))
    moves = list(map(lambda x: [int(k) for k in x], moves))
    
    stack_list =[int(x) for x in positions[-1].split("  ")] 
    stacks = [[] for _ in stack_list]

    for x in positions[:-1][::-1]:
        for i in range(len(stack_list)):
            crate = x[1+4*i : 2+4*i]
            if(crate != " "):
                stacks[i].append(crate)
   # print(stacks)
    """
    #OLD CRATE MOVER
    for x in moves:# qqt, from, to
        #print(f"move {x[0]} crates from {x[1]} to {x[2]}")
        for _ in range(x[0]):
            crate = stacks[stack_list.index(x[1])].pop()
            stacks[stack_list.index(x[2])].append(crate)
    """     
    
    for x in moves:# qqt, from, to
        #print(f"move {x[0]} crates from {x[1]} to {x[2]}")
        #print([a[::-1] for a in stacks])
        crates_to_move = stacks[stack_list.index(x[1])][-x[0]:]
        #print(crates_to_move)
        stacks[stack_list.index(x[2])] = stacks[stack_list.index(x[2])] + crates_to_move
        stacks[stack_list.index(x[1])] = stacks[stack_list.index(x[1])][:-x[0]]
        #print([a[::-1] for a in stacks])
        #print()
        #for _ in range(x[0]):
        #    crate = stacks[stack_list.index(x[1])].pop()
        #    stacks[stack_list.index(x[2])].append(crate)
   
    #Final state of crates 
    #print([a[::-1] for a in stacks])
    print("".join(([a[-1] for a in stacks])))
    #for x in moves:
    #    print(x)

    #for x in positions:
    #    print(x)
    




#def get_moves():

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

