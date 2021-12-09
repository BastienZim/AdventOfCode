'''
up=Down
down = up


'''

from functools import reduce
from operator import ge
import numpy as np

def main():
    input = get_input(False)
    #print(input)
    #part1
    #check_grid(input)
    
    low_pts = get_low_points(input)
    #for pt in low_pts:
    #    bassin_points = get_bassin(pt, input)
        #print(pt, len(bassin_points), bassin_points)
        #print(len(bassin_points))
    all_bassins_size = [len(get_bassin(pt, input)) for pt in low_pts]
    #print(all_bassins_size)
    top_3_bassins = sorted(all_bassins_size)[-3:]
    print(top_3_bassins)
    print(reduce(lambda x,y: x*y, top_3_bassins))
#    print(low_pts)
    #print(input.shape)

#---------------------Funcs--------------------
def check_grid(grid):
    total_risk = 0
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if check_point(row,col, grid):
                total_risk += risk_level(grid[row,col])
    print(total_risk)

def get_low_points(grid):
    low_pts = []
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if check_point(row,col, grid):
                low_pts.append([row,col])
    return(low_pts)

def get_bassin(low_point, grid):
    #print(low_point)
    bassin_points = [(low_point[0],low_point[1])]
    check_i = 0
    while(check_i < len(bassin_points)):
        pt_check = bassin_points[check_i]
        new_points = get_flow_sources(pt_check[0], pt_check[1], grid)
        new_points = list(map(lambda x: (x[0],x[1]), new_points))
        new_points = list(filter(lambda x: x not in bassin_points, new_points))
        bassin_points += new_points
        check_i += 1
#    print(low_point, bassin_points)
    return(bassin_points)

def get_flow_sources(x,y, grid):
    neighs = get_neighbours(x,y, grid)
    return([ pt for pt in neighs if is_upper_hill(pt, [x,y], grid)])


def is_upper_hill(pt1, pt2, grid):#can flow
    val_1, val_2 = grid[pt1[0],pt1[1]], grid[pt2[0],pt2[1]]
    return(val_1 < 9 and val_1 > val_2)
    

def isinGrid(row, col, grid):
    return(0<= row <grid.shape[0] and 0<= col <grid.shape[1])

def risk_level(height):
    return(1+height)

def is_low_point(point, neighbours, grid):
    return(grid[point[0],point[1]] < min([grid[x[0],x[1]] for x in neighbours]))
    
def get_neighbours(x,y, grid):
    return(list(filter(lambda x: isinGrid(x[0],x[1], grid),
        [np.add((x,y),transi) for transi in [(-1,0),(0,-1),(1,0),(0,1)]])))
        
def check_point(x,y, grid):
    neighbours = list(filter(lambda x: isinGrid(x[0],x[1], grid),
        [np.add((x,y),transi) for transi in [(-1,0),(0,-1),(1,0),(0,1)]]))
    return(is_low_point([x,y], neighbours, grid))


#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day9/example_in.txt" 
    else: path = "./day9/input.txt" 

    with open(path) as f:
        input = f.readlines()

    input = list(map(lambda x: [int(num) for num in x.replace("\n","")], input))
    
    return (np.array(input))


if __name__ == "__main__":
    main()

