'''
@author: BastienZim

'''

import os
import numpy as np
import timeit

path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


example = False


if(example):
    source_point = (16, 0)
    global_max_depth = 11
else:
    source_point = (193, 0)
    global_max_depth = 184

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

    max_depth = max([x[1] for x in nodes_to_draw])+2
    max_width = 1+2*(max_depth-1)
    print(f"max_depth: {max_depth} - max_width: {max_width} - > center at {max_width/2} -> Source {500-min([x[0] for x in nodes_to_draw])+int(max_width/2)}")
    
    g_map = np.zeros((max_width+int(max_width/2), max_depth), dtype=bool)
    centered_nodes = [(a[0]-min([x[0] for x in nodes_to_draw])+int(max_width/2), a[1])
                      for a in nodes_to_draw]
    for n in centered_nodes:
        g_map[n] = 1

    i_final, map = propagate_sand(g_map)

    #print(np.array(map.T, dtype=int))
    
    #n_iter = 1000
    #time = timeit.timeit(lambda: propagate_sand(g_map), number=n_iter)
    #print(time)

    #i,map = propagate_sand(centered_nodes)
    print(f"===> n_steps: {i_final, np.sum(map)-len(centered_nodes)} <===")

    res_nodes = []
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if(map[(i, j)] == 1):
                res_nodes.append((i, j))

    print(np.sum(map)-len(centered_nodes))
    draw_rocks_map(centered_nodes, res_nodes)
    #draw_rocks(nodes_to_draw, sand, input)


def propagate_sand(g_map):
    last_sand_len = np.sum(g_map)
    for i in range(1000000):
        g_map = update_sand_map(g_map)
        if(last_sand_len == np.sum(g_map)):
            break
        else:
            last_sand_len = np.sum(g_map)
        if(i%1000 == 0):
            print(i)
    g_map[source_point] = 1
    return(i, g_map)


def update_sand(sand_in, rocks):
    can_move, move = next_move((6, 0), sand_in, rocks)
    if(not can_move):
        return(sand_in)

    sand = sand_in.copy()
    while(can_move):
        point = move
        can_move, move = next_move(point, sand, rocks)
    sand.append(point)
    return(sand)


def update_sand_map(g_map):
    can_move, move = next_move_map(source_point, g_map)  # (500, 0) is sand source
    if(not can_move):
        return(g_map)
    while(can_move):
        point = move
        can_move, move = next_move_map(point, g_map)
    g_map[point] = 1
    return(g_map)


def next_move(point, sand, rocks):
    bellow = tuple(np.add(point, (0, 1)))
    left = tuple(np.add(bellow, (-1, 0)))
    right = tuple(np.add(bellow, (1, 0)))
    for test in [bellow, left, right]:
        type_test = get_type(test, sand, rocks)
        if(type_test == "nothing"):
            return(True, test)
    else:
        return(False, None)


def next_move_map(point, g_map):
    test = (point[0], point[1]+1)
    if(test[1] >= global_max_depth):  # 184
        return(False, None)
    if(g_map[test] == 0):
        return(True, test)
    test = (point[0]-1, point[1]+1)
    if(g_map[test] == 0):
        return(True, test)
    test = (point[0]+1, point[1]+1)
    if(g_map[test] == 0):
        return(True, test)
    return(False, None)


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
    rocks = np.array(list(set(nodes_to_draw)))
    sand = np.array(list(set(sand)))
    min_x = min(np.min(rocks[:, 0]), np.min(sand[:, 0]))
    max_x = max(np.max(rocks[:, 0]), np.max(sand[:, 0]))
    max_y = max(np.max(rocks[:, 1]), np.max(sand[:, 1]))
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
            elif((i, j) in source_point):
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
