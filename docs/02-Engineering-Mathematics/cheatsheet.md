# ⚡ Cheatsheet: Engineering Mathematics

## Discrete Mathematics
| Topic | Formula |
| :--- | :--- |
| **Logic** | $p \to q \equiv \neg p \lor q \equiv \neg q \to \neg p$ |
| **Sets** | $|A \cup B| = |A| + |B| - |A \cap B|$ |
| **Graphs** | $\sum deg(v) = 2 \times |E|$ |
| **Planar** | $V - E + R = 2$ |
| **Functions**| Injectives: $P(n,m)$ ($n \ge m$). Surjectives: $n^m - \binom{n}{1}(n-1)^m...$ |
| **Poset** | Lattices must have unique LUB and GLB for every pair. |

## Linear Algebra

- **Rank**: Number of linearly independent rows/cols. $\rho(A) = \rho(A^T)$.
- **Determinant**: Product of eigenvalues. Triangular matrix det = Product of diagonal.
- **Eigenvalues**:
  - $\sum \lambda_i = Trace(A)$.
  - $\prod \lambda_i = det(A)$.
  - Eigenvalues of $A^k$ are $\lambda^k$.
  - Eigenvalues of $A^{-1}$ are $1/\lambda$.
- **Cayley-Hamilton**: Every square matrix satisfies its own characteristic equation. $A^n + c_{n-1}A^{n-1} ... + c_0 I = 0$.

## Calculus

- **Limits**: L'Hopital's Rule (if $0/0$ or $\infty/\infty$, differentiate Num/Denom).
- **Mean Value**: $\exists c \in (a,b)$ s.t. $f'(c) = \frac{f(b)-f(a)}{b-a}$.
- **Maxima/Minima**: $f'(x)=0$. If $f''(x) > 0$ (Min), if $f''(x) < 0$ (Max).
- **Taylor Series**: $f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + ...$

## Probability

- **Bayes**: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.
- **Binomial**: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$. (Mean $np$, Var $npq$).
- **Poisson**: $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$. (Mean $\lambda$, Var $\lambda$).
- **Normal**: PDF $\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$.
- **Exponential**: $f(x) = \lambda e^{-\lambda x}$ ($x \ge 0$). (Mean $1/\lambda$).
