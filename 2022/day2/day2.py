'''
@author: BastienZim

'''

import os
import numpy as np

path = "/home/bastienzim/Documents/perso/adventOfCode/2022/"



example = False


elf_to_shape = {"A":"R", "B":"P", "C":"S"}
me_to_shape = {"X":"R", "Y":"P", "Z":"S"}
me_to_outcome = {"X":"L", "Y":"D", "Z":"W"}
to_lose =  {"R":"S", "P":"R", "S":"P"}
to_win =  {"R":"P", "P":"S", "S":"R"}

shape_to_score = {"R":1, "P":2, "S":3}
outcome_to_score = {"W":6, "D":3, "L":0}


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    #print(input)
    input = sanitize_input(input)
    #print(input)
    #for  x in input:
    #    print(x)
    #    sym_1, dec = elf_to_shape[x[0]], me_to_outcome[x[1]]
    #    sym_2 = obtain_outcome(sym_1, dec)
    #    print(sym_1, sym_2, dec)
    #    print(shape_to_score[sym_2] + outcome_to_score[dec])
        #outcome = compute_outcome(sym_1, sym_2)
        #print(outcome)
        #print(compute_score(sym_1, sym_2))
    results = list(map(lambda x: shape_to_score[obtain_outcome(x[0], x[1])] + outcome_to_score[x[1]], map(lambda x: (elf_to_shape[x[0]], me_to_outcome[x[1]]), input)))
    print(sum(results))

def obtain_outcome(sym_1, dec):
    if(dec == "W"):
        return(to_win[sym_1])
    elif(dec == "L"):
        return(to_lose[sym_1])
    else:
        return(sym_1)

def compute_outcome(sym_1,sym_2):
    if(sym_1==sym_2):return("D")
    else:
        if(sym_1=="R"):
            if(sym_2=='P'): return("W")
            else: return("L")
        elif(sym_1=="P"):
            if(sym_2=='S'): return("W")
            else: return("L")
        elif(sym_1=="S"):
            if(sym_2=='R'): return("W")
            else: return("L")

def compute_score(sym_1, sym_2):
    score = 0
    score += outcome_to_score[compute_outcome(sym_1, sym_2)]
    score += shape_to_score[sym_2]

    return score

#total_score = shape_score + outcome_score 



def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n","").split(" "), input))




if __name__ == "__main__":
    main()

