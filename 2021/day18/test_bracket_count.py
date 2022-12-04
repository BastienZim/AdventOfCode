
stringIN = "[[[[4,0],[5,4]],[[7,7],[0,[6,7]]]],[[5,[5,5]],[[0,[[5,5],[5,5]]],[0,6]]]]"
stringIN = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"

def show_count_brackets(stringIN, level = 4 ,verbose = False):
    count, res = 0, ""
    pairaa = ""
    has_found=False
    for i, x in enumerate(stringIN):
        if x=="[": 
            count += 1
            res+=str(count)+" "
            if(not has_found and count==level+1): 
                res = res[:-1]+"A"
                pairaa += "A "
                has_found = True
                beg = i
            else:
                pairaa += "- "
        elif x=="]": 
            count -= 1
            if(has_found and count == level):
                print("RESS", res, stringIN[beg:i])
                res = res[:-1]+"B"
                pairaa += "B "
                has_found = False
#                return([beg, i, stringIN[beg:i+1]])
            else:
                pairaa += "_ "
                #print(count)
            res+=str(count)+" "
        else: 
            res += "  "
            pairaa += "  "
    if(verbose):
        print(" ".join(stringIN))
        print(res)
        print(pairaa)

def get_exploding_pair(stringIN, level = 4 ,verbose = False):
    count = 0
    has_found=False
    for i, x in enumerate(stringIN):
        if x=="[": 
            count += 1
            if(not has_found and count==level+1): 
                beg = i
                has_found = True
        elif x=="]": 
            count -= 1
            if(has_found and count == level): return([beg, i, stringIN[beg:i+1]])
    return(None)

show_count_brackets(stringIN, verbose = True)

exploding_pair = get_exploding_pair(stringIN, level = 4)
if(exploding_pair):
    print(exploding_pair)
    ind_start, ind_end, pair = exploding_pair
    print(ind_start, ind_end, pair)

#print("\n\n\n")
#for i,x in enumerate(stringIN):
    #print(i,x)
#print(pair)
