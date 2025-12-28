# Dynamic Programming & Greedy Algorithms

## Short Notes
Two major paradignms for optimization problems.

### Greedy Method
Makes the locally optimal choice at each step in the hope of finding the global optimum.
- **Applications**: Huffman Coding, Fractional Knapsack, Prim's, Kruskal's, Dijkstra's.

### Dynamic Programming (DP)
Solves complex problems by breaking them into simpler subproblems and storing the results (Memoization/Tabulation).
- **Requirements**: Overlapping subproblems, Optimal substructure.
- **Applications**: 0/1 Knapsack, Matrix Chain Multiplication, LCS, Floyd-Warshall.

## Key Theories & Formulas

### 1. Huffman Coding
- Goal: Minimum length prefix codes.
- Complexity: $O(n \log n)$.
- Average bits per character = $\sum (P_i \times L_i)$.

### 2. Matrix Chain Multiplication
- Complexity: $O(n^3)$.
- Number of ways to parenthesize: Catalan Number $C_n$.

---

## Example Problems

**Problem:** Find Huffman code for probabilities: $A: 0.5, B: 0.25, C: 0.125, D: 0.125$.
1. Combine C and D (0.25).
2. Combine Result with B (0.5).
3. Combine Result with A (1.0).
**Result:** A=0, B=10, C=110, D=111. Avg length: $1(0.5) + 2(0.25) + 3(0.125) + 3(0.125) = 0.5 + 0.5 + 0.375 + 0.375 = 1.75$ bits.

---

## Hardest GATE Questions

**Topic: Greedy failure in 0/1 Knapsack**
**Tricky Question (GATE 2011/2016):**
Can Greedy (based on value/weight ratio) solve the 0/1 Knapsack problem?
- **Analysis:** **NO**. Greedy only works for the **Fractional** Knapsack. In 0/1, avoiding a high-ratio item to fit two slightly lower-ratio items might be better.
- **The "Trap":** Sometimes the question gives specific weights and values where greedy *happens* to give the optimal answer, and asks if it's "always" optimal.
- **Hard Aspect:** Identifying the DP recurrence for specific problems.
  - Example: $T(i, j) = max(T(i-1, j), T(i-1, j-w_i) + v_i)$. 
  - Question: "Which of the following entries in the DP table is accessed to calculate $T(n, W)$?"
- **Complexity:** Comparison of Huffman bits for different frequencies. Finding the range of bits for the most frequent character.
