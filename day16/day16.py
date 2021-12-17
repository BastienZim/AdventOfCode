'''
up=Down
down = up


'''
def main():
    input = get_input(exBOOL = True)
    
    print(input)



#---------------------Funcs--------------------

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day14/example_in.txt" 
    else: path = "./day14/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #input = list(map(lambda x: [int(x) for x in x.replace("\n","")], input))
    #print(input)
    #print(np.array(input))
    return (input)


if __name__ == "__main__":
    main()

