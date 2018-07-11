import pymysql
from bs4 import BeautifulSoup
import urllib.request as urllib
import re
import array

# import lxml

# conn=pymysql.connect(host="localhost",user="root",passwd="",db="link_table")
# mycursor=conn.cursor()
url = "https://timesofindia.indiatimes.com/rss.cms"
page = urllib.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('width') and tag['width'] == "640")


#def Find(String):
#    table_link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+',
#                            String)
#    return table_link


#print("URLS:", Find(table))
table_links = []
for link in table.findAll('a'):
    table_links.append = link.get('href').replace("javascript:void(0)", "")
    print(table_links)
    # mycursor.execute("INSERT INTO link(link) VALUES(%s)",(table_links))
    # mycursor.execute("DELETE FROM link where link=10;")

# conn.commit()
# conn.close()
