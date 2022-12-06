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
    input = input[0]
    n_distinct = 14
    for i in range(0,len(input)-n_distinct):
        buffer = input[i:i+n_distinct]
        #print(buffer)
        if(len(np.unique(list(buffer))) == n_distinct):
            print(i+n_distinct)
            break
    

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

