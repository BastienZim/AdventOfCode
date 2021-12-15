'''
up=Down
down = up


'''
import numpy as np

check_nap = np.array([('11637517422274862853338597396444961841755517295286'.split("")),
                    ('13813736722492484783351359589446246169155735727126'),
                     ('21365113283247622439435873354154698446526571955763'),
                        ('36949315694715142671582625378269373648937148475914'),
                       ('74634171118574528222968563933317967414442817852555'),
                       ('13191281372421239248353234135946434524615754563572'),
                        ('13599124212461123532357223464346833457545794456865'),
                        ('31254216394236532741534764385264587549637569865174'),
                        ('12931385212314249632342535174345364628545647573965'),
                        ('23119445813422155692453326671356443778246755488935')])







def main():
    map = get_input(exBOOL = True)
    #print(map)
    start = (0,0)
    end = (map.shape[0]-1, map.shape[1]-1)

    #part1
#    search(start, end, map)
    #distances, parrents = Dijkstra(start, end, map)
    #print(parrents)
    #print(distances[(9,9)])
    #path = get_path(parrents,start, end)
    #print(path, distances[end])
    
    #part2
    map = replicateMap(map)
    


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
    
    update_patch = np.vectorize(lambda x: x+1 if x<9 else 0)
    
    patch = np.copy(map)
    for i in range(4):
        new_patch = update_patch(patch)
        new_map = np.hstack((new_map, new_patch))
        patch = new_patch
    print(new_map[0:3,-5:])
    print(check_nap[0])
#    print(new_map[0])
#    patch += np.ones(patch_shape, int)
    
#    print(new_map)
    #print(new_patch)
    return()


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
        neighbours = get_neighbours(node,map, map_shape)
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


#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day15/example_in.txt" 
    else: path = "./day15/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)    
    input = list(map(lambda x: list(x.replace("\n","")), input))
    return (np.array(input, dtype = int))

if __name__ == "__main__":
    main()

