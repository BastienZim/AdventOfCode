'''
up=Down
down = up


'''




def main():
    input = get_input(True)
    
    

       
    
    


def get_input(exBOOL = False):
    if(exBOOL): path = "./day5/example_in.txt" 
    else: path = "./day5/input.txt" 

    with open(path) as f:
        input = f.readlines()
    #print(input)
    print(input)
    input = list(map(lambda x: x.replace("\n","").split(" -> "), input))
    input = list(map(lambda x: (x[0].split(","), x[1].split(",")), input))
    input = list(map(lambda a: ([int(x) for x in a[0]],[int(x) for x in a[1]]), input))
#    print(input)

    return (input)


if __name__ == "__main__":
    main()

