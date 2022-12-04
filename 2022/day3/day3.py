'''
@author: BastienZim

'''

import os
import numpy as np

path = "/home/bastienzim/Documents/perso/adventOfCode/2022/"
path = "/home/bastien/Documents/AdventOfCode/2022/"


example = False
alphabet = "abcdefghijklmnopqrstuvwxyz"


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
    badges = []
    for i in range(0,len(input), 3):
        #for k in range(3)
        print(i)
        e1, e2, e3 = input[i], input[i+1], input[i+2]
        #print(np.intersect1d(list(e1), list(e2)))#
        #print(np.intersect1d(list(e2), list(e3)))
        badges.append(np.intersect1d(np.intersect1d(list(e1), list(e2)), list(e3))[0])
    print(badges)
    print(sum(list(map(lambda x: score(x), badges))))
    #duplicated_items = [np.intersect1d(list(x[:int(len(x)/2)]),list(x[int(len(x)/2):]))[0] for x in  input]
    #print(duplicated_items)
    #prios  = list(map(lambda  x: score(x), duplicated_items))
    #print(sum(prios))


def score(letter):
    if(letter.isupper()):
        score = 27 + alphabet.index(letter.lower())    
    else:
        score = 1 + alphabet.index(letter.lower())    
    return(score)

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

