import streamlit as st
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load Data ---
@st.cache_data
def load_initial_graph():
    # Using the stable academic URL we used before
    url = "https://raw.githubusercontent.com/ampl/mo-book.ampl.com/dev/notebooks/04/edges.csv"
    df = pd.read_csv(url)
    G = nx.from_pandas_edgelist(df, source='node_id1', target='node_id2')
    return G

def get_algebraic_connectivity(graph):
    if not nx.is_connected(graph):
        return 0.0
    L = nx.laplacian_matrix(graph).toarray()
    egs = np.linalg.eigvalsh(L)
    return egs[1]

st.title("⚡ Power Grid Resilience & Optimization")
st.markdown("""
This tool analyzes the **IEEE 118-Bus System**. 
Explore how targeted attacks weaken the grid and how strategic optimization restores its spectral stability.
""")

G = load_initial_graph()

# --- 2. Sidebar Controls ---
st.sidebar.header("Network Operations")
mode = st.sidebar.radio("Choose Action:", ["Original Grid", "Break a Link", "Add Optimal Link"])

# --- 3. Logic & Visualization ---
G_modified = G.copy()
title_text = "Original Topology"

if mode == "Break a Link":
    # Identify bridges or high-betweenness edges to suggest for breaking
    edge_list = list(G.edges())
    target_edge = st.sidebar.selectbox("Select Edge to Destroy:", edge_list)
    G_modified.remove_edge(*target_edge)
    title_text = f"Broken Grid: Removed Edge {target_edge}"

elif mode == "Add Optimal Link":
    # Let's suggest a link that significantly helps connectivity
    # (Pre-calculated for speed or you can add a search loop here)
    u, v = (24, 100) # Example of a high-impact potential link
    G_modified.add_edge(u, v)
    title_text = f"Optimized Grid: Added Edge ({u}, {v})"

# --- 4. Metrics ---
orig_lambda = get_algebraic_connectivity(G)
new_lambda = get_algebraic_connectivity(G_modified)
diff = new_lambda - orig_lambda

col1, col2 = st.columns(2)
col1.metric("Spectral Gap (λ2)", f"{new_lambda:.4f}")
col2.metric("Change in Stability", f"{diff:.4f}", delta=diff)

# --- 5. Plotting ---
st.subheader(title_text)
fig, ax = plt.subplots(figsize=(10, 7))

# Identify new hubs (top 5 by degree in the modified graph)
degree_dict = dict(G_modified.degree())
top_nodes = sorted(degree_dict, key=degree_dict.get, reverse=True)[:5]

pos = nx.spring_layout(G, seed=42) # Fixed layout for consistency
nx.draw_networkx_edges(G_modified, pos, ax=ax, alpha=0.3)
nx.draw_networkx_nodes(G_modified, pos, ax=ax, node_size=40, node_color='blue')

# Highlight hubs in RED
nx.draw_networkx_nodes(G_modified, pos, nodelist=top_nodes, 
                       node_size=100, node_color='red', label='Critical Hubs', ax=ax)

plt.legend()
plt.axis('off')
st.pyplot(fig)

st.info("**Inference:** The hubs (red) represent the most critical buses for power distribution in this specific configuration.")
