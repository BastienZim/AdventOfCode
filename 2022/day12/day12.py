'''
@author: BastienZim

'''

import os
import numpy as np


#path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
path = "/home/bastien/Documents/AdventOfCode/2022"


example = False


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
    current_alphabet = "".join(list(filter(lambda x: x in input, list(alphabet))))
    #print("AA",current_alphabet)
    #print("","".join(list(np.unique(input))))
    
    #print(input)
    #input = np.array(input)
    
    S =np.ravel(np.where(input =='S'))
    E = np.ravel(np.where(input =='E'))
    
    for x in input:
        print("".join(x))
    print(f"E: {E}, - S: {S}")
    print("BEGIN")

    best_path(input, S, E,  current_alphabet)








def a_star(graph, heuristic, start, goal):
    """
    Finds the shortest distance between two nodes using the A-star (A*) algorithm
    :param graph: an adjacency-matrix-representation of the graph where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: an estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance
    :param start: the node to start from.
    :param goal: the node we're searching for
    :return: The shortest distance to the goal node. Can be easily modified to return the path.
    """

    # This contains the distances from the start node to all other nodes, initialized with a distance of "Infinity"
    distances = [float("inf")] * len(graph)

    # The distance from the start node to itself is of course 0
    distances[start] = 0

    # This contains the priorities with which to visit the nodes, calculated using the heuristic.
    priorities = [float("inf")] * len(graph)

    # start node has a priority equal to straight line distance to goal. It will be the first to be expanded.
    priorities[start] = heuristic[start][goal]

    # This contains whether a node was already visited
    visited = [False] * len(graph)

    # While there are nodes left to visit...
    while True:
        # ... find the node with the currently lowest priority...
        lowest_priority = float("inf")
        lowest_priority_index = -1
        for i in range(len(priorities)):
            # ... by going through all nodes that haven't been visited yet
            if priorities[i] < lowest_priority and not visited[i]:
                lowest_priority = priorities[i]
                lowest_priority_index = i

        if lowest_priority_index == -1:
            # There was no node not yet visited --> Node not found
            return -1

        elif lowest_priority_index == goal:
            # Goal node found
            # print("Goal node found!")
            return distances[lowest_priority_index]

        # print("Visiting node " + lowestPriorityIndex + " with currently lowest priority of " + lowestPriority)

        # ...then, for all neighboring nodes that haven't been visited yet....
        for i in range(len(graph[lowest_priority_index])):
            if graph[lowest_priority_index][i] != 0 and not visited[i]:
                # ...if the path over this edge is shorter...
                if distances[lowest_priority_index] + graph[lowest_priority_index][i] < distances[i]:
                    # ...save this path as new shortest path
                    distances[i] = distances[lowest_priority_index] + graph[lowest_priority_index][i]
                    # ...and set the priority with which we should continue with this node
                    priorities[i] = distances[i] + heuristic[i][goal]
                    # print("Updating distance of node " + i + " to " + distances[i] + " and priority to " + priorities[i])

                # Lastly, note that we are finished with this node.
                visited[lowest_priority_index] = True
                # print("Visited nodes: " + visited)
                # print("Currently lowest distances: " + distances)













def best_path(input, S, E, current_alphabet):
    unexplored_in = input.copy()
    last_choice = []
    i,j = S
    current_letter="a"
    current_path = []
    last_options = np.zeros(input.shape)
    while(current_letter!="E"):
        
        candidates = get_all_accessible_neigh(i,j, unexplored_in, current_letter, current_alphabet)
        if(len(candidates)>1):
            current_option = last_options[i,j]
            if(current_option<len(candidates)):
                last_options[i,j] = current_option+1
                last_choice.append((i,j, unexplored_in, current_path, current_letter))
                #chosen_one = candidates[int(current_option)]
            else:
                i,j, unexplored_in, current_path, current_letter= last_choice.pop()
        #elif(len(candidates)==1):
        #    print(current_option, )
            #chosen_one = candidates[int(last_options[i,j])]
        elif(len(candidates)==0):#backtrack to the last intersection
            print(unexplored_in)
            for x in unexplored_in:
                print("".join(x))
            i,j, unexplored_in, current_path, current_letter= last_choice.pop()
            continue
        chosen_one = candidates[int(last_options[i,j])]
        unexplored_in[i,j] = "#"
        i,j = chosen_one[0], chosen_one[1]
        current_path.append([i,j])
        current_letter = unexplored_in[i,j]
    print(current_path)
    print((len(current_path)))
    last_x = [0,0]
    for x in current_path:
        if(last_x[0] != x[0] and last_x[1]!= x[1]):
            print(x, last_x)
            print("ASL:DJHASDJLKLJKSADJLKADSJLKADJLSK")
        last_x = x
    return



