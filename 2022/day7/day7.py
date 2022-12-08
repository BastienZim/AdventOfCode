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

    dict_dir_weight = {}
    dict_dir_counted = {}
    current_path=""
    for x in input:
        if("$" in x):
            if("cd" in x):
                command = x.split("cd ")[1]
                if(command == "/"): current_path = "/"
                elif(command == ".."):
                    if(sum([1 if x == "/" else 0 for x in current_path]) > 1):
                        current_path = "/".join(current_path.split("/")[:-1])
                    else: current_path = current_path[0]
                else:
                    if(current_path[-1] == "/"): current_path = current_path + str(command)
                    else: current_path = current_path + "/" + str(command)
            else:  continue
        else:
            #print(f"                        pwd :: {current_path}")
            if(current_path not in dict_dir_weight.keys()):
                dict_dir_weight[current_path] = 0
                dict_dir_counted[current_path] = []
            if(len(x.split(" "))!= 2):
                print("AAAAAAAAAAAAAAAAA")
            file_weight, file_name = x.split(" ")
            if(file_weight != "dir"):
                if(file_name not in dict_dir_counted[current_path]):
                    dict_dir_weight[current_path] += + int(file_weight)
                    dict_dir_counted[current_path].append(file_name)

    all_dirs = dict_dir_counted.keys()
    #print(dict_dir_weight)
    #Sort by depth. MAYBE NO NEED TO SORT
    sorted_dirs = sorted([(b, a) for a,b in zip(all_dirs,[sum([1 if x == "/" else 0 for x in dir]) if dir!="/" else 0 for dir in all_dirs])],reverse=True)
    for depth in range(max([x[0] for x in sorted_dirs]), -1, -1):
        for dir1 in [x[1] for x in sorted_dirs if x[0] == depth]:
            for dir2 in [x[1] for x in sorted_dirs if x[0] == depth-1]:
                if(dir2 in dir1):
                    if(sum([1 if x == "/" else 0 for x in dir1])>1):
                        if("/".join(dir1.split("/")[:-1]) == dir2):
                            dict_dir_weight[dir2] += dict_dir_weight[dir1]
                            #print(f"adding weight of {dir1} to {dir2}")
                        else:
                            true_parent = "/".join(dir1.split("/")[:-1])
                        #    print(f"{dir1} is NOT inside {dir2}, it is inside: {true_parent}")
                    else:
                        if("/" == dir2):
                            dict_dir_weight[dir2] += dict_dir_weight[dir1]
                            #print(f"adding weight of {dir1} to {dir2}")
                        #else:
                           # print(f"{dir1} is NOT inside {dir2}, it is inside: /")

    
    total_disk_space = 70000000
    space_required = 30000000

    current_free_space = total_disk_space - dict_dir_weight['/']
    print(f"Remaining space {total_disk_space - dict_dir_weight['/']}")
    if( current_free_space < space_required):
        space_to_be_free = space_required - current_free_space
        print(f"Space needed to be freed {space_to_be_free}")
    all_weights = list(dict_dir_weight.values())
    all_weights.append(space_to_be_free)
    all_weights = sorted(all_weights)
    weight_to_delete = all_weights[all_weights.index(space_to_be_free) + 1 ]
    print("CHOSEN WEIGHT :", weight_to_delete)
    selectable_weights = [weight for weight in dict_dir_weight.values() if weight >= space_to_be_free]
    print(sorted(selectable_weights)[0])
    
    print(f"Answer part 1: {sum([weight for weight in dict_dir_weight.values() if weight<100000 ])}")
    #for dir in:
            #
24933642==24933642
def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

