import requests
from bs4 import BeautifulSoup
import os

url = 'https://en.wikipedia.org/wiki/The_Pillars_of_Creation'

sourcecode = requests.get(url)

parsed_code = BeautifulSoup(sourcecode)

all_divs=parsed_code.findAll('div')

for div in all_divs:
    R1 = div.find('h1')
    print(R1)
