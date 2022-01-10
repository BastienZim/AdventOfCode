'''
up=Down
down = up


'''
from os import curdir
import re
import numpy as np


def main():
    content = get_input(exBOOL = False)

    #print(f"Content: {content}")
    #print()

    #snailfish( [[[[1,1],[2,2]],[3,3]],[4,4]], [5,5], verbose = True)

    """snail = snailfish(content[0], content[1], verbose = False)

    #print(content[0],"   ", content[1])


    print(f"First Snail:   {snail}")
    
    if(len(content)>2):#print(init_snail)
        for x in content[2:]:
            #print(x)
            new_snail = snailfish(snail, x)
            #print(f"\n Partial Snail: {new_snail}")
            #print(snail,"    ",x)
            snail = new_snail
        #print(new_snail)
        print(f"\n\nFINAL SNAIL is:     {new_snail}")
        #print(f"\n\TRUE   SNAIL is:   [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
        #print(f"\n\TRUE   SNAIL is:   [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
        print(f"The Final sum is {sum_pair(new_snail)}")
    """

    print("PART 2")
    max_sum = iterate_all_pairs(content)
    print(max_sum)


#---------------------Funcs--------------------
def iterate_all_pairs(content):
    max_sum = 0
    for p_1 in content:
        for p_2 in content:
            if(p_1 != p_2):
                new_snail = snailfish(p_1, p_2)
                p_sum = sum_pair(new_snail)
                if(p_sum > max_sum):
                    max_sum = p_sum
    return(max_sum) 

def test_explosion(snail):
    snail = explode(snail, verbose=True)
    #snail = explode_MAX(snail, verbose=True)
    #snail = split_MAX(snail, verbose=True)
    #print(" - Round 2")
    #snail = explode_MAX(snail, verbose=True)
    #    if(snail == old_snail):
    ##        evolving = False
    #    else:
    #        old_snail = str(snail)

    return()

def snailfish(nums_a, nums_b, verbose = False):
    nums_a, nums_b = compact_str(nums_a), compact_str(nums_b)
    #1: Concat numbers
    added_nums = "["+str(nums_a) +","+ str(nums_b)+"]"
    snail = compact_str(added_nums)

    if(verbose):
        print(f"Input : {nums_a} - { nums_b}")
        #print(f"Added nums : {added_nums}")
        print(f"Snail : {snail}")

        #print(f"Snail Before expl: {snail}")

    evolving = True
    old_snail = str(snail)
    while(evolving == True):
        
        snail = explode_MAX(snail)
        snail = is_10_or_greater(snail)
        snail = explode_MAX(snail)
        
        if(verbose): print(f"            Splitting \n{snail}")
        if(snail == old_snail):
            evolving = False
        else:
            old_snail = str(snail)

    if(verbose): print(f"Final Reduced Snail : {snail}")

    return(compact_str(snail))


def sum_pair(pair, count = 0):
    real_pair = eval(pair)
    if(is_1_pair(pair)):
        count += pair[0]*3+pair[1]*2
    else:
        count+= sum_pair(pair[0])*3 + sum_pair(pair[1])*2
    return(count)


def split_MAX(snail, verbose = False):
    spl_snail = ""
    while(True):
        spl_snail = is_10_or_greater(snail)
        if(verbose): print(f"  Splitted Snail is :       {spl_snail}")
        if(spl_snail == snail):
            break
        else:
            #print(f"Reduced exploded Snail is : {snail}")
            snail = spl_snail

    if(verbose): print(f"Totally Splitted Snail is : {spl_snail}")
    return(spl_snail)


def explode_MAX(snail, verbose = False):
    count_expl = 0
    red_snail = ""
    while(True):
        red_snail = explode(snail, verbose = False)
        if(red_snail == snail):
            break
        else:
            if(verbose): print(f"  Exploded Snail is :       {red_snail}")
            snail = red_snail
            count_expl += 1
    #if(verbose): print(f"{count_expl} Explosions. Totally exploded Snail is : {red_snail}")
    if(verbose): print(f"Totally exploded Snail is : {red_snail}")
    return(red_snail)

