'''
@author: BastienZim

'''

import os
import numpy as np


path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


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

    H, T = [0, 0], [0, 0]
    dict_dir = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
    #print(input)
    tail_visited = [list(T)]
    
    for dir, n_times in input:
        #print("------------------")
        #print(dir, n_times)
        for _ in range(int(n_times)):
            #print(H, T)
            H = np.add(H, dict_dir[dir])
            T = follow(H, T)
            if(list(T) not in tail_visited):
                tail_visited.append(list(T))
    print(len(tail_visited))
            # print(T)
        #print(H, T)
        
        # print()


def follow(H, T):
    #print(f" H:{H} - T:{T}")
    distL2_HT = np.linalg.norm(H-T, ord=2)
    if(distL2_HT == 1 or distL2_HT == 0):
        #print("superposed or same line/col")
        return(T)
    distL1_HT = np.linalg.norm(H-T, ord=1)
    if(distL1_HT == distL2_HT and distL2_HT != 1):
        #print("Same line")
        plusdir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # print(H-T)
        for x in plusdir:
            if(np.linalg.norm(H-(T+np.array(x)), ord=2) == 1):
                return(T+np.array(x))
    elif(distL2_HT > np.sqrt(2)+0.1):
        # print("Diag")
        neighbourhood = [np.array([-1+i, -1+j])
                         for i in range(3) for j in range(3)]
        for x in neighbourhood:
            candidate = np.add(T, x)
            dist_head = np.linalg.norm(candidate-H, ord=2)
            if(dist_head <= 1):
                return(candidate)
        pritn("FAILURED")
    else:
        # print("diag close enough")#, distL2_HT)
        return(T)


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n", "").split(" "), input))


if __name__ == "__main__":
    main()
