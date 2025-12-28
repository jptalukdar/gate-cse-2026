# Combinatorics

## Short Notes
Combinatorics is the branch of mathematics concerning the study of finite or countable discrete structures.
- **Permutation**: Arrangement of objects where order matters. $P(n, r)$.
- **Combination**: Selection of objects where order does not matter. $C(n, r)$.
- **Pigeonhole Principle**: If $n$ items are put into $m$ containers, with $n > m$, then at least one container must contain more than one item.

## Key Theories & Formulas

### 1. Basic Counting
- **Sum Rule**: If task A can be done in $m$ ways and task B in $n$ ways (mutually exclusive), then A OR B can be done in $m+n$ ways.
- **Product Rule**: If task A can be done in $m$ ways and task B in $n$ ways, then A AND B can be done in $m \times n$ ways.

### 2. Permutations & Combinations
- $P(n, r) = \frac{n!}{(n-r)!}$
- $C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$
- **Circular Permutations**: $(n-1)!$ ways to arrange $n$ distinct objects in a circle.
- **Distinguishable Permutations**: $\frac{n!}{n_1! n_2! ...}$ where $n_1, n_2$ are counts of identical items.

### 3. Inclusion-Exclusion Principle
- $|A \cup B| = |A| + |B| - |A \cap B|$
- $|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$
- **Derangements ($D_n$)**: Number of permutations where no element appears in its original position.
  - $D_n = n! [1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + ... + (-1)^n \frac{1}{n!} ]$
  - $D_3 = 2, D_4 = 9, D_5 = 44$.

### 4. Generalized Pigeonhole Principle
- If $n$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil n/k \rceil$ objects.

### 5. Binomial Theorem
- $(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k$
- Number of terms: $n+1$.
- Sum of coefficients: $2^n$ (put $x=1, y=1$).

---

## Example Problems

**Problem**: How many solutions does $x_1 + x_2 + x_3 = 11$ have, where $x_i \ge 0$ are integers?
- This is "stars and bars". Formula for $x_1 + ... + x_k = n$ is $\binom{n+k-1}{k-1}$.
- Here $n=11, k=3$.
- Result: $\binom{11+3-1}{3-1} = \binom{13}{2} = \frac{13 \times 12}{2} = 78$.

**Problem**: How many ways to arrange letters of "MISSISSIPPI"?
- Total letters = 11.
- M=1, I=4, S=4, P=2.
- Result: $\frac{11!}{1! 4! 4! 2!} = 34650$.

---

## Hardest GATE Questions

**Topic: Generating Functions / Coefficients**

**Tricky Question**:
Find the coefficient of $x^{12}$ in $(x^3 + x^4 + x^5 + ...)^3$.

- **Analysis**:
  - Expression is $[x^3 (1 + x + x^2 + ...)]^3$
  - $= x^9 (1 + x + x^2 + ...)^3$
  - $= x^9 (1-x)^{-3}$
  - We need coefficient of $x^{12}$ in $x^9 (1-x)^{-3}$.
  - This is equivalent to finding coefficient of $x^{12-9} = x^3$ in $(1-x)^{-3}$.
  - General Term: Coeff of $x^r$ in $(1-x)^{-n}$ is $\binom{n+r-1}{r}$.
  - Here $n=3, r=3$.
  - $\binom{3+3-1}{3} = \binom{5}{3} = 10$.

- **Result**: 10.
- **Why it's hard**: Requires manipulating infinite geometric series and knowing the negative binomial expansion formula.

---

## References
- [Combinatorics (Wikipedia)](https://en.wikipedia.org/wiki/Combinatorics)
