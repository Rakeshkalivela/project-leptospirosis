# Let's start by loading the file to get an idea of its contents and structure.
import pandas as pd

# Load the supplied CSV file
articles_file = 'C:\\Users\\admin\\Desktop\\group3\\Group 3\\articles.leptospirosis.csv'
authors_file = 'C:\\Users\\admin\\Desktop\\group3\\Group 3\\authors.leptospirosis.csv'
paper_counts_file = 'C:\\Users\\admin\\Desktop\\group3\\Group 3\\paper_counts.csv'

# Reading the files
articles_df = pd.read_csv(articles_file)
authors_df = pd.read_csv(authors_file)
paper_counts_df = pd.read_csv(paper_counts_file)

# Display the first few rows of each dataframe to understand their structure and content
articles_df.head(), authors_df.head(), paper_counts_df.head()
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from collections import Counter

# Analysis and Visualization 1: Most active researchers
# Counting the number of publications for each author
author_counts = authors_df['AuthorLastname'].value_counts().head(10)

# Visualization 2: Collaboration Networks among Top Researchers
# Filtering the dataset to include only the top researchers
top_authors = author_counts.index.tolist()
top_authors_df = authors_df[authors_df['AuthorLastname'].isin(top_authors)]

# Creating a graph to represent collaborations
collab_graph = nx.Graph()

for _, article in top_authors_df.groupby('PMID'):
    authors = article['AuthorLastname'].tolist()
    for i in range(len(authors)):
        for j in range(i+1, len(authors)):
            if collab_graph.has_edge(authors[i], authors[j]):
                collab_graph[authors[i]][authors[j]]['weight'] += 1
            else:
                collab_graph.add_edge(authors[i], authors[j], weight=1)

# Visualization 3: Research Trends Over Time
# Plotting the annual publication count
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Count', data=paper_counts_df)
plt.title('Research Publications in Leptospirosis Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()

# Displaying the three visualizations
plt.figure(figsize=(10, 6))
sns.barplot(x=author_counts.values, y=author_counts.index, palette="viridis")
plt.title('Top 10 Most Active Researchers in Leptospirosis')
plt.xlabel('Number of Publications')
plt.ylabel('Author Last Name')

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(collab_graph, k=0.1)
nx.draw_networkx(collab_graph, pos, with_labels=True, node_color='skyblue', edge_color='gray', font_size=10)
plt.title('Collaboration Network Among Top Researchers')
plt.show()
