# import relevant library's
import numpy as np
import pandas as pd

# relevant filepaths
fp_art=("articles.leptospirosis.csv")
fp_aut=("authors.leptospirosis.csv")
fp_year=("paper_counts.csv")
# create suitable data frames
df_art=pd.read_csv(fp_art)
df_aut=pd.read_csv(fp_aut)
df_year=pd.read_csv(fp_year)

# making a clean data frame without irrelevant columns and with a column for full name
df_aut["Full"]=df_aut["AuthorForename"]+' '+df_aut["AuthorLastname"]
df_clear=df_aut.drop(['AuthorInitials', 'AuthorAffiliation','AuthorForename','AuthorLastname'], axis=1)
# making a list of every author
AUTH=list(dict.fromkeys(df_clear['Full'].tolist()))
# making a table that counts for duplicates
count=df_clear.pivot_table(index=['Full'],aggfunc='size')
print(count)
# make a unstacked DF
ind=df_clear.set_index(["PMID","AuthorN"])
df_unstack=ind.unstack()
print(df_unstack)
# return a list of collaborator for a specific person
colab_search = np.column_stack([df_unstack[col].str.contains(r"A A Adesiyun", na=False) for col in df_unstack])
df_colab_search=df_unstack.loc[colab_search.any(axis=1)]
stack=df_colab_search.stack()
COLAB=list(dict.fromkeys(stack['Full'].tolist()))
COLAB.remove('A A Adesiyun')
# return a data frame for all authors
lst=[]
for i in AUTH:
    colab_search = np.column_stack([df_unstack[col].str.contains(i, na=False) for col in df_unstack])
    df_colab_search = df_unstack.loc[colab_search.any(axis=1)]
    stack = df_colab_search.stack()
    COLAB = list(dict.fromkeys(stack['Full'].tolist()))
    COLAB.remove(i)
    lst.append(i)
    lst.append(COLAB)
df_COLAB=pd.DataFrame(lst,columns=['Author','collaborators'])
print(df_COLAB)

