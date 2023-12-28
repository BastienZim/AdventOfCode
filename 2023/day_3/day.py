import regex as re
import numpy as np

INPUT_FILE_PATH = "./input.txt"
#INPUT_FILE_PATH = "./example_in.txt"


def main():
    lines = parse_input_file()

    grid = np.array([np.array(list(x)) for x in lines])
    grid_shape = grid.shape

    part_numbers = []
    part_number_dict = []

    unique_symbols = get_unique_symbols(grid)
    # print(sorted(unique_symbols))
    numbers = find_numbers_and_pos(lines)

    for x in numbers:
        num = x["num"]
        positions = x["positions"]
        if is_part_num(positions, grid, unique_symbols):
            part_numbers.append(int(num))
            part_number_dict.append(x)

    print(f"  PART 1 Solution: {sum(part_numbers)}\n")

    all_ratios = find_gears(part_number_dict, lines)
    print(f"  PART 2 Solution: {sum(all_ratios)}\n")

    # print(aaa)


def find_gears(part_number_dict, lines):

    dict_pos_number = {}
    for x in part_number_dict:
        num = int(x["num"])
        for pos in x["positions"]:
            dict_pos_number[tuple(pos)] = x

    all_gears = []
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == "*":
                
                adj = adjacent_positions((i, j), (len(lines), len(lines[0])))
                
                ratio = 1
                unique_pos = []
                for pos in adj:
                    if(pos in dict_pos_number.keys()):
                        item = dict_pos_number[pos]
                        num = item['num']
                        p = item['positions']
                        p = (p[0],p[-1])
                        if(p not in unique_pos):
                            unique_pos.append(p)
                            ratio *= int(num)
                if(len(unique_pos)==2):
                    all_gears.append(ratio)
                elif len(unique_pos) > 2:
                    print("WHAT DO WE DO ????/")
    return all_gears


def find_numbers_and_pos(lines):
    numbers = []
    for i, l in enumerate(lines):
        num = ""
        num_positions = []
        for j, char in enumerate(l):
            if char.isdigit():
                num += char
                num_positions.append([i, j])
            else:
                if len(num) > 0:
                    numbers.append({"num": num, "positions": num_positions})
                    num = ""
                    num_positions = []

        if len(num) > 0:
            numbers.append({"num": num, "positions": num_positions})
    return numbers


def is_part_num(positions, grid, unique_symbols):
    neighbour_pos = []
    grid_shape = grid.shape
    for pos in positions:
        neighbour_pos += adjacent_positions(pos, grid_shape)
    neighbour_pos = set(neighbour_pos)
    candidates_pos = [
        x for x in set(neighbour_pos) if not x in [tuple(pos) for pos in positions]
    ]
    candidates = [grid[x] for x in candidates_pos]

    is_part_number = any([x in unique_symbols for x in set(candidates)])
    return is_part_number


def get_unique_symbols(lines):
    # set.union(*[set(list(l)) for l in lines])
    symbols_and_nums = np.unique(np.ravel(lines))
    #    unique_symbols = [x for x in symbols_and_nums if (x != "." and not x.isdigit())]
    unique_symbols = [x for x in symbols_and_nums if (x != ".")]
    return unique_symbols


def adjacent_positions(pos, grid_shape):
    neighbours_relative_pos = np.array(
        [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    )
    candidates = np.add(pos, neighbours_relative_pos)
    candidates = [tuple(x) for x in candidates if isin_grid(x, grid_shape)]
    return candidates


def adjacent_symbols(pos, grid):
    neighbours_relative_pos = np.array(
        [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    )
    candidates = np.add(pos, neighbours_relative_pos)
    grid_shape = grid.shape
    candidates = [tuple(x) for x in candidates if isin_grid(x, grid_shape)]
    candidates = [grid[x] for x in candidates]
    return candidates


def isin_grid(pos, grid_shape):
    i, j = pos[0], pos[1]
    if 0 <= i and i < grid_shape[1]:
        if 0 <= j and j < grid_shape[0]:
            return True
    return False


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.read().split("\n")
    return lines


if __name__ == "__main__":
    main()
