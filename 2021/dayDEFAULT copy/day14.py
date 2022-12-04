'''
up=Down
down = up


'''
def main():
    content = get_input(exBOOL = True)
    
    print(content)



#---------------------Funcs--------------------

#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day18/example_in.txt" 
    else: path = "./day18/input.txt" 

    with open(path) as f:
        content = f.readlines()
    content = list(map(lambda x: [x for x in x.replace("\n", "")], content))

    return (content)


if __name__ == "__main__":
    main()

