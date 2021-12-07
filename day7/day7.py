'''
up=Down
down = up


'''

import numpy as np

def main():
    input = get_input(False)
    #print(input)
    
    x = 5
    all_distances =[distance_to_crab(input, pos) for pos in range(max(input))]
    all_distances =[real_crab_engineering_distance(input, pos) for pos in range(max(input))]
    min_dist = min(all_distances)
    argmin_dist = np.argmin(all_distances)
    print(argmin_dist, min_dist)


def real_crab_engineering_distance(crabs, pos):
    
    return(sum([int((abs(crab-pos)*(abs(crab-pos)+1))/2) for crab in crabs]))

def distance_to_crab(crabs, crabi):
    return(sum([abs(crab-crabi) for crab in crabs]))
    



def get_input(exBOOL = False):
    if(exBOOL): path = "./day7/example_in.txt" 
    else: path = "./day7/input.txt" 

    with open(path) as f:
        input = f.readlines()
    input = [int(x) for x in input[0].split(",")]
    #print(input)
    return (input)


if __name__ == "__main__":
    main()

