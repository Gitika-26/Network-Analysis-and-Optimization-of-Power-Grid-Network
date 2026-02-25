# Vulnerability Assessment and Spectral Optimization of Power Grid Networks

🔗 **Streamlit Deployment:**  
[Click here to view the live app]((https://network-analysis-and-optimization-of-power-grid-network-cdvhav.streamlit.app/))

---

## Introduction

This project investigates the structural integrity and synchronization stability of the **IEEE 118-Bus system**. Utilizing **Network Science** and **Spectral Graph Theory**, the study identifies critical vulnerabilities within the grid and proposes mathematical optimizations to enhance resilience against targeted attacks.

---

## Fundamental Definitions

### 1. Network Topology and Connectivity

A power grid is modeled as an undirected graph:

\[
G = (V, E)
\]

Where:

- \(V\) represents electrical buses  
- \(E\) represents transmission lines  

**Bridges**

These are edges whose removal disconnects the graph. In infrastructure, a bridge represents a **single point of failure**.

**Largest Connected Component (LCC)**

This is the largest set of nodes where a path exists between any two members.

The reduction in LCC size during an attack is a primary measure of **network collapse**.

---

### 2. Centrality and Node Importance

Centrality metrics are used to rank the importance of buses:

**Degree Centrality**

Measures the number of direct connections.

Hubs with high degree are **local distribution centers**.

**Betweenness Centrality**

Measures the extent to which a node lies on the shortest paths between other nodes.

Nodes with high betweenness control the **flow across the system** and are often the **most critical targets**.

---

## Mathematical Inference: Spectral Graph Theory

### The Graph Laplacian

The properties of the network are encoded in the Laplacian Matrix:

\[
L = D - A
\]

Where:

- \(D\) is the degree matrix  
- \(A\) is the adjacency matrix  

The eigenvalues of \(L\) characterize the network's behavior.

---

### Algebraic Connectivity (\(\lambda_2\))

The second smallest eigenvalue of the Laplacian, \(\lambda_2\), is termed:

- **Spectral Gap**
- **Algebraic Connectivity**

**Mathematical Inference**

\(\lambda_2\) provides a lower bound on:

- Node connectivity
- Graph conductance

**Physical Inference**

In power systems, \(\lambda_2\) governs:

- Synchronization stability
- Frequency stability

A smaller gap indicates a network prone to **desynchronization**.

---

## Analysis and Methodology

### Targeted Attack Simulation

The project simulates a **Targeted Attack** by iteratively removing nodes with the highest betweenness centrality.

**Result**

The system exhibits a **non-linear collapse**.

Removing a small percentage of critical hubs causes:

- Catastrophic decrease in spectral gap
- Loss of synchronization capability

This happens **before physical fragmentation**.

---

### Bridge Fragmentation

Removing all bridges isolates the **k-core components**.

This reveals:

- Autonomous micro-grid capable clusters
- Leaf nodes most vulnerable to failure

---

### Spectral Optimization (Redundancy Design)

A greedy optimization algorithm evaluates potential new transmission lines and selects those that maximize:

\[
\lambda_2
\]

**Inference**

Strategic placement of few redundant lines:

- Significantly increases spectral gap
- Improves robustness
- Enhances synchronization stability

Transforms topology from:

- Vulnerable → Highly resilient

---

## Conclusions

This project demonstrates that **spectral analysis provides deeper insight into grid vulnerability** than simple topological metrics.

By optimizing the spectral gap, we can mathematically guarantee:

- Higher structural resilience
- Improved synchronization stability
- Better robustness against targeted attacks

---

## Technical Stack

**Language**

- Python

**Libraries**

- NetworkX — Graph Algorithms
- NumPy — Linear Algebra
- Matplotlib — Visualization
- Streamlit — Deployment

**Dataset**

- IEEE 118-Bus System

