import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
from matplotlib import cm
from community import community_louvain
from collections import Counter






interaction_matrix=pd.read_csv('data/voting_interaction_matrix.csv', index_col=0)
user_in_interaction_=pd.read_csv('data/voting_interaction_matrix.csv')
user_in_interaction=user_in_interaction_.index

# Create a graph from the interaction matrix
# We'll assume a weighted undirected graph where the weight is the voting interaction (1 or 0)
G = nx.Graph()

for user in interaction_matrix.index:
    for admin, vote in interaction_matrix.loc[user].items():
        if vote > 0:  
            G.add_edge(user, admin, weight=vote)

resolution=2
partition = community_louvain.best_partition(G, resolution=resolution)

nx.set_node_attributes(G, partition, "community")

community_sizes = Counter(partition.values()) 
num_communities = len(set(partition.values()))

min_size = 5
small_communities = {community for community, size in community_sizes.items() if size < min_size}
nodes_to_remove = [node for node, community in partition.items() if community in small_communities]
G_filtered = G.copy()
G_filtered.remove_nodes_from(nodes_to_remove)
updated_partition = {node: community for node, community in partition.items() if community not in small_communities}
community_sizes_updated = Counter(updated_partition.values()) 
print("Updated community sizes:", community_sizes_updated)
num_communities_updated = len(set(updated_partition.values()))
print(f"Number of communities detected: {num_communities_updated}")

# treat User Categories ---------------------------------------------------
feature_matrix=pd.read_csv('data/all_features_dataframe.csv')
feature_matrix = feature_matrix.drop_duplicates(subset='username', keep='first')

feature_matrix['community'] = feature_matrix['username'].map(updated_partition)
df_melted = feature_matrix.melt(
    id_vars=['username', 'community'],
    value_vars=['categ1', 'categ2', 'categ3', 'categ4'],
    var_name='category_level',
    value_name='category'
).dropna(subset=['category'])  

category_counts = df_melted.groupby(['community', 'category']).size().reset_index(name='count')

community_sizes = feature_matrix.groupby('community').size().reset_index(name='total_users')

category_counts = category_counts.merge(community_sizes, on='community')

category_counts['percentage'] = (category_counts['count'] / category_counts['total_users']) * 100

category_counts = category_counts.sort_values(by=['community', 'percentage'], ascending=[True, False])
top_categories = category_counts.groupby('community').head(3)
 
community_top_categories = top_categories.groupby('community').apply(
    lambda group: "<br>".join(
        [f"{row['category']}: {row['percentage']:.2f}%" for _, row in group.iterrows()]
    )
).to_dict()

admin_scores = feature_matrix.iloc[:, 1]
feature_matrix['admin_score'] = admin_scores

mean_admin_scores = feature_matrix.groupby('community')['admin_score'].mean().to_dict()


# Interactive plot-------------------------------------------------------------------------------
community_sizes = {}
for node, community in updated_partition.items():
    if community not in community_sizes:
        community_sizes[community] = 0
    community_sizes[community] += 1

community_graph = nx.Graph()

for community, size in community_sizes.items():
    community_graph.add_node(community, size=size)

for node1, node2 in G_filtered.edges:
    community1 = updated_partition[node1]
    community2 = updated_partition[node2]
    if community1 != community2:  
        if not community_graph.has_edge(community1, community2):
            community_graph.add_edge(community1, community2, weight=0)
        community_graph[community1][community2]['weight'] += 1

pos = nx.spring_layout(community_graph, k=20, iterations=100)

node_x = []
node_y = []
node_sizes = []
node_text = []
node_ids = []
for node, coords in pos.items():
    node_x.append(coords[0])
    node_y.append(coords[1])
    node_sizes.append(community_graph.nodes[node]['size'] * 10)
    top_category_info = community_top_categories.get(node, "No data available")
    mean_admin_score = mean_admin_scores.get(node, "No score available")
    node_text.append(
        f"Community {node}<br>"
        f"Users: {community_graph.nodes[node]['size']}<br>"
        f"Mean Admin Score: {mean_admin_score:.2f}<br>"
        f"{top_category_info}"
    )
    node_ids.append(node)
