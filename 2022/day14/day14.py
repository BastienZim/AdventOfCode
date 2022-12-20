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
    input = [[tuple(int(a) for a in l.split(","))
              for l in x.split(" -> ")] for x in input]
    # print(input)
    for x in input:
        print(x)
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
    sand = []
    draw_rocks(nodes_to_draw, sand, input)
    print()
    last_sand_len = len(sand)
    for i in range(10000):
        sand = update_sand(sand, nodes_to_draw)
        if(last_sand_len == len(sand)):
            print("ENDING")
            break
        else:
            last_sand_len=len(sand)

    print(i,len(sand))
    draw_rocks(nodes_to_draw, sand, input)
    


def update_sand(sand_in, rocks):
    sand_source = (500, 0)
    sand = sand_in.copy()
    can_move, move =  next_move(sand_source, sand, rocks)
    while(can_move):
        point = move
        can_move, move = next_move(point, sand, rocks)
    if(move != "STOP"):
        sand.append(point)
    return(sand)

def next_move(point, sand, rocks):
    if(point[1] > max([x[1] for x in rocks])):
        #print("THE END !!!!")
        return(False, "STOP")
    bellow = tuple(np.add(point, (0, 1)))
    left = tuple(np.add(bellow, (-1, 0)))
    right = tuple(np.add(bellow, (1, 0)))
    for test in [bellow, left, right]:
        type_test= get_type(test, sand, rocks)
        if(type_test == "nothing"):
            return(True, test)
    else:
        return(False, None)
        """elif(type_bellow == "rock"):
            return(False, None)
        else:
            #print(type_bellow, bellow)
            #print(sand)
            left = tuple(np.add(bellow, (-1, 0)))
            #print(left)
            #print()
            if(get_type(left, sand, rocks)=="nothing"):
                return(True, left)
            right = tuple(np.add(bellow, (1, 0)))
            if(get_type(right, sand, rocks)=="nothing"):
                return(True, right)
            return(False, None)
            """


def get_type(point, sand, rocks):
    if(len(rocks) > 0):
        if(point in rocks):
            return("rocks")
    if(len(sand) > 0):
        if(point in sand):
            return("sand")
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


def draw_rocks(nodes_to_draw, sand, input):
    rocks = []
    sand_source = [(500, 0)]
    for row in input:
        rocks = rocks + row
    rocks = np.array(list(set(rocks)))
    min_x = np.min(rocks[:, 0])
    max_x = np.max(rocks[:, 0])
    max_y = np.max(rocks[:, 1])
    rocks = [tuple(x) for x in rocks]
    map = []
    for i in range(min_x, max_x+1):
        row = []
        for j in range(0, max_y+1):
            if((i, j) in nodes_to_draw):
                row.append("#")
            elif((i, j) in sand_source):
                row.append("+")
            elif((i, j) in sand):
                row.append("o")
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
