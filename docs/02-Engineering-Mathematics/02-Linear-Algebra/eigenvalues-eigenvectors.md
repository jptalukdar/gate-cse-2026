# Eigenvalues & Eigenvectors

## Short Notes
For a square matrix **A**, a scalar λ is called an **eigenvalue** if there exists a non-zero vector **v** such that **Av = λv**. The vector **v** is called the corresponding **eigenvector**.

- **Characteristic Equation**: $\det(A - \lambda I) = 0$
- **Eigenspace**: The set of all eigenvectors corresponding to an eigenvalue λ, along with the zero vector, forms a subspace.
- **Algebraic Multiplicity**: The number of times λ appears as a root of the characteristic equation.
- **Geometric Multiplicity**: The dimension of the eigenspace corresponding to λ.
- **Diagonalizability**: A matrix is diagonalizable if and only if algebraic multiplicity = geometric multiplicity for all eigenvalues.

## Key Theories & Formulas

### 1. Properties of Eigenvalues

- Sum of eigenvalues = **Trace(A)** = $\sum_{i} a_{ii}$
- Product of eigenvalues = **det(A)**
- Eigenvalues of $A^T$ are same as eigenvalues of $A$
- Eigenvalues of $A^{-1}$ are $\frac{1}{\lambda}$ (if A is invertible)
- Eigenvalues of $A^k$ are $\lambda^k$
- Eigenvalues of $A + kI$ are $\lambda + k$
- Eigenvalues of $kA$ are $k\lambda$

### 2. Special Matrices

| Matrix Type | Eigenvalue Properties |
|-------------|----------------------|
| Symmetric ($A = A^T$) | All eigenvalues are **real** |
| Skew-Symmetric ($A = -A^T$) | All eigenvalues are **purely imaginary or zero** |
| Orthogonal ($A^T A = I$) | All eigenvalues have **magnitude 1** |
| Idempotent ($A^2 = A$) | Eigenvalues are **0 or 1** |
| Nilpotent ($A^k = 0$) | All eigenvalues are **0** |
| Involutory ($A^2 = I$) | Eigenvalues are **1 or -1** |

### 3. Cayley-Hamilton Theorem
Every square matrix satisfies its own characteristic equation.

- If characteristic equation is $\lambda^2 - 5\lambda + 6 = 0$, then $A^2 - 5A + 6I = 0$
- Useful for computing $A^{-1}$ and higher powers of $A$

### 4. Diagonalization
If $A$ is diagonalizable: $A = PDP^{-1}$

- $P$ = matrix of eigenvectors (column-wise)
- $D$ = diagonal matrix of eigenvalues
- $A^n = PD^nP^{-1}$ (efficient for computing powers)

---

## Example Problems

**Problem 1**: Find eigenvalues of $A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$

1. Characteristic equation: $\det(A - \lambda I) = 0$
2. $(4-\lambda)(3-\lambda) - 2 = 0$
3. $\lambda^2 - 7\lambda + 10 = 0$
4. $(\lambda - 5)(\lambda - 2) = 0$
5. **Eigenvalues: λ = 5, 2**

**Verification**: 

- Trace = 4 + 3 = 7 = 5 + 2 ✓
- Det = 12 - 2 = 10 = 5 × 2 ✓

**Problem 2**: Find $A^{100}$ if eigenvalues of $A$ are 1 and -1.

Using diagonalization: Eigenvalues of $A^{100}$ are $1^{100} = 1$ and $(-1)^{100} = 1$.

---

## Hardest GATE Questions

**Topic: Cayley-Hamilton & Matrix Powers**

**Question (GATE 2017 Style)**:
Let $A$ be a 3×3 matrix with eigenvalues 1, 2, 3. Find the value of $\det(A^2 - 4A + 3I)$.

**Solution**:

1. The eigenvalues of $A^2 - 4A + 3I$ are obtained by substituting eigenvalues of $A$ into $f(\lambda) = \lambda^2 - 4\lambda + 3$
2. For $\lambda_1 = 1$: $f(1) = 1 - 4 + 3 = 0$
3. For $\lambda_2 = 2$: $f(2) = 4 - 8 + 3 = -1$
4. For $\lambda_3 = 3$: $f(3) = 9 - 12 + 3 = 0$
5. Eigenvalues of $(A^2 - 4A + 3I)$ are: 0, -1, 0
6. $\det(A^2 - 4A + 3I) = 0 \times (-1) \times 0 = \mathbf{0}$

**Why it's hard**: Requires understanding that polynomial functions of matrices preserve eigenvalue relationships.

---

**Topic: Geometric vs Algebraic Multiplicity**

**Question (GATE 2015 Variant)**:
For which value of $k$ is the matrix $A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & k \\ 0 & 0 & 2 \end{pmatrix}$ diagonalizable?

**Solution**:

1. Eigenvalue: λ = 2 with algebraic multiplicity 3
2. For diagonalizability: geometric multiplicity must also be 3
3. Find eigenspace: $(A - 2I)v = 0$
4. $A - 2I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & k \\ 0 & 0 & 0 \end{pmatrix}$
5. For k ≠ 0: rank = 2, nullity = 1 (not diagonalizable)
6. For k = 0: rank = 1, nullity = 2 (still not 3)
7. **Never diagonalizable for any k** (upper triangular with repeated eigenvalues and non-zero superdiagonal)

---

## References

- [Eigenvalues and eigenvectors (Wikipedia)](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [Cayley-Hamilton theorem (Wikipedia)](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem)
