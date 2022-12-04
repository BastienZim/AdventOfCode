'''
up=Down
down = up


'''

#This IS UGLY !!!!!

import numpy as np
from functools import reduce

all_versions = []


def main():
    input = get_input(exBOOL=False)
    print(input)
    bin_number = hexa_converter(input)#"{0:b}".format((int(input,16)))#
    print(bin_number)
    #print(len(bin_number))
    #version, id = get_paquet_info(bin_number)
    #print("Version %d, Id:%d"%(version, id))

    version, id , message, next, paquet_list = parse_input(bin_number)
    #print(sum(all_versions))
    #print("OK NOW WE ENDED", c, e)
    print("\n\n")
    print(paquet_list)
    print()
    #print("Sum of versions is: ",sum_versions(paquet_list))

    print()
    print(message)
    print()
    decode_message(message)
# ---------------------Funcs--------------------
def decode_message(message):
    copy = str(message)
    copy = copy.replace(")#","),#")
    copy = copy.replace(",)",")")
    for x in range(10):
        copy = copy.replace(")"+str(x),"),"+str(x))
    
    
    #replace operators
    copy = copy.replace("#0-","add")
    #add = lambda x,y: x+y
    copy = copy.replace("#1-","mult")
    #mult = lambda x,y: x*y
    copy = copy.replace("#2-","minim")
    #minim = lambda x: min(x.split(","))
    copy = copy.replace("#3-","maxim")
    #maxim = lambda x,y: max(x,y)
    copy = copy.replace("#5-","great")
    great = lambda x,y: int(x>y)
    copy = copy.replace("#6-","less")
    less = lambda x,y: int(x<y)
    copy = copy.replace("#7-","eq")
    eq = lambda x,y: int(x==y)
    #replace parenthesis
    #copy = copy.replace("\\","(")
    print(copy)
    print(eval(copy))
    return()

def add(inputs, *kwargs):
    return(sum([inputs]+[x for x in kwargs]))
def mult(inputs, *kwargs):
    aaa = [inputs]+[x for x in kwargs]
    prod = 1
    for x in aaa:
        prod = prod * x
    return prod
    
#    print([inputs]+[x for x in kwargs])
#    return(list(reduce(lambda x, y: x * y, [inputs]+[x for x in kwargs]))[0])
def minim(inputs, *kwargs):
    return(min([inputs]+[x for x in kwargs]))
def maxim(inputs, *kwargs):
    return(max([inputs]+[x for x in kwargs]))

def extract_current_depth(message):#not working because the depth do not close ...``
    cursor = 0
    beg = message.index("\\")
    i = beg
    depths = [[] for i in range(0,10)]
    depths[0] = [message]
    #print(i)
    for d in range(10):
        print(f"DEPTH: {d}")
        for submessage in depths[d]:
            print(submessage)
            beg = submessage.index("\\")
            i = beg
            while(i<len(submessage)):
                if(submessage[i]=="\\"):
                    cursor+=1
                    #print(f"+1 {cursor}")
                elif(submessage[i] == "/"):
                    if(cursor>0):
                        cursor -= 1
                        #print(f" -1 {cursor}")
                    elif(cursor == 0):
                        end = i
                        submessage = submessage[beg+1:end]
                        left = submessage[end+1:]
                        print(f"beg: {beg} end: {i}", left)
                        break

            i+=1


def sum_versions(paquet_list, sum=None):
    if(sum == None):
        sum=0
    print("BEGINS")

    for sub_paquet in paquet_list:
        #print()

        if(type(sub_paquet[1]) != str):
            print("TEHHEHEH",sub_paquet[0])
            if(type(sub_paquet[1]) != str):
                print("asdas")
                version = sub_paquet[0][0].split("-")[0]
                sum += int(version)
                sum = sum_versions(sub_paquet, sum)
            else:
                print("asasdJHKHJLHKJKHJLKHJLdas")

                version = sub_paquet[0].split("-")[0]
                sum += int(version)
                sum = sum_versions(sub_paquet, sum)
        else:
            print("xxxxxxxxs")
            version = sub_paquet.split("-")[0]
            sum += int(version)

    return(sum)


def bin_to_letters(paquet):
    to_consider = paquet[6:]
    #print(to_consider)
    encoded_num = ""
    i=0
    group = to_consider[i:i+5]
    while(group[0] =="1"):
        encoded_num += group[1:]
        i+=5
        group = to_consider[i:i+5]
    encoded_num += group[1:]
    decimal_num = int(encoded_num,2)
    #print(encoded_num)
    #print(decimal_num)

    return()


