'''
up=Down
down = up


'''
import numpy as np

def main():
    dots, folds = get_input(exBOOL = False)
    
    #print(dots)
    grid = dots_to_grid(dots)
    print(folds)
    for fold in folds:
        grid = fold_grid(grid, fold)
        
        #print(grid)
        print(count_dots(grid))
    #print(grid.T)
    for x in grid.T:
        print("".join(x))
    

#---------------------Funcs--------------------
def count_dots(grid):
    return(sum([list(x).count("#") for x in grid]))

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

def fold_grid(grid, fold):
    
    axis = ['x','y'].index(fold[0])
    k = int(fold[1])
    #print(grid)
    if axis == 0:
        grid[k,:] = "_"
        for col in range(grid.shape[1]):
            for row in range(k+1, grid.shape[0]):
                if(grid[row,col]=="#"):
                    #print(row, col, row, grid.shape[1]-col-1)
                    grid[grid.shape[0]-row-1, col] = "#"
        grid = grid[:k,:]
    else:
        grid[:,k] = "|"
        for col in range(k+1, grid.shape[1]):
            for row in range(grid.shape[0]):
                if(grid[row,col]=="#"):
                    #print(row, col, row, grid.shape[1]-col-1)
                    grid[row,grid.shape[1]-col-1] = "#"
        grid = grid[:,:k]
    #print(grid)
    return(grid)

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day13/example_in.txt" 
    else: path = "./day13/input.txt" 

    with open(path) as f:
        input = f.readlines()
    input = list(map(lambda x: x.replace("\n",""), input))

    dots = [[int(x) for x in x.split(",")] for x in input if "," in x]
    
    folds = [x[(x.index("=")-1):].split("=") for x in input if "fold" in x]
    #print(dots)
    #print(folds)
    
    return ((dots, folds))


if __name__ == "__main__":
    main()

