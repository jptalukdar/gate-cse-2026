# ⚡ Cheatsheet: Algorithms

## Time & Space Complexity

| Algorithm | Best | Average | Worst | Space | Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** | $\Omega(n^2)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Bubble Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Insertion Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Merge Sort** | $\Omega(n \log n)$| $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | $\Omega(n \log n)$| $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No |
| **Heap Sort** | $\Omega(n \log n)$| $\Theta(n \log n)$ | $O(n \log n)$ | $O(1)$ | No |

## Master Theorem
$$T(n) = aT(n/b) + f(n)$$
Compare $n^{\log_b a}$ vs $f(n)$.
1. **Case 1**: $f(n) = O(n^{\log_b a - \epsilon}) \implies T(n) = \Theta(n^{\log_b a})$
2. **Case 2**: $f(n) = \Theta(n^{\log_b a}) \implies T(n) = \Theta(n^{\log_b a} \log n)$
   - Extension: If $f(n) = \Theta(n^{\log_b a} \log^k n) \implies T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$ (for $k \ge 0$)
3. **Case 3**: $f(n) = \Omega(n^{\log_b a + \epsilon}) \implies T(n) = \Theta(f(n))$ (Structure condition required)

## Graph Algorithms
| Algorithm | Complexity (Adjacency List) | Application |
| :--- | :--- | :--- |
| **BFS** | $O(V+E)$ | Shortest Path (Unweighted) |
| **DFS** | $O(V+E)$ | Cycle Detection, Topo Sort |
| **Dijkstra** | $O(E \log V)$ or $O(E + V \log V)$ (Fib Heap) | SSSP (Non-negative weights) |
| **Bellman-Ford**| $O(VE)$ | SSSP (Negative weights allowed) |
| **Floyd-Warshall**| $O(V^3)$ | All-Pairs Shortest Path |
| **Prim's** | $O(E \log V)$ or $O(E + V \log V)$ | MST |
| **Kruskal's** | $O(E \log E)$ or $O(E \log V)$ | MST |

## ⚠️ Common Traps
- **Greedy vs DP**: Greedy makes locally optimal choice (e.g., Fractional Knapsack). DP solves all subproblems (e.g., 0/1 Knapsack).
- **In-Place**: Merge Sort is NOT in-place (requires $O(n)$ aux space).
- **Quick Sort Worst Case**: Happens when array is already sorted (or reverse sorted) with standard pivot.
- **Hashing**: $Load Factor (\alpha) = \frac{n}{m}$.
  - Chaining Search: $1 + \alpha$.
  - Open Addressing Unsuccessful Search: $\frac{1}{1-\alpha}$.