def greedy_path(input, S, E, current_alphabet):
    unexplored_in = input.copy()
    i,j = S
    current_letter="a"
    current_path = []
    while(current_letter!="E"):
        
        candidates = get_higher_accessible_neigh(i,j, unexplored_in, current_letter, current_alphabet)
        chosen_one = candidates[0]
        unexplored_in[i,j] = "#"
        i,j = chosen_one[0], chosen_one[1]
        current_path.append([i,j])
        current_letter = unexplored_in[i,j]
    print(current_path)
    print((len(current_path)))
    return


def get_all_accessible_neigh(i,j, input, current_letter, current_alphabet):
    current_hight = get_hight(current_letter, current_alphabet)
    candidates = [np.add([i, j], x) for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0<=x[0]<input.shape[0], candidates)
    candidates = list(filter(lambda x: 0<=x[1]<input.shape[1], candidates))
    candidates = list(map(lambda x: (x[0],x[1], get_hight(input[x[0],x[1]], current_alphabet)), candidates))
    candidates = list(filter(lambda x: x[2]==current_hight or x[2]==(current_hight+1), candidates))
    candidates = list(map(lambda x: (x[0],x[1]), candidates))
    return(candidates)

def get_higher_accessible_neigh(i,j, input, current_letter, current_alphabet):
    
    current_hight = get_hight(current_letter, current_alphabet)
    candidates = [np.add([i, j], x) for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0<=x[0]<input.shape[0], candidates)
    candidates = list(filter(lambda x: 0<=x[1]<input.shape[1], candidates))
    candidates = list(map(lambda x: (x[0],x[1], get_hight(input[x[0],x[1]], current_alphabet)), candidates))
    
    heights = [x[2] for x in candidates]
    
    candidates = list(filter(lambda x: x[2]==current_hight or x[2]==(current_hight+1), candidates))
    #if(i==4 and j==2): print("AMSD",current_letter,  candidates)
    #candidates = list(filter(lambda x: x[2] in [current_hight, current_hight+1], candidates))
    #max(lis,key=lambda item:item[1])

    max_height = max([x[2] for x in candidates])
    candidates = filter(lambda x: x[2] == max_height, candidates)
    candidates = list(map(lambda x: (x[0],x[1]), candidates))
    return(candidates)

def get_neighbours(i,j, input):
    candidates = [np.add([i, j], x) for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
    candidates = filter(lambda x: 0<=x[0]<=input.shape[0], candidates)
    candidates = filter(lambda x: 0<=x[1]<=input.shape[1], candidates)
    candidates = list(map(lambda x: (x[0],x[1], input[x[0],x[1]]), candidates))
    return(candidates)


def get_hight(letter, current_alphabet):
    if(letter == "#"): return(99)
    if letter=="S": letter="a"
    if letter=="E": letter="z"
    
    return(current_alphabet.index(letter))

def can_climb(letter_1, letter_2):
    print(letter_1,letter_2)
    if(letter_2 == "#" or letter_1 == "#"): return(False)
    if letter_1=="S": letter_1="a"
    if letter_2=="S": letter_2="a"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return(alphabet.index(letter_1) == alphabet.index(letter_2) or
           alphabet.index(letter_1) == alphabet.index(letter_2)+1)

def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    return np.array(list(map(lambda x: list(x.replace("\n","")), input)))




if __name__ == "__main__":
    main()

