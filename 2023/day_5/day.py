import regex as re
import numpy as np

INPUT_FILE_PATH = './input.txt'
#INPUT_FILE_PATH = './example_in.txt'

list_to_find= ["seeds", "seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map"]




def main():
    lines = parse_input_file()

    all_things = get_interesting_things(lines)
    map_1 = all_things['seed-to-soil']
    
    dict_map_order = get_map_order(all_things)
    elements = [k.split("-to-")[-1] for k in all_things.keys()]
    map_order = [dict_map_order[elt] for elt in elements if elt in dict_map_order.keys()]
    
    
    seeds = all_things['seeds'][0]

    first_location =min( [process_seed(s, all_things, map_order) for s in seeds])
    print(f"  Part 1 Solution is {first_location}")


    all_seeds = []
    for i in range(0,len(seeds),2):
        start, length = seeds[i], seeds[i+1]
        all_seeds.append((start,start+length))
    all_seeds = sorted(all_seeds, key= lambda x: x[0])
    for s1, s2 in zip(all_seeds, all_seeds[1:]):
        print(s1[1]>s2[0]>s1[0])
        print(s1[1])
        print(s2[0])
    print(sorted(all_seeds, key= lambda x: x[0]))

    #mini = np.inf
    #for i in range(0,len(seeds),2):
    #    start, length = seeds[i], seeds[i+1]
    #    for s in range(start,start+length):
    #        new_loc = process_seed(s, all_things, map_order)
    #        if(new_loc<mini):
    #            mini = new_loc
    #            print(mini)
    #    all_mins.append(min_loc)
    #    
#
 #   print(f"  Part 2 Solution is {mini}")

    

def process_seed(s, all_things, map_order):
    number = s
    #temp_nums = [s]
    for map_name in map_order:
        number = find_correspondences(number, all_things[map_name])
        #temp_nums.append(number)
    return(number)

        
def get_map_order(all_things):
    dict_map_order = {}
    for k in all_things:
        if("-to-") in k:
            bef, aft = k.split("-to-")
            if("seed" in bef):
                bef = bef.replace("seed","seeds")
            dict_map_order[bef] = k

    return(dict_map_order)


def find_correspondences(number, map):

    source_mins = [x[1] for x in map]
    source_maxs = [x[1]+x[2] for x in map]
    offsets = [x[0]-x[1] for x in map]
    for mini, maxi, ofst in zip(source_mins, source_maxs, offsets):
        if mini <= number < maxi:
            #print(number+ofst)
            return(number+ofst)

    return(number)

def get_interesting_things(lines):
    new_stock=[]
    all_things = {}
    for i,l in enumerate(lines):
        for w in list_to_find:
            if(w in l):
                
                if(len(new_stock)>0):
                    new_stock[0] = ": ".join(new_stock[0].split(":")[1:])
                    new_stock = list(filter(lambda x: len(x)>0,new_stock))
                    new_stock = list(map(lambda x: x.split(" "),new_stock))
                    new_stock = list(map(lambda x: [int(a) for a in x if(len(a)>0)],new_stock))
                    if("to" in current_name):
                        current_name = "".join(current_name.split(" map")[:-1])
                    all_things[current_name]= new_stock
                new_stock = []
                current_name = w
        new_stock.append(l)
    
    new_stock[0] = ": ".join(new_stock[0].split(":")[1:])
    new_stock = list(filter(lambda x: len(x)>0,new_stock))
    new_stock = list(map(lambda x: x.split(" "),new_stock))
    new_stock = list(map(lambda x: [int(a) for a in x if(len(a)>0)],new_stock))
    if("to" in current_name):
        current_name = "".join(current_name.split(" map")[:-1])
    all_things[current_name]= new_stock
    return(all_things)



def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()