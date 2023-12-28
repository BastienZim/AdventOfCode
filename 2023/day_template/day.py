import regex as re

INPUT_FILE_PATH = './input.txt'
INPUT_FILE_PATH = './example_in.txt'

def main():
    lines = parse_input_file()
    print(sum(calibration_values))



def parse_input_file():
    with open(INPUT_FILE_PATH, 'r') as f:
        lines = f.read().split("\n")
    return lines

if __name__ == "__main__":
    main()