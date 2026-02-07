# Mean Value Theorem

## Short Notes
The **Mean Value Theorem (MVT)** establishes a relationship between the average rate of change and the instantaneous rate of change of a function.

**Statement**: If f(x) is continuous on [a, b] and differentiable on (a, b), then there exists at least one c ∈ (a, b) such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

**Geometric Interpretation**: There exists a point where the tangent line is parallel to the secant line connecting (a, f(a)) and (b, f(b)).

## Key Theories & Formulas

### 1. Rolle's Theorem (Special Case of MVT)
If f(x) is continuous on [a, b], differentiable on (a, b), and **f(a) = f(b)**, then there exists at least one c ∈ (a, b) such that:
$$f'(c) = 0$$

### 2. Cauchy's Mean Value Theorem (Generalized MVT)
If f(x) and g(x) are both continuous on [a, b] and differentiable on (a, b), with g'(x) ≠ 0, then there exists c ∈ (a, b) such that:
$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

### 3. Applications of MVT

1. **Proving Inequalities**: Show $f'(x)$ bounds using MVT
2. **Finding Root Bounds**: If f(a), f(b) have opposite signs and f is continuous
3. **Proving Uniqueness of Roots**: Using Rolle's theorem in reverse
4. **Taylor's Theorem**: MVT is a special case of Taylor's with n=1

### 4. Common Results from MVT

- If f'(x) = 0 for all x ∈ (a, b), then f is constant on [a, b]
- If f'(x) > 0 for all x ∈ (a, b), then f is strictly increasing
- If f'(x) < 0 for all x ∈ (a, b), then f is strictly decreasing
- If |f'(x)| ≤ M for all x, then |f(b) - f(a)| ≤ M|b - a|

### 5. Lagrange's Mean Value Theorem
Another name for MVT. The value c is called the **mean value point** or **intermediate point**.

---

## Example Problems

**Problem 1**: Verify MVT for f(x) = x² on [1, 3] and find c.

**Solution**:

1. f is continuous on [1, 3] and differentiable on (1, 3) ✓
2. f(1) = 1, f(3) = 9
3. $\frac{f(3) - f(1)}{3 - 1} = \frac{9 - 1}{2} = 4$
4. f'(x) = 2x, so f'(c) = 2c = 4
5. **c = 2** ∈ (1, 3) ✓

**Problem 2**: Use Rolle's theorem to prove x³ - 3x + 1 = 0 has at least two roots in (-2, 2).

**Solution**:

1. f(-2) = -8 + 6 + 1 = -1
2. f(0) = 1
3. f(2) = 8 - 6 + 1 = 3
4. By IVT: one root in (-2, 0), another possibility in (0, 2)? f(1) = -1 < 0
5. Root in (0, 1) and root in (1, 2)
6. Between two roots, by Rolle's theorem, f'(c) = 0 somewhere
7. f'(x) = 3x² - 3 = 0 ⟹ x = ±1 (two critical points)
8. This confirms at least **two roots** in (-2, 2)

**Problem 3**: Show that $\sin x < x$ for x > 0.

**Solution**:

1. Let f(x) = x - sin x
2. f(0) = 0
3. f'(x) = 1 - cos x ≥ 0 for all x (equals 0 only when x = 2nπ)
4. f is non-decreasing, and strictly increasing except at isolated points
5. For x > 0: f(x) > f(0) = 0
6. Therefore, **x > sin x** for x > 0 ✓

---

## Hardest GATE Questions

**Topic: Finding the Mean Value Point**

**Question (GATE 2017 Style)**:
For f(x) = ln x on [1, e], find the value of c guaranteed by MVT.

**Solution**:

1. f(1) = 0, f(e) = 1
2. $\frac{f(e) - f(1)}{e - 1} = \frac{1 - 0}{e - 1} = \frac{1}{e - 1}$
3. f'(x) = 1/x, so f'(c) = 1/c
4. $\frac{1}{c} = \frac{1}{e-1}$
5. **c = e - 1** ≈ 1.718 ∈ (1, e) ✓

**Why it's hard**: Requires careful algebraic manipulation with natural logarithm.

---

**Topic: Cauchy's MVT Application**

**Question (GATE 2015 Variant)**:
Using Cauchy's MVT, prove that $\frac{\ln b - \ln a}{b - a} = \frac{1}{c}$ for some c ∈ (a, b) where 0 < a < b.

**Solution**:

1. Let f(x) = ln x, g(x) = x
2. f'(x) = 1/x, g'(x) = 1
3. By Cauchy's MVT:
   $$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

4. $$\frac{1/c}{1} = \frac{\ln b - \ln a}{b - a}$$
5. Therefore, $\frac{\ln b - \ln a}{b - a} = \frac{1}{c}$ for some c ∈ (a, b) ✓

**Corollary**: $\ln b - \ln a < \frac{b - a}{a}$ (since c > a implies 1/c < 1/a)

---

**Topic: Using MVT to Prove Bounds**

**Question**:
Show that for x > 0: $\frac{x}{1+x} < \ln(1+x) < x$

**Solution**:
**Upper bound (ln(1+x) < x)**:

1. Let f(t) = ln(1+t), apply MVT on [0, x]
2. f(x) - f(0) = f'(c) · x for some c ∈ (0, x)
3. ln(1+x) = $\frac{1}{1+c} \cdot x$
4. Since c > 0: $\frac{1}{1+c} < 1$
5. Therefore, ln(1+x) < x ✓

**Lower bound (x/(1+x) < ln(1+x))**:

1. Since c < x: $\frac{1}{1+c} > \frac{1}{1+x}$
2. ln(1+x) = $\frac{x}{1+c} > \frac{x}{1+x}$ ✓

---

## References

- [Mean value theorem (Wikipedia)](https://en.wikipedia.org/wiki/Mean_value_theorem)
- [Rolle's theorem (Wikipedia)](https://en.wikipedia.org/wiki/Rolle%27s_theorem)
