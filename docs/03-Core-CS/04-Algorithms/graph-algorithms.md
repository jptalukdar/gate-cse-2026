# Graph Algorithms

## Short Notes
Algorithms designed to solve problems on graph structures.

### Categories

- **Shortest Path**: Dijkstra, Bellman-Ford, Floyd-Warshall.
- **Minimum Spanning Tree (MST)**: Prim's, Kruskal's.

## Key Theories & Formulas

### 1. Minimum Spanning Tree (MST)

- **Kruskal's**: $O(E \log E)$. Uses Disjoint Set Union (DSU). Greedy.
- **Prim's**: $O(E \log V)$. Greedy.
- *Property:* If all edge weights are unique, the MST is unique.

### 2. Shortest Path Algorithms

- **Dijkstra**: $O((V+E)\log V)$. Unweighted/Positive weights.
- **Bellman-Ford**: $O(VE)$. Handles negative weights. Detects negative cycles.
- **Floyd-Warshall**: $O(V^3)$. All-pairs shortest path.

### 3. Complexity Table
| Algorithm | Complexity | Technique |
| :--- | :--- | :--- |
| BFS/DFS | $O(V+E)$ | Traversal |
| Kruskal | $O(E \log E)$ | Greedy |
| Prim | $O(E \log V)$ | Greedy |
| Dijkstra | $O(E \log V)$ | Greedy |
| Bellman-Ford | $O(VE)$ | DP |
| Floyd-Warshall | $O(V^3)$ | DP |

---

## Example Problems

**Problem:** In Kruskal's, if the edges are already sorted, what is the complexity?

- **Result:** $O(E \alpha(V))$ where $\alpha$ is the inverse Ackermann function (from DSU). Sorting is the bottleneck.

---

## Hardest GATE Questions

**Topic: MST Unique Edges and Cut Property**
**Tricky Question (GATE 2015/2018):**
If a graph has two edges with the same minimum weight, is the MST always unique?

- **Analysis:** No. If multiple edges have the same weight, different choices can lead to different MSTs.
- **The "Trap":** Sum of weights in MST is always unique even if the MST itself isn't.
- **Hard Aspect:** Dijkstra's behavior with negative edges.
  - Question: "Will Dijkstra find the shortest path if there is one negative edge (no cycles)?"
  - Answer: **NO**. Dijkstra might permanently set a distance to a node before seeing a later negative correction.
- **Complexity:** Number of possible Topological Sorts for a Directed Acyclic Graph (DAG). Requires finding nodes with in-degree 0 and exploring permutations

---

## References

- [Dijkstra's algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Prim's algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [Kruskal's algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