def explode(snail, verbose = False):
    #verbose = True
    a = get_exploding_pair(snail, level = 4)
    b = get_exploding_pair(snail, level = 5)
    c = get_exploding_pair(snail, level = 6)
    get_expl_every_levels = [get_exploding_pair(snail, level = k) for k in range(4,9,1)]
    potential_expl = [x for x in get_expl_every_levels if x]
    if(len(potential_expl)>0):
        first_pair_idx = np.argmin([x[0] for x in potential_expl])
        #print(np.argmin(first_pair_idx))
        exploding_pair = potential_expl[first_pair_idx]
        #print(exploding_pair)
        ind_start, ind_end, to_explode = exploding_pair
        if(verbose):
            print(f"     FOUND: -> {exploding_pair}")
            print(f"     To explode: {to_explode}")
            print(f"snail : {snail}")
    else:
        return(snail)


    will_explode = eval(to_explode)

    #ind_end+=1
    num_left, i_left = number_to_left(snail[:ind_start], verbose = False)
    if(verbose): print(f"SNAILLL: {snail}")
    #print(f"LEFTTTT : {num_left}, {i_left}")
    if(i_left > 0):
        num_left = str(int(num_left)+will_explode[0])
        old_left_num = int(num_left) - will_explode[0]
    else:
        old_left_num = ""
    num_right, i_right = number_to_right(snail[ind_end:])
    if(i_right > 0):
        num_right = str(int(num_right)+will_explode[1])
        old_right_num = int(num_right) - will_explode[1]
    else:
        old_right_num = ""


    if(len(str(old_left_num))>0):
        if(len(str(old_left_num)) == 1):
            bef = snail[:ind_start-i_left-len(str(old_left_num))]
            aft = snail[ind_start-i_left  : ind_start]
        else:
            bef = snail[:ind_start-i_left-len(str(old_left_num))+1]
            aft = snail[ind_start-i_left + 1  : ind_start]
        left_part = bef + num_left + aft
        if(verbose):
            print(f"       L bef {bef}")
            print(f"     L num_left {num_left}")
            print(f"     L aft {aft}")
            print(f"     There is a left num:  {num_left} -> {left_part} ")
    else:
        left_part = snail[:ind_start]+"0"
        if(verbose):    print(f"     There NO left num:  -> {left_part} ")
    if(len(str(old_right_num))>0):
        bef = snail[ind_end + 1 : ind_end + i_right - len(str(old_right_num))]
        aft = snail[ind_end+i_right :]
        right_part = bef + num_right + aft
        if(verbose):
            print(f"       R bef {bef}")
            print(f"     R num_left {num_right}")
            print(f"     R aft {aft}")
            print(f"     There is a right num:  {num_right} -> {right_part} ")
    else:
        right_part = "0"+snail[ind_end+1 :]
        if(verbose):    print(f"     There NO right num:  -> {right_part} ")

    #print(f"    right_part:  {right_part}" )
    #print(f"    left_part :  {left_part}" )
    before_padding = left_part + "," + right_part
    #print(f"     NEW Snail : {new_snail}")
    while(",," in before_padding):
        before_padding = before_padding.replace(",,",",")
    before_padding = before_padding.replace("[,","[0,")
    new_snail = before_padding.replace(",]",",0]")
    #print(f"     NEW Snail : {new_snail}")
    if(verbose):
        #print(f"     Snail: {snail}")
        #print(f"     True left number: {old_left_num} - New left : {num_left}")
        #print(f"     True right number: {old_right_num} - New Right : {num_right}")

        print(f"     Bef pad   : {before_padding}")
        print(f"     NEW Snail : {new_snail}")


    return(new_snail)



def number_to_left(snail, verbose=False):
    #print(snail)
    #print(snail.split())
    extracted_nums = [s for s in re.findall(r'\b\d+\b', snail)]
    if(verbose): print(f"  EXtracted_nums: {extracted_nums}")
    #print()
    if(len(extracted_nums)>0):
        number = extracted_nums[-1]
        #print(snail, number)
        #print("AAA"*33)

        #print(f"OLD: {snail[::-1].index(number)} - NEW: {len(snail) - snail.rfind(number) - 1}")
        #index = snail[::-1].index(number)

        index = len(snail) - snail.rfind(number) - 1
        return((number, index))
    else:
        return(("0",0))


