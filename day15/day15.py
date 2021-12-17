'''
up=Down
down = up


'''
import numpy as np
from time import time
from collections import deque
import heapq






def main():
    map = get_input(exBOOL = False)
    #print(map)

    #part1
#    search(start, end, map)
    #distances, parrents = Dijkstra(start, end, map)
    #print(parrents)
    #print(distances[(9,9)])
    #path = get_path(parrents,start, end)
    #print(path, distances[end])
    
    #part2
    map = replicateMap(map)
    start = (0,0)
    end = (map.shape[0]-1, map.shape[1]-1)
    t1 = time()
    distances, parrents = Dijkstra_queue(start, map)
#    #distances, parrents = Dijkstra(start, end, map)
    print("Dijkstra QQQQ time : %.4f s "%(time()-t1))
    path = get_path(parrents, start, end)
    #print(path, distances[end])
    print(distances[end])


    




"""
    print(map[start])
    point = start
    neighs = get_neighbours(point, map, map_shape)
    print(neighs)
    greedy = greedy_iteration(point, map, map_shape)
    print(greedy)
"""

#---------------------Funcs--------------------

def replicateMap(map):
    new_map = np.copy(map)
    patch_shape = map.shape
    
    update_patch = np.vectorize(lambda x: x+1 if x<9 else 1)
    
    patch = np.copy(map)
    for i in range(4):
        new_patch = update_patch(patch)
        new_map = np.hstack((new_map, new_patch))
        patch = new_patch
    
    patch = np.copy(new_map)
    for j in range(4):
        new_patch = update_patch(patch)
        new_map = np.vstack((new_map, new_patch))
        patch = new_patch
    #print(new_map[:,-5:])
#    print(new_map[0])
#    patch += np.ones(patch_shape, int)
    
#    print(new_map)
    #print(new_patch)
    return(new_map)


#---------------------Part1--------------------

def isinGrid(point, grid_shape):
    return(0<= point[0] <grid_shape[0] and 0<= point[1] <grid_shape[1])

def get_neighbours(point,  grid, map_shape):
    return(list(filter(lambda x: isinGrid(x, map_shape),
        [tuple(map(sum,zip(point,transi))) for transi in [(-1,0),(0,-1),(1,0),(0,1)]])))

def get_path(parrents,start, end):
    node = end
    path = [end]
    while(node!=start):
        new = parrents[node]
        path.append(new)
        node = new
    path.reverse()
    return(path)

def Dijkstra(start, end, map):
    map_shape = map.shape
    nodes = [(i,j) for i in range(0,map_shape[0]) for j in range(0,map_shape[1])]
    unvisited = {node: None for node in nodes}
    parrents = {}
    distances = {}
    node = start
    current_distance = 0
    while(True):
        neighbours = get_neighbours(node, map, map_shape)
        #for dist neighbor in neighbours
        for dist, n in zip([map[x] for x in neighbours], neighbours):
            if(n not in unvisited): continue
            new_Distance = dist + current_distance
            if(unvisited[n] is None or new_Distance < unvisited[n]):
                unvisited[n] = new_Distance
                parrents[n] = node
            
        distances[node] = current_distance
        del unvisited[node]
        if not unvisited:break
        candidates = [node for node in unvisited.items() if node[1]]
        node, current_distance = sorted(candidates, key= lambda x: x[1])[0]
    
    
    return(distances, parrents)


def Dijkstra_queue(start, map):
    
    map_shape = map.shape
    nodes = [(i,j) for i in range(0,map_shape[0]) for j in range(0,map_shape[1])]
    distances = {}
    parrents = {}
    queue = []
    distances[start] = 0
    for n in nodes: 
        if n != start :
            distances[n] = np.inf
            parrents[n] = None
        heapq.heappush(queue, (n, distances[n]))
    
    while (len(queue)>0):
        current_node, distan = heapq.heappop(queue)
        neighbours = get_neighbours(current_node, map, map_shape)
        
        for dist, n in zip([map[x] for x in neighbours], neighbours):
            current_distance = distances[current_node] + dist
            if current_distance < distances[n]:
                distances[n] = current_distance
                parrents[n] = current_node
                #problem no update priority in heapq.... only O(n)
                #queue.decrease_priority((n, current_distance))
                heapq.heappush(queue,(n, current_distance))
                
    
    return(distances, parrents)


#-------------INPUT--------------------------
def get_input(exBOOL = False, path=None):
    if(path == None):
        if(exBOOL): path = "./day15/example_in.txt" 
        else: path = "./day15/input.txt" 
    

    with open(path) as f:
        input = f.readlines()
    #print(input)    
    input = list(map(lambda x: list(x.replace("\n","")), input))
    return (np.array(input, dtype = int))

if __name__ == "__main__":
    main()

