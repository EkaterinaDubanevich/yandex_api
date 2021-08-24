#!/usr/bin/env python
# coding: utf-8

# In[115]:


import requests
import json
import pandas as pd
import seaborn as sns
df = pd.DataFrame()


# In[116]:


url = ''
dates = ['2021-02-14', '2021-02-15', '2021-02-16']
for date in dates:
    visits = f"metrics=ym:s:visits&dimensions=ym:s:date&filters=ym:s:date=='{date}'&dimensions=ym:s:isRobot&id=44147844"
    visits_url = url + visits
    response =  requests.get(visits_url)
    
    json_data = response.json()
    
    for records in json_data['data']:
        metr = records['metrics']
        inter = records['dimensions']
        print (inter[0]['name'], inter[1]['name'])
        df = df.append([[inter[0]['name'], inter[1]['name'], metr[0]]])


# In[117]:


df.columns = ['Date', 'Type', 'Visits']
df


# In[ ]:




