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
    grid = np.array(input, int)
    print(grid)
    maxi=1
    vis_counter =0
    #print(grid.shape)
    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            score = count_visible(i,j, grid)
            if(score> maxi):
                maxi = score
                print(i,j,score)
            #if(is_visible(i,j, grid)):
            #    vis_counter +=1 #print(i,j)
#            print(i,j, is_visible(0,0,grid))
    print(maxi)
    #print(count_visible(3,2,grid))
            

#visible: all tree between it and the ege of grid are shorter() -> same row/col

def is_visible(i,j, grid):
    tree = grid[i,j]
    row = grid[i, :]
    r_row = [x for k,x in enumerate(row) if k>j] 
    l_row = [x for k,x in enumerate(row) if k<j] 
    col = grid[:,j] 
    l_col = [x for k,x in enumerate(col) if k>i] 
    u_col = [x for k,x in enumerate(col) if k<i] 
    
    #print(l_row,r_row)
    #print(np.reshape(u_col,(-1,1)))
    #print(np.reshape(l_col,(-1,1)))
    #return
    for to_check, dir in zip([l_row, r_row, u_col, l_col], ['l','r','u','l']):
        if(len(to_check)==0):
            return(True)
        if(tree>max(to_check)):
            #print(dir)
            return(True)
    return(False)

def count_visible(i,j, grid):
    tree = grid[i,j]
    row = grid[i, :]
    r_row = [x for k,x in enumerate(row) if k>j] 
    l_row = [x for k,x in enumerate(row) if k<j] 
    col = grid[:,j] 
    l_col = [x for k,x in enumerate(col) if k>i] 
    u_col = [x for k,x in enumerate(col) if k<i] 
    count_vis = 1
    for to_check, dir in zip([l_row, r_row, u_col, l_col], ['l','r','u','low']):
        dir_count = 0
        if(len(to_check)!=0):
            if(dir in ["l","u"]):
                to_check = to_check[::-1]
            #print(to_check)
            for x in to_check:
                dir_count+=1
                #print(dir, x)
                if(x>=tree):
                    break
        count_vis *= dir_count
    return(count_vis)        


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: [int(k) for k in x.replace("\n","")], input))




if __name__ == "__main__":
    main()

