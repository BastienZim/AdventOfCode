'''
@author: BastienZim

'''

import os
import numpy as np

import heapq


path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


example = True


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    input = sanitize_input(input)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    current_alphabet = "".join(
        list(filter(lambda x: x in input, list(alphabet))))
    # print("AA",current_alphabet)
    # print("","".join(list(np.unique(input))))

    # print(input)
    #input = np.array(input)

    S = np.ravel(np.where(input == 'S'))
    E = np.ravel(np.where(input == 'E'))
    start = (S[0], S[1])
    end = (E[0], E[1])
    for x in input:
        print("".join(x))
    print(f"E: {E}, - S: {S}")
    print(f"start: {start}, - end: {end}")
    print("BEGIN")
    #best_path(input, S, E,  current_alphabet)
    distances, parents = adapt_Dijkstra(start, input, current_alphabet)
    print(len(parents))
    #for x in parents:
        #print(x)

def adapt_Dijkstra(start, map, current_alphabet):
    map_shape = map.shape
    nodes = [(i, j) for i in range(0, map_shape[0])
             for j in range(0, map_shape[1])]
    distances = {}
    parents = {}
    queue = []
    distances[start] = 0
    for n in nodes:
        if n != start:
            distances[n] = np.inf
            parents[n] = None
        heapq.heappush(queue, (n, distances[n]))

    while (len(queue) > 0):
        current_node, _ = heapq.heappop(queue)
        #print(map[current_node])
        neighbours = get_all_accessible_neigh(
            current_node, map, current_alphabet)
        heights = [get_hight(map[x], current_alphabet) for x in neighbours]
        dist = [1 if x==max(heights) else 22 for x in heights]
        for dist, n in zip(dist, neighbours):
            current_distance = distances[current_node] + dist
            if current_distance < distances[n]:
                distances[n] = current_distance
                parents[n] = current_node
                # problem no update priority in heapq.... only O(n)
                #queue.decrease_priority((n, current_distance))
                heapq.heappush(queue, (n, current_distance))

    return(distances, parents)


def Dijkstra_queue(start, map):

    map_shape = map.shape
    nodes = [(i, j) for i in range(0, map_shape[0])
             for j in range(0, map_shape[1])]
    distances = {}
    parrents = {}
    queue = []
    distances[start] = 0
    for n in nodes:
        if n != start:
            distances[n] = np.inf
            parrents[n] = None
        heapq.heappush(queue, (n, distances[n]))

    while (len(queue) > 0):
        current_node, _ = heapq.heappop(queue)
        neighbours = get_neighbours(current_node, map, map_shape)

        for dist, n in zip([map[x] for x in neighbours], neighbours):
            current_distance = distances[current_node] + dist
            if current_distance < distances[n]:
                distances[n] = current_distance
                parrents[n] = current_node
                # problem no update priority in heapq.... only O(n)
                #queue.decrease_priority((n, current_distance))
                heapq.heappush(queue, (n, current_distance))

    return(distances, parrents)


def get_all_accessible_neigh(current_node, input, current_alphabet):
    current_letter = input[current_node]
    current_hight = get_hight(current_letter, current_alphabet)
    candidates = [np.add(list(current_node), x)
                  for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0 <= x[0] < input.shape[0], candidates)
    candidates = list(filter(lambda x: 0 <= x[1] < input.shape[1], candidates))
    candidates = list(map(lambda x: (x[0], x[1], get_hight(
        input[x[0], x[1]], current_alphabet)), candidates))
    candidates = list(filter(
        lambda x: x[2] == current_hight or x[2] == (current_hight+1), candidates))
    candidates = list(map(lambda x: (x[0], x[1]), candidates))
    return(candidates)


