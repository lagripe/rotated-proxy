from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import random
import re
ua = UserAgent()

# Rotating User-Agent
def rotate_agent():
    return ua.random 
def random_proxy(proxies):
    return random.randint(0,len(proxies)-1)

# Collecting proxies
def getProxies():
    Req = requests.get('https://www.sslproxies.org/',headers = {'User-Agent':rotate_agent()})
    bs = BeautifulSoup(Req.content,features="html.parser")
    Proxies =[]
    for row in bs.tbody.find_all('tr'):
        cols = row.find_all('td')
        Proxies.append({'IP':cols[0].text,'Port':cols[1].text})
    return Proxies

# Rotating proxies each request
Proxies = getProxies()
req_number = 50
for i in range(req_number):
    if len(Proxies)==0:
        print('No proxies left!')
        break
    proxy_index = random_proxy(Proxies)
    proxy = Proxies[proxy_index]
    try:
        Req = requests.get('http://icanhazip.com/',headers = {'User-Agent':rotate_agent()}, proxies = {'http':proxy['IP'] + ':'+proxy['Port']})
        #
        #   Scrape,..,..,DO something
        #
        myip = re.sub(r'[^0-9^\.]','',str(Req.content))
        print('#Rotated --> '+ str(myip))
    except:
        print('#Dead --> ' + proxy['IP'] + ':'+ proxy['Port'])
        del Proxies[proxy_index]