'''
up=Down
down = up


'''
import numpy as np
from time import time

def main():
    input = get_input(exBOOL = False)
    
    #print(input)
    graph = create_graph(input)
    print(graph)
    #t1 = time()
    #all_paths_1 = get_all_path(graph, "start", "end")
    #print("%.2f"%(time()-t1))
    t1 = time()
    #all_paths = get_all_path_opti(graph, "start", "end")
    count_all_paths = get_all_path_opti(graph, "start", "end")
    print("%.2f"%(time()-t1))
    #print("\n\n\n")
    #for x in all_paths:
    #    print(x)
#    print(all_paths)
    #print(len(np.unique(all_paths)))
    print(count_all_paths)#, len(all_paths_1))

#---------------------Class--------------------

#---------------------Funcs--------------------




def is_big_cave(cave):
    return(cave.isupper())

def separate_big_small_cave(graph):
    return([x for x in graph if is_big_cave(x)],[x for x in graph if not is_big_cave(x)])

def is_complete(path, end):
    if(len(path) < 2): return(False)
    else:
        if(path[-1] == end):
            return(True)
        else:
            return(False)

def is_complet_simplified(path):
    return(path[-1] == 'end')

def add_step(current_path, graph, small):
    new_paths = []
    #all_possible = graph[current_path[-1]]
    for x in graph[current_path[-1]]:
        to_check = current_path + [x]
        if(is_valid_advanced(to_check)):
            new_paths.append(to_check)
    #[path for x in all_possible if is_valid_advanced(current_path + [x])]) _
    return(new_paths)

def only_add_possible_steps(current_path, graph, small, small_node_count):
    
    potential_nodes = [x for x in graph[current_path[-1]]]
    small_pot = [x for x in potential_nodes if x in small]
    big_pot = [x for x in potential_nodes if x not in small_pot]
    
    
    if(2 in small_node_count.values()):
        candidates_nodes = big_pot + [x for x in small_node_count if small_node_count[x]<1 if x in small_pot] + [x for x in small_pot if x not in small_node_count]
    else:
        candidates_nodes = big_pot + [x for x in small_node_count if small_node_count[x]<2 if x in small_pot] + [x for x in small_pot if x not in small_node_count]
        
    new_paths = []
    for x in candidates_nodes:
        if(x in small_node_count):
            count_update = {k:small_node_count[k] for k in small_node_count}
            count_update[x]+=1
            new_paths.append((current_path+[x], count_update))
            #print((current_path+[x], count_update))
        elif(x in small):
            count_update = {k:small_node_count[k] for k in small_node_count}
            count_update[x] = 1
            new_paths.append((current_path+[x], count_update))
            #print(current_path+[x], count_update)
        else:
            new_paths.append((current_path+[x], small_node_count))
            #print((current_path+[x], small_node_count))
        #print("-")
    return(new_paths)
    #return([current_path + [x] for x in candidates_nodes])
    


def potential_next(current_path, graph, small):
    start_node = current_path[-1]
    potential_nodes = [x for x in graph[start_node]]
    small_pot = [x for x in potential_nodes if x in small]
    big_pot = [x for x in potential_nodes if x not in small_pot]
    small_node_count = {x: current_path.count(x) for x in small}
    if(2 in small_node_count.values()):
        return(big_pot + [x for x in small_pot if small_node_count[x]<1])
    else:
        return(big_pot + [x for x in small_pot if small_node_count[x]<2])

def is_valid_path(path): 
    for x in path:
        if(not x.isupper()):
            if(path.count(x) > 1): return(False)
    return(True)

def is_valid_advanced(path):
    allow_one = True
    for x in np.unique(path):
        if(path.count(x)>1):
            if(x == 'end'): return(False)
            elif(not x.isupper()):
                if(allow_one and path.count(x) == 2): allow_one = False
                else: return(False)
    return(True)

def get_all_path_opti(graph, start, end):
    #paths_complete = []
    #all path, with small nodes count
    all_path = [[[start],{}]]
    
    graph = remove_start(graph)
    big, small = separate_big_small_cave(graph)
    small.remove('start')
    small.remove('end')
    count = 0
    i=0
#    while(not all([is_complet_simplified(x[0]) for x in all_path])):
    while(len(all_path)>0):
        
        #all_path = [add_step(path,graph, small) for path in all_path]
        
        all_path = [only_add_possible_steps(path, graph,small, small_node_count) for (path, small_node_count) in all_path]
        all_path_new = [sub_path for path in all_path for sub_path in path]
        
        
        complete_new_paths = [path for (path, small_node_count) in all_path_new if path[-1] == 'end']
        #paths_complete = paths_complete + complete_new_paths
        count += len(complete_new_paths)
        
        all_path = [(path, small_node_count) for (path, small_node_count) in all_path_new if path[-1] != 'end']
        
        
        #print(complete_new_paths)
        #print("---", [x[0] for x in all_path])
        i+=1
        if(i>20):
            break        
        #print("\n")
    print()
    return(count)



def get_all_path(graph, start, end):
    paths_complete = []
    all_path = [[start]]
    
    graph = remove_start(graph)
    big, small = separate_big_small_cave(graph)
    small.remove('start')
    small.remove('end')
    while(not all([is_complet_simplified(x) for x in all_path])):
        
        all_path = [add_step(path,graph, small) for path in all_path]
        #all_path = [only_add_possible_steps(path,graph, small) for path in all_path]
        all_path_new = [sub_path for path in all_path for sub_path in path]
        
        complete_new_paths = [path for path in all_path_new if is_complet_simplified(path)]
        paths_complete = paths_complete + complete_new_paths
        all_path = [x for x in all_path_new if x not in complete_new_paths]
    return(paths_complete)


def remove_start(graph):
    for x in graph:
        if(x != 'start' and 'start' in graph[x]):
            graph[x].remove('start')
    return(graph)

def create_graph(description):
    graph = {x: "" for x in np.unique(description)}
    for (a,b) in description:
        graph[a] += b+","
        graph[b] += a+","
    #clean graph 
    for x in graph:
        graph[x] = graph[x].split(",")[:-1]
    return(graph)

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day12/example_in.txt" 
    else: path = "./day12/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)
    input = list(map(lambda x: x.replace("\n","").split('-'), input))
    #print(input)
    #print(np.array(input))
    return (input)


if __name__ == "__main__":
    main()

