# Rank & Determinant

## Short Notes

### Rank
The **rank** of a matrix is the maximum number of linearly independent rows (or columns). Equivalently, it's the number of non-zero rows in the row echelon form.

- rank(A) ≤ min(m, n) for an m×n matrix
- rank(A) = rank(Aᵀ) (row rank = column rank)
- A matrix has **full rank** if rank = min(m, n)

### Determinant
The **determinant** is a scalar value that can be computed from a square matrix. It encodes important properties about the linear transformation represented by the matrix.

- |A| = 0 ⟺ A is singular (not invertible)
- |A| ≠ 0 ⟺ A is non-singular (invertible)
- Geometrically: |det(A)| = volume scaling factor of the transformation

## Key Theories & Formulas

### 1. Determinant Properties
| Property | Result |
|----------|--------|
| $\det(AB) = \det(A) \cdot \det(B)$ | Multiplicative |
| $\det(A^T) = \det(A)$ | Transpose invariant |
| $\det(A^{-1}) = \frac{1}{\det(A)}$ | Inverse |
| $\det(kA) = k^n \det(A)$ | Scalar multiplication (n×n matrix) |
| $\det(A^n) = [\det(A)]^n$ | Powers |
| Row swap → $-\det(A)$ | Sign change |
| Row × k → $k \cdot \det(A)$ | Scalar row |
| $R_i + kR_j$ → $\det(A)$ | Row addition (unchanged) |

### 2. Computing Determinant

**For 2×2 Matrix**:
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

**For 3×3 Matrix** (Sarrus Rule or Cofactor expansion):
$$\det\begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = a(ei-fh) - b(di-fg) + c(dh-eg)$$

**For upper/lower triangular matrices**: 
$$\det(A) = \prod_{i} a_{ii}$$ (product of diagonal elements)

### 3. Rank Properties

- $rank(AB) \leq \min(rank(A), rank(B))$
- $rank(A + B) \leq rank(A) + rank(B)$
- $rank(A) + nullity(A) = n$ (Rank-Nullity Theorem)
- If A is m×n and B is n×p with AB = 0, then $rank(A) + rank(B) \leq n$

### 4. Rank and Determinant Connection

- A square matrix A is **invertible** iff rank(A) = n iff det(A) ≠ 0
- For any k×k submatrix, if its determinant ≠ 0, the rank of A ≥ k
- Rank = largest order of non-zero minor

### 5. Adjoint and Inverse
$$A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)$$

where adj(A) = transpose of cofactor matrix.

---

## Example Problems

**Problem 1**: Find the determinant of $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$

**Solution**: Upper triangular matrix → det = product of diagonal = $1 \times 4 \times 6 = \mathbf{24}$

**Problem 2**: If det(A) = 5, find det(3A) where A is a 4×4 matrix.

**Solution**: $\det(3A) = 3^4 \cdot \det(A) = 81 \times 5 = \mathbf{405}$

**Problem 3**: Find the rank of $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 3 & 4 \end{pmatrix}$

**Solution**:

1. $R_2 \leftarrow R_2 - 2R_1$: $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 1 & 3 & 4 \end{pmatrix}$
2. $R_3 \leftarrow R_3 - R_1$: $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$
3. Non-zero rows = 2 → **rank = 2**

---

## Hardest GATE Questions

**Topic: Determinant Properties**

**Question (GATE 2019 Style)**:
If A is a 3×3 matrix such that det(A) = 4, find det(2A⁻¹(adj(A))ᵀ).

**Solution**:

1. $\det(adj(A)) = [\det(A)]^{n-1} = 4^2 = 16$
2. $\det((adj(A))^T) = \det(adj(A)) = 16$
3. $\det(A^{-1}) = \frac{1}{\det(A)} = \frac{1}{4}$
4. $\det(2A^{-1}) = 2^3 \cdot \det(A^{-1}) = 8 \times \frac{1}{4} = 2$
5. $\det(2A^{-1}(adj(A))^T) = \det(2A^{-1}) \cdot \det((adj(A))^T) = 2 \times 16 = \mathbf{32}$

**Why it's hard**: Requires combining multiple determinant properties systematically.

---

**Topic: Rank and Nullity**

**Question (GATE 2017 Variant)**:
Let A be a 6×8 matrix with rank 4. Let B be an 8×6 matrix with rank 3. What is the maximum possible rank of AB?

**Solution**:

- AB is a 6×6 matrix
- rank(AB) ≤ min(rank(A), rank(B)) = min(4, 3) = **3**
- Maximum possible rank = **3**

---

**Topic: Singular Matrix Condition**

**Question**:
For what value of k is the matrix $A = \begin{pmatrix} 1 & 2 & k \\ 2 & k & 8 \\ k & 8 & 26 \end{pmatrix}$ singular?

**Solution**:

1. Matrix is singular when det(A) = 0
2. Using cofactor expansion along row 1:
   $\det(A) = 1(26k - 64) - 2(52 - 8k) + k(16 - k^2)$

3. $= 26k - 64 - 104 + 16k + 16k - k^3$
4. $= -k^3 + 58k - 168$
5. Setting $-k^3 + 58k - 168 = 0$
6. $k^3 - 58k + 168 = 0$
7. Testing k = 4: $64 - 232 + 168 = 0$ ✓
8. **k = 4** (and two other roots from factoring)

---

## References

- [Rank (linear algebra) (Wikipedia)](https://en.wikipedia.org/wiki/Rank_(linear_algebra))
- [Determinant (Wikipedia)](https://en.wikipedia.org/wiki/Determinant)
- [Adjugate matrix (Wikipedia)](https://en.wikipedia.org/wiki/Adjugate_matrix)
