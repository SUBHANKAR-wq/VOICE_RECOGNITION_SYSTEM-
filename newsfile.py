import pandas as pd
from bs4 import BeautifulSoup
import lxml #used in jypiter note book but here html
import requests

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpg=requests.get("https://timesofindia.indiatimes.com/world",headers=header).text


soup=BeautifulSoup(webpg,'html')



newz=[]
i=1

for j in range(1,6):
    
    for i in soup.find_all('div',class_='WavNE'): 
        newz.append(i.text.strip())



hdln={"news":newz[0:6],
      "headline":newz[0:6]}