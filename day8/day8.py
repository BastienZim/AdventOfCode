'''
up=Down
down = up


'''

from functools import total_ordering
from operator import contains, le, pos
from os import linesep, nice
import numpy as np
from numpy.core.numeric import correlate
from numpy.lib.arraysetops import intersect1d

digits_segments = {
        0:"abcefg",
        1:"cf",
        2:"acdeg",
        3:"acdfg",
        4:"bcdf",
        5:"abdfg",
        6:"abdefg",
        7:"acf",
        8:"acbdefg",
        9:"abcdfg"
        }


def main():
    input = get_input(False)

    #get meta lists
    #contained_in_list = common_seggs()

    #print(input)
#Part 1-------------------------------------------------------
    #part 1 solution in 1 line    
    #count = sum([len(get_sureList(entry[1])[0]) for entry in input])
    
    #in several lines:
    #count = 0
    #for entry in input:
    #    output_value = entry[1]
    #    sureDigits, corresponding_segs = get_sureList(output_value)
    #    count+=len(sureDigits)

    #    print(count)

#Part 2-------------------------------------------------------
    

    counter = 0
    for entry in input:
        signal_pattern = entry[0]
        output_value = entry[1]
        
        sureList = get_sure_numbers(signal_pattern)
        sureList = deduce_others(sureList, signal_pattern)

        out_number_translated = translate(output_value, sureList)
        counter += out_number_translated
        #print(out_number_translated)
    print(counter)

def translate(segments, sureList):
    numbers = [[str(x[1]) for x in sureList if compare_segments(x[0], seg)][0] \
                for seg in segments]    
    return(int("".join(numbers)))

def possible_by_len(check_seg):
    
    #len_to_numbers = {i: [x[0] for x in num_segs_to_digit(i)] for i in range(2,8)}
    len_to_numbers = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
    possibleList = len_to_numbers[len(check_seg)]
    return(possibleList)

def by_contain_contain_e(check_seg, sureList):
    letters = ["a","b","c","d","e","f","g"]
    if(9 in [x[1] for x in sureList]):
        nine = [x[0] for x in sureList if x[1] ==9][0]
        e_letter = [x for x in letters if x not in nine][0]
        if e_letter in check_seg:
            #print("e inside")
            return([0,2,6,8])
        else:
            #print("no e")
            return([1,3,4,5,7,8])
    else:
        #print("no idea")
        return([i for i in range(10)])
    
def possible_not_found(sureList):
    nums_discovered = [num for (seg,num) in sureList]
    return([i for i in range(0,10) if i not in nums_discovered])

def possible_by_contain(check_seg, sureList):
    contained_in_dict = {1: [3,9,0], 4:[9], 7:[3,9,0]}
    possible_list = []
    for (seg,num) in sureList:
        #print(num, seg, check_seg)
        commons = [x for x in check_seg if x in seg]
        if(len(seg)==len(commons)):
            #print("ok sure number in to check")
            if num in contained_in_dict.keys(): 
                possible_list.append(contained_in_dict[num])
    
    if(len(possible_list)>0):
        min_len = min([len(x) for x in possible_list])
        possible_list = list(filter( lambda x: len(x) == min_len, possible_list))[0]
    else:
        return([1,2,4,5,6,7,8])
    return(possible_list)

def deduce_recursive(segs_left, sureList):
    "update sureList given the segs we still have to check"
    for check_seg in segs_left:
        #print(check_seg)
        #possibilities given the len
        by_len = possible_by_len(check_seg)
        #filter by not found
        by_not_found = possible_not_found(sureList)
        #print(" to be found:",by_not_found)
        possibilities = [x for x in by_len if x in by_not_found]
        #print(by_not_found, possibilities)
        #filter by contained
        by_contain = possible_by_contain(check_seg, sureList)
        possibilities = intersect1d(possibilities , by_contain)
        #filtered by segment e inside (if we know 9)
        by_e = by_contain_contain_e(check_seg, sureList)
        possibilities = [x for x in possibilities if x in by_e]

        if(len(possibilities) == 1):
            sureList.append((check_seg, possibilities[0]))


    segs_left = [seg for seg in segs_left if seg not in [x[0] for x in sureList]]
    return(segs_left, sureList)
    

def deduce_others(sureList, signal_pattern):

    segs_left = [seg for seg in signal_pattern if seg not in [x[0] for x in sureList]]

    while(len(sureList)<10):
        
        segs_left, sureList = deduce_recursive(segs_left, sureList)
    
    #print("\n success !!!!!!!!")
    #print("SureList",len(sureList),sureList)
    
    return(sureList)
    

def get_sure_numbers(segments):
    sureList = []
    for i, seg in enumerate(segments):
        possible = num_segs_to_digit(len(seg))
        if(len(possible)==1):
            real_num = possible[0][0]
            sureList.append((seg, real_num))
    return(sureList)

def get_sureList(segments):
    sureList = []
    for i, seg in enumerate(segments):
        possible = num_segs_to_digit(len(seg))
        if(len(possible)==1):
            #print(possible)
            real_num = possible[0][0]
            real_segs = possible[0][1]
            sureList.append((i,real_num, seg, real_segs))
    sureDigits = [x[1] for x in sureList]
    corresponding_segs = [(x[2], x[3]) for x in sureList]
    return(sureDigits, corresponding_segs)


def num_segs_to_digit(num):
    segs = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'acbdefg', 'abcdfg']
    return([(i,x) for i, x in enumerate(segs) if len(x)==num])

def compare_segments(seg_1, seg_2):
    return(sorted(seg_1)==sorted(seg_2))

def common_seggs():
    '''
    contained_in_list = common_seggs()
    '''
    segs = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'acbdefg', 'abcdfg']
    contained_in_list = []
    for i in [1,4,7,8]:
        seg_1 = segs[i]
        for j in [2,3,5,6,9,0]:
            seg_2 = segs[j]
            commons = [x for x in seg_1 if x in seg_2]
            if(len(seg_1)==len(commons)):
                contained_in_list.append((i,j))
                #print("number %d is contained in number %d"%(i,j))
    #print(contained_in_list)
    return(contained_in_list)





def get_input(exBOOL = False):
    if(exBOOL): path = "./day8/example_in.txt" 
    else: path = "./day8/input.txt" 

    with open(path) as f:
        input = f.readlines()

    input = list(map(lambda x: x.replace("\n",""), input))
    input = [[sub_x.split(" ") for sub_x in x.split(" | ")] for x in input]

    return (input)


if __name__ == "__main__":
    main()

