# Vulnerability Assessment and Spectral Optimization of Power Grid Networks

## [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://network-analysis-and-optimization-of-power-grid-network-cdvhav.streamlit.app/)

---

## Introduction

This project investigates the structural integrity and synchronization stability of the **IEEE 118-Bus power system**. Using concepts from **Network Science** and **Spectral Graph Theory**, the study identifies structurally critical components within the grid and proposes mathematically grounded optimization strategies to improve resilience against targeted failures and attacks.

---

## Fundamental Definitions

### 1. Network Topology and Connectivity

A power grid can be modeled as an undirected graph:

$$
G = (V, E)
$$

Where:

- $V$ represents the set of electrical buses (nodes)  
- $E$ represents the set of transmission lines (edges)

#### Bridges

A **bridge** is an edge whose removal disconnects the graph.

In power infrastructure, bridges represent **single points of failure**, where the loss of one transmission line can fragment the network.

#### Largest Connected Component (LCC)

The **Largest Connected Component (LCC)** is the largest subset of nodes such that a path exists between every pair of nodes.

The reduction in LCC size during failures serves as a primary indicator of **network fragmentation and collapse**.

---

### 2. Centrality and Node Importance

Centrality measures quantify the structural importance of nodes within the network.

#### Degree Centrality

Degree centrality measures the number of direct connections of a node.

Nodes with high degree act as **local hubs** and play a key role in power distribution.

#### Betweenness Centrality

Betweenness centrality measures how frequently a node appears on the shortest paths between other nodes.

Nodes with high betweenness centrality:

- Control power flow across the network  
- Act as structural bottlenecks  
- Represent **high-value targets in deliberate attacks**

---

## Mathematical Inference: Spectral Graph Theory

### Graph Laplacian

The structural properties of the network are encoded in the **Graph Laplacian Matrix**:

$$
L = D - A
$$

Where:

- $D$ is the degree matrix  
- $A$ is the adjacency matrix  

The eigenvalues of $L$ reveal fundamental structural and dynamical properties of the network.

---

### Algebraic Connectivity ($\lambda_2$)

The second smallest eigenvalue of the Laplacian, denoted by $\lambda_2$, is called:

- **Algebraic Connectivity**
- **Spectral Gap**

#### Mathematical Interpretation

$\lambda_2$ provides a lower bound for:

- Node connectivity  
- Network robustness  
- Graph conductance  

A larger value indicates a more strongly connected network.

#### Physical Interpretation in Power Systems

In electrical power networks, $\lambda_2$ governs:

- Synchronization stability  
- Frequency stability  

A smaller spectral gap indicates a network that is more vulnerable to:

- Desynchronization  
- Cascading failures  
- Instability during disturbances  

---

## Analysis and Methodology

### Targeted Attack Simulation

The project simulates a **targeted attack strategy** by iteratively removing nodes with the highest betweenness centrality.

#### Key Result

The network exhibits **non-linear collapse behavior**.

Removing a small fraction of critical nodes leads to:

- A rapid decrease in $\lambda_2$
- Loss of synchronization stability
- Structural weakening before complete fragmentation

This demonstrates that **functional collapse occurs before topological collapse**.

---

### Bridge Fragmentation Analysis

Removing all bridge edges isolates the network into smaller components.

This reveals:

- Core clusters capable of functioning as autonomous microgrids  
- Peripheral nodes highly vulnerable to disconnection  

This analysis helps identify structurally weak regions of the grid.

---

### Spectral Optimization (Redundancy Design)

To improve network robustness, a **greedy spectral optimization algorithm** was developed.

The algorithm evaluates potential new transmission lines and selects those that maximize:

$$
\lambda_2
$$

#### Key Insight

Strategic addition of a small number of redundant transmission lines can:

- Significantly increase algebraic connectivity  
- Improve synchronization stability  
- Enhance structural robustness  

This transforms the network from a fragile topology into a highly resilient structure.

---

## Conclusions

This project demonstrates that **spectral graph analysis provides deeper insight into power grid vulnerability than purely topological measures**.

Optimizing the network based on algebraic connectivity enables:

- Improved structural resilience  
- Enhanced synchronization stability  
- Increased resistance to targeted attacks  

Rather than adding transmission lines randomly, **spectral optimization provides a mathematically optimal strategy for strengthening power grid networks**.

---

## Technical Stack

**Language**

- Python

**Libraries**

- NetworkX — Graph algorithms and network analysis  
- NumPy — Linear algebra and eigenvalue computation  
- Matplotlib — Visualization  
- Streamlit — Interactive deployment  

**Dataset**

- IEEE 118-Bus Power System
