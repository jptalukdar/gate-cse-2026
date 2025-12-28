# Sorting

## Short Notes
Sorting is the arrangement of data in a specific order (ascending/descending).

### Algorithms Overview
- **Selection**: $O(n^2)$. Find min, swap.
- **Bubble**: $O(n^2)$. Adjacent swaps.
- **Insertion**: $O(n^2)$. Best case $O(n)$ for sorted data.
- **Merge**: $O(n \log n)$. Divide & Conquer. Stable.
- **Quick**: $O(n \log n)$ average. $O(n^2)$ worst. Not stable.
- **Heap**: $O(n \log n)$. Not stable.

## Key Theories & Formulas

### 1. Stability
A sorting algorithm is **stable** if it preserves the relative order of records with equal keys.
- Stable: Merge, Insertion, Bubble.
- Unstable: Quick, Heap, Selection.

### 2. In-place
Uses $O(1)$ extra space (besides the input).
- In-place: Bubble, Insertion, Selection, Quick (recursive stack excluded), Heap.
- Not in-place: Merge Sort ($O(n)$ extra space).

### 3. Comparison Lower Bound
Any comparison-based sorting algorithm must take $\Omega(n \log n)$ in the worst case.

---

## Example Problems

**Problem:** What is the worst-case scenario for QuickSort?
- **Result:** Already sorted or reverse-sorted array when the first/last element is chosen as pivot. The recurrence becomes $T(n) = T(n-1) + O(n)$.

---

## Hardest GATE Questions

**Topic: QuickSort Pivot Selection and Partition Counts**
**Tricky Question (GATE 2014/2019):**
How many comparisons are made by QuickSort to sort an array of $n$ identical elements?
- **Analysis:**
  - Even if elements are identical, the partition process compares each element with the pivot.
  - If pivot is first element, it compares with $n-1$ others.
  - The partition will be highly unbalanced ($0$ and $n-1$).
  - Total comparisons = $(n-1) + (n-2) + ... + 1 = \frac{n(n-1)}{2}$.
- **The "Trap":** Thinking that "identical elements" means $0$ swaps or faster execution. Standard QuickSort still performs the same number of comparisons.
- **Hard Aspect:** Finding the number of swaps in Bubble Sort or specific behavior of Selection Sort (Selection sort always performs $O(n^2)$ comparisons regardless of input).
