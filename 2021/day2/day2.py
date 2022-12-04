'''
up=Down
down = up


'''

dir = "/home/bastienzim/Documents/perso/adventOfCode/"
day = "day2/"

class Submarine:

    def __init__(self, depth=0, pos=0, aim=0):
         self.depth = depth
         self.pos = pos
         self.aim = aim

    def __str__(self):
        return("The submarines is %d m deep and\n\
         advanced %d m !!!\n the aim is of %d"%(self.depth, self.pos, self.aim))

    def get_res(self):
        return(self.depth*self.pos)

    def follow_path(self, path):
        for step in path:
            move = step[0]
            impact = step[1]
            if(move =='forward'):
                self.pos += impact
            elif(move =='down'):self.depth += impact
            elif(move =='up'):self.depth -= impact

    def advanced_path(self, path):
        for step in path:
            move = step[0]
            impact = step[1]
            if(move =='forward'):
                self.pos += impact
                self.depth += self.aim*impact
            elif(move =='down'):self.aim += impact
            elif(move =='up'):self.aim -= impact


commandList = ['forward',
                'down',
                'up']




def main():
    sub = Submarine(0,0)
    print(sub.depth)
    path = get_path()
#    sub.follow_path(path)
    sub.advanced_path(path)
    print(sub)
    print(sub.get_res())


def get_path():
    with open("./day2/input.txt") as f:
        input = f.readlines()
    input = list(map(lambda x: x.replace("\n",""), input))
    input = list(map(lambda x: x.split(" "), input))
    input = list(map(lambda x: [x[0],int(x[1])], input))
    return input


if __name__ == "__main__":
    main()

