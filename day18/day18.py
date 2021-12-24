'''
up=Down
down = up


'''
import re
from typing import Union

def main():
    content = get_input(exBOOL = True)
    
    print(f"Content: {content}")
    print()
    #print()
    #print( content[1])
    #snailfish(content[0], content[1])
    snailfish([1,2], [[3,4],5])



#---------------------Funcs--------------------
def find_deep_nested_pairs(snail, verbose = False):

    depth = 0
    nested_deep = []#list containing 4 pairs or deeper pairs
    pairs_contained  = {}# to list which pairs are inside
    
    if(verbose): 
        print(f"Snail : {snail}")
        print("==="*20)
    pairs_indexes = find_number_pairs(snail, verbose=False)
    while(True):
        if(verbose):
            print(f"  --  level: {depth} !")
            #print(snail)
        new_indexes, pairs_contained = find_higher_pairs(snail, pairs_indexes, pairs_contained, verbose = False)
        new_pairs = [snail[beg:end] for beg,end in pairs_indexes]
        if(verbose): print(f"   new_pairs: {new_pairs} !")

        if(depth>=3):
            pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
            nested_deep.append((depth, pairs))
        if(new_indexes == pairs_indexes or depth>20):
            break
        else: 
            pairs_indexes = new_indexes
            depth+=1
    if(verbose): 
        print(f"  --  Final level reached: {depth} !")
        pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
        print(f"Pairs: {pairs}")
        print()
        print("==="*20)
    return(nested_deep, pairs_contained)


def snailfish(nums_a, nums_b, verbose = True):

    #1: Concat numbers
    added_nums = [nums_a + nums_b]
    snail = compact_str(added_nums)
    #snail = "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    snail = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    
    if(verbose): 
        print(f"Input : {nums_a} - { nums_b}")
        print(f"Snail : {snail}")

    #2 Find pairs nested inside 4 pairs and explode
    red_snail = explode(snail, verbose = False)
    print(f"\nReduced exploded Snail is : {red_snail}")

    #3 Find nums >= 10 and split !
    spl_snail = is_10_or_greater(red_snail)
    #if (has_nested_pair(added_nums)):
    #    print("EXPLODE leftmost")
    #elif(is_10_or_greater(added_nums)):
    #    print("leftmost number splits")
    #else:
        #reduce
    #    print()
    #reduce


def explode(snail, verbose = False):
    nested_pairs, pairs_contained = find_deep_nested_pairs(snail)
    #print("AAA"*99)
    print()
    
    print(f"Nested pairs: {nested_pairs}")
    print(f"pairs_contained: {pairs_contained}")

    pair, depth = count_nested(nested_pairs, pairs_contained)
    if(depth>4):
        print(f"PAIR: {pair} DEPTH: {depth}")
    print(snail.index(pair), len(pair))
    ind_start = snail.index(pair)
    to_explode = pair
    
    if(len(nested_pairs)==0):
        return(snail)
    to_explode = nested_pairs[0][1][0][0]
    ind_start = nested_pairs[0][1][0][1]

    if(verbose):
        print(f"Nested pairs: {nested_pairs}")
        print()
        print(f"To explode: {to_explode}")
    #this might become 1 more [ symbol
    print()

    leftmost_nested_pair = to_explode[to_explode.index("[[[[")+3:]
    ind_start += 3
    count = 0
    for i, x in enumerate(leftmost_nested_pair):
        if x == "[":   count += 1
        elif x == "]": count -= 1
        elif x == ',' and count == 0:
            will_explode = eval(leftmost_nested_pair[:i])
            #print(f"Will explode: {will_explode}")
            ind_end = ind_start + i
            break
    
    num_left, i_left = number_to_left(snail[:ind_start])
    if(i_left > 0): num_left = str(int(num_left)+will_explode[0])
    num_right, i_right = number_to_right(snail[ind_end:])
    if(i_right > 0): num_right = str(int(num_right)+will_explode[1])
    
    patch = snail[ind_start-i_left : ind_end+i_right]
    patch = num_left + snail[ind_start - i_left -len(num_left)+1 : ind_start]+\
            snail[ind_end : ind_end + i_right -1] + num_right
    
    new_snail = snail[:ind_start-i_left] + patch + snail[ind_end+i_right:]
    
    if(verbose):
        print("now----left")
        print(f"num: {num_left}, index: {i_left}")
        print("now----right")
        print(f"num: {num_right}, index: {i_right}")
        print(f"Patch    : {patch}")
        print(f"Snail    : {snail}")
        print(f"NEW Snail: {new_snail}")
    return(new_snail)



def number_to_left(snail):
    #print(snail)
    #print(snail.split())
    extracted_nums = [s for s in re.findall(r'\b\d+\b', snail)]
    #print(extracted_nums)
    if(len(extracted_nums)>1):
        number = extracted_nums[-1]
        
        index = snail[::-1].index(number)
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


