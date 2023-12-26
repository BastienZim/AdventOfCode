'''
@author: BastienZim

'''

import os
import numpy as np

example = False

path = "/home/bastienzim/Documents/perso/adventOfCode/2022/"



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
    #print(input)
    elves = []
    current_elf = []
    for x in input: 
        if(x == ""):
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(x))
        #print(x)
    
    elves.append(current_elf)
    #print(elves)
    #print(np.argmax([sum(x) for x in elves]))
    #print(max([sum(x) for x in elves]))
    maxs=[0,0,0]
    #print([sum(x) for x in elves])
    for x in [sum(x) for x in elves]:
        if(x> min(maxs)):
            maxs[np.argmin(maxs)] = x
    print(sum(maxs))
    #inc = has_increased(input, verbose = False)
    #print(inc)
    #counter = count_inc(input)
    #print(counter, sum(inc[1:]))

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

