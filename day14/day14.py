'''
up=Down
down = up


'''
from os import replace
import numpy as np
from numpy.core.fromnumeric import sort

def main():
    template, rules = get_input(exBOOL = True)
    new_rules = translate_rules(rules)
    b_i, h_i = get_index_B_H(rules)
    #to_check = [x[0] for x in rules]
    #letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #init count
    letters_short = "BH"
    count = [0 for x in letters_short]
    for x in template:
        if(x in letters_short):
            count[letters_short.index(x)]+=1
    print(" "+", ".join(letters_short))
    print(count)
    print(template)
    for i in range(3):
        print("------------BEGIN step",i)
        print(template)
        print()
        template, count = batch_insert_count(template, count, new_rules, b_i, h_i)
        print(template)
        #print("\n",template)
        #print("summmarrrry",i+1, len(template),score_2(count),count)
        
        #print(template)
        #print("After step %d:"%(i+1), len(template))
        #print(score(template), score_2(count))
   # print(score(template))


#---------------------Funcs--------------------
def score(template):
    count = [(x,template.count(x)) for x in np.unique([x for x in template])] 
    sorted_count = sorted(count, key=lambda x: x[1])
    return(sorted_count[-1][1]-sorted_count[0][1])


def score_2(count):
    count = list(filter(lambda x: x>0, count))
    return(max(count)-min(count))


def get_index_B_H(rules):
    B_indexes = [i for i,x in enumerate(rules) if x[1] == "B"]
    H_indexes = [i for i,x in enumerate(rules) if x[1] == "H"]
    return(B_indexes, H_indexes)


def translate_rules(rules):
    return([(pattern, pattern[0]+letter+pattern[1]) for pattern, letter in rules])


def batch_insert_count(template, count, new_rules, b_i, h_i):
    new_template = []
    to_check = [x[0] for x in new_rules]
    
    batch_size = 10

    template_lens = [len(x) for x in template]
    cum_sum = np.cumsum(template_lens)
    total_len = sum(template_lens)
    n_seen = 0
    for i in range(0,total_len,batch_size):
        print(i)
        #find where we would be
        index = cum_sum.index(n_seen)
        #print(i,"=====I====","another_batch")
        #print(batch)
        
        if(i==0):
            batch = template[i:i+batch_size]
        else:
            batch = template[i-1:i+batch_size]
        replace_batch = batch[0]
        #print("Batch:", batch)
        for k in range(len(batch)-1):
            chunk = batch[k:k+2]
            #print(chunk)
            if(chunk in to_check):
                change_i = to_check.index(chunk)
                new_pattern = new_rules[change_i][1]
                #print(new_rules[change_i])
                if(change_i in b_i): count[0]+=1
                if(change_i in h_i): count[1]+=1
                replace_batch  = replace_batch[:-1]+new_pattern
                #print(replace_batch, new_pattern)
            else:
                replace_batch+=chunk
#        print("solution", replace_batch[1:])
        new_template.append(replace_batch[1:])
    print("res", new_template)
    return(new_template, count)


def insert_and_count(template, count, rules, to_check, letters):
    new_template = template[0]
    #to_check = [x[0] for x in rules]
    for i in range(len(template)-1):
        chunk = template[i:i+2]
        if(chunk in to_check):
            new_letter = rules[to_check.index(chunk)][1]
            new_chunk = new_letter+chunk[1]
            if(new_letter in letters):
                count[letters.index(new_letter)]+=1
            new_template += new_chunk
        else:
            new_template += chunk
    return(new_template, count)



def insert_rule(template, rules):
    new_template = template[0]
    to_check = [x[0] for x in rules]
    for i in range(len(template)-1):
        chunk = template[i:i+2]
        #print("chunk",chunk)
        #print(chunk)
        if(chunk in to_check):
            new_letter = rules[to_check.index(chunk)][1]
            #print(new_letter)
            new_chunk = new_letter+chunk[1]
            #print("   ",new_chunk)
            new_template += new_chunk
        else:
            new_template += chunk
        #print(new_template)
    return(new_template)


#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day14/example_in.txt" 
    else: path = "./day14/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)
    input = list(map(lambda x: x.replace("\n",""), input))
    template = input[0]
    
    rules = [x.split(" -> ") for x in input[2:]]
    
    return(template, rules)


if __name__ == "__main__":
    main()

