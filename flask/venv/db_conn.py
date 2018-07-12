import pymysql
from bs4 import BeautifulSoup
import urllib.request as urllib
import re

final_link=[]
links_list=[]
conn=pymysql.connect(host="localhost",user="root",passwd="",db="link_table")
mycursor=conn.cursor()
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
del links_list[17:20]
del links_list[79:80]
del final_link[17:20]
del final_link[79:80]
print (len(links_list))
print (len(final_link))

#for link in table.findAll('a'):
#    table_links=link.get('href').replace("javascript:void(0)","")
#    print(table_links)

    #mycursor.execute("INSERT INTO link(link) VALUES(%s)",(table_links))
    #mycursor.execute("DELETE FROM link where link=10;")

conn.commit()
conn.close()