def best_path(input, S, E, current_alphabet):
    unexplored_in = input.copy()
    last_choice = []
    i, j = S
    current_letter = "a"
    current_path = []
    last_options = np.zeros(input.shape)
    while(current_letter != "E"):

        candidates = get_all_accessible_neigh(
            i, j, unexplored_in, current_letter, current_alphabet)
        if(len(candidates) > 1):
            current_option = last_options[i, j]
            if(current_option < len(candidates)):
                last_options[i, j] = current_option+1
                last_choice.append(
                    (i, j, unexplored_in, current_path, current_letter))
                #chosen_one = candidates[int(current_option)]
            else:
                i, j, unexplored_in, current_path, current_letter = last_choice.pop()
        # elif(len(candidates)==1):
        #    print(current_option, )
            #chosen_one = candidates[int(last_options[i,j])]
        elif(len(candidates) == 0):  # backtrack to the last intersection
            print(unexplored_in)
            for x in unexplored_in:
                print("".join(x))
            i, j, unexplored_in, current_path, current_letter = last_choice.pop()
            continue
        chosen_one = candidates[int(last_options[i, j])]
        unexplored_in[i, j] = "#"
        i, j = chosen_one[0], chosen_one[1]
        current_path.append([i, j])
        current_letter = unexplored_in[i, j]
    print(current_path)
    print((len(current_path)))
    last_x = [0, 0]
    for x in current_path:
        if(last_x[0] != x[0] and last_x[1] != x[1]):
            print(x, last_x)
            print("ASL:DJHASDJLKLJKSADJLKADSJLKADJLSK")
        last_x = x
    return


def greedy_path(input, S, E, current_alphabet):
    unexplored_in = input.copy()
    i, j = S
    current_letter = "a"
    current_path = []
    while(current_letter != "E"):

        candidates = get_higher_accessible_neigh(
            i, j, unexplored_in, current_letter, current_alphabet)
        chosen_one = candidates[0]
        unexplored_in[i, j] = "#"
        i, j = chosen_one[0], chosen_one[1]
        current_path.append([i, j])
        current_letter = unexplored_in[i, j]
    print(current_path)
    print((len(current_path)))
    return


def get_higher_accessible_neigh(i, j, input, current_letter, current_alphabet):

    current_hight = get_hight(current_letter, current_alphabet)
    candidates = [np.add([i, j], x)
                  for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0 <= x[0] < input.shape[0], candidates)
    candidates = list(filter(lambda x: 0 <= x[1] < input.shape[1], candidates))
    candidates = list(map(lambda x: (x[0], x[1], get_hight(
        input[x[0], x[1]], current_alphabet)), candidates))

    heights = [x[2] for x in candidates]

    candidates = list(filter(
        lambda x: x[2] == current_hight or x[2] == (current_hight+1), candidates))
    #if(i==4 and j==2): print("AMSD",current_letter,  candidates)
    #candidates = list(filter(lambda x: x[2] in [current_hight, current_hight+1], candidates))
    #max(lis,key=lambda item:item[1])

    max_height = max([x[2] for x in candidates])
    candidates = filter(lambda x: x[2] == max_height, candidates)
    candidates = list(map(lambda x: (x[0], x[1]), candidates))
    return(candidates)


def get_neighbours(i, j, input):
    candidates = [np.add([i, j], x)
                  for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0 <= x[0] <= input.shape[0], candidates)
    candidates = filter(lambda x: 0 <= x[1] <= input.shape[1], candidates)
    candidates = list(
        map(lambda x: (x[0], x[1], input[x[0], x[1]]), candidates))
    return(candidates)


def get_hight(letter, current_alphabet):
    if(letter == "#"):
        return(99)
    if letter == "S":
        letter = "a"
    if letter == "E":
        letter = "z"

    return(current_alphabet.index(letter))


def can_climb(letter_1, letter_2):
    print(letter_1, letter_2)
    if(letter_2 == "#" or letter_1 == "#"):
        return(False)
    if letter_1 == "S":
        letter_1 = "a"
    if letter_2 == "S":
        letter_2 = "a"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return(alphabet.index(letter_1) == alphabet.index(letter_2) or
           alphabet.index(letter_1) == alphabet.index(letter_2)+1)


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return np.array(list(map(lambda x: list(x.replace("\n", "")), input)))


if __name__ == "__main__":
    main()
