# LU Decomposition

## Short Notes
**LU Decomposition** factors a square matrix A into the product of a **Lower triangular matrix (L)** and an **Upper triangular matrix (U)**: $A = LU$

- L has 1s on the diagonal (unit lower triangular)
- U is the upper triangular matrix obtained from Gaussian elimination
- Used for efficient solving of multiple systems Ax = b
- Not all matrices can be LU decomposed (may require row pivoting → PA = LU)

## Key Theories & Formulas

### 1. LU Decomposition Process
Given matrix A, apply Gaussian elimination without row swaps:
1. Record multipliers in L (below diagonal)
2. The resulting upper triangular matrix is U
3. L has 1s on the diagonal

**Example**:
$$A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$$

Steps:
- $R_2 \leftarrow R_2 - 2R_1$ (multiplier = 2)
- $R_3 \leftarrow R_3 - 4R_1$ (multiplier = 4)
- $R_3 \leftarrow R_3 - 3R_2$ (multiplier = 3)

$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

### 2. Solving Ax = b using LU
1. Decompose: $A = LU$
2. Solve $Ly = b$ (forward substitution)
3. Solve $Ux = y$ (back substitution)

**Advantage**: If solving multiple systems with same A but different b, compute LU once and reuse.

### 3. LU with Partial Pivoting (PA = LU)
When a zero or small pivot is encountered:
- P = permutation matrix representing row swaps
- More numerically stable

### 4. Determinant from LU
$$\det(A) = \det(L) \times \det(U) = 1 \times \prod_{i} u_{ii}$$
(Product of diagonal elements of U, accounting for row swaps)

### 5. Existence Conditions
- LU decomposition exists if all leading principal minors are non-zero
- If row swaps are needed, use PA = LU (always possible for non-singular matrices)

---

## Example Problems

**Problem 1**: Find the LU decomposition of $A = \begin{pmatrix} 1 & 2 \\ 3 & 8 \end{pmatrix}$

**Solution**:
1. $R_2 \leftarrow R_2 - 3R_1$
2. $U = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}$
3. $L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$

**Verification**: $LU = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 8 \end{pmatrix} = A$ ✓

**Problem 2**: Solve the system using LU decomposition:
$$\begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$$

**Solution**:
1. **Find L and U**:
   - $R_2 \leftarrow R_2 - 3R_1$
   - $L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$, $U = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$

2. **Solve Ly = b** (forward substitution):
   - $y_1 = 1$
   - $3y_1 + y_2 = 5 \Rightarrow y_2 = 2$
   - $y = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

3. **Solve Ux = y** (back substitution):
   - $x_2 = 2$
   - $2x_1 + x_2 = 1 \Rightarrow x_1 = -0.5$
   - $\mathbf{x = \begin{pmatrix} -0.5 \\ 2 \end{pmatrix}}$

---

## Hardest GATE Questions

**Topic: LU Decomposition Construction**

**Question (GATE 2018 Style)**:
Given $A = LU$ where $L = \begin{pmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{pmatrix}$ and $U = \begin{pmatrix} 1 & 2 & 4 \\ 0 & 3 & 6 \\ 0 & 0 & u_{33} \end{pmatrix}$

If $A = \begin{pmatrix} 1 & 2 & 4 \\ 2 & 7 & 14 \\ 1 & 4 & 10 \end{pmatrix}$, find $u_{33}$.

**Solution**:
1. From $A = LU$, element $(2,1)$: $l_{21} \cdot 1 = 2 \Rightarrow l_{21} = 2$
2. Element $(3,1)$: $l_{31} \cdot 1 = 1 \Rightarrow l_{31} = 1$
3. Element $(2,2)$: $l_{21} \cdot 2 + 1 \cdot 3 = 7 \Rightarrow 4 + 3 = 7$ ✓
4. Element $(3,2)$: $l_{31} \cdot 2 + l_{32} \cdot 3 = 4 \Rightarrow 2 + 3l_{32} = 4 \Rightarrow l_{32} = \frac{2}{3}$
5. Element $(3,3)$: $l_{31} \cdot 4 + l_{32} \cdot 6 + 1 \cdot u_{33} = 10$
   - $4 + 4 + u_{33} = 10 \Rightarrow \mathbf{u_{33} = 2}$

**Why it's hard**: Requires understanding the multiplication structure and solving for unknowns systematically.

---

**Topic: Determinant via LU**

**Question**:
If the LU decomposition of A gives $U = \begin{pmatrix} 3 & 1 & 2 \\ 0 & -2 & 4 \\ 0 & 0 & 5 \end{pmatrix}$, find det(A).

**Solution**:
- det(L) = 1 (unit lower triangular)
- det(U) = product of diagonal = $3 \times (-2) \times 5 = -30$
- **det(A) = -30**

---

## References
- [LU decomposition (Wikipedia)](https://en.wikipedia.org/wiki/LU_decomposition)
- [Triangular matrix (Wikipedia)](https://en.wikipedia.org/wiki/Triangular_matrix)
