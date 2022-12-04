'''
@author: BastienZim







'''

def main():
    with open("./input.txt") as f:
        input = f.readlines()
    input = sanitize_input(input)
    inc = has_increased(input, verbose = False)
    #print(inc)
    counter = count_inc(input)
    print(counter, sum(inc[1:]))

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return list(map(lambda x: int(x.replace("\n","")), input))

def has_increased(measures, verbose = False):
    previous=measures[0]
    if verbose:
        print(previous, "N/A")
        for i,current in enumerate(measures[1:]):
            print(previous, current, previous>current)
            previous = current

    else:
        previous = measures[:-1]
        current = measures[1:]
        inc = ['N/A']+[x>y for x,y in zip(current, previous)]
        return inc


def count_inc(measures):

    counter = 0
    previous = measures[0]
    for current in measures[1:]:
        if(current > previous): counter+=1
        previous = current

    return counter


if __name__ == "__main__":
    main()

