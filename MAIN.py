# import relevant library's
import numpy as np
import pandas as pd
import networkx as nx

# relevant filepaths
fp_art=("articles.leptospirosis.csv")
fp_aut=("authors.leptospirosis.csv")
fp_year=("paper_counts.csv")
# create suitable data frames
df_art=pd.read_csv(fp_art)
df_aut=pd.read_csv(fp_aut)
df_year=pd.read_csv(fp_year)

# finding a way of checking for collaboration
df_aut["Full"]=df_aut["AuthorForename"]+' '+df_aut["AuthorLastname"]
df_clear=df_aut.drop(['AuthorInitials', 'AuthorAffiliation','AuthorForename','AuthorLastname'], axis=1)
ind=df_clear.set_index(["PMID","AuthorN"])
df_unstack=ind.unstack()
print(df_unstack)