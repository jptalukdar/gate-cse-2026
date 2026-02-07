# Trees

## Short Notes
A tree is a non-linear data structure with a hierarchical relationship between nodes.

### Binary Tree (BT)
A tree where each node has at most two children.

### Types of Binary Trees

- **Full**: Every node has 0 or 2 children.
- **Complete**: All levels are full except possibly the last, which is filled from left to right.
- **Perfect**: All internal nodes have 2 children and all leaves are at the same level.
- **Balanced**: Height difference of left and right subtrees of any node is $\le 1$.

## Key Theories & Formulas

### 1. Binary Tree Properties

- Max nodes at level $l$: $2^l$.
- Max nodes in tree of height $h$: $2^{h+1} - 1$.
- Minimum height for $n$ nodes: $\lceil log_2(n+1) - 1 \rceil$.
- **Number of Leaf Nodes ($L$):** $L = I_2 + 1$ (where $I_2$ is number of nodes with 2 children).

### 2. Traversals

- **Pre-order**: Root, Left, Right.
- **In-order**: Left, Root, Right. (Produces sorted order for BST).
- **Post-order**: Left, Right, Root.
- **Level-order**: Breadth-First Search (BFS).

---

## Example Problems

**Problem:** How many binary trees can be formed with 3 nodes?

- Formula: $\frac{1}{n+1} \binom{2n}{n} = \frac{1}{4} \binom{6}{3} = \frac{20}{4} = 5$.
- Trees: (Left-Left, Left-Right, Right-Left, Right-Right, Balanced).

---

## Hardest GATE Questions

**Topic: Recovery of Tree from Traversals**
**Tricky Question (GATE 2017):**
Which combination of traversals uniquely identifies a binary tree?

- **Analysis:**
  - Pre-order + In-order $\implies$ Unique.
  - Post-order + In-order $\implies$ Unique.
  - Pre-order + Post-order $\implies$ **NOT Unique** (unless the tree is a Full Binary Tree).
- **The "Trap":** Questions often give you traversals and ask for the "Total sum of leaf nodes" or "Height of the tree". You must draw it manually.
- **Hard Aspect:** Binary Tree Node count with degree constraints.
  - Example: A tree with $n$ nodes has $n_0$ leaf nodes, $n_1$ nodes with 1 child, and $n_2$ nodes with 2 children.
  - $n = n_0 + n_1 + n_2$.
  - Total edges = $n - 1$.
  - Sum of Out-degrees = $0 \cdot n_0 + 1 \cdot n_1 + 2 \cdot n_2 = n - 1$.
  - Solving these equations is a common GATE requirement

---

## References

- [Tree (data structure) (Wikipedia)](https://en.wikipedia.org/wiki/Tree_(data_structure))
- [Binary tree (Wikipedia)](https://en.wikipedia.org/wiki/Binary_tree)
