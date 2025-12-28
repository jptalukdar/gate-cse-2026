# Searching

## Short Notes
Locating an element within a data structure.

### Basic Algorithms
- **Linear Search**: $O(n)$. Works on unsorted data.
- **Binary Search**: $O(\log n)$. Requires sorted data and random access (array).

## Key Theories & Formulas

### 1. Binary Search Comparisons
- Max comparisons: $\lfloor log_2 n \rfloor + 1$.
- Average comparisons: $\approx log_2 n$.

### 2. Searching in Matrices
- In a sorted $M \times N$ matrix (rows and columns sorted), we can search in $O(M+N)$.

---

## Example Problems

**Problem:** How many comparisons for Binary Search in an array of 1000 elements?
- $log_2 1000 \approx 10$.
**Result:** 10.

---

## Hardest GATE Questions

**Topic: Binary Search on non-unique elements and range queries**
**Tricky Question (GATE 2013/2015):**
Given a sorted array with duplicates, how to find the *first* occurrence of $X$?
- **Analysis:** Standard Binary Search finds *any* occurrence. To find the first, if $A[mid] == X$, you must continue searching in the left half: $high = mid - 1$.
- **The "Trap":** Binary Search on a **Linked List**.
  - Question: "Complexity of Binary Search on a Sorted Singly Linked List?"
  - Answer: **$O(n)$**. Why? Even though we reduce the range logically, finding the `mid` element takes $O(k)$ steps in a linked list.
- **Complexity:** Ternary Search vs Binary Search.
  - Ternary search uses $2 \times log_3 n$ comparisons. 
  - In terms of comparisons, Binary Search is superior

---

## References
- [Search algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Search_algorithm)
- [Binary search algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Binary_search_algorithm)
