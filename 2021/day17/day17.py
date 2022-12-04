'''
Code by Bastien Zimmermann - @ BastienZim on github
'''
from os import SCHED_OTHER
import numpy as np

def main():
    input = get_input(exBOOL = False)
    print(input)
    #draw_target(input)

    find_highest_y(input)
    #print("---"*40)
    #v_x, v_y = 6, 3 
    #shot_list, _ = generate_shot_list(v_x, v_y, input, max_shots = 100, verbose = False)
    #print("shot_list", shot_list)
    #grid = draw_shots(draw_target(input), shot_list = shot_list)
    #show_map(grid)

    #grid = draw_target(input)
    #print(shot_list)
    #grid = draw_shots(draw_target(input), shot_list = shot_list)
    #show_map(grid)



#---------------------Funcs--------------------
def find_highest_y(input):
    
    #all the vxs we want to try
    test_vxs = [x for x in range(1,max(input[0])+5)]

    results = [[-np.inf] for x in test_vxs]
    velocities = [[(0,0)] for x in test_vxs]
    #before_target = True
    min_vx, max_vx = test_vxs[0], test_vxs[-1]
    min_vy = min(input[1])
#    print(min_vy, "THIS IS TJE MININIMUMUAMDLIASDLJ")
    #vy_lims = []

    for k, v_x in enumerate(test_vxs):
        v_y = min_vy
        for i in range(1000):
            shot_list, has_hit = generate_shot_list(v_x, v_y, input, max_shots=1000, verbose=False)
            if(has_hit):
                max_hight = get_max_hight(shot_list)
                results[k].append(max_hight)
                velocities[k].append((v_x,v_y))
            v_y += 1 
            
            
        #print(k,max(results[k]),velocities[k][np.argmax(results[k])])
        """if(before_target):
            if(len(results[k])>1):
                min_vx = v_x
                before_target = False
        else:
            if(len(results[k])>1):
                max_vx = v_x
            else:
                break"""
    
    print(f"\n\nMIN MAX vx : {min_vx}, {max_vx}")
    i_max = np.argmax([max(x) for x in results])
    print(f"Max height was with: {velocities[i_max][np.argmax(results[i_max])]} and we reached : {max([max(x) for x in results])} m")
    #print([max(x) for x in results])
    #print()
    #print()
    winning_things = []
    for x in velocities:
        #print("aaaa",x[1:])
        winning_things = winning_things + x[1:]
    winning_things = list(set(winning_things))#delete duplicates
    print(f"There are: {len(winning_things)} unique solutions found by brute force")
    #print(winning_things)
    #with open("./day17/temp.txt") as f:
    #    aaa = f.readlines()
    #aaa = aaa[0].replace("  "," ").replace("  "," ").replace("  "," ").replace(" ","_").split("_")
    #aaa = list(map(lambda x: (int(x.split(",")[0]),int(x.split(",")[1])), aaa))
    #print(np.sort(aaa) == np.sort(winning_things))
    #print(len(aaa), len(winning_things))
    #print()
    #print("in aaa not in winning",[x for x in aaa if x not in winning_things], len([x for x in aaa if x not in winning_things]))
    #print()
    #print("in winning not in aaa",[x for x in winning_things if x not in aaa], len([x for x in winning_things if x not in aaa]))
#    print([x for x in aaa if x not in winning_things])
   #winning_things = [(max(x),velocities[k][np.argmax(x)]) for k,x in enumerate(results) if max(x) != 0]    
    #for x in winning_things:
    #    print(x)

def update_probe_pos(x, y, v_x, v_y):
    
    new_x, new_y = x + v_x, y + v_y  #add speed
    #add drag
    if(v_x>=1): v_x -= 1
    elif(v_x<=-1): v_x += 1
    v_y -= 1  #add gravity
    return(new_x, new_y, v_x, v_y)


def generate_shot_list(v_x, v_y, input, max_shots = 10, verbose = False):
    x, y = 0, 0
    shot_list = []
    has_hit, target_passed = False, False
    n_shot = 0
    while(not has_hit and not target_passed and n_shot < max_shots):
        x, y, v_x, v_y =  update_probe_pos(x, y, v_x, v_y)
        shot_list.append((x, y))
        #print(x, y, v_x, v_y)
        n_shot += 1
        has_hit = isin_target((x,y), input)
        if(x > max(input[0])): target_passed = True
    if(verbose):
        if(not has_hit):
            print("either too bad or too fiew shots")
        else:
            print(" !!!!!!!!!!!!!!!! IT's a HIT !!!!!! ")
            print("----"*100)
    return(shot_list, has_hit)
    

def draw_target(input, target_char = "T"):
    xmin, xmax = input[0]
    ymin, ymax = input[1]
    max_x = max(abs(xmin), abs(xmax))
    max_y = max(abs(ymin), abs(ymax))
    shape = (max_x, max_y)
    grid = np.array(["." for i in range((max_x+1)*(max_y+1))]).reshape((max_x+1, max_y+1))
    grid[xmin : xmax+1, min(abs(ymin), abs(ymax)) : max(abs(ymin), abs(ymax))+1] = target_char
    grid[0,0] = "S"
    return(grid)


def add_padding(grid, shot_list=[(33,-5)]):
    xs = [x[0] for x in shot_list]
    ys = [x[1] for x in shot_list]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    z_offset = [0,0,0,0]
    if(xmin < 0):
        pading = np.array(["." for i in range((abs(xmin))*(grid.shape[1]))]).reshape((abs(xmin), grid.shape[1])) 
        grid = np.vstack((pading, grid))
        z_offset[0] = abs(xmin)
    if(xmax >= grid.shape[0]):
        pading = np.array(["." for i in range((abs(xmax)-grid.shape[0]+1)*(grid.shape[1]))]).reshape((abs(xmax)-grid.shape[0]+1, grid.shape[1])) 
        grid = np.vstack((grid, pading))
        z_offset[0] = abs(xmax)-grid.shape[0]+1
    if(ymin <= -grid.shape[1]):
        pading = np.array(["." for i in range((abs(ymin)-grid.shape[1]+1)*(grid.shape[0]))]).reshape((grid.shape[0], abs(ymin)-grid.shape[1]+1)) 
        grid = np.hstack((grid, pading))
        z_offset[0] = abs(ymin)-grid.shape[1]+1
    if(ymax > 0):
        pading = np.array(["." for i in range((abs(ymax))*(grid.shape[0]))]).reshape((grid.shape[0], abs(ymax))) 
        grid = np.hstack((pading, grid))
        z_offset[0] = abs(ymax)
    return(grid,  z_offset)


def isin_target(shot, input):
    #print("\n\n")
    xmin, xmax = input[0]
    ymin, ymax = input[1]
    #print(shot)
    if(xmin <= shot[0] and shot[0] <= xmax):
        #print(" - -- - - -- - - - - X OK")
        if(min(ymin, ymax) <= shot[1] and shot[1] <= max(ymin, ymax)):
            #print(" - -- - - -- - - - - Y OK")
            #print(shot, input)
            return(True)
    return(False)
    

def draw_shots(grid, shot_list=[(33,-5)]):
    grid, offset = add_padding(grid, shot_list)


    center = np.where(grid == "S")
    #print(center)
    for shot in shot_list:
        #print(shot)
        pos_x = center[0] + shot[0]
        pos_y = center[1] - shot[1]
        grid[pos_x, pos_y] = "#"
    return(grid)


def show_map(grid):
    for x in grid.T:
        print("".join(x))
    

def get_max_hight(shot_list):
    return(max([x[1] for x in shot_list]))

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

