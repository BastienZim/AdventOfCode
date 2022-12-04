'''
@author: BastienZim

'''

import os
import numpy as np

path = "/home/bastienzim/Documents/perso/adventOfCode/2022/"
path = "/home/bastien/Documents/AdventOfCode/2022/"


example = False


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
    print(sum([overlap(x) for x in input]))
    #for x in input:
    #    print(x, overlap(x))
    #    print()


def overlap(pair):
    
    p1, p2 = pair[0], pair[1]
    ap1 = np.arange(p1[0],p1[1]+1)
    ap2 = np.arange(p2[0],p2[1]+1)
    #print(ap1)
    #print(ap2)
    #print(np.intersect1d(ap1, ap2))
    if(len(np.intersect1d(ap1, ap2))>0):
        return(True)
    else:
        return(False)

def fully_contains(pair):
    p1, p2 = pair[0], pair[1]
    if (p1[0]<=p2[0]) and (p1[1]>=p2[1]):
        return(True)
    elif(p1[0]>=p2[0]) and (p1[1]<=p2[1]):
        return(True)
    else:
        return(False)



def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: list(map(lambda k : [int(j) for j in k.split("-")], x.replace("\n","").split(","))), input))




if __name__ == "__main__":
    main()

