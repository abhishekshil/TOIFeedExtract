import os
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
import warnings

warnings.filterwarnings("ignore")

title=[]
category=[]
ID=[]
site_root=os.path.realpath(os.path.dirname(__file__))
json_url=os.path.join(site_root,"static","temp.json")
with open(json_url,'r+') as fl:
    data=json.load(fl)

    for i in range(len(data["Response"])):
       title.append(data["Response"][i]["Title"])
       category.append(data["Response"][i]["Categories"])
       ID.append(data["Response"][i]["Article Id"])

news_data = pd.DataFrame (category, columns=["Categories"])
#news_data["Categories"] = category
news_data["Title"]=title
print(news_data)
corpus = news_data["Title"]
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus).toarray()
X.shape
#vectorizer.get_feature_names()
categories = news_data["Categories"].unique()
category_dict = {value:index for index, value in enumerate(categories)}
results = news_data["Categories"].map(category_dict)
vectorizer.get_feature_names()
print ("corpus size: %s" % len(vectorizer.get_feature_names()))
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