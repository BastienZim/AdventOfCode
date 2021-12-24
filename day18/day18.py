'''
up=Down
down = up


'''
import re

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
    
    
    if(verbose): 
        print(f"Snail : {snail}")
        print("==="*20)
    pairs_indexes = find_number_pairs(snail, verbose=False)
    while(True):
        if(verbose):
            print(f"  --  level: {depth} !")
            #print(snail)
        new_indexes = find_higher_pairs(snail, pairs_indexes, verbose = False)
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
    return(nested_deep)


def snailfish(nums_a, nums_b, verbose = True):

    #1: Concat numbers
    added_nums = [nums_a + nums_b]
    snail = compact_str(added_nums)
    snail = "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    
    if(verbose): 
        print(f"Input : {nums_a} - { nums_b}")
        print(f"Snail : {snail}")

    #2 Find pairs nested inside 4 pairs and explode
    nested_pairs = find_deep_nested_pairs(snail)
    to_explode = nested_pairs[0][1][0][0]
    ind_start = nested_pairs[0][1][0][1]
    print(f"Nested pairs: {nested_pairs}")
    
    print()
    print(f"To explode: {to_explode}")
    #this might become 1 more [ symbol
    leftmost_nested_pair = to_explode[to_explode.index("[[[[")+3:]
    ind_start += 3
    #print(f"Leftmost: {leftmost_nested_pair}")
    count = 0
    for i, x in enumerate(leftmost_nested_pair):

        #print(i,x, count)
        if x == "[":   count += 1
        elif x == "]": count -= 1
        elif x == ',' and count == 0:
            will_explode = eval(leftmost_nested_pair[:i])
            print(f"Will explode: {will_explode}")
            ind_end = ind_start + i
            break
        #elif(x == "]" and count == 0):
        #    ind_expl_e = ind_start + i
        #    break
    pair_left = will_explode[0]
    print("HERE",ind_start, ind_end, pair_left)

    print("now----left")
    if(number_to_left(snail[:ind_start])):
        print("add to left number")
    else:
        print("do not add")
    print("now----right")
    if(number_to_right(snail[ind_end:])):
        print("add to right number")
    else:
        print("do not add")
        

    #if (has_nested_pair(added_nums)):
    #    print("EXPLODE leftmost")
    #elif(is_10_or_greater(added_nums)):
    #    print("leftmost number splits")
    #else:
        #reduce
    #    print()
    #reduce



def number_to_left(snail):
    print(snail)
    print(snail.split())
    extracted_nums = [s for s in snail.split() if s.isdigit()]
    print(extracted_nums)
    if(len(extracted_nums)>1):
        print(extracted_nums[-1])
    else:
        return("")
    print()      
    return(True)

def number_to_right(snail):
    print(snail)
    print(snail.split())
    extracted_nums = [s for s in snail.split() if s.isdigit()]
    print(extracted_nums)
    if(len(extracted_nums)>0):
        print(extracted_nums[-1])
    print()     
    return(True)


def find_higher_pairs(snail, pairs_indexes, verbose = False):
    pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]

    if(verbose): print([x[0] for x in pairs])
    new_indexes = []
    i = 0
    if(len(pairs)==1):
        return(pairs_indexes)


    while(i<len(pairs)-1):
        p_1, b_1, e_1 = pairs[ i ]
        p_2, b_2, e_2 = pairs[ i + 1 ]
        p_pair = "[" + p_1 + "," + p_2 + "]"
        ref = snail[b_1-1 : e_2+1]
        if(verbose): print("\n",p_pair, ref)
        if(p_pair == ref):
            if(verbose): print("YES", p_1, p_2)
            new_indexes.append((b_1-1, e_2+1))
            i+=2
        else:
            if(verbose): print("NO", p_1, p_2, "_-_", p_pair, ref)
            if(i <= len(pairs)-2):
                #print("NO",p_1)
                new_indexes.append((b_1,e_1))
            else:
                new_indexes.append((b_1,e_1))
                new_indexes.append((b_2,e_2))
            i+=1
    
    return(new_indexes)
    #left = snail[:beg][::-1]

    #print(left, snail[:beg])
        #extend_left:


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
    

def find_2_digits_nums(snail):
    extracted_nums = [s for s in potential_pair.split() if s.isdigit() if len(s)>=2]
    print(snail.index(s))


def compact_str(snail):
    if(type(snail) != str):
        snail = str(snail)
    while("  " in snail):
        snail = snail.replace("  "," ")
    snail = snail.replace(" ","")
    return(snail)


def explode(pair):
    expl = pair
    p_sum = sum(pair)

    
    return(expl)

def has_nested_pair(numbers):
    """If any pair is nested inside four pairs, the leftmost such pair explodes."""
    return(True)


def is_10_or_greater(numbers):
    """If any regular number is 10 or greater, the leftmost such regular number splits"""
    return(True)

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

