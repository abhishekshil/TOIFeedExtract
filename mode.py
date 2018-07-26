import os
import pandas as pd
import requests
import lxml.etree
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
import warnings

warnings.filterwarnings("ignore")
url_list = ["http://feeds.reuters.com/reuters/businessNews",
            "http://feeds.reuters.com/reuters/technologyNews",
            "http://feeds.reuters.com/reuters/sportsNews",
            ]
documents = []

for url in url_list:
    response = requests.get(url)
    xml_page = response.text
    parser = lxml.etree.XMLParser(recover=True, encoding='utf-8')
    documents.append(lxml.etree.fromstring(xml_page.encode("utf-8"), parser=parser))

def print_tag(node):
    print ("<%s %s>%s" % (node.tag, " ".join(["%s=%s" % (k,v)for k,v in node.attrib.iteritems()]), node.text))
    for item in node[:25]:
        print ("  <%s %s>%s</%s>" % (item.tag, " ".join(["%s=%s" % (k,v)for k,v in item.attrib.iteritems()]), item.text, item.tag))
    print ("</%s>" % node.tag)
temp_node = documents[0]
print(temp_node)
temp_node=temp_node[0]
print_tag(temp_node)

title_list = []
description_list = []
category_list = []

for xml_doc in documents:
    articles = xml_doc.xpath("//item")
    for article in articles:
        title_list.append(article[0].text)
        description_list.append(article[1].text)
        category_list.append(article[2].text)
        

news_data = pd.DataFrame(title_list, columns=["title"])
news_data["description"] = description_list
news_data["category"] = category_list
#news_data["short_description"] = [item[item.find(" - ")+3:item.find("<")] for item in news_data["description"]]
print(news_data)

corpus = news_data["title"]
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus).toarray()
X.shape
#vectorizer.get_feature_names()
categories = news_data["category"].unique()
category_dict = {value:index for index, value in enumerate(categories)}
results = news_data["category"].map(category_dict)
vectorizer.get_feature_names()
print("corpus size: %s" % len(vectorizer.get_feature_names()))
x_train,x_test, y_train,y_test = train_test_split(X, results, test_size=0.25, random_state=1, )
clf = MultinomialNB()
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
category_dict
clf.predict(x_test)

text = ["Isro allows 3 industries to make 27 satellites"]
vec_text = vectorizer.transform(text).toarray()
List=list(category_dict.values())
key=list(category_dict.keys())
key[List.index(clf.predict(vec_text)[0])]