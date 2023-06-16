import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load your data
df = pd.read_csv('net-analyze.csv')

# Display the dataframe
print(df)

# Group by 'Source' and count the number of communications
source_counts = df.groupby('Source').count().sort_values(by='No.', ascending=False)
print(source_counts)

# Group by 'Destination' and count the number of communications
destination_counts = df.groupby('Destination').count().sort_values(by='No.', ascending=False)
print(destination_counts)

# Group by 'Protocol' and count the number of communications
protocol_counts = df.groupby('Protocol').count().sort_values(by='No.', ascending=False)
print(protocol_counts)

# Create a graph using networkx
G = nx.from_pandas_edgelist(df, 'Source', 'Destination', edge_attr=True)

# Draw the graph
nx.draw_circular(G, with_labels=True)
plt.show()

# Let's say '192.168.1.2' is a suspect device
suspect = '192.168.1.2'

# Create a color map
color_map = ['red' if node == suspect else 'blue' for node in G.nodes()]

# Draw the graph with the color map
nx.draw_circular(G, node_color=color_map, with_labels=True)
plt.show()

# Create a new dataframe that includes other devices the suspect communicated with
suspect_df = df[(df['Source'] == suspect) | (df['Destination'] == suspect)]
print(suspect_df)
