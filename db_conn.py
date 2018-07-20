from bs4 import BeautifulSoup
import urllib.request as urllib
import re

final_link=[]
links_list=[]

url = "https://timesofindia.indiatimes.com/rss.cms"
page = urllib.urlopen(url)
soup=BeautifulSoup(page,'lxml')
table=soup.find_all('div',{'id':"main-copy"})
for List in table:
        link1=List.find_all('a')
        for tr in link1:
            if(tr.text != 'More' and tr.text !=''):
                   links_list.append(tr.text)
for List in table:
    link1=List.find_all('a',{'class':"rssurl"})
    for tr in link1:
           final_link.append(tr.get('href').replace("javascript:void(0)",""))



