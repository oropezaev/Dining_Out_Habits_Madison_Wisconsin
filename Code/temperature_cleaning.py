#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[83]:


rv = pd.read_csv('reviews_madison.csv')
ba = pd.read_csv('business_attributes_madison.csv')
bs = pd.read_csv('business_madison.csv')
ci = pd.read_csv('checkin_madison.csv')
ws = pd.read_csv('weather_summary.csv')
#wr1 = pd.read_csv('weather1.csv')
#wr2 = pd.read_csv('weather2.csv')
#sw = pd.read_csv('storm_data.csv')


# In[90]:


ws.set_index("DATE", inplace = True)


# In[77]:


list_col = list(rv.columns)
print(list_col)
list_col = list(ba.columns)
print(list_col)
list_col = list(bs.columns)
print(list_col)
list_col = list(ci.columns)
print(list_col)
list_col = list(ws.columns)
print(list_col)


# In[138]:


list(ws.columns)
#ttc = ws.drop([clm for clm in list(ws.columns) if clm not in ['STATION','NAME','LATITUDE','LONGITUDE','DATE','TAVG','TMIN','TMAX']], axis = 1)
tt = ws.drop([clm for clm in list(ws.columns) if clm not in ['DATE','TAVG','TMIN','TMAX']], axis = 1)


# In[160]:


temp = tt.groupby('DATE').mean()


# In[189]:


temp['TAVG'].plot(figsize=(15,5))
plt.title('Madison (Dane County) Temperature - TAVG')
plt.ylabel('Temerature (F)')
plt.savefig('temperature_TAVG.png')


# In[191]:


temp.to_csv('temperature_madison_dana_county_2005_03_to_2017_12.csv')

