# Binary Search Trees

## Short Notes
A Binary Search Tree (BST) is a binary tree where for every node:

- Left subtree nodes < Node value.
- Right subtree nodes > Node value.

### AVL Trees (Self-Balancing)
A BST where the balance factor ($Height_{left} - Height_{right}$) of every node is $-1, 0, \text{ or } 1$.

## Key Theories & Formulas

### 1. Operations Complexity
| Operation | Average (Balanced) | Worst (Skewed) |
| :--- | :--- | :--- |
| Search | $O(log n)$ | $O(n)$ |
| Insertion | $O(log n)$ | $O(n)$ |
| Deletion | $O(log n)$ | $O(n)$ |

### 2. AVL Rotations

- **LL**: Single Right rotation.
- **RR**: Single Left rotation.
- **LR**: Left then Right rotation.
- **RL**: Right then Left rotation.

## Example Problems

**Problem:** Inserting 10, 20, 30 into a BST.

1. 10 is root.
2. 20 > 10, right of 10.
3. 30 > 20, right of 20.
**Result:** Skewed tree. In-order: 10, 20, 30.

---

## Hardest GATE Questions

**Topic: Insertion/Deletion impact on Height and AVL properties**
**Tricky Question (GATE 2014):**
Delete 10 (root) from a BST. Who replaces it?

- **Analysis:** Either the **Maximum of the Left Subtree** or the **Minimum of the Right Subtree**.
- **The "Trap":** Questions about "Successful Search" vs "Unsuccessful Search" average counts.
  - Successful: $\sum \text{levels of all nodes} / n$.
  - Unsuccessful: $\sum \text{levels of empty slots (leaves)} / (n+1)$.
- **Complexity:** Minimum nodes required to form an AVL tree of height $h$.
  - $N(h) = N(h-1) + N(h-2) + 1$. (Fibonacci-like).
  - $N(0)=1, N(1)=2, N(2)=4, N(3)=7, N(4)=12$.
  - This is a very common numerical question

---

## References

- [Binary search tree (Wikipedia)](https://en.wikipedia.org/wiki/Binary_search_tree)
- [AVL tree (Wikipedia)](https://en.wikipedia.org/wiki/AVL_tree)
