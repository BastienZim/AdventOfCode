import requests
from bs4 import BeautifulSoup as bs

import sys
import os

print(len(sys.argv))
if(len(sys.argv)>1):
    year = str (sys.argv[1])
    day = str (sys.argv[0])
else:
    year = "2022"
    day = "1"

year, day = list(sys.argv)[1:3]

print(f"Loading data from ADVENT OF CODE year: {year}, day: {day}")




"""
/bin/python3 /home/bastienzim/Documents/perso/adventOfCode/2022/day1/import_input.py 2022 4
/home/bastien/Documents/AdventOfCode/2022
"""

url = "https://adventofcode.com/" + year + "/day/" + day + "/input"

SESSIONID = "53616c7465645f5f51507adf997beeaac6b92e8984a6d0b52e3b25d7fbc1213abfc228dc37548520c9805d79e3557dcb868f5b8c303ca9aad0c48aec68b0f848"

response = requests.get(url, cookies={'session': SESSIONID})

#print(response.content)
#base_path = "/home/bastien/Documents/AdventOfCode/"
base_path = "/home/bastienzim/Documents/perso/adventOfCode/"

#if(not os.path.exists("/home/bastienzim/Documents/perso/adventOfCode/" + year + "/day" + day)):
if(not os.path.exists(base_path + year + "/day" + day)):
    os.mkdir(base_path + year + "/day" + day )
with open (base_path + year + "/day" + day + "/input.txt", "wb" ) as f:
    f.write(response.content)




#if __name__ == "__main__":
    
#    main()

