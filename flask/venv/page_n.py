import lxml.etree
import requests
import pandas as pd
import db_conn
import numpy as np
import array
url_list =db_conn.final_link
url_name=db_conn.links_list
documents = []
#title_list = []
#description_list = []
#links = []
#pub_dates = []
def content(documents):
    #title_list.clear()
    #links.clear()
    #description_list.clear()
    #pub_dates.clear()
    for xml_doc in documents:
           articles = xml_doc.xpath ("//item")
           #articles = xml_doc.find_all ('item')
           for article in articles:
               title_list=article.xpath("//title/text()")
               description_list= article.xpath("//description/text()")
               links=article.xpath("//link/text()")
               pub_dates=article.xpath("//pubDate/text()")

    output=[]
    for info in zip(title_list,description_list,links,pub_dates):
        resp={}
        resp['Title']=info[0]
        resp['Description'] = info[1]
        resp['Link'] = info[2]
        resp['Publishing Date'] = info[3]
        output.append(resp)

    print(output)

        # print( np.array([title_list,description_list,links,pub_dates]))
   #news_data["description"] = description_list
    #news_data["links"] = links
    #news_data["publishing Dates"]=pub_dates
    #print((news_data))
    #news_data
    #for disp in (title_list,description_list,links,pub_dates):
     #       print ((disp))
      #      disp.clear()


for url in url_list:
    response = requests.get (url)
    xml_page = response.text
    parser = lxml.etree.XMLParser (recover=True, encoding='utf-8')
    documents.append (lxml.etree.fromstring (xml_page.encode ("utf-8"), parser=parser))
    content(documents)
    documents.clear()

#def print_tag(node):
#    print ("<%s %s>%s"  % (node.tag, " ".join(["%s=%s" % (k,v)for k,v in node.attrib.iteritems()]), node.text))
#   for item in node[:25]:
#        print ("  <%s %s>%s</%s>" % (item.tag, " ".join(["%s=%s" % (k,v)for k,v in item.attrib.iteritems()]), item.text, item.tag))
#    print ("</%s>" % node.tag)

#temp_node = documents[0]
#print_tag(temp_node)

#temp_node = temp_node[0]
#print_tag(temp_node)

#temp_node = temp_node.xpath("item")[0]
#print_tag(temp_node)





#news_data = pd.DataFrame(title_list, columns=["title"])
#news_data["description"] = description_list
#news_data["Page Link"] =links_list
#news_data["Publishing Date"] = pub_dates
#print (len(news_data))
#print(news_data)