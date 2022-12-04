'''
up=Down
down = up


'''

import numpy as np


def main():
    input, rules = get_input(exBOOL=False)
    template = str(input)
    new_rules = translate_rules(rules)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = init_count_letters(template, letters)
    print(template)
    pairs = count_pairs(new_rules, template)
    #print(pairs)

    #print_count_letters(count_letter(pairs, input))
    print("----------------------------BEGIN CHECK----------------------------")
    for i in range(40):
        #template_to_pairs(template)
        pairs = update_pair_count(pairs, new_rules)
        #template = insert_rule(template, rules)
        #print(template)
        #print_count_letters(count_letter(pairs, input))
        
    #print(template)
    #print("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")
    #print(count_pairs(new_rules, template))
        #`print("count method ", pairs)
    #print(pairs)
    #print(count)
    count = count_letter(pairs, input)
    #print_count_letters(count)
    print(score_2(count))

    #print(template)
    #count_temp = count_letter(count_pairs(new_rules, template), input)
    #print_count_letters(count_temp)
    #print(score_2(count_temp))

    

# ---------------------Funcs--------------------
def count_letter(pairs, input):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count_let = [0 for l in letters]
    for pair, count in pairs.items():
        count_let[letters.index(pair[1])] += count
    count_let[letters.index(input[0])] += 1
    #count_let[letters.index("B")] += 1
    #print(count_let)
    return(count_let)

def update_pair_count(count_pairs, new_rules):
    for pair, count in list(count_pairs.items()):
        if(count > 0):
            #print(pair, count)
            #print("%s -%d ; %s +%d %s +%d"%( pair, count, new_rules[pair][0], count, new_rules[pair][1], count))
            count_pairs[pair] -= count
            for p in new_rules[pair]:
                count_pairs[p] += count
    return(count_pairs)


def template_to_pairs(template):
    print(template)
    pairs = [template[i:i+2] for i in range(0, len(template)-1)]
    print(pairs)

    return(pairs)


def init_count_letters(template, letters):
    count = [0 for x in letters]  # [0 for x in letters_short]
    for x in template:
        if(x in letters):
            count[letters.index(x)] += 1
    return(count)


def print_count_letters(count):
    n = len(str(max(count)))
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print([l+" "*(n)  for l, count in zip(letters, count)])
    print([str(count)+" "*((n+1)-len(str(count))) for l, count in zip(letters, count)])
    

def count_pairs(new_rules, template):
    count = {pair: 0 for pair, _ in new_rules.items()}
    pairs = [template[i:i+2] for i in range(0, len(template)-1)]
    for pair in pairs:
        count[pair]+=1
    return(count)

# ------------------------------------------------------


def score(template):
    count = [(x, template.count(x)) for x in np.unique([x for x in template])]
    sorted_count = sorted(count, key=lambda x: x[1])
    return(sorted_count[-1][1]-sorted_count[0][1])


def score_2(count):
    count = list(filter(lambda x: x > 0, count))
    return(max(count)-min(count))


def get_index_B_H(rules):
    B_indexes = [i for i, x in enumerate(rules) if x[1] == "B"]
    H_indexes = [i for i, x in enumerate(rules) if x[1] == "H"]
    return(B_indexes, H_indexes)


def translate_rules(rules):
    return({pattern: (pattern[0]+letter, letter+pattern[1]) for pattern, letter in rules})
    

def insert_and_count(template, count, rules, to_check, letters):
    new_template = template[0]
    #to_check = [x[0] for x in rules]
    for i in range(len(template)-1):
        chunk = template[i:i+2]
        if(chunk in to_check):
            new_letter = rules[to_check.index(chunk)][1]
            new_chunk = new_letter+chunk[1]
            if(new_letter in letters):
                count[letters.index(new_letter)] += 1
            new_template += new_chunk
        else:
            new_template += chunk
    return(new_template, count)


def insert_rule(template, rules):
    new_template = template[0]
    to_check = [x[0] for x in rules]
    for i in range(len(template)-1):
        chunk = template[i:i+2]
        # print("chunk",chunk)
        # print(chunk)
        if(chunk in to_check):
            new_letter = rules[to_check.index(chunk)][1]
            # print(new_letter)
            new_chunk = new_letter+chunk[1]
            #print("   ",new_chunk)
            new_template += new_chunk
        else:
            new_template += chunk
        # print(new_template)
    return(new_template)


# -------------INPUT--------------------------
def get_input(exBOOL=False):
    if(exBOOL):
        path = "./day14/example_in.txt"
    else:
        path = "./day14/input.txt"

    with open(path) as f:
        input = f.readlines()
    # print(input)
    input = list(map(lambda x: x.replace("\n", ""), input))
    template = input[0]

    rules = [x.split(" -> ") for x in input[2:]]

    return(template, rules)


if __name__ == "__main__":
    main()
