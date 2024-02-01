#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import IPython.display as ipd
import plotly.express as px
import matplotlib.pyplot as plt

lep_author_data = pd.read_csv('../project-leptospirosis/authors.leptospirosis.csv')
lep_article_data = pd.read_csv('../project-leptospirosis/articles.leptospirosis.csv')

