#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys 
import time 
import requests
import codecs
import random
url = requests.get('https://news.yahoo.co.jp/')
soup = BeautifulSoup(url.content,'html.parser')
news1 =  soup.find(class_='contentsWrap').find(class_='toptopics_list').get_text().strip()
#news2 =  soup.find_all(class_='listFeedWrapBox')[1].find(class_='titl').get_text().strip()
#news3 =  soup.find_all(class_='listFeedWrapBox')[2].find(class_='titl').get_text().strip()
#news4 =  soup.find_all(class_='listFeedWrapBox')[3].find(class_='titl').get_text().strip()
#text  = news1 + " :" +  news2  + " :" +  news3  + " :" +  news4
text = news1.replace(" ","").split("\n")
contents = [] 
for news in text:
    if news == "NEW" or news == "":
        pass 
    else:
        contents.append(news)
contents = contents[:-2]
random.shuffle(contents) 
#i = int(time.time()%500)
i=0
print("\r{}".format("•" + " •".join(contents)),end="")
