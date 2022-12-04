'''
up=Down
down = up


'''

from os import chdir
from typing import BinaryIO


dir = "/home/bastienzim/Documents/perso/adventOfCode/"
day = "day2/"

class Submarine:

    def __init__(self, pow=0):
        self.pow_consumption = pow
        
        self.gamma = 0
        self.eps = 0

        self.c02_scrub_rate = 0
        self.life_sup_rate = 0
        self.oxy_sup_rate = 0



    def __str__(self):
        return("The actual power consumption is of %d"%self.pow_consumption)
   
    def compute_ls_rating(self, input):
        self.compute_ratings(input)
        self.life_sup_rate = self.c02_scrub_rate * self.oxy_sup_rate
        print( self.oxy_sup_rate, self.c02_scrub_rate , self.life_sup_rate)


    def compute_consumption(self, input):
        self.compute_gamma(input)
        self.compute_epsilon(input)
        self.compute_consumption = self.gamma * self.eps


    def compute_ratings(self, numbers):
        filt_nums = numbers
        for bit in range(len(numbers[0])):
            current_bit_list = [int(num[bit]) for num in filt_nums]
            ones = sum(current_bit_list)
            zeros = len(current_bit_list) - ones
            if ones>=zeros: most_common = 1
            else: most_common = 0
            filt_nums  = list(filter(lambda x: int(x[bit])==most_common, filt_nums))
            if(len(filt_nums)==1):
                break
        self.oxy_sup_rate = int(filt_nums[0],2)

        filt_nums = numbers
        for bit in range(len(numbers[0])):
            current_bit_list = [int(num[bit]) for num in filt_nums]
            ones = sum(current_bit_list)
            zeros = len(current_bit_list) - ones
            if ones>=zeros: least_common = 0
            else: least_common = 1
            #print(bit, "   " ,least_common)
            filt_nums  = list(filter(lambda x: int(x[bit])==least_common, filt_nums))
            #print(filt_nums)
            if(len(filt_nums)==1):
                break
        self.c02_scrub_rate = int(filt_nums[0],2)
        


    

    def compute_gamma(self, numbers):
        rule = ""
        #counts = [[0,0] for bit in range(len(numbers[0]))]
        num_count = len(numbers)
        for bit in range(len(numbers[0])):
            zeros = sum([int(num[bit]) for num in numbers])
            ones = num_count - zeros
            if(ones>zeros): rule += '0'
            else: rule += '1'
        #print(self.rule)        
        self.gamma = int(rule,2)

    def compute_epsilon(self, numbers):
        rule = ""
        #counts = [[0,0] for bit in range(len(numbers[0]))]
        num_count = len(numbers)
        for bit in range(len(numbers[0])):
            zeros = sum([int(num[bit]) for num in numbers])
            ones = num_count - zeros
            if(ones>zeros): rule += '1'
            else: rule += '0'
        #print(self.rule)        
        self.eps = int(rule,2)




def main():
    sub = Submarine()
    input = get_input()
    sub.compute_ls_rating(input)
    print( sub.gamma, sub.eps, sub.compute_consumption)
#    sub.follow_path(path)
    

def get_input():
    with open("./day3/input.txt") as f:
        input = f.readlines()
    input = list(map(lambda x: x.replace("\n",""), input))
    #print(input)
    return input


if __name__ == "__main__":
    main()

