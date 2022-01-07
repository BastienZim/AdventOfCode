'''
up=Down
down = up


'''
from os import curdir
import re
from typing import Union

def main():
    content = get_input(exBOOL = True)
    
    print(f"Content: {content}")
    print()

    #snailfish( [[[[1,1],[2,2]],[3,3]],[4,4]], [5,5], verbose = True)

    #snail = snailfish(content[0], content[1])
    
    print(content[0],"   ", content[1])


    print("\n\n               TEEEEEEEEEEEESSTT")

    added_nums = "["+str(content[0]) +","+ str(content[1])+"]"
    snail = compact_str(added_nums)
    #print(added_nums)
    print(snail)
    test_explosion(snail)


    print("              ENNNNNDDDDD   ____    TEEEEEEEEEEEESSTT\n")
    


    #print(f"First Snail:   {snail}")
    #print("Supposed to be","[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
    #print("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    if(len(content)>2):#print(init_snail)
        for x in content[2:]:
            #print(x)
            new_snail = snailfish(snail, x)
            print(f"\n Partial Snail: {new_snail}")
            #print(snail,"    ",x)
            snail = new_snail
        #print(new_snail)
        print(f"\n\nFINAL SNAIL is:     {new_snail}")
#    for i,x in enumerate(content[:-1]):
#        print(x, content[i+1])
    #print()
    #print( content[1])
    #snailfish(content[0], content[1])
    #snailfish([1,2], [[3,4],5])
    #
    #snailfish([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])



#---------------------Funcs--------------------
def test_explosion(snail):

    snail = explode_MAX(snail, verbose=True)
    snail = split_MAX(snail, verbose=True)
    print(" - Round 2")
    snail = explode_MAX(snail, verbose=True)
    #    if(snail == old_snail):
    ##        evolving = False
    #    else:
    #        old_snail = str(snail)

    return()

def snailfish(nums_a, nums_b, verbose = False):

    #1: Concat numbers
    added_nums = "["+str(nums_a) +","+ str(nums_b)+"]"
    snail = compact_str(added_nums)

    #snail = "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    #snail = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    #snail = "[[[[4,0],[5,4]],[[7,7],[0,[6, 7]]]],[[5, [5, 5]],[[0,[[5, 5], [5, 5]]],[0,6]]]]"

    if(verbose): 
        print(f"Input : {nums_a} - { nums_b}")
        print(f"Added nums : {added_nums}")
        print(f"Snail : {snail}")

    #2 Find pairs nested inside 4 pairs and explode
    #3 Find num>10 and split
    #2-3 do that to the max => NOT OPTI
    #print()
    #print(f"Snail Before expl: {snail}")
    evolving = True
    old_snail = str(snail)
    while(evolving == True):
        snail = explode_MAX(snail, verbose=False)
        snail = split_MAX(snail)
        if(snail == old_snail):
            evolving = False
        else:
            old_snail = str(snail)


    if(verbose): print(f"Final Reduced Snail : {snail}")
    
    return(compact_str(snail))



def find_deep_nested_pairs(snail, verbose = False):
    
    depth = 0
    nested_deep = []#list containing 4 pairs or deeper pairs
    pairs_contained  = {}# to list which pairs are inside
    
    if(verbose): 
        print(f"Snail : {snail}")
        print("==="*20)
    #better than find Number pairs !
    #Seems to work
    #old method
    pairs_indexes = new_find_number_pairs(snail)#find_number_pairs(snail, verbose=False)
    #print(f"FIRST Indexes  {pairs_indexes}")
    #print(f"First pairs: {[snail[beg:end] for beg,end in pairs_indexes]}")
    if(verbose): print(f"First pairs: {[snail[beg:end] for beg,end in pairs_indexes]}")
    while(True):
        if(verbose):
            print(f"\n\n  -------  level: {depth} !")
        #print(f"\n\n  -------  level: {depth} !")
                #print(snail)
        #if(snail == "[[[[4,0],[5,4]],[[7,7],[0,[6, 7]]]],[[5, [5, 5]],[[0,[[5, 5], [5, 5]]],[0,6]]]]" and 5 >= depth >=0):
        #    new_indexes, pairs_contained = find_higher_pairs(snail, pairs_indexes, pairs_contained, depth, verbose = False)
        #else:
        new_indexes, pairs_contained = find_higher_pairs(snail, pairs_indexes, pairs_contained, depth, verbose = False)
        new_pairs = [snail[beg:end] for beg,end in new_indexes]
        if(verbose): 
 
