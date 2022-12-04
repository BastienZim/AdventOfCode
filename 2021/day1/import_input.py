import requests
from bs4 import BeautifulSoup as bs


#uri = 'http://adventofcode.com/{year}/day/{day}/input'.format(year=YEAR, day=day)
#response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})


url = 'https://adventofcode.com/2021/day/1/input'

response = requests.get(url)

print(response.content)