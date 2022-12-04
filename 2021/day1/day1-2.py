'''
@author: BastienZim







'''
import sys
sys.path.append('./day1')

from day1 import count_inc

dir = "/home/bastienzim/Documents/perso/adventOfCode/"
day = "day2/"

def main():
    with open(dir+day+"input.txt") as f:
        input = f.readlines()
    #for x in input:
    #    print(x, x[:3])
    input = sanitize_input(input)
    
    print(input)
    sums = slide(input)
    print(count_inc(sums))

def slide(input):
    len_win = 3
    windows = [input[i:i+len_win] for i in range(len(input)-len_win+1)]
    #print(windows)
    sums = [sum(x) for x in windows]
    #print(sums)
    return(sums)

def monitor(input):
    len_win = 3
    n_wins = 3
    windows = [[] for i in range(n_wins)]
    for i in range(n_wins):
        windows[i] = input[i:i+len_win]

    for i in range(3):
        print(i, windows[i], sum(windows[i]))
    #print(win1, win2, win3)
    











def sanitize_input(input):
    return list(map(lambda x: int(x.replace("\n","")), input))


if __name__ == "__main__":
    main()

