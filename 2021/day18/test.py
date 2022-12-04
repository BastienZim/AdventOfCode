
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

#pair = "[9,1]"
#print(sum_pair(pair))
#pair = "[1,9]"
#print(sum_pair(pair))
pair = "[[1,2],[[3,4],5]]"
pair = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
pair = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
pair = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
pair = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
pair = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
pair = "[[[[6,6],[7,7]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[8,8],[9,9]]]]"
pair = "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
print(sum_pair(pair))