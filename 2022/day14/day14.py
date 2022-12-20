'''
@author: BastienZim

'''

import os
import numpy as np
import timeit

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
    input = [[tuple(int(a) for a in l.split(","))
              for l in x.split(" -> ")] for x in input]
    # print(input)
    
    nodes_to_draw = []
    for x in input:
        for b, a in zip(x, x[1:]):
            if(a[0] == b[0]):
                for k in range(min(a[1], b[1]), max(a[1], b[1])+1):  # pos
                    nodes_to_draw.append((a[0], k))
            elif(a[1] == b[1]):
                for k in range(min(a[0], b[0]), max(a[0], b[0])+1):  # pos
                    nodes_to_draw.append((k, a[1]))
            else:
                print('diag')

    nodes_to_draw = list(set(nodes_to_draw))
    print("MAX_DEPTH =",max([x[1] for x in nodes_to_draw])+2)
    sand = []
    map = {n: "rocks" for n in nodes_to_draw}
    map = [n for n in nodes_to_draw]
    print()

    '''
    last_sand_len = len(map)
    for i in range(10000):
        #sand = update_sand(sand, nodes_to_draw)
        map = update_sand_map(map)
        if(last_sand_len == len(map)):
            print("ENDING")
            break
        else:
            last_sand_len=len(map)
        if(i%500 == 0):
            print(i)

            draw_rocks_map(nodes_to_draw, map, input)
            
    #sand.append((500,0))
    map.append((500,0))'''

    max_depth = max([x[1] for x in nodes_to_draw])+2
    max_width = 1+2*(max_depth-1)
    g_map = np.zeros((max_depth, max_width), dtype=bool)

    centered_nodes = [(a[0]-min([x[0] for x in nodes_to_draw]), a[1]) for a in nodes_to_draw]
    for n in centered_nodes:
        g_map[n] = 1
    #print(np.array(g_map, dtype=int))

    #First result = 7.78 for 1000
    #n_iter = 1000
    #time = timeit.timeit(lambda: propagate_sand(centered_nodes), number = n_iter)
    #print(time)
    
    
    #i,map = propagate_sand(centered_nodes)
    #print(f"===> n_steps: {i, len(map)-len(nodes_to_draw)} <===")
    #draw_rocks_map(centered_nodes, map)
    #draw_rocks(nodes_to_draw, sand, input)



def propagate_sand(nodes_to_draw):
    map = [n for n in nodes_to_draw]
    last_sand_len = len(map)
    for i in range(10000):
        #sand = update_sand(sand, nodes_to_draw)
        map = update_sand_map(map)
        if(last_sand_len == len(map)):
            #print("ENDING")
            break
        else:
            last_sand_len=len(map)
        #if(i%500 == 0):
        #    print(i)
    map.append((6,0))
    return(i,map)

def update_sand(sand_in, rocks):
    can_move, move =  next_move((6, 0), sand_in, rocks)#(500, 0) is sand source
    if(not can_move):
        #print("Filled up")
        return(sand_in)

    sand = sand_in.copy()
    while(can_move):
        point = move
        can_move, move = next_move(point, sand, rocks)
    if(move != "STOP"):
        sand.append(point)
    return(sand)

def update_sand_map(map_in):
    can_move, move =  next_move_map((6, 0), map_in)#(500, 0) is sand source
    if(not can_move):
        #print("Filled up")
        return(map_in)

    map = map_in.copy()
    while(can_move):
        point = move
        can_move, move = next_move_map(point, map_in)
    if(move != "STOP"):
        #print(point)
        map.append(point)
        
    return(map)

def next_move(point, sand, rocks):
    #if(point[1] > max([x[1] for x in rocks])+2):#if reached bellow bottom.
    #    return(False, "STOP")
    bellow = tuple(np.add(point, (0, 1)))
    left = tuple(np.add(bellow, (-1, 0)))
    right = tuple(np.add(bellow, (1, 0)))
    for test in [bellow, left, right]:
        type_test= get_type(test, sand, rocks)
        if(type_test == "nothing"):
            return(True, test)
    else:
        return(False, None)

#example
def next_move_map(point, map):
    bellow = tuple(np.add(point, (0, 1)))
    if(bellow[1] >= 11):#184
        return(False, None)
    if(bellow not in map):
        return(True, bellow)
    test = tuple(np.add(bellow, (-1, 0)))
    if(test not in map):
        return(True, test)
    test = tuple(np.add(bellow, (1, 0)))
    if(test not in map):
        return(True, test)
    
    return(False, None)

#def get_type(point, map):
#    return(map[point])

def get_type(point, sand, rocks):
    if(len(rocks) > 0):
        if(point in rocks):
            return("rocks")
    if(len(sand) > 0):
        if(point in sand):
            return("sand")
    if(point[1] == max([x[1] for x in rocks])+2):
        return("rocks")
    return("nothing")


def get_ground(col, sand, rocks):
    s_col = [s for s in sand if s[0] == col]
    r_col = [r for r in rocks if r[0] == col]
    if(len(r_col) > 0 and len(s_col) > 0):
        s_high = np.min(s_col, axis=0)
        r_high = np.min(r_col, axis=0)
        if(r_high[1] > s_high[1]):
            candidate, type = s_high, "sand"
        else:
            candidate, type = r_high, "rock"
    elif(len(s_col) > 0):
        s_high = np.min(s_col, axis=0)
        candidate, type = s_high, "sand"
    elif(len(r_col) > 0):
        r_high = np.min(r_col, axis=0)
        candidate, type = r_high, "rock"
    else:
        print("Bottomless Pit")
    return(candidate, type)


def draw_rocks_map(nodes_to_draw, map):
    sand = [n for n in map if n not in nodes_to_draw]
    draw_rocks(nodes_to_draw, sand)


def draw_rocks(nodes_to_draw, sand):
    rocks = []
    sand_source = [(6, 0)]
    
    rocks = np.array(list(set(nodes_to_draw)))
    sand = np.array(list(set(sand)))
    min_x = min(np.min(rocks[:, 0]),np.min(sand[:, 0]))
    max_x = max(np.max(rocks[:, 0]),np.max(sand[:, 0]))
    max_y = max(np.max(rocks[:, 1]),np.max(sand[:, 1]))
    rocks = [tuple(x) for x in rocks]
    sand = [tuple(x) for x in sand]
    map = []
    #print(min_x, max_x+1, 0, max_y+1)
    for i in range(min_x, max_x+1):
        row = []
        for j in range(0, max_y+1):
            if((i, j) in nodes_to_draw):
                row.append("#")
            elif((i, j) in sand):
                row.append("o")
            elif((i, j) in sand_source):
                row.append("+")
            else:
                row.append(".")

        map.append(row)
    map = list(np.array(map).T)
    for row in map:
        print("".join(row))


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n", ""), input))


if __name__ == "__main__":
    main()
