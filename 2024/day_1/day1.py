import regex as re
import numpy as np

INPUT_FILE_PATH = './input.txt'
INPUT_FILE_PATH = './example_in.txt'
DIGIT_WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
RE = '\d|' + '|'.join(DIGIT_WORDS)

def main():
    lines = parse_input_file()
    print(lines)
    cols = [l.split("   ") for l in lines]
    cols = np.array(cols).T.astype(int)
    list_1 = list(cols[0])
    list_2 = list(cols[1])

    all_dists=[]
    while len(list_1)>0:
        argmini_1 = np.argmin(list_1)
        mini_1 = list_1.pop(argmini_1)
        
        argmini_2 = np.argmin(list_2)
        mini_2 = list_2.pop(argmini_2)
        dist = abs(mini_1-mini_2)
        all_dists.append(dist)
    print(sum(all_dists))

def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()