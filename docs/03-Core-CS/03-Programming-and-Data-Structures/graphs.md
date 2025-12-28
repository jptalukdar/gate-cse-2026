# Graphs

## Short Notes
A graph consists of vertices ($V$) and edges ($E$).

### Representations
- **Adjacency Matrix**: $V \times V$ matrix. Good for dense graphs. Space: $O(V^2)$.
- **Adjacency List**: Array of lists. Good for sparse graphs. Space: $O(V + E)$.

## Key Theories & Formulas

### 1. BFS vs DFS
- **BFS (Breadth-First Search)**: Uses a **Queue**. Finds the shortest path in an unweighted graph.
- **DFS (Depth-First Search)**: Uses a **Stack** (or recursion). Used for cycle detection, topological sort.

### 2. Connected Components
- **Directed Graph**: Strongly Connected if path exists between every pair $(u, v)$ in both directions.
- **Undirected Graph**: Connected if path exists between every pair.

---

## Example Problems

**Problem:** Find the space complexity of an adjacency matrix for a graph with 100 vertices.
- Matrix size: $100 \times 100 = 10,000$ entries.
- Space: $O(V^2)$.

---

## Hardest GATE Questions

**Topic: BFS/DFS Edge Classification**
**Tricky Question (GATE 2014/15/21):**
During a DFS, an edge $(u, v)$ is found where $v$ is an ancestor of $u$. What type of edge is this?
- **Analysis:** **Back Edge**.
- Types:
  - **Tree Edge**: Part of the DFS tree.
  - **Back Edge**: Edge to an ancestor. (Indicates Cycle).
  - **Forward Edge**: Edge to a descendant.
  - **Cross Edge**: Between siblings or subtrees.
- **The "Trap":** In an **Undirected Graph**, only Tree Edges and Back Edges exist. Forward and Cross edges are impossible.
- **Complexity:** Number of possible BFS/DFS sequences for a given graph.
  - Rule: A BFS sequence must visit all neighbors of a node before moving to neighbors of neighbors.
  - Question: "Which of the following CANNOT be a BFS traversal of this graph?"

---

## References
- [Graph (abstract data type) (Wikipedia)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type))
- [Breadth-first search (Wikipedia)](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Depth-first search (Wikipedia)](https://en.wikipedia.org/wiki/Depth-first_search)
