# Asymptotic Analysis

## Short Notes
Asymptotic analysis describes the behavior of algorithms as the input size ($n$) approaches infinity.

### Benchmarks
- **Big-O ($O$)**: Upper bound (Worst case).
- **Omega ($\Omega$)**: Lower bound (Best case).
- **Theta ($\Theta$)**: Tight bound (Average case).

### Common Growth Rates
$1 < \log \log n < \log n < n^{1/k} < n < n \log n < n^k < a^n < n! < n^n$

## Key Theories & Formulas

### 1. Master Theorem
For recurrences of the form $T(n) = aT(n/b) + f(n)$:

1. If $f(n) = O(n^c)$ where $c < \log_b a$, then $T(n) = \Theta(n^{\log_b a})$.
2. If $f(n) = \Theta(n^c)$ where $c = \log_b a$, then $T(n) = \Theta(n^c \log n)$.
3. If $f(n) = \Omega(n^c)$ where $c > \log_b a$, then $T(n) = \Theta(f(n))$.

### 2. Recurrence for Common Algorithms
- **Binary Search**: $T(n) = T(n/2) + 1 \implies O(\log n)$
- **Merge Sort**: $T(n) = 2T(n/2) + n \implies O(n \log n)$
- **Quick Sort (Worst)**: $T(n) = T(n-1) + n \implies O(n^2)$

---

## Example Problems

**Problem:** Rank the functions by growth rate: $n^2, n \log n, 2^n, n!$.
**Result:** $n \log n < n^2 < 2^n < n!$

---

## Hardest GATE Questions

**Topic: Comparison of complex log functions**
**Tricky Question (GATE 2011/2015):**
Compare $f(n) = 2^n$ and $g(n) = n^{\log n}$.

- **Analysis:**
  - Take $\log$ on both sides:
  - $\log(f(n)) = n$
  - $\log(g(n)) = (\log n) \cdot (\log n) = (\log n)^2$
  - Since $n$ grows faster than $(\log n)^2$, $f(n) > g(n)$.
- **The "Trap":** Confusing $n^{\log n}$ with $(\log n)^n$. $(\log n)^n$ is actually very large, roughly $n^{\log \log n}$.
- **Complexity:** Master Theorem cases where $f(n) = n^c \log^k n$.
  - If $c = \log_b a$, then $T(n) = \Theta(n^c \log^{k+1} n)$.
  - *Example:* $T(n) = 2T(n/2) + n \log n \implies c=1, \log_2 2=1 \implies T(n) = n \log^2 n$

---

## References
- [Asymptotic analysis (Wikipedia)](https://en.wikipedia.org/wiki/Asymptotic_analysis)
- [Big O notation (Wikipedia)](https://en.wikipedia.org/wiki/Big_O_notation)
- [Master theorem (analysis of algorithms) (Wikipedia)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
