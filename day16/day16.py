'''
up=Down
down = up


'''


def main():
    input = get_input(exBOOL=True)
    print(input)
    bin_number = hexa_converter(input)#"{0:b}".format((int(input,16)))#
    print(bin_number)
    #version, id = get_paquet_info(bin_number)
    #print("Version %d, Id:%d"%(version, id))
    a,b,c,d = parse_input(bin_number)
    print("OK NOW WE ENDED", c)
    #print("110100101111111000101000")
#    version = get_paquet_version("100")
    # print(version)

# ---------------------Funcs--------------------

def bin_to_letters(paquet):
    to_consider = paquet[6:]
    print(to_consider)
    encoded_num = ""
    i=0
    group = to_consider[i:i+5]
    while(group[0] =="1"):
        encoded_num += group[1:]
        i+=5
        group = to_consider[i:i+5]
    encoded_num += group[1:]
    decimal_num = int(encoded_num,2)
    print(encoded_num)
    print(decimal_num)
    
    return()



def parse_input(bin_number, message=None, paquet_list = None):
    if(len(bin_number)<6):
        print("it has ended")
        return("_","_",message,"")
    if(message==None):
        message = ""
    if(paquet_list==None):
        paquet_list = []
    version, id = get_paquet_info(bin_number)
    to_consider = bin_number[6:]
    print()
    print("Version %d, Id:%d"%(version, id), bin_number[:6])
    if(id == 4):
        #print("  litteral")
        decimal_num, next = parse_literals(to_consider)
        #print("paquet is a litteral: %d"%decimal_num)
        message += str(decimal_num)+","
        paquet_list.append((version, id, "L", str(decimal_num)))
        #print("L:",message)
    else:#operators
        #print("  operator")
        #len type ID
#        print(to_consider)
        operator_message, next = parse_operator(to_consider)
        message += operator_message
        paquet_list.append((version, id, "O", operator_message))
        #print("O:",message)


    return(version, id , message, next, paquet_list)


def parse_operator(to_consider):
    message = "O-"
    if(to_consider[0] == '0'):#length
        n=15
        n_bits_sub = get_n_subs(to_consider[1:n+1])
        sub_paquet = to_consider[n+1 : n+1 + n_bits_sub]
        while len(sub_paquet)>0:
            #print("1 iteration")
            #print(len(sub_paquet))
            version, id , message, sub_paquet = parse_input(sub_paquet, message)
            #print("result from iteration",version, id , message, sub_paquet)
    elif(to_consider[0] == '1'):#number
        n=11
        n_sub_paquets = get_n_subs(to_consider[1:n+1])
        #print("%d sub paquets to read ! "%n_sub_paquets)
        sub_paquets = to_consider[n+1:]
        n_sub_read = 0
        while n_sub_read != n_sub_paquets:
            #print("1 iteration")
            #print(len(sub_paquets))
            version, id , message, sub_paquets = parse_input(sub_paquets, message)
            #print("result from iteration",version, id , message, sub_paquet)
            n_sub_read += 1
        message = message[:-1]+"-"
        #print(message)
        
        next = sub_paquets
    return(message, next)

def parse_literals(to_consider):
    #message = "L-"
    encoded_num = ""
    i=0
    group = to_consider[i:i+5]
    while(group[0] =="1"):
        encoded_num += group[1:]
        i+=5
        group = to_consider[i:i+5]
    encoded_num += group[1:]
    decimal_num = int(encoded_num,2)
    to_consider = to_consider[i+5:]
    return(decimal_num, to_consider)




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
