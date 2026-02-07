# Systems of Linear Equations

## Short Notes
A system of linear equations can be represented as **Ax = b** where A is the coefficient matrix, x is the variable vector, and b is the constant vector.

- **Consistent System**: Has at least one solution
- **Inconsistent System**: Has no solution
- **Homogeneous System**: When b = 0 (always consistent, trivial solution exists)

## Key Theories & Formulas

### 1. Existence and Uniqueness of Solutions
For a system **Ax = b** of n equations in n unknowns:

| Condition | Solution Type |
|-----------|--------------|
| rank(A) = rank(A|b) = n | **Unique solution** |
| rank(A) = rank(A|b) < n | **Infinite solutions** |
| rank(A) ≠ rank(A|b) | **No solution** |

### 2. Homogeneous Systems (Ax = 0)
- Always consistent (x = 0 is always a solution)
- **Trivial solution only**: if rank(A) = n (number of unknowns)
- **Non-trivial solutions exist**: if rank(A) < n
- Number of free variables = n - rank(A)
- **Key Result**: If m < n (fewer equations than unknowns), non-trivial solutions always exist.

### 3. Row Echelon Form (REF) & Reduced REF (RREF)
Steps for Gaussian Elimination:
1. Convert to upper triangular form (REF)
2. Further reduce to RREF (leading 1s, zeros above and below pivots)

**Example**:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{pmatrix} \xrightarrow{RREF} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

### 4. Cramer's Rule
For a system with unique solution (det(A) ≠ 0):
$$x_i = \frac{\det(A_i)}{\det(A)}$$
where $A_i$ is A with column i replaced by b.

### 5. Matrix Inverse Method
If A is invertible: $x = A^{-1}b$

---

## Example Problems

**Problem 1**: For what value of k does the system have infinite solutions?
$$\begin{align}
x + 2y + 3z &= 4 \\
2x + 3y + 4z &= 5 \\
3x + 4y + 5z &= k
\end{align}$$

**Solution**:
1. Form augmented matrix: $\begin{pmatrix} 1 & 2 & 3 & | & 4 \\ 2 & 3 & 4 & | & 5 \\ 3 & 4 & 5 & | & k \end{pmatrix}$
2. $R_2 \leftarrow R_2 - 2R_1$: $\begin{pmatrix} 1 & 2 & 3 & | & 4 \\ 0 & -1 & -2 & | & -3 \\ 3 & 4 & 5 & | & k \end{pmatrix}$
3. $R_3 \leftarrow R_3 - 3R_1$: $\begin{pmatrix} 1 & 2 & 3 & | & 4 \\ 0 & -1 & -2 & | & -3 \\ 0 & -2 & -4 & | & k-12 \end{pmatrix}$
4. $R_3 \leftarrow R_3 - 2R_2$: $\begin{pmatrix} 1 & 2 & 3 & | & 4 \\ 0 & -1 & -2 & | & -3 \\ 0 & 0 & 0 & | & k-6 \end{pmatrix}$
5. For infinite solutions: $k - 6 = 0 \Rightarrow \mathbf{k = 6}$

**Problem 2**: Find the number of solutions for the homogeneous system with coefficient matrix:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$

**Solution**:
- det(A) = 0 (rows are in arithmetic progression)
- rank(A) = 2 < 3 (number of unknowns)
- **Infinite solutions** with 1 free variable

---

## Hardest GATE Questions

**Topic: Condition for Consistent System**

**Question (GATE 2016 Style)**:
Consider the system:
$$\begin{align}
x + y + z &= 1 \\
x + 2y + 3z &= 2 \\
x + 2y + (a^2-5)z &= a
\end{align}$$
For what values of 'a' does the system have (i) no solution, (ii) unique solution, (iii) infinite solutions?

**Solution**:
1. Augmented matrix after row operations:
   $\begin{pmatrix} 1 & 1 & 1 & | & 1 \\ 0 & 1 & 2 & | & 1 \\ 0 & 0 & a^2-8 & | & a-2 \end{pmatrix}$

2. **Case 1**: $a^2 - 8 \neq 0$ (i.e., $a \neq \pm 2\sqrt{2}$)
   - rank(A) = rank(A|b) = 3 → **Unique solution**

3. **Case 2**: $a^2 - 8 = 0$ (i.e., $a = \pm 2\sqrt{2}$)
   - If $a = 2\sqrt{2}$: $a - 2 = 2\sqrt{2} - 2 \neq 0$ → **No solution**
   - If $a = -2\sqrt{2}$: $a - 2 = -2\sqrt{2} - 2 \neq 0$ → **No solution**

**Final Answer**:
- No solution: $a = \pm 2\sqrt{2}$
- Unique solution: $a \neq \pm 2\sqrt{2}$
- Infinite solutions: Never (for this system)

**Why it's hard**: Requires careful case analysis and understanding when rank conditions fail.

---

## References
- [System of linear equations (Wikipedia)](https://en.wikipedia.org/wiki/System_of_linear_equations)
- [Gaussian elimination (Wikipedia)](https://en.wikipedia.org/wiki/Gaussian_elimination)
