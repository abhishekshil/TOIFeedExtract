
# coding: utf-8

# In[53]:


import requests
from bs4 import BeautifulSoup
import urllib2
import re


# In[54]:


url = "https://timesofindia.indiatimes.com/rss.cms"


# In[55]:


page = urllib2.urlopen(url)


# In[56]:


soup=BeautifulSoup(page,'html.parser')


# In[61]:


table=soup.find(lambda tag: tag.name=='table' and tag.has_attr('width') and tag['width']=="640")


# In[48]:


#table_links = re.findall('''((http|ftp)s?://.*)''',url)


# In[83]:


#soup1=BeautifulSoup(table,'html.parser')
#print table
#table.prettify()
table_links=[]
for link in table.findAll('a'):
#, attrs={'href': re.compile("^http://")}):
#table_links.append(table_links.get('href'))
    print (link.get('href'))


# In[64]:


for anchor in table.findAll('a',href=True);
    #table_links = {}
    #table_links['Link'] = item.title.text
    #news_item['description'] = item.description.text
    #news_item['link'] = item.link.text
    #news_item['image'] = item.content['url']
    #news_items.append(news_item)


# In[49]:


print table_links


# In[50]:


print(table_links)

