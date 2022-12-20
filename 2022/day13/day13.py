'''
@author: BastienZim

'''

import os
import numpy as np
import ast


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

    # print(input)
    """ ### PART 1
    sum_indices = 0
    for i in range(0, len(input), 3):
        p1 = ast.literal_eval(input[i])
        p2 = ast.literal_eval(input[i+1])
        print(f"\n\n== PAIR {int(i/3)+1} ==")
        #print(f"p1:{p1}, p2:{p2}")
        last_res = compare_paq(p1, p2, None, verbose=False)
        print("       ", last_res)
        if(last_res == "<"):
            sum_indices += (int(i/3) + 1)
            #print((int(i/3) + 1))
    print("SUM INDICES", sum_indices)

    """

    all_paquets = []
    for i in range(0, len(input), 3):
        p1 = ast.literal_eval(input[i])
        p2 = ast.literal_eval(input[i+1])
        all_paquets.append(p1)
        all_paquets.append(p2)
    # print(all_paquets)
    sorted_paquets = sort_paquets(all_paquets)
    # for p in sorted_paquets:
    #    print(p)
    print((sorted_paquets.index([[2]])+1) * (sorted_paquets.index([[6]])+1))


def sort_paquets(all_paquets):
    sorted_paquets = [all_paquets[0]]
    all_paquets.append([[2]])
    all_paquets.append([[6]])
    for p1 in all_paquets[1:]:
        is_placed = False
        for i, p2 in enumerate(sorted_paquets):
            if(compare_paq(p1, p2, None) == "<"):
                new_sorted = sorted_paquets[:i] + [p1] + sorted_paquets[i:]
                is_placed = True
                break
        if(not is_placed):
            sorted_paquets.append(p1)
        else:
            sorted_paquets = new_sorted
    return(sorted_paquets)


def compare_paq(p1, p2, res, verbose=False):
    if(res is not None):
        return(res)
    if(verbose):
        print(f"Compare {p1} vs {p2}")  # , res:{res}")

    if(np.array(p1, dtype=object).shape == () and np.array(p2, dtype=object).shape == ()):
        # if(p1 == p2): #    if(verbose): print("         Compare as equality -> continue")
        if(p1 < p2):
            if(verbose):
                print("         Left Smaller -> STOP")
            if(res == None):
                res = "<"
        elif(p1 > p2):
            if(verbose):
                print("         Right Smaller wrong order -> STOP")
            if(res == None):
                res = ">"
        return(res)
    elif((np.array(p1, dtype=object).shape == () and np.array(p2, dtype=object).shape != ())):
        if(verbose):
            print("        Mixed Types -> recurse with first pair as list")
        res = compare_paq([p1], p2, res, verbose)
    elif(np.array(p1, dtype=object).shape != () and np.array(p2, dtype=object).shape == ()):
        if(verbose):
            print("        Mixed Types -> recurse with second pair as list")
        res = compare_paq(p1, [p2], res, verbose)
    else:
        if(verbose):
            print("    Recurse")
        for a, b in zip(p1, p2):
            res = compare_paq(a, b, res, verbose)
        # if(len(p1) == len(p2)): #    print("PROBELMELJLJHLKJHLKJ")
        if(len(p1) > len(p2)):
            if(res == None):
                if(verbose):
                    print("Right Side less elts")
                res = ">"
        elif(len(p1) < len(p2)):
            if(res == None):
                if(verbose):
                    print("Left Side less elts")
                res = "<"
    return(res)


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n", ""), input))


if __name__ == "__main__":
    main()
