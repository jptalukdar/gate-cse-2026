# Graph Theory

## Short Notes
- **Graph $G(V, E)$**: A set of vertices $V$ and edges $E$.
- **Degree $deg(v)$**: Number of edges incident to $v$.
- **Path**: Sequence of edges connecting two vertices.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected Graph**: There is a path between every pair of vertices.
- **Planar Graph**: Can be drawn without edge crossings.

## Key Theories & Formulas

### 1. Handshaking Lemma
- Sum of degrees = $2 \times |E|$.
- $\sum_{v \in V} deg(v) = 2|E|$.
- **Corollary**: The number of vertices with odd degree is always even.

### 2. Types of Graphs
- **Complete Graph ($K_n$)**: Every pair is connected. $|E| = \binom{n}{2} = \frac{n(n-1)}{2}$.
- **Bipartite Graph ($K_{m,n}$)**: Vertices partitioned into two sets. Edges only between sets. Max edges = $m \times n$.
- **Tree**: Connected graph with no cycles. $|E| = |V| - 1$.
- **Euler Graph**: Contains a closed walk covering all edges exactly once. Exists iff all vertices have **even degree**.
- **Hamiltonian Graph**: Contains a cycle visiting every vertex exactly once. (NP-Complete to check).

### 3. Planarity (Euler's Formula)
- For a connected planar graph: $V - E + R = 2$ (where $R$ is regions/faces).
- **Kuratowski's Theorem**: A graph is non-planar iff it contains a subgraph homeomorphic to $K_5$ or $K_{3,3}$.

### 4. Graph Coloring
- **Chromatic Number $\chi(G)$**: Min colors to color vertices such that no adjacent vertices share a color.
- $\chi(G) \le \Delta(G) + 1$ (where $\Delta$ is max degree).
- For Planar graphs, $\chi(G) \le 4$. (Four Color Theorem).

---

## Example Problems

**Problem**: What is the max number of edges in a bipartite graph with 12 vertices?
- To maximize $m \times n$ where $m+n=12$, we set $m=n=6$.
- Max edges = $6 \times 6 = 36$.

**Problem**: A planar graph has 10 vertices and 15 edges. How many regions?
- $V - E + R = 2$
- $10 - 15 + R = 2$
- $-5 + R = 2 \implies R = 7$.

---

## Hardest GATE Questions

**Topic: Isomorphism and Spectrum**

**Tricky Question**:
Which of the following is a necessary condition for two graphs to be isomorphic?
1. Same number of vertices.
2. Same number of edges.
3. Same degree sequence.
4. Same chromatic number.
(All are necessary, but none are sufficient).

**Hard Question**: Number of non-isomorphic abelian groups of order 8... (Wait, this is Group Theory).
**Hard Graph Question (GATE 2017)**:
Let $G$ be a simple undirected graph. Let $A$ be the adjacency matrix. The eigenvalues of $A$ are $\lambda_1 \ge \lambda_2 \ge ...$.
If $G$ is a $K_4$, what are the eigenvalues?
- **Analysis**:
  - $K_n$ Adjacency matrix has 0s on diagonal, 1s elsewhere.
  - $A = J - I$, where $J$ is all-ones matrix.
  - Eigenvalues of $J$ are $n$ (once) and $0$ ($n-1$ times).
  - Eigenvalues of $J-I$ are $n-1$ (once) and $0-1 = -1$ ($n-1$ times).
  - For $K_4$, $n=4$.
  - Eigenvalues are $3, -1, -1, -1$.
- **Why it's hard**: Links Linear Algebra (Eigenvalues) with Graph Theory ($K_n$).

---

## References
- [Graph theory (Wikipedia)](https://en.wikipedia.org/wiki/Graph_theory)
