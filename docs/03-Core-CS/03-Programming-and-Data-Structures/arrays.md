# Arrays

## Short Notes
An array is a collection of elements of same type stored in contiguous memory.

### Address Calculation (GATE Focus)
Base Address ($BA$) + (Index * Size of Element).

## Key Theories & Formulas

### 1. 2D Array Address Mapping
Given `A[m][n]` where $m$ is rows, $n$ is columns.
- **Row Major Order (RMO)**: Rows are stored one after another.
  - $Address(A[i][j]) = BA + [i \times n + j] \times Size$
- **Column Major Order (CMO)**: Columns are stored one after another.
  - $Address(A[i][j]) = BA + [j \times m + i] \times Size$

---

## Example Problems

**Problem:** Given `int A[10][20]` starting at address 1000. Each `int` is 4 bytes. Find address of `A[5][10]` in RMO.
- $i=5, j=10, n=20$ (columns).
- $Address = 1000 + (5 \times 20 + 10) \times 4$
- $Address = 1000 + (110) \times 4 = 1000 + 440 = 1440$.

---

## Hardest GATE Questions

**Topic: Non-zero Indexing and Multi-dimensional Mapping**
**Tricky Question (GATE 2013):**
An array `A[-5...5][-10...10]` is stored in Row Major Order. Find the index calculation formula for `A[i][j]`.
- **Analysis:**
  - Row range: Lower bound $L_1 = -5$, Upper bound $U_1 = 5 \implies$ Count = $5 - (-5) + 1 = 11$.
  - Column range: $L_2 = -10, U_2 = 10 \implies$ Count $n = 10 - (-10) + 1 = 21$.
  - $Address = BA + [(i - L_1) \times n + (j - L_2)] \times Size$.
- **The "Trap":** Using $i$ directly instead of $(i - L_1)$ when the lower bound is not zero.
- **Complexity:** Tri-diagonal or Band-matrix mapping.
  - A matrix where only $A[i][i]$, $A[i][i-1]$, $A[i][i+1]$ are non-zero.
  - Efficiently mapping these few elements into a 1D array to save space and finding the formula.
