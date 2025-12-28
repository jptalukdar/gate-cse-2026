# File Organization & Indexing

## Short Notes
Storage of relations on physical disk and data structures to speed up retrieval.

### Index Types
- **Primary Index**: Ordered file, search key is primary key. (Sparse).
- **Clustering Index**: Ordered file, search key is non-key. (Sparse).
- **Secondary Index**: Unordered file or search key is not the ordering key. (Dense).

## Key Theories & Formulas

### 1. B-Trees and B+ Trees
- **B-Tree**: Data pointers in all nodes.
- **B+ Tree**: Data pointers only in leaf nodes. Leaves are linked. (Better for range queries).
- **Order ($p$)**: Max number of pointers in a node.
- **Leaf Node size (B+ Tree)**: $(p \cdot \text{KeySize}) + (p \cdot \text{DataPtr}) + \text{NodePtr} \le \text{BlockSize}$.

---

## Example Problems

**Problem:** How many levels in a B+ tree with 1 million records and order 100?
- $100^h \ge 10^6 \implies h=3$.
**Result:** 3 levels (excluding root maybe).

---

## Hardest GATE Questions

**Topic: Node Capacity Calculation and Splitting**
**Tricky Question (GATE 2011/2015/2021):**
Calculate the max order of a B+ tree node given Block Size, Key size, Pointer size.
- **Analysis:** 
  - Internal Node: $(p \cdot P) + (p-1) \cdot K \le B$.
  - Solving for $p$ often gives a non-integer, you must **floor** it ($p = \lfloor \dots \rfloor$).
- **The "Trap":** Leaf node vs Internal node structure. 
  - Leaves in B+ trees have a "next leaf pointer", so their capacity formula is slightly different: $p(K+P) + P_{next} \le B$.
- **Hard Aspect:** Number of blocks accessed for a query.
  - For an index: $Height + 1$ (for data block access).
- **Complexity:** Static vs Dynamic Hashing.
  - Extendible Hashing: Uses a directory. Directory size doubles when a bucket overflows and local depth equals global depth

---

## References
- [Database index (Wikipedia)](https://en.wikipedia.org/wiki/Database_index)
- [B+ tree (Wikipedia)](https://en.wikipedia.org/wiki/B%2B_tree)