#                print(f"   pairs_indexes: {pairs_indexes} !")
#                print(f"   new_indexes  : {new_indexes} !")
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            print(f"   Old_pairs:   {[snail[beg:end] for beg,end in pairs_indexes]} !")
            print(f"   New_pairs:   {new_pairs} !")
            print(f"   Snail: {snail} !")

        if(depth>3):#>=3
            pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
            nested_deep.append((depth, pairs))
        if(new_indexes == pairs_indexes or depth>50):
            if(depth>=50):
                print("TOO DEEP ESCAPING - ERROOR PRONE"*10)
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
    red_snail = ""
    while(True):
        red_snail = explode(snail, verbose = False)
        if(verbose): print(f"  Exploded Snail is :       {red_snail}")
        if(red_snail == snail):
            break
        else:
            snail = red_snail
    if(verbose): print(f"Totally exploded Snail is : {red_snail}")
    return(red_snail)

def explode(snail, verbose = False):
    
    nested_pairs, pairs_contained = find_deep_nested_pairs(snail, verbose=False)
    #print()
    #print(f"Nested pairs: {nested_pairs}")
    #print(f"pairs_contained: {pairs_contained}")
    
    pair, depth = count_nested(nested_pairs, pairs_contained)
    #print(snail)
    #print(f" Pairs: {pair},- Depth: {depth}")
    if(depth>=4):
        if(verbose): print(f"PAIR: {pair} DEPTH: {depth}")
    else:
        return(snail)
    #print(snail.index(pair), len(pair))

    ind_start = snail.index(pair)
    to_explode = pair
    
    if(verbose):
        print(f"Nested pairs: {nested_pairs}")
        print()
        print(f"To explode: {to_explode}")
    
    
    will_explode = eval(to_explode)
    ind_end = ind_start + len(to_explode)
    

    num_left, i_left = number_to_left(snail[:ind_start], verbose = False)
    if(i_left > 0): 
        num_left = str(int(num_left)+will_explode[0])
        old_left_num = int(num_left) - eval(pair)[0]
        #truncated = truncated[0] + str(num_left) + truncated[1+len(str(old_left_num)):]
    else: 
        old_left_num = ""
    num_right, i_right = number_to_right(snail[ind_end:])
    if(i_right > 0): 
        num_right = str(int(num_right)+will_explode[1])
        old_right_num = int(num_right) - eval(pair)[1]
        #truncated = truncated[:-len(str(old_right_num))] + str(num_right) 
    else:
        old_right_num = ""

    
    #remove pair
    truncated = snail[ind_start-i_left-1 : ind_start] + snail[ind_end : ind_end+i_right+1]
    if(i_left>0):
        truncated = str(num_left) + truncated[len(str(old_left_num)):] 
    if(i_right>0):
        truncated = truncated[:-len(str(old_right_num))-1] + str(num_right) + truncated[-1]
    if("[," in truncated): truncated = truncated.replace("[,","[0,")
    if(",]" in truncated): truncated = truncated.replace(",]",",0]")


    
 
    new_snail = snail[ : ind_start - i_left - 1] + truncated + snail[ind_end + i_right+1 : ]
    if(verbose):
        print(f"Snail: {snail}")
        print(f"True left number: {old_left_num} - New left : {num_left}")
        print(f"True right number: {old_right_num} - New Right : {num_right}")
        print()
        print(f"Truncated: {truncated}")
        print(f"NEW Truncated: {truncated}")
        print(f"NEW FILLED Truncated: {truncated}")
        print(f"NEW Snail : {new_snail}")
    
    
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


