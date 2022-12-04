'''
up=Down
down = up


'''

import numpy as np


def main():
    content = get_input(exBOOL = True)
    
    print(content)

#scanner detects closest beacon
# do not know own position 
# detect at least 12 beacons with 2 scanners at 1 time
# unknow rotation - i.e. facing direction
# 24 different orientations

#---------------------Funcs--------------------

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day19/example_in.txt" 
    else: path = "./day19/input.txt" 

    with open(path) as f:
        content = f.readlines()
    content = list(map(lambda x: x.replace("\n", ""), content))

    all_scanners = []
    new_scanner = []
    for line in content:
        if "scanner" in line:
            print(f"{line}")
            if(len(new_scanner)>0): all_scanners.append(new_scanner)
            new_scanner = []
        elif(any(i.isdigit() for i in line)):
            print(line)
            line = [int(x) for x in line.split(",")]
            new_scanner.append(line)
            print(f"  ->{line}")
    all_scanners.append(new_scanner)
    all_scanners = np.array(all_scanners)
#    all_scanners = all_scanners.reshape((1))
    
    print(f"\n\n\n all scanners: {all_scanners}\n")
    print(f" all scanners SHAPE: {np.shape(all_scanners)}\n")


    return (content)


if __name__ == "__main__":
    main()

