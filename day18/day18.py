'''
up=Down
down = up


'''
import re

def main():
    content = get_input(exBOOL = True)
    
    print(content)
    print()
    #print()
    #print( content[1])
    #snailfish(content[0], content[1])
    snailfish([1,2], [[3,4],5])



#---------------------Funcs--------------------
def snailfish(nums_a, nums_b):
    print(nums_a, nums_b)
    added_nums = [nums_a + nums_b]
    snail = compact_str(added_nums)
    print(snail)
    checked = ""
    depth = 0
    print("==="*20)
    snail = "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    pairs_indexes = find_number_pairs(snail)
    #print(pairs_indexes)
    #find_higher_pairs(snail, pairs_indexes)
    i=0
    while(True):
        print(f"  --  level: {i} !")
        new_indexes = find_higher_pairs(snail, pairs_indexes, verbose = True)
        if(new_indexes == pairs_indexes or i>2):
            break
        else: 
            pairs_indexes = new_indexes
            i+=1
 
    print()
    print("==="*20)



    if (has_nested_pair(added_nums)):
        print("EXPLODE leftmost")
    elif(is_10_or_greater(added_nums)):
        print("leftmost number splits")
    else:
        #reduce
        print()
    #reduce
    print()

def find_higher_pairs(snail, pairs_indexes, verbose = False):
    pairs = [(snail[beg:end],beg,end) for beg,end in pairs_indexes]
    if(verbose): print([x[0] for x in pairs])
    new_indexes = []
    i = 0
    while(i<len(pairs)-1):
        p_1, b_1, e_1 = pairs[ i ]
        p_2, b_2, e_2 = pairs[ i + 1 ]
        p_pair = "[" + p_1 + "," + p_2 + "]"
        ref = snail[b_1-1 : e_2+1]
        print(p_pair, ref)
        if(p_pair == ref):
            print("YES", p_1, p_2)
            new_indexes.append((b_1-1, e_2+1))
            i+=2
        else:
            print("NO", p_1, p_2)
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
                if(verbose): print(f" new to check : {to_check}")
            else:#all is ok
                if(verbose): print(f"this is a pair : {potential_pair} !!!!")
                if(verbose): print(snail.index(potential_pair))
                pair_start = snail.index(potential_pair)
                pair_end = snail.index(potential_pair)+len(potential_pair)
                pairs_indexes.append((pair_start, pair_end))
                to_check = to_check[i_close:]
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

