import requests
import lxml.etree
import db_conn
import re
import fileinput
import os
import pandas as pd
def run():
        documents = []
        response=[]

        url_list = db_conn.final_link
        categories = db_conn.links_list
        counter=0
        with open ('temp1.json', 'w') as f:
            f.seek (0)
            f.write ('{"Response":[')
        for url in url_list:

            response = requests.get(url)
            xml_page = response.text
            parser = lxml.etree.XMLParser(recover=True, encoding='utf-8')
            documents.append(lxml.etree.fromstring(xml_page.encode("utf-8"), parser=parser))
            cat=categories[counter]
            counter=counter+1
            panda_n(documents,cat)
            documents.clear()
        fn = "temp1.json"
        text_to_search = [',,,,', ',,,', ',,']
        text_to_replace = [',', ']}', ',']
        for i in range (len (text_to_search)):
            with fileinput.FileInput (fn, inplace=True, backup='.bak') as file:
                for line in file:
                    print (line.replace (text_to_search[i], text_to_replace[i]), end='')


def panda_n(documents,cat):
        title_list = []
        cati=[]
        id=[]
        description_list = []
        guid_url_list = []
        dop = []

        for xml_doc in documents:
                #articles = xml_doc.xpath ("//item")
                title_list=xml_doc.xpath ("//title/text()")
                description_list=xml_doc.xpath ("//description/text()")
                guid_url_list= xml_doc.xpath ("//link/text()")
                dop=xml_doc.xpath ("//pubDate/text()")
        a=len(title_list)
        b=len(description_list)
        c=len(guid_url_list)
        d=len(dop)

        del title_list[0:a-min(a,b,c,d)]
        del description_list[0:b-min(a,b,c,d)]
        del guid_url_list[0:c-min(a,b,c,d)]
        del dop[0:d-min(a,b,c,d)]
        for i in range(len(dop)):
            id.append(i+1)
            cati.append(cat)



        news_data = pd.DataFrame (id, columns=["Article Id"])
        news_data["Categories"] = cat
        news_data["Title"]=title_list

        news_data["description"] = description_list
        news_data["short_description"] = [item[item.find (" - ") + 1:item.find ("<")] for item in
                                          news_data["description"]]
        #news_data["category"] = categories
        news_data["links"]=guid_url_list
        news_data["Date Of Publishing"]=dop
        with open ('temp1.json', 'a') as f:
           f.write (news_data.to_json (orient='records')[1:-1].replace('}][{', '},{'))
           f.write(',')

        #print(news_data)
        #print(news_data.to_json(orient='records',lines=True))

    #return (news_data)
run()