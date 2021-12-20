'''
up=Down
down = up


'''


all_versions = []
def main():
    input = get_input(exBOOL=True)
    #print(input)
    bin_number = hexa_converter(input)#"{0:b}".format((int(input,16)))#
    #print(bin_number)
    #print(len(bin_number))
    #version, id = get_paquet_info(bin_number)
    #print("Version %d, Id:%d"%(version, id))

    a,b,c,d, e = parse_input(bin_number)
    print(sum(all_versions))
    #print("OK NOW WE ENDED", c, e)
    print("\n\n")
    print(e)
    print()
    print("Sum of versions is: ",sum_versions(e))


# ---------------------Funcs--------------------

def sum_versions(paquet_list, sum=None):
    if(sum == None):
        sum=0
    for version, id , message, sub_paquet in paquet_list:
        sum += version
        #print(version)
        #print(type(sub_paquet), len(sub_paquet), sub_paquet)
        if(type(sub_paquet) != str):#same as: if(message == "O"):
        #    print("YES, message", message)
            sum = sum_versions(sub_paquet, sum)
        #else:
        #    print("NO : message", message, sub_paquet)
            #sum += int(sub_paquet)
        #if(message == "O"):#if operator:
            #print("  Operator")
    return(sum)


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
    if(len(bin_number)<6):#less than 6 bit makes it uncompatible with version id format.
        #print("   -----------it has ended", message)
        return("_","_",message,"", paquet_list)
    if(message==None):
        message = ""
    if(paquet_list==None):
        paquet_list = []
    version, id = get_paquet_info(bin_number)
    to_consider = bin_number[6:]
    all_versions.append(version)
    print("Version %d, Id:%d"%(version, id), bin_number[:6])
    if(id == 4):
        decimal_num, next = parse_literals(to_consider)
        message += str(decimal_num)+","
        paquet_list.append((version, id, "L", str(decimal_num)))
    else:#operators
        #print("  New operator, Version %d, Id:%d"%(version, id), bin_number[:6])
        operator_message, next, paquets_operator = parse_operator(to_consider, [])
        message += operator_message
        #print(operator_message, paquets_operator)
        #paquet_list.append((version, id, "O", paquets_operator))
        #print("O:", message, paquets_operator)
        #print("   Operator CLosed, Version %d, Id:%d"%(version, id), bin_number[:6], 
        #        operator_message, paquets_operator)
        if("L" in [x[2] for x in paquets_operator]):
            #print("  OKKKK")
            #print([x for x in paquets_operator if x[2] == "L"])#marche au plus profond...
            #print(paquet_list)
            paquet_list.append((version, id, "O", [x for x in paquets_operator if x[2] == "L"]))
            #print(paquet_list)
        else:    
            #print("  NOOOOOO")
            #print(paquets_operator)
            paquet_list.append((version, id, "O",paquets_operator))
            #print(paquet_list)
    #print("--------------------- RETURN  : ", version, id , message, next, paquet_list)
    return(version, id , message, next, paquet_list)


def parse_operator(to_consider, paquet_list, depth=0):
    message = "O-"
    paquets_operator = list(paquet_list)
    if(to_consider[0] == '0'):#length
        n=15
        n_bits_sub = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1 : n+1 + n_bits_sub]
        while len(sub_paquets)>0:
            version, id , message, sub_paquets, paquet_list = parse_input(sub_paquets, message, paquet_list=paquets_operator)
        
        next = to_consider[n+1 + n_bits_sub:]
        message = message[:-1]+"_"
    elif(to_consider[0] == '1'):#number
        n=11
        n_sub_paquets = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1:]
        n_sub_read = 0
        len_subs_seen = 0
        old_len = len(to_consider)
        while n_sub_read != n_sub_paquets:
            #print(n_sub_read, n_sub_paquets)
            
            version, id , message, sub_paquets, paquet_list = parse_input(sub_paquets, message, paquet_list=paquets_operator)
            len_subs_seen += old_len - len(sub_paquets)
            old_len = len_subs_seen
            n_sub_read += 1
        message = message[:-1]+"_"
        next = sub_paquets
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
    decimal_num = int(encoded_num,2)
    checking = checking[i+5:]
    #print("   end-litteral, number: %d"%decimal_num)
    return(decimal_num, checking)




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
