# Divide-and-Conquer

## Short Notes
A design paradigm that breaks a problem into smaller independent subproblems of the same type.

### Steps

1. **Divide**: Split problem into sub-problems.
2. **Conquer**: Solve sub-problems recursively.
3. **Combine**: Merge results of sub-problems.

## Key Theories & Formulas

### 1. Common Algorithms

- **Merge Sort**: $2T(n/2) + O(n)$.
- **Quick Sort**: $T(k) + T(n-k-1) + O(n)$.
- **Binary Search**: $T(n/2) + O(1)$.
- **Strassen's Matrix Mult**: $7T(n/2) + O(n^2) \implies O(n^{2.81})$.
- **Closest Pair of Points**: $O(n \log n)$.

---

## Example Problems

**Problem:** Solve $T(n) = T(n-1) + n$ (not divide and conquer, but common in analysis).

- $T(n) = n + (n-1) + (n-2) + ... + 1 = \frac{n(n+1)}{2}$.
**Result:** $O(n^2)$.

---

## Hardest GATE Questions

**Topic: Median Finding and Selection**
**Tricky Question (GATE 2011/2014):**
What is the complexity of finding the Median of $n$ elements in the worst case?

- **Analysis:** **$O(n)$** using the "Median of Medians" (Deterministic Selection) algorithm.
- **The "Trap":** Thinking you MUST sort the array first. Sorting takes $O(n \log n)$. $O(n)$ is possible but more complex.
- **Hard Aspect:** When the "Combine" step is more expensive than the subproblems.
  - *Example:* An algorithm that divides a problem into 2 parts of size $n/2$ but takes $O(n^2)$ to merge.
  - $T(n) = 2T(n/2) + n^2 \implies O(n^2)$ by Master Theorem.
- **Complexity:** Multiplication of large integers (Karatsuba Algorithm).
  - Standard: $O(n^2)$.
  - Karatsuba: $O(n^{1.58})$ using $3$ multiplications of size $n/2$

---

## References

- [Divide-and-conquer algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
