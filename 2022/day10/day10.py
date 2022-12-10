'''
@author: BastienZim

'''

import os
import numpy as np


#path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
path = "/home/bastien/Documents/AdventOfCode/2022"


example = True


def get_sprite_pos(sprite, reg_X):
    return("."*(reg_X-1)+sprite+"."*(40-len(sprite)-(reg_X-1)))

def get_simbol_to_print(sprite_pos, position):
    return(sprite_pos[position%40])

def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    input = sanitize_input(input)

    to_execute = []
    for x in input:
        if x == "noop":
            to_execute.append("N")
        else:
            val = x.split(" ")[1]
            to_execute.append("W "+str(val))
            to_execute.append(val)

    CTX_w, CRT_h = 40,6
    reg_X = 1
    signals=[]
    current_CRT_row = ""
    sprite = "###"

    sprite_pos = get_sprite_pos(sprite, reg_X)
    #print(f"Sprite position : " + sprite_pos)
    verbose = True
    
    for i, instruction in enumerate(to_execute):
        i_cicle = i+1
        #print()
        #print(i_cicle, instruction, reg_X)\
        #if((i_cicle-20)%40==0):#here newLIne
        #if(i_cicle==22):#here newLIne
        #    break
        #    signal_strength = reg_X *i_cicle
        #    signals.append(signal_strength)
            #print("  ", i_cicle, reg_X)
            #print(i_cicle, signal_strength)
        #PROBLEM AT 40 + 12
        ####...###...###...###...###...###...###.
        ####...###..##..##...###...####.###.####
        if(len(current_CRT_row)==39):
#            if(verbose):
            print(current_CRT_row)
            current_CRT_row = ""

        if("W" in instruction):
            if(verbose):print(f"Start cycle    {i_cicle}: begin executing Addx "+ instruction.split(" ")[1])
            #print("SYMBOL TO PRINT" ,get_simbol_to_print(sprite_pos, i))
            current_CRT_row = current_CRT_row + get_simbol_to_print(sprite_pos, i)
            if(verbose):print(f"During cyle    {i_cicle}: CRT draws pixel in position {i}")
            if(verbose):print(f"Current CRT row : {current_CRT_row}")
            
        elif("N" in instruction):
            if(verbose):print(f"Start cycle    {i_cicle}: begin executing Noop")
            continue
        else:
            #print(f"Start cycle    {i_cicle}: begin executing Addx "+ instruction.split(" ")[1])
            current_CRT_row = current_CRT_row + get_simbol_to_print(sprite_pos, i)
            if(verbose):print(f"During cyle    {i_cicle}: CRT draws pixel in position {i}")
            if(verbose):print(f"Current CRT row : {current_CRT_row}")
            reg_X += int(instruction)
            if(verbose):print(f"End of cycle   {i_cicle}: finish executing addx {instruction} (Register X is now {reg_X})")
            sprite_pos = get_sprite_pos(sprite, reg_X)
            if(verbose):print(f"Sprite position : " + sprite_pos)
    
    print(sum(signals))

    



def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: x.replace("\n",""), input))




if __name__ == "__main__":
    main()

