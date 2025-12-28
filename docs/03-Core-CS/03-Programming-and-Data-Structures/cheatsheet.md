# ⚡ Cheatsheet: Programming & Data Structures

| Topic | Formula / Concept | Note |
| :--- | :--- | :--- |
| **C Programming** | `sizeof`: char(1), short(2), int(2/4), float(4), double(8), ptr(4/8) | Architecture dependent rules |
| | **Static Scoping**: Variables bound at compile time | Default in C |
| | **Dynamic Scoping**: Bound at runtime based on call stack | Not in standard C |
| | **Parameter Passing**: Call by Value (Copy), Call by Reference (Address) | Arrays always decay to pointers |
| **Trees** | Max nodes in height $h$: $2^{h+1}-1$ | Height starts at 0 |
| | Height with $n$ nodes: $\lfloor \log_2 n \rfloor$ | For Complete Binary Tree |
| | Leaf nodes ($L$) vs Degree-2 nodes ($I_2$): $L = I_2 + 1$ | For any Binary Tree |
| **BST** | Search/Insert/Delete: $O(h)$ | worst case $O(n)$ (skewed) |
| | Inorder Traversal gives **Sorted Sequence** | Key property |
| **Heaps** | Parent of $i$: $\lfloor (i-1)/2 \rfloor$ | 0-based index |
| | Left Child: $2i+1$, Right Child: $2i+2$ | |
| | Build Heap: $O(n)$ | Heapify: $O(\log n)$ |
| **Graphs** | Sum of degrees = $2|E|$ | Handshaking Lemma |
| | Max edges (Undirected): $n(n-1)/2$ | Complete Graph $K_n$ |
| | Max edges (Directed): $n(n-1)$ | |
| **Stacks/Queues** | Stack Permutations: $\frac{1}{n+1}\binom{2n}{n}$ | Catalan Number |
| | Queue with 2 Stacks: Enqueue $O(1)$, Dequeue $O(n)$ | Or vice-versa |

## ⚠️ Common Traps
- **Operator Precedence**: `*ptr++` is `*(ptr++)`. `++*ptr` is `++(*ptr)`.
- **Macro Expansion**: Macros do textual substitution. `SQUARE(x) x*x` called with `SQUARE(1+2)` becomes `1+2*1+2` (Evaluates to 5, not 9). Always encompass args in parenthesis `((x)*(x))`.
- **Structure Padding**: Compilers add padding to align members. Total size $\ge$ Sum of members. Order matters!
- **Dangling Pointer**: Pointer pointing to memory that has been freed.
