#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
os.getcwd()#查看文件应该存放在哪里


# In[3]:


data = pd.read_csv('C:\\Users\\13810\\tmdb_5000_movies.csv')


# In[8]:


import pdpipe as pdp#导入pdpipe包


# In[13]:


#创建pdp.pdppipeline ,其中pdp.ColDrop和pdp.ApplyByCols和pdp.Rowdrop都是pdpipe中常用的API，是固定写法，有固定的语法格式
first_pipeline = pdp.PdPipeline(
[pdp.ColDrop("original_title"),#ColDrop用于对指定单个或多个列进行丢弃
 pdp.ApplyByCols(columns=['title'], func=lambda x: x.lower()),#对每一列进行应用
 pdp.RowDrop({'vote_average': lambda x: x <= 7, 'original_language': lambda x: x != 'en'}),#对行进行删除
 pdp.ApplyByCols(columns=['genres'], func=lambda x: [item['name'] for item in eval(x)].__len__(), result_columns=['genres_num']),
 pdp.RowDrop({'genres_num': lambda x: x <= 5})]
)


# In[19]:


data1=first_pipeline(data, verbose=True).reset_index(drop=True)
 pdp.RowDrop({'vote_average': lambda x: x <= 7, 'original_language': lambda x: x != 'en'}),
 pdp.ApplyByCols(columns=['genres'], func=lambda x: [item['name'] for item in eval(x)].__len__(), re


# In[20]:


data1


# In[ ]:




