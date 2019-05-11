
# coding: utf-8

# In[1]:


import pprint
import os
import googleapiclient.discovery
import pandas as pd
import re
import html
import numpy as np
import time
import requests
from bs4 import BeautifulSoup


# In[9]:


data = pd.read_csv('../../data/music.csv')


# In[41]:


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"

DEVELOPER_KEY = "AIzaSyBhenw27oynm5xYfmccxXbtZa-DUSfXnsU"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)


# In[42]:


# method 1: use youtube data api
#j = i
for i in range(0, 10000):
    if pd.isnull(data.loc[i,'title']):
        continue
    query = data.loc[i,'title'] + ' ' + data.loc[i,'artist.name']
    query = re.sub("[\(\[].*?[\)\]]", "", query)
    query = re.sub(r'[^A-Za-z0-9\']+', ' ', query)
    #print(i, query)
    '''
    if data.loc[i,'duration'] < 240:
        dur = 'short'
    elif data.loc[i,'duration'] > 1200:
        dur = 'long'
    else:
        dur = 'medium'
    '''
    request = youtube.search().list(
        part = 'snippet',
        maxResults=5,
        type = 'video',
        q = query
    )
    response = request.execute()['items']
    videoID = []
    list_of_words = query.split()
    for item in response:
        sentence = item['snippet']['description']+' ' + item['snippet']['title']
        sentence = html.unescape(sentence)
        if all(re.compile(r'\b'+w+r'\b', re.IGNORECASE).search(sentence) for w in list_of_words):
            videoID.append(item['id']['videoId'])
    if len(videoID) == 0:
        continue
    request = youtube.videos().list(
        part = 'statistics',
        id = ', '.join(videoID)
    )
    response = request.execute()['items']
    for item in response:
        hotness[i] += int(item['statistics']['viewCount'])  


np.savetxt('../../data/hotness.csv', hotness)

    