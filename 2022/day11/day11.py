'''
@author: BastienZim

'''

import os
import numpy as np


#path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
path = "/home/bastien/Documents/AdventOfCode/2022"


example = True


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    input = sanitize_input(input)
    #print(input)
    
    monkeys = []
    for x in input:
        if("Monkey" in x):
            monk = {}
            print("New Monkey",x)
        elif("Starting" in x):
            start_items = [int(x) for x in x.split(": ")[-1].split(', ')]
            print(start_items)
            #print(x)
        elif("Operation" in x):
            ope = x.split(": ")[-1]
            print(ope)

        else:
            print(x)    


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

