'''
up=Down
down = up


'''
import numpy as np


def main():
    grid = get_input(exBOOL = False)
    
    #print(grid)

    #grid = np.zeros((10,10))
    flash_count = 0
    n_steps = 2000
    for i in range(n_steps):
        grid, have_flashed = update_energy(grid)
        flash_count+=len(have_flashed)
        if(all_flash(grid)):
            #print("step %d:\n flash count: %d\n"%((i+1), flash_count), grid)
            break
        #print("step %d:\n flash count: %d\n"%((i+1), flash_count))#, grid)
    """
    for i in range(n_steps, n_steps+5):
        grid, have_flashed = update_energy(grid)
        flash_count+=len(have_flashed)
        
        print("step %d:\n flash count: %d\n"%((i+1), flash_count), grid)
    
   """
    print("step %d:\n flash count: %d\n\n"%((i+1), flash_count), grid)
    



#---------------------Funcs--------------------
def all_flash(grid):
    return(len(np.unique(grid))==1 and grid[0,0]==0)
    

def update_energy(grid):
    
    grid += np.ones(grid.shape,int)
    
    old_sum = 0
    have_flashed = []
    while(np.sum(grid)!= old_sum):
        old_sum = np.sum(grid)
        flashing_octos = get_flashing(grid, have_flashed)
        grid = radiate(grid, flashing_octos, have_flashed)
        have_flashed += flashing_octos
        
    flashing_octos = get_flashing(grid, have_flashed)
    if(len(flashing_octos)>0):
        print("PROBLEM IT HAS STOPPED WHILE NEW ARE FLASHING")
        print("last_flashing", flashing_octos)
        
    grid = flush_tired(grid, have_flashed)
    return(grid, have_flashed)


def flush_tired(grid, flashings):
    for row,col in flashings:
        grid[row, col] = 0 
    return(grid)


def radiate(grid, flashings, have_flashed):
    to_flash = [octo for octo in flashings if octo not in have_flashed]
    for row,col in to_flash:
        for n in get_neighbours(row, col, grid):
            grid[n[0],n[1]] += 1 
    return(grid)

def get_flashing(grid, have_flashed):
    flash = []
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if(grid[row,col]>9):
                flash.append((row, col))
    return([x for x in flash if x not in have_flashed])


def get_neighbours(row, col, grid):
    potential_neighbours = [np.add((row, col),transi) for transi in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]]
    return(list(filter(lambda n: isinGrid(n[0],n[1], grid),potential_neighbours)))
    

def isinGrid(row, col, grid):
    return(0<= row <grid.shape[0] and 0<= col <grid.shape[1])

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day11/example_in.txt" 
    else: path = "./day11/input.txt" 
    #path = "./day11/simpler_ex.txt"

    with open(path) as f:
        input = f.readlines()
    input = list(map(lambda x: [int(x) for x in x.replace("\n","")], input))
    #print(input)
    #print(np.array(input))
    return (np.array(input))


if __name__ == "__main__":
    main()

