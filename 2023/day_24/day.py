import regex as re
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE_PATH = './input.txt'
INPUT_FILE_PATH = './example_in.txt'

def main():
    lines = parse_input_file()
    all_hail = []
    for l in lines:
        
        pos, vel = par_hail(l)
        all_hail.append({"pos":pos, "vel":vel})
    for h in all_hail:
        #print(h)
        get_hail_path(h)

def par_hail(line):
    pos, vel = line.split("@")
    pos = pos.split(",")
    pos = [int(x) for x in pos]
    vel = vel.split(",")
    vel = [int(x) for x in vel]
    return(pos, vel)

def get_hail_path(h):
    print([f"{p}+{v}*t" for (p,v) in zip(h['pos'],h['vel'])])


#['19+-2*t', '13+1*t']
#y = ax +b
#
#y = 13 + (19- x)/2
x_plot = np.arange(-6,20)
y_plot = [13 + (19- x)/2 for x in x_plot]
plt.plot(x_plot, y_plot)
plt.show()


['18+-1*t', '19+-1*t']


def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()