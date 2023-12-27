import regex as re

INPUT_FILE_PATH = "./input.txt"
# INPUT_FILE_PATH = './example_in.txt'

def main():
    possible_games = []
    all_powers = []
    requirements = {"red": 12, "green": 13, "blue": 14}
    lines = parse_input_file()
    for l in lines:
        max_cubes = {}
        #        game_num = l.split("Game ")[1].split(":")[0]
        game_num = l[5:].split(":")[0]
        cubes = "".join(l[5:].split(":")[1:]).replace(";", ",").split(",")
        cubes = [x[1:] for x in cubes]
        cubes = [x.split(" ") for x in cubes]
        cubes = [[int(x[0]), x[1]] for x in cubes]

        for c in cubes:
            if c[1] in max_cubes.keys():
                if max_cubes[c[1]] < c[0]:
                    max_cubes[c[1]] = c[0]
            else:
                max_cubes[c[1]] = c[0]
        power = 1
        for v in max_cubes.values():
            power *= v
        all_powers.append(power)
        if all([k in max_cubes.keys() for k in requirements.keys()]):
            if all([max_cubes[k] <= v for k, v in requirements.items()]):
                possible_games.append(game_num)
    print("PART 1", sum([int(x) for x in possible_games]))
    print("PART 2", sum(all_powers))


#    print(lines)


def parse_input_file():
    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.read().split("\n")
    return lines


if __name__ == "__main__":
    main()
