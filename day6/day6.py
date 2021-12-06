'''
up=Down
down = up


'''



class Fish():
    def __init__(self, timer=3, name='fibonacci', days=0):
        self.timer = timer
        self.name = name
        self.days = days
        self.baby = None

    def day_passed(self):
        self.days += 1
        self.timer -= 1
        if(self.timer < 0):
            self.baby = Fish(timer = 8)
            self.timer = 6
        else:
            self.baby = None
        return(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        #return("%s is %d days old and an internal timer of %d "%(self.name, self.days, self.timer))
        return("%d"%(self.timer))

def anotherDay(fishList):
    fishList = [fish.day_passed() for fish in fishList]
    babies = [fish.baby for fish in fishList if fish.baby]
    fishList = fishList + babies
    return(fishList)

def alternative(fishDict):
    '''
    Fast as fck boi
    '''
    newFishDict = {i:fishDict[i+1] for i in range(0,8)}
    newFishDict[8] = fishDict[0]
    newFishDict[6] += fishDict[0]
    return(newFishDict)


def main():
    input = get_input(False)
    print(input)
    fishDict = {i: 0 for i in range(0,9)}
    for i in input:
        fishDict[i] += 1
    #equivalent to the three lines above, however it is more complex as it goes through the input samples several times.
    #fishDict = {i: input.count(i) for i in range(0,9)}


    #print(fishDict)
    n_days = 256
    for day in range(1,n_days+1):
        fishDict = alternative(fishDict)
    print(sum(fishDict.values()))

    #the part later is for the POO programmation

    #fishList = [Fish(timer=x) for x in input]
    #print("input Fish    ",fishList)
    #n_days = 256 #number of days of evolution
    #for day in range(1,n_days+1):
    #    fishList = anotherDay(fishList)
        #print("After  %d days:"%day,fishList)
    #print(len(fishList),"Fishes")
        
    
       
    
    


def get_input(exBOOL = False):
    if(exBOOL): path = "./day6/example_in.txt" 
    else: path = "./day6/input.txt" 

    with open(path) as f:
        input = f.readlines()
        
    input = [int(x) for x in input[0].split(",")]

    return (input)


if __name__ == "__main__":
    main()