def parse_input(bin_number, message=None, paquet_list = None):
    if(len(bin_number)<=6):#less than 6 bit makes it uncompatible with version id format.
        return("_","_",message,"", paquet_list)
    if(message==None):
        message = ""
    if(paquet_list==None):
        paquet_list = []
    version, id = get_paquet_info(bin_number)
    #FOR PART 2 !!!!!!!!!!!!!!!!!!
    version = ""
    to_consider = bin_number[6:]
    #DEGUELASSSE CETTE ligne mais ça marche
    #all_versions.append(version)
    #print(" BEGIN Version %d, Id:%d"%(version, id), paquet_list)#, bin_number[:6])
    if(id == 4):#Litteral -> its easy
        decimal_num, next = parse_literals(to_consider)
        message += str(decimal_num)+","
        paquet_list.append((f"{id}-{version}:L", str(decimal_num)))
    else:#operators
        #print("-------------",to_consider)
        operator_message, next, paquets_operator = parse_operator(to_consider, f"#{id}-{version}(", paquet_list = paquet_list)
        message += operator_message
        message = message+")"
        #if("L" in [x[0] for x in paquets_operator]):
        if("L" in [x[0][-1] for x in paquets_operator]):
            paquet_list.append((f"{id}-{version}:O", [x for x in paquets_operator if x[0][-1] == "L"]))
        else:
            paquet_list.append((f"{id}-{version}:O", paquets_operator))
        #print("------------PO",paquets_operator)
    #print("    ",message, paquet_list)
    #input("    END Version %d, Id:%d         "%(version, id))#, bin_number[:6])
    #input("Press ENTER to continue")
   # print(f"\npaquet V {version} id: {id}")
    #print(f"paquet end, next is : {next}\n    message: {message}\n    content: {paquet_list}")
    return(version, id , message, next, paquet_list)


def parse_operator(to_consider, message, paquet_list = []):
    paquets_operator = list(paquet_list)
    #print(len(paquet_list))
    #print(f"+++++++++++++++ {to_consider} || {len(to_consider)}")
    if(to_consider[0] == '0'):#length
        n=15
        n_bits_sub = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1 : n+1 + n_bits_sub]
        while len(sub_paquets)>0:
            version, id , message, sub_paquets, paquets_operator = parse_input(sub_paquets, message, paquet_list=paquets_operator)
            #message += "/"
        next = to_consider[n+1 + n_bits_sub:]
        #message = message+"/"#message[:-1]+"/"
        #message = message[:-2]+message[-1]
        print("HERE:, ",message[-2:])
    elif(to_consider[0] == '1'):#number
        n=11
        n_sub_paquets = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1:]
        n_sub_read = 0
        len_subs_seen = 0
        old_len = len(to_consider)
        while n_sub_read != n_sub_paquets:
            version, id , message, sub_paquets, paquets_operator = parse_input(sub_paquets, message, paquet_list=paquets_operator)
            len_subs_seen += old_len - len(sub_paquets)
            old_len = len_subs_seen
            n_sub_read += 1
        #message = message+"/"#message[:-1]+"/"
        
        print("Theres:, ",message[-2:])
        next = sub_paquets
    else:#health check
        print(  "BIG PROBLEM")
    #print(len(str(paquets_operator)))
    return(message, next, paquets_operator)

def parse_literals(to_consider):
    #message = "L-"
    checking = str(to_consider)
    encoded_num = ""
    i=0
    group = checking[i:i+5]
    while(group[0] =="1"):
        encoded_num += group[1:]
        i+=5
        group = checking[i:i+5]
    encoded_num += group[1:]

    checking = checking[i+5:]
    return(int(encoded_num,2), checking)




def get_n_subs(bits):
    return(int(bits,2))

def get_paquet_version(paquet):
    return(int(paquet[:3], 2))

def get_paquet_id(paquet):
    return(int(paquet[3:6], 2))

def get_paquet_info(paquet):  # both id and version
    return((int(paquet[:3], 2), int(paquet[3:6], 2)))

def hexa_converter(input):

    map = { "0" : '0000',
            "1" : '0001',
            "2" : '0010',
            "3" : '0011',
            "4" : '0100',
            "5" : '0101',
            "6" : '0110',
            "7" : '0111',
            "8" : '1000',
            "9" : '1001',
            "A" : '1010',
            "B" : '1011',
            "C" : '1100',
            "D" : '1101',
            "E" : '1110',
            "F" : '1111'}
    res =""
    for x in input:
        res+=map[x]
    return(res)




# -------------INPUT--------------------------


def get_input(exBOOL=False):
    if(exBOOL):
        path = "./day16/example_in.txt"
    else:
        path = "./day16/input.txt"

    with open(path) as f:
        input = f.readlines()
    # print(input)
    input = list(map(lambda x: x.replace("\n", ""), input))[0]
    # print(input)
    # print(np.array(input))
    return (input)


if __name__ == "__main__":
    main()