def find_higher_pairs(snail, pairs_indexes, pairs_contained, verbose = False):
    pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
    elts =  [(s) for s in re.findall(r'\b\d+\b', snail)]
    elts_i =  [(s.start(),s.end()) for s in re.finditer(r'\b\d+\b', snail)]
    elts_w_i = [(x, s[0], s[1]) for x, s in zip(elts, elts_i)]
    for p, pb, pe in pairs:
        elts_w_i = list(filter(lambda x: (x[1]<pb or x[1]>pe), elts_w_i))
        elts_w_i = list(filter(lambda x: (x[2]<pb or x[2]>pe), elts_w_i))
    #print(f" ### ELTS {elts_w_i}")
    #print(f" ### Pairs {pairs}")
    
    pair_elts = sorted(elts_w_i+pairs, key = lambda x: x[1])
    
    if(verbose): print([x[0] for x in pair_elts])
    new_indexes = []
    i = 0
    if(len(pair_elts)==1):
        return(pairs_indexes, pairs_contained)


    while(i<len(pair_elts)-1):
        p_1, b_1, e_1 = pair_elts[ i ]
        p_2, b_2, e_2 = pair_elts[ i + 1 ]
        p_pair = "[" + p_1 + "," + p_2 + "]"
        ref = snail[b_1-1 : e_2+1]
        if(verbose): print("\n",p_pair, ref)
        if(p_pair == ref):
            if(verbose): print("YES", p_1, p_2)
            new_indexes.append((b_1-1, e_2+1))
            if(is_pair(p_1)): 
                if p_pair not in pairs_contained.keys():
                    pairs_contained[p_pair] = p_1
            if(is_pair(p_2)): 
                if p_pair not in pairs_contained.keys():
                    pairs_contained[p_pair] = p_2
            i+=2
        else:
            if(verbose): print("NO", p_1, p_2, "_-_", p_pair, ref)
            if(i <= len(pair_elts)-2):
                #print("NO",p_1)
                new_indexes.append((b_1,e_1))
            else:
                new_indexes.append((b_1,e_1))
                new_indexes.append((b_2,e_2))
            i+=1
    
    return(new_indexes, pairs_contained)
    #left = snail[:beg][::-1]

    #print(left, snail[:beg])
        #extend_left:


def is_pair(p_pair):
    if(p_pair.count("[") == p_pair.count("]") and p_pair.count("[") > 0):
        return(True)
    else:
       return(False)


def count_nested(nested_pairs, pairs_contained):
    #print("\n\n\n")
    pairs = [x for x in nested_pairs if x[0] == max([x[0] for x in nested_pairs])]
    #print(pairs)
    pair = pairs[0][1][0][0]
    #print(pair)
    depth = 0
    while (pair in pairs_contained.keys()):
    #    print(pair)
        pair = pairs_contained[pair]
        depth += 1
    #print(pair, depth)
    return(pair,depth)

def find_number_pairs(snail, verbose = False):
    pairs_indexes = []
    to_check = str(snail)
    n_seen = 0
    while(len(to_check) > 4):
        m_num1 = re.search(r"[\[]\d", to_check)
        if(m_num1):
            i_open = m_num1.start()
            left_pair = to_check[i_open : m_num1.end()+1]
            if(verbose): print(f"Num1 found : {left_pair}")
            i_close = i_open + to_check[i_open:].index("]")+1
            potential_pair = to_check[i_open : i_close]
            if(verbose): print(f"Potential pair : {potential_pair}")
            extracted_nums = [int(s) for s in potential_pair.split() if s.isdigit()]
            if("[" in potential_pair[1:-1] or potential_pair.count(",")>1):#check no intruders in the pair
                #start again at : i_open + to_check[i_open:].index("[")
                if(verbose): print("intruder")
                i_past_num1 = m_num1.start() + m_num1.end()
                new_i_start =  i_past_num1 + to_check[i_past_num1:].index("[")
                #print(f"new i start: {new_i_start}")
                to_check = to_check[new_i_start:]
                n_seen += new_i_start
                if(verbose): print(f" new to check : {to_check}")
            else:#all is ok
                if(verbose): print(f"this is a pair : {potential_pair} !!!!")
                #if(verbose): print(snail.index(potential_pair))
                if(verbose): print(n_seen+i_open, n_seen+i_close)
                pair_start = n_seen + i_open
                pair_end = n_seen + i_close
                pairs_indexes.append((pair_start, pair_end))
                to_check = to_check[i_close:]
                n_seen += i_close
                if(verbose): print(f" new to check : {to_check}")
        else:
            #print(("no pairs left as no numbers"))
            break
    if(verbose):
        print("\ncheck ended")
        for a,b in pairs_indexes:
            print(f"   pair: {snail[a:b]} - start at {a} end at {b}")
    return(pairs_indexes)
    
"""
def find_2_digits_nums(snail):
    extracted_nums = [s for s in potential_pair.split() if s.isdigit() if len(s)>=2]
    print(snail.index(s))

"""
def compact_str(snail):
    if(type(snail) != str):
        snail = str(snail)
    while("  " in snail):
        snail = snail.replace("  "," ")
    snail = snail.replace(" ","")
    return(snail)

        
    

'''
def has_nested_pair(numbers):
    """If any pair is nested inside four pairs, the leftmost such pair explodes."""
    return(True)'''


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
    if(verbose):
        print(f"Patch    : {patch}")
        print(f"Snail    : {snail}")
        print(f"NEW Snail: {new_snail}")
    return(new_snail)

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

