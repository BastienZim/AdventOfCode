'''
Code by Bastien Zimmermann - @ BastienZim on github
'''
import numpy as np

def main():
    input = get_input(exBOOL = True)
    print(input)
    draw_target(input)
    #initial position
    x,y = 0,0



    


#---------------------Funcs--------------------
def update_probe_pos(x,y, x_v, y_v):
    #add speed
    new_x, new_y = x+x_v, y+y_v
    #add drag
    if(x_v>1): x_v -= 1
    elif(x_v<-1): x_v += 1
    #add gravity
    if(y_v>1): y_v -= 1
    #elif(y_v<-1): y_v += 1

    return(new_x, new_y)

def draw_target(input):

    xmin, xmax = input[0]
    ymin, ymax = input[1]
    print(xmin, xmax, ymin, ymax)
    max_x = max(abs(xmin), abs(xmax))
    max_y = max(abs(ymin), abs(ymax))
    shape = (max_x, max_y)
    grid = np.array(["." for i in range((max_x+1)*(max_y+1))]).reshape((max_x+1, max_y+1))
    print(shape)
#    grid[xmin : xmax+1, ymin : ymax+1] = "#"
    grid[xmin : xmax+1, min(abs(ymin), abs(ymax)) : max(abs(ymin), abs(ymax))+1] = "#"
    grid[0,0] = "S"
    
    show_map(grid)
    print("/\\//\/\\//\/\/\/\/\/\\//\/\/\/\/\/\\//\/\/\/\/\\")
    grid = add_padding(grid)
    print("/\\//\/\\//\/\/\/\/\/\\//\/\/\/\/\/\\//\/\/\/\/\\")
    show_map(grid)


def add_padding(grid, shot_list=[(33,-5)]):
    xs = [x[0] for x in shot_list]
    ys = [x[1] for x in shot_list]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys) 
    if(xmin < 0):
        pading = np.array(["." for i in range((abs(xmin))*(grid.shape[1]))]).reshape((abs(xmin), grid.shape[1])) 
        grid = np.vstack((pading, grid))
    if(xmax > grid.shape[0]):
        pading = np.array(["." for i in range((abs(xmax)-grid.shape[0]+1)*(grid.shape[1]))]).reshape((abs(xmax)-grid.shape[0]+1, grid.shape[1])) 
        grid = np.vstack((grid, pading))
    if(ymin < -grid.shape[1]):
        pading = np.array(["." for i in range((abs(ymin)-grid.shape[1])*(grid.shape[0]))]).reshape((grid.shape[0], abs(ymin)-grid.shape[1])) 
        show_map(pading)
        print(pading.shape, grid.shape)
        grid = np.hstack((grid, pading))
    if(ymax > 0):
        pading = np.array(["." for i in range((abs(ymax))*(grid.shape[0]))]).reshape((grid.shape[0], abs(ymax))) 
        grid = np.hstack((pading, grid))
    return(grid)

def draw_shots(grid, shot_list=[(33,-5)]):
    grid = add_padding(grid, shot_list)

def show_map(grid):
    for x in grid.T:
        print("".join(x))
    

def dots_to_grid(dots):
    min_x = min([x[0] for x in dots])
    max_x = max([x[0] for x in dots])
    min_y = min([x[1] for x in dots])
    max_y = max([x[1] for x in dots])
    grid = np.zeros(shape=(max_x+1, max_y+1), dtype = int)
    grid = np.array(["." for i in range((max_x+1)*(max_y+1))]).reshape((max_x+1, max_y+1))
    #print(grid)
    for d in dots:
        grid[d[0],d[1]] = "#"
    return(grid) 


#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day17/example_in.txt" 
    else: path = "./day17/input.txt" 

    with open(path) as f:
        input = f.readlines()
    xs, ys = input[0].split(": ")[1].split(", ")
    
    input = [xs[2:].split(".."),ys[2:].split("..")]
    input = [[int(x) for x in input[0]], [int(x) for x in input[1]]]
    return (input)


if __name__ == "__main__":
    main()

