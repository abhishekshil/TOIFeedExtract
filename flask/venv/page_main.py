import re
from linkGrabber import Links
import pandas as pd
import requests


url = "https://timesofindia.indiatimes.com/rss"
response = requests.get(url)
tables = pd.read_html(url)
print(tables[0])

##documents = Links(url)
#documents.find(duplicates=False, pretty=True)
#print(documents)