def number_to_right(snail):
    #print(snail)
    extracted_nums = [str(s) for s in re.findall(r'\b\d+\b', snail)]
    #print(extracted_nums)
    if(len(extracted_nums)>0):
        number = extracted_nums[0]
        index = snail.index(number)+len(str(number))
        #print(f"num: {number}, index: {index}")
        return((number, index))
    else:
        return(("0",0))



def is_pair(p_pair):
    if(p_pair.count("[") == p_pair.count("]") and p_pair.count("[") > 0):
        return(True)
    else:
       return(False)


def is_1_pair(p_pair):
    if(type(p_pair) != str):
        p_pair=str(p_pair)
    if(p_pair.count("[") == p_pair.count("]") and p_pair.count("[") == 1 and p_pair.count(",") == 1):
        return(True)
    else:
       return(False)

def sum_pair(original_pair,):
    count = 0
    if(type(original_pair) == str):
        pair = eval(original_pair)
    else: pair = original_pair

    if(type(pair) == int):
        count = pair
    elif(type(pair[0])==int and type(pair[1])==int ):
        count = pair[0]*3 + pair[1]*2
    elif(type(pair[0])==int):
        count = pair[0]*3 + sum_pair(pair[1])*2
    elif(type(pair[1])==int):
        count = sum_pair(pair[0])*3 + pair[1]*2
    else:
        count = sum_pair(pair[0])*3 + sum_pair(pair[1])*2
    return(count)


def compact_str(snail):
    if(type(snail) != str):
        snail = str(snail)
    while("  " in snail):
        snail = snail.replace("  "," ")
    snail = snail.replace(" ","")
    return(snail)


def is_10_or_greater(snail, verbose=False):
    """If any regular number is 10 or greater, the leftmost such regular number splits"""
    dd_num = [int(s) for s in re.findall(r'\b\d{2}\b', snail)]
    if(len(dd_num)!=0):
        dd_num = dd_num[0]
    else:
        return(snail)
    dd_i = [(s.start(),s.end()) for s in re.finditer(r'\b\d{2}\b', snail)][0]
    if(verbose): print(dd_num, dd_i)
    if((dd_num/2)%1 !=0):
        left_val = int(dd_num/2)
        right_val = int(dd_num/2)+1
    else:
        left_val = int(dd_num/2)
        right_val = int(dd_num/2)

    patch = str([left_val,right_val])
    new_snail = snail[:dd_i[0]] + patch + snail[dd_i[1]:]

    new_snail=compact_str(new_snail)
    if(verbose):
        print(f"Patch    : {patch}")
        print(f"Snail    : {snail}")
        print(f"NEW Snail: {new_snail}")
    return(new_snail)

def show_count_brackets(stringIN, level = 4 ,verbose = False):
    count, res = 0, ""
    has_found=False
    for i, x in enumerate(stringIN):
        if x=="[":
            count += 1
            res+=str(count)+" "
            if(not has_found and count==level+1):
                res = res[:-1]+"A"
                has_found = True
        elif x=="]":
            if(has_found and count == level):
                res = res[:-1]+"B"
                has_found = False
    #            return([beg, i, stringIN[beg:i+1]])
            count -= 1
            res+=str(count)+" "
        else: res+="  "
    if(verbose):
        print(" ".join(stringIN))
        print(res)

def get_exploding_pair(snail, level = 4 ,verbose = False):
    count = 0
    has_found=False
    for i, x in enumerate(snail):
        if x=="[":
            count += 1
            if(not has_found and count==level+1):
                beg = i
                has_found = True
        elif x=="]":
            count -= 1
            #if(is_1_pair(snail[beg:i+1])):
           #    if(has_found and count == level): return([beg, i, snail[beg:i+1]])
            if(has_found and count == level):
                if(is_1_pair(snail[beg:i+1])):
                    return([beg, i, snail[beg:i+1]])
                else:
                    has_found = False
            #else: has_found = False
    return(None)

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day18/example_in.txt"
    else: path = "./day18/input.txt"

    with open(path) as f:
        content = f.readlines()
    print
    content = list(map(lambda x: eval(x.replace("\n", "")), content))

    return(content)


if __name__ == "__main__":
    main()

