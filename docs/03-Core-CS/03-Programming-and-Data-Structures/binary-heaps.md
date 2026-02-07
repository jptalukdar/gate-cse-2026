# Binary Heaps

## Short Notes
A Heap is a Complete Binary Tree that satisfies the Heap Property.

### Types

- **Max-Heap**: Value of parent $\ge$ values of children. Root is maximum.
- **Min-Heap**: Value of parent $\le$ values of children. Root is minimum.

## Key Theories & Formulas

### 1. Array Representation
For a node at index $i$ (1-indexed):

- **Left Child**: $2i$
- **Right Child**: $2i + 1$
- **Parent**: $\lfloor i/2 \rfloor$

### 2. Time Complexity

- **Build Heap**: $O(n)$. (Trick: sum of heights of all nodes).
- **Insert**: $O(log n)$.
- **Delete Root**: $O(log n)$.
- **Extract Min/Max**: $O(log n)$.

---

## Example Problems

**Problem:** Build a Max-heap from $\{10, 20, 15, 30, 40\}$.

1. Insert 10.
2. Insert 20, swap with 10. `[20, 10]`
3. Insert 15. `[20, 10, 15]`
4. Insert 30, swap with 10, then 20. `[30, 20, 15, 10]`
5. Insert 40, swap with 20, then 30. `[40, 30, 15, 10, 20]`
**Result:** `[40, 30, 15, 10, 20]`.

---

## Hardest GATE Questions

**Topic: Selection and Build-Heap optimization**
**Tricky Question (GATE 2012):**
What is the complexity of finding the $k$-th smallest element using a Max-heap?

- **Analysis:** This is inefficient. You should use a **Min-heap** to find small elements.
- **The "Trap":** Thinking `Build-Heap` is $O(n log n)$. It is actually **$O(n)$**.
- **Hard Aspect:** Heap properties during deletion. When you delete an element, you replace it with the **last** element and then "Heapify down".
  - Question often asks: "Which of the following values can be the result of exactly 2 deletions/insertions in this heap?"
- **Complexity:** Comparison of Heaps vs BSTs for "Find Min", "Find Max", and "Search".
  - Heap: Find Min (Min-heap) is $O(1)$. Search is $O(n)$.
  - BST: Find Min is $O(log n)$. Search is $O(log n)$

---

## References

- [Binary heap (Wikipedia)](https://en.wikipedia.org/wiki/Binary_heap)
