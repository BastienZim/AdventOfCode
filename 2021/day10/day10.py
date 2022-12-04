'''
up=Down
down = up


'''



def main():
    input = get_input(exBOOL = False)
    #print(input)
    illegals = ""
    scores = []
    for line in input:
        validity, illegal_char, isin_chunk = brute_force(line, get_chunks_found = True)
        
        if(validity):
            padding = endLine(line, isin_chunk)
            scores.append(get_padding_cost(padding))
            
        illegals += illegal_char
    res = get_illegal_cost(illegals)
    print("part1", res)
    print("part2", select_score(scores) )
    

#---------------------Funcs--------------------
def select_score(scores):
    return (sorted(scores)[int(len(scores)/2)])


def get_illegal_cost(illegals):
    dict_values = {"}":1197,")":3,"]":57,">":25137}
    return(sum([dict_values[x] for x in illegals]))

def get_padding_cost(padding):
    dict_values = {"}":3,")":1,"]":2,">":4}
    score = 0
    for x in padding:
        score = score * 5 + dict_values[x]
    return(score)



def endLine(line, isin_chunk):
    
    i = 0
    res = ""
    while(i<len(line)):
        if(isin_chunk[i] == '0'):
            res = get_opposite(line[i])+ res
            i+=1
        elif(isin_chunk[i] == 'k'):
            i += 1
            print("??????")
        else:
            #print(isin_chunk[i])
            i += int(isin_chunk[i])+1
    #print("RES___", res)  
    #}}
    return(res)

def brute_force(line, get_chunks_found=False):
    isin_chunk = [str(0) for x in line]
    chunk_id = 1
    for chunk_size in range(1, len(line)):
        #print("CHUNK SIZE",chunk_size)
        for i in range(0,len(line)-chunk_size):
            chunk = line[i:i+chunk_size+1]
            #check if valid and not checked yet
            if(open_close(chunk[0],chunk[-1]) and \
                isin_chunk[i]==str(0) and isin_chunk[i+chunk_size]==str(0)):
                if(check_matching(chunk)):
                        isin_chunk[i] = str(chunk_size)
                        isin_chunk[i+chunk_size] = "k"
                        chunk_id+=0
                else:
                    #print("--- ERROR: We wanted %s but we have %s"%(get_opposite(chunk[0]),chunk[-1]))
                    if(get_chunks_found):return(False, chunk[-1], isin_chunk)
                    else: return(False, chunk[-1])
    if(get_chunks_found): return(True, "", isin_chunk)
    else: return(True, "")
    
        
#
#note: should be class methods...
def get_opposite(char):
    openings=["{","(","[","<"]
    closings=["}",")","]",">"]
    if(char in openings): return(closings[openings.index(char)])
    elif((char in openings)): return(openings[closings.index(char)])
    else: return(-1)

def open_close(open_char, close_char):
    openings=["{","(","[","<"]
    closings=["}",")","]",">"]
    return(open_char in openings and close_char in closings)


def check_matching(chunk):
    openings=["{","(","[","<"]
    closings=["}",")","]",">"]
    
    #print(chunk, chunk[0], chunk[-1])
    symbol_index = openings.index(chunk[0])
    #symbols = openings[symbol_index], closings[symbol_index]
    return(closings[openings.index(chunk[0])] == chunk[-1])     



#-------------INPUT--------------------------
def get_input(exBOOL = False):
    if(exBOOL): path = "./day10/example_in.txt" 
    else: path = "./day10/input.txt" 

    with open(path) as f:
        input = f.readlines()
    input = list(map(lambda x: x.replace("\n",""), input))
    #print(input)
    
    return (input)


if __name__ == "__main__":
    main()

