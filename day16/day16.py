'''
up=Down
down = up


'''

#This IS UGLY !!!!!
all_versions = []


def main():
    input = get_input(exBOOL=False)
    #print(input)
    bin_number = hexa_converter(input)#"{0:b}".format((int(input,16)))#
    #print(bin_number)
    #print(len(bin_number))
    #version, id = get_paquet_info(bin_number)
    #print("Version %d, Id:%d"%(version, id))

    version, id , message, next, paquet_list = parse_input(bin_number)
    print(sum(all_versions))
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
    i=0
    while i<len(message):
        print(message[i])
        break
    print("asdsasda")
    #extract_current_depth(message)
    #print(message.split("#"))

def extract_current_depth(message):#not working because the depth do not close ...``
    cursor = 0
    i=message.index("\\")
    print(i)
    while(i<len(message)):
        if(message[i]=="\\"):
            cursor+=1
            print(f"+1 {cursor}")
        elif(message[i] == "/"):
            if(cursor>0):
                cursor -= 1
                print(f" -1 {cursor}")
            else:
                print(f"ending at {i}")
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
    if(len(bin_number)<6):#less than 6 bit makes it uncompatible with version id format.
        return("_","_",message,"", paquet_list)
    if(message==None):
        message = ""
    if(paquet_list==None):
        paquet_list = []
    version, id = get_paquet_info(bin_number)
    to_consider = bin_number[6:]
    all_versions.append(version)
    #print(" BEGIN Version %d, Id:%d"%(version, id))#, bin_number[:6])
    
    if(id == 4):
        decimal_num, next = parse_literals(to_consider)
        message += str(decimal_num)+","
        paquet_list.append((f"{version}-{id}:L", str(decimal_num)))
    else:#operators
        operator_message, next, paquets_operator = parse_operator(to_consider, [], version, id)
        message += operator_message
        #if("L" in [x[0] for x in paquets_operator]):
        
        if("L" in [x[0][-1] for x in paquets_operator]):
            paquet_list.append((f"{version}-{id}:O", [x for x in paquets_operator if x[0][-1] == "L"]))
        else:
            paquet_list.append((f"{version}-{id}:O", paquets_operator))
    #print("    END Version %d, Id:%d"%(version, id))#, bin_number[:6])
    return(version, id , message, next, paquet_list)


def parse_operator(to_consider, paquet_list, version, id,depth=0):
    message = f"#{version}-{id}\\"
    paquets_operator = list(paquet_list)
    if(to_consider[0][-1] == '0'):#length
        n=15
        n_bits_sub = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1 : n+1 + n_bits_sub]
        while len(sub_paquets)>0:
            version, id , message, sub_paquets, paquet_list = parse_input(sub_paquets, message, paquet_list=paquets_operator)
            message += "/"
        next = to_consider[n+1 + n_bits_sub:]
        message = message[:-1]+"/"
    elif(to_consider[0] == '1'):#number
        n=11
        n_sub_paquets = get_n_subs(to_consider[1:n+1])
        sub_paquets = to_consider[n+1:]
        n_sub_read = 0
        len_subs_seen = 0
        old_len = len(to_consider)
        while n_sub_read != n_sub_paquets:
            version, id , message, sub_paquets, paquet_list = parse_input(sub_paquets, message, paquet_list=paquets_operator)
            len_subs_seen += old_len - len(sub_paquets)
            old_len = len_subs_seen
            n_sub_read += 1
        message = message[:-1]+"/"
        next = sub_paquets
    else:#health check
        print(  "???????????????????????????????????????????????????????????")
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
