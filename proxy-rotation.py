from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import random
import re
from threading import Thread

ua = UserAgent()

# Rotating User-Agent
def rotate_agent():
    return ua.random 
def random_proxy(proxies):
    return random.randint(0,len(proxies)-1)
PATH = 'out.txt'
# Collecting proxies
def getProxies():
    Req = requests.get('https://www.sslproxies.org/',headers = {'User-Agent':rotate_agent()})
    bs = BeautifulSoup(Req.content,features="html.parser")
    Proxies =[]
    for row in bs.tbody.find_all('tr'):
        cols = row.find_all('td')
        Proxies.append({'IP':cols[0].text,'Port':cols[1].text})
    return Proxies
def addDataToFile(ip):
    with open(PATH, 'r') as f:
        proxies = f.readlines()
    if ip not in proxies:
        with open(PATH, 'a') as f:
            f.write(ip)
def check(ip,port):
    try:
        Req = requests.get('http://icanhazip.com/',headers = {'User-Agent':rotate_agent()}, proxies = {'http':ip + ':'+port},timeout=10)
        #
        #   Scrape,..,..,DO something
        #
        myip = re.sub(r'[^0-9^\.:]','',str(Req.content))
        print('#Rotated --> {}:{}'.format(ip,port))
        addDataToFile('{}:{}\n'.format(ip,port))
    except:
        print('#Dead --> {}:{}'.format(ip,port))
# Rotating proxies each request
Proxies = getProxies()
NUMBER_OF_THREADS = 10

i=0
while True:
    Threads = []
    for k in range(i,i+NUMBER_OF_THREADS):
        i+=1
        if(k >= len(Proxies)):
            break
        th = Thread(target=check,args=[Proxies[k]['IP'],Proxies[k]['Port']])
        th.start()
        Threads.append(th)
    for th  in Threads:
        th.join()
    #os.system('cls' if os.name == 'nt' else 'clear')
    if(i >= len(Proxies)):
        break
        