node_sizes = np.power(np.log10(node_sizes), 3) - 3

max_weight = max(data['weight'] for _, _, data in community_graph.edges(data=True))
min_weight = min(data['weight'] for _, _, data in community_graph.edges(data=True))

edges = {}
for community1, community2, data in community_graph.edges(data=True):
    x0, y0 = pos[community1]
    x1, y1 = pos[community2]
    weight = data['weight']
    normalized_thickness = 1 + (5 * (weight - min_weight) / (max_weight - min_weight))  # Scale between 1 and 6
    edges[(community1, community2)] = {
        "x": [x0, x1, None],
        "y": [y0, y1, None],
        "weight": weight,
        "thickness": normalized_thickness
    }


unique_communities = set(updated_partition.values()) 
num_communities = len(unique_communities)

community_colors = [to_hex(c) for c in cm.Pastel1(np.linspace(0, 1, num_communities))]

community_color_map = {community: community_colors[i % len(community_colors)] 
                       for i, community in enumerate(unique_communities)}

user_color_map = {node: community_color_map[updated_partition[node]] 
                  for node in G_filtered.nodes}

node_color_map = {node: community_color_map[node] for node in node_ids}



fig = go.Figure()

fig.add_trace(go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    marker=dict(
        size=node_sizes,
        color=[node_color_map[node] for node in node_ids],  
        line=dict(width=2, color="black")
    ),
    hovertext=node_text,
    hoverinfo="text",
    customdata=node_ids,
    name="Communities"
))

max_thickness = max(edge_data["thickness"] for edge_data in edges.values())
min_thickness = min(edge_data["thickness"] for edge_data in edges.values())

for (community1, community2), edge_data in edges.items():
    normalized_thickness = (edge_data["thickness"] - min_thickness) / (max_thickness - min_thickness)
    edge_opacity = 0.2 + 0.8 * normalized_thickness
    
    fig.add_trace(go.Scatter(
        x=edge_data["x"],
        y=edge_data["y"],
        mode="lines",
        line=dict(width=edge_data["thickness"], color="#BABABA"),  
        hoverinfo="none",
        name=f"Edge {community1}-{community2}",
        opacity=edge_opacity  
    ))

fig.update_layout(
    plot_bgcolor="white",  
    paper_bgcolor="white",  
    showlegend=False, 
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False  
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False  
    ),
    height=800,
    width=800,
    margin=dict(l=50, r=50, t=50, b=50),  
    title=dict(
        text="Community Graph",  
        font=dict(size=20),  
        x=0.5,  
        y=0.95  
    )
)

fig.show()

def plot_interactive_graph():
    fig = go.Figure()
    fig.show()


def plot_static_graph():
    import matplotlib.pyplot as plt
    import networkx as nx
    from matplotlib.colors import to_hex
    import matplotlib.transforms as transforms

    fig, ax = plt.subplots(figsize=(15, 15))
    pos = nx.spring_layout(G_filtered, seed=42)
    node_colors = [user_color_map[node] for node in G_filtered.nodes]
    node_sizes = [G_filtered.degree(node) * 10 for node in G_filtered.nodes]

    rotate = transforms.Affine2D().rotate_deg(90)
    ax.transData = rotate + ax.transData

    nx.draw_networkx_edges(
        G_filtered,
        pos=pos,
        ax=ax,
        alpha=0.05,
        width=0.2
    )
    nx.draw_networkx_nodes(
        G_filtered,
        pos=pos,
        ax=ax,
        node_size=node_sizes,
        node_color=node_colors,
        linewidths=0.5,
        edgecolors="black"
    )

    plt.axis("off")
    plt.show()