def find_higher_pairs(snail, pairs_indexes, pairs_contained, depth, verbose = False):
    pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
    elts =  [(s) for s in re.findall(r'\b\d+\b', snail)]
    elts_i =  [(s.start(),s.end()) for s in re.finditer(r'\b\d+\b', snail)]
    elts_w_i = [(x, s[0], s[1]) for x, s in zip(elts, elts_i)]
    for p, pb, pe in pairs:
        elts_w_i = list(filter(lambda x: (x[1]<pb or x[1]>pe), elts_w_i))
        elts_w_i = list(filter(lambda x: (x[2]<pb or x[2]>pe), elts_w_i))
    #print(f" ### ELTS {elts_w_i}")
    #print(f" ### Pairs {[x[0] for x in pairs]}")
    
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
        if(verbose): print(f"\npotential pair: {p_pair}, ref: {ref}")
        #print(f"p_1 :{p_1}  p_2 :{p_2}")
        #print(f"snail :{snail}")
        if(p_pair == ref):
            if(verbose): print("YES", p_1, p_2)
            new_indexes.append((b_1-1, e_2+1))
            if(is_pair(p_1)): 
                if p_pair not in pairs_contained.keys():
                    pairs_contained[p_pair] = [str(p_1)]
                else:
                    pairs_contained[p_pair] = [p_1] + pairs_contained[p_pair]
            if(is_pair(p_2)): 
                if p_pair not in pairs_contained.keys():
                    pairs_contained[p_pair] = [str(p_2)]
                else:
                    pairs_contained[p_pair] = [p_2] + pairs_contained[p_pair]
            i+=2
        else:
            if(verbose):
                print("NO", p_1, p_2, "_-_", p_pair, ref,"---", i, len(pair_elts))
            if(i < len(pair_elts)-2):
                new_indexes.append((b_1,e_1))
                #new_indexes.append((b_2,e_2))
            else:
                new_indexes.append((b_1,e_1))
                new_indexes.append((b_2,e_2))
                #print(f"##########HERE AND DEPTH --- {depth} -- {p_2}")
                #print(i, [i - k for k in range(0,depth) if (i-k)>0])

                #try to match last pair deeper:
                for d, back in enumerate([i - k for k in range(0,depth) if (i-k)>0]):

                    #print(f"-------------------------- --- {back}")
                    all_pairs = [pair_elts[x][0] for x in range(back,i+1)]
                    #print(len(all_pairs))
                    p_3, b_3, e_3 = pair_elts[ back ]
                    new_p_pair = "[" 
                    for p in all_pairs:
                        new_p_pair = new_p_pair + p + ","
                    new_p_pair = new_p_pair + p_2 + "]"
                    new_ref = snail[b_3-1-d : e_2+1+d]
                    #print(f"P-PAIR {new_p_pair} - ref {new_ref}")
                    #print(snail[e_2-5:])
                    if(new_p_pair == new_ref):
                        print("VICTORY"*400)
                #print()
            i+=1
    #print(f"Not in new_indexes {[x for x in pairs_indexes if x not in new_indexes ]}")
    
    #if(verbose):
    #print(f"HEHEHEHE {new_indexes[-1][-1] -1} -- {pairs_indexes[-1][-1]}-- len(snail): {len(snail)} ")
    #if(int(new_indexes[-1][-1]) < int(pairs_indexes[-1][-1]+1 )):
    #    print("One less pair covered  HEHEHEHEHEHEHEHEHEHEHEHE ##########################")
        #print(new_indexes[-1][-1], pairs_indexes[-1])
    #    if(new_indexes[-1][-1] < pairs_indexes[-1][0] and new_indexes[-1][-1] < pairs_indexes[-1][1]):
    #        print("MEGA HEHEHEHHEH XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #        print("a")
            #new_indexes.append(pairs_indexes[-1])   
        #
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
    #print("BBB"*29)
    #print(f"Nested Pairs : {nested_pairs}\n")
    if(len(nested_pairs)==0):
        return([],0)

        """
    has_pairs = True
    p_pairs = [x for x in nested_pairs if x[0] > 3]
    print(f"Pairs contained {pairs_contained}")
    print(len(p_pairs))
    i = 0
    while(i<len(p_pairs)):
        pairs =  [p_pairs[i]]
        print(pairs)
        current_pairs = [str(pairs[0][1][0][0])]
        #print(f"Pair: {current_pairs}")
        
        depth = 0
        has_changed = True
        while (has_changed):
            
            #print(f"    Inside {current_pairs}")
            sub_pairs = []
            for pair in current_pairs:
                if pair in pairs_contained.keys():
                    sub_pairs = sub_pairs + pairs_contained[pair]

            #print(f"    Contains {sub_pairs}")
            #print(f"    Depth {depth}")
            
            if(current_pairs == sub_pairs):
                break
            elif(len(sub_pairs) == 0):
                break
            else:
                current_pairs = sub_pairs
            
            depth += 1
        print("TRYING")
        print(f"PAIR FOUND: {pair}, DEPTH: {depth}")
        i+=1


"""

    #-----------------------------------------------------------------------------------------

    pairs = [x for x in nested_pairs if x[0] == max([x[0] for x in nested_pairs])]
    #print(f"Pairs: {pairs}")
    current_pairs = [str(pairs[0][1][0][0])]
    #print(f"Pair: {current_pairs}")
    
    depth = 0
    has_changed = True
    while (has_changed):
        
        #print(f"    Inside {current_pairs}")
        sub_pairs = []
        for pair in current_pairs:
            if pair in pairs_contained.keys():
                sub_pairs = sub_pairs + pairs_contained[pair]

        #print(f"    Contains {sub_pairs}")
        #print(f"    Depth {depth}")
        
        if(current_pairs == sub_pairs):
            break
        elif(len(sub_pairs) == 0):
            break
        else:
            current_pairs = sub_pairs
        
        depth += 1
    #print(pair, depth)
    return(pair,depth)


def new_find_number_pairs(snail, verbose = False):

    pairs_indexes = [(s.start(),s.end()) for s in re.finditer(r'\b\d+\b', snail)]
    new_indexes, _ = find_higher_pairs(snail, pairs_indexes, {}, 0)
    new_pairs = [(beg,end) for beg,end in new_indexes if end-beg>3]
    
    return(new_pairs)

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
               # print("AAA"*33)
                #print(to_check[i_past_num1:])
                if("[" in to_check[i_past_num1:]):
                    new_i_start =  i_past_num1 + to_check[i_past_num1:].index("[")
                else:
                    new_i_start = len(to_check)
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

    new_snail=compact_str(new_snail)
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

