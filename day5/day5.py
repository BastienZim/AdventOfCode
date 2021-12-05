'''
up=Down
down = up


'''
import numpy as np


def add_vector(grid, vect):
    return()

def vector_to_points(vect):
    #print(vect)
    start = vect[0]
    end = vect[1]
    if(start[0]==end[0]):
        points_drawn = [(start[0], x) for x in range(min(start[1], end[1]), max(start[1], end[1])+1)]
    elif(start[1]==end[1]):
        points_drawn = [(x, start[1]) for x in range(min(start[0], end[0]), max(start[0], end[0])+1)]
    else:
        up = False #boolean for diag up or diag down
        if(start[0]<end[0]): l_point, r_point = start, end
        else: l_point, r_point = end, start
        if(l_point[1]<r_point[1]): up = True
        if(up): 
            points_drawn = [((l_point[0]+i),(l_point[1]+i)) for i in range(r_point[1]-l_point[1]+1)]
        else: 
            points_drawn = [((l_point[0]+i),(l_point[1]-i)) for i in range(l_point[1]-r_point[1]+1)]
        
    return(points_drawn)


def dangerous_points(grid):
    
    count = 0
    for row in grid:
        for elt in row:
            if(elt >= 2):
                count+=1
#    for x in range(np.shape(grid)[0]+1):
#        for y in range(np.shape(grid)[0]+1):
#            if(grid[x,y] >= 2):
#                count+=1
    return(count)
    


def create_grid(vectors):
    
    points=[vector_to_points(vect) for vect in vectors]
    points=list(filter(lambda x : len(x)>1, points))
    
    all_points = []
    for sub_points in points:
        for x in sub_points:
            all_points.append(x)

    x_min, x_max = min([x[0] for x in all_points]), max([x[0] for x in all_points])
    y_min, y_max = min([x[1] for x in all_points]), max([x[1] for x in all_points])
    
    #print(x_min, x_max, y_min, y_max)
    
    grid = np.array([[0 for x in range(0, x_max+1)] for y in range(0, y_max+1)]).T
    
    for point in all_points:    
        grid[point[0]][point[1]] += 1 
    
    return(grid)



def main():
    input = get_input(True)
    
    grid = create_grid(input)
    print(grid)
    print(dangerous_points(grid))

       
    
    


def get_input(exBOOL = False):
    if(exBOOL): path = "./day5/example_in.txt" 
    else: path = "./day5/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)
    input = list(map(lambda x: x.replace("\n","").split(" -> "), input))
    input = list(map(lambda x: (x[0].split(","), x[1].split(",")), input))
    input = list(map(lambda a: ([int(x) for x in a[0]],[int(x) for x in a[1]]), input))
#    print(input)

    return (input)


if __name__ == "__main__":
    main()

