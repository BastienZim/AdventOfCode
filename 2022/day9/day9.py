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

    nodes = [np.array([0,0]) for _ in range(10)]
    dict_dir = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
    #print(input)
    tail_visited = [list(nodes[-1])]
       
    for dir, n_times in input:
        #print("->",dir, n_times)
        for _ in range(int(n_times)):
            nodes[0] = np.add(nodes[0], dict_dir[dir])
            previous_node = nodes[0]
            for i, n in enumerate(nodes[1:]):
                n = follow(previous_node, n)
                nodes[i+1] = n 
                previous_node = n
            if(list(nodes[-1]) not in tail_visited):
                tail_visited.append(list(nodes[-1]))
        #print([list(x) for x in nodes])
        #print("#"*20)
        #print_grid(nodes)
    print(len(tail_visited))
            # print(T)
        #print(H, T)
    
    #print(follow(np.array([4,-2]),np.array([3,0])))


    #[4,-2],[3,0]
        # print()
#    print_grid([np.array([5, 0]), np.array([4, 0]), np.array([3, 0]), np.array([2, 0])])

'''

.....
.0...
.....
...AB

'''
def print_grid(nodes, min_size = 0):
    list_nodes = [list(x) for x in nodes]
    #print(list_nodes)
    pad = 2
    min_x, max_x = min([x[1] for x in nodes])-pad, max([x[1] for x in nodes])+1+pad
    min_y, max_y = min([x[0] for x in nodes])-1-pad, max([x[0] for x in nodes])+pad
    
    #print(min_y, max_y, min_x, max_x)
    #min_y, max_y, min_x, max_x = -1, 6, -6, 1
    for j in range(min(min_x,0), max(max_x, min_size)):
        plot_string = ""
        for i in range(max(max_y, min_size), min(min_y,0), -1):
            if(i==j and i==0):
                plot_string = "s" + plot_string
            elif(list([i,j]) in list_nodes):
                #print("ASD")
                plot_string = str(list_nodes.index(list([i,j]))) + plot_string
            else:                
                plot_string = "."+plot_string
        print(plot_string)


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
    #elif(distL2_HT > 2*np.sqrt(2)):
    #    #move in dir of L2
    #    print("ASLKJDALJSDSAKJDS")
    #    print(H-T)
    elif(distL2_HT > np.sqrt(2)+0.1):
        #print("Diag")
        neighbourhood = [np.array([-1+i, -1+j])
                         for i in range(3) for j in range(3)]
        candidates = [np.add(T, x) for x in neighbourhood]
        candidates = list(map(lambda x: (np.linalg.norm(x-H, ord=2), x), candidates))
        
        if(min([x[0] for x in candidates]) <= np.sqrt(2)):
            return(np.array([x[1] for x in candidates if x[0] == min([x[0] for x in candidates])][0]))
#            return(min(candidates)[1])
        else:
            print("FAILURE")
    else:
        # print("diag close enough")#, distL2_HT)
        return(T)


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n", "").split(" "), input))


if __name__ == "__main__":
    main()
