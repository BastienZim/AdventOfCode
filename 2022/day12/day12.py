'''
@author: BastienZim

'''

import os
import numpy as np


path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


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
    #input = np.array(input)
    S = np.where(input =='S')
    E = np.where(input =='E')
    for x in input:
        print("".join(x))
    

def is_higher(letter_1, letter_2):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return(alphabet.index(letter_1) <= alphabet.index(letter_2))

def can_clim(letter_1, letter_2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return(alphabet.index(letter_1) == alphabet.index(letter_2) or
           alphabet.index(letter_1) == alphabet.index(letter_2)+1)

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return np.array(list(map(lambda x: list(x.replace("\n","")), input)))




if __name__ == "__main__":
    main()

