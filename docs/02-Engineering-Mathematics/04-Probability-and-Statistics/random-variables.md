# Random Variables

## Short Notes
A **random variable** is a function that assigns a numerical value to each outcome in a sample space.

- **Discrete Random Variable**: Takes countable values (e.g., 0, 1, 2, ...)
- **Continuous Random Variable**: Takes any value in an interval

## Key Theories & Formulas

### 1. Probability Mass Function (PMF) - Discrete
$$P(X = x) = p(x)$$

Properties:
- $p(x) \geq 0$ for all x
- $\sum_{x} p(x) = 1$

### 2. Probability Density Function (PDF) - Continuous
$$f(x) \geq 0$$

Properties:
- $\int_{-\infty}^{\infty} f(x) \, dx = 1$
- $P(a \leq X \leq b) = \int_a^b f(x) \, dx$
- $P(X = a) = 0$ for continuous variables

### 3. Cumulative Distribution Function (CDF)
$$F(x) = P(X \leq x) = \begin{cases} \sum_{t \leq x} p(t) & \text{discrete} \\ \int_{-\infty}^x f(t) \, dt & \text{continuous} \end{cases}$$

Properties:
- $0 \leq F(x) \leq 1$
- F is non-decreasing
- $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$
- $P(a < X \leq b) = F(b) - F(a)$

### 4. Expected Value (Mean)
$$E[X] = \mu = \begin{cases} \sum_x x \cdot p(x) & \text{discrete} \\ \int_{-\infty}^{\infty} x \cdot f(x) \, dx & \text{continuous} \end{cases}$$

**Properties**:
- $E[c] = c$ (constant)
- $E[aX + b] = aE[X] + b$
- $E[X + Y] = E[X] + E[Y]$ (always true)
- $E[XY] = E[X] \cdot E[Y]$ (only if X, Y independent)

### 5. Variance and Standard Deviation
$$Var(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

**Properties**:
- $Var(c) = 0$
- $Var(aX + b) = a^2 \cdot Var(X)$
- $Var(X + Y) = Var(X) + Var(Y)$ (if X, Y independent)

$$\sigma = \sqrt{Var(X)}$$ (Standard Deviation)

### 6. Higher Moments
- **n-th moment about origin**: $E[X^n]$
- **n-th moment about mean**: $E[(X - \mu)^n]$
- **Coefficient of Variation**: $CV = \frac{\sigma}{\mu}$

### 7. Moment Generating Function (MGF)
$$M_X(t) = E[e^{tX}]$$

Useful property: $E[X^n] = M_X^{(n)}(0)$ (n-th derivative at t=0)

---

## Example Problems

**Problem 1**: A random variable X has PMF: P(X=1) = 0.2, P(X=2) = 0.5, P(X=3) = 0.3. Find E[X] and Var(X).

**Solution**:
1. $E[X] = 1(0.2) + 2(0.5) + 3(0.3) = 0.2 + 1 + 0.9 = \mathbf{2.1}$
2. $E[X^2] = 1(0.2) + 4(0.5) + 9(0.3) = 0.2 + 2 + 2.7 = 4.9$
3. $Var(X) = E[X^2] - (E[X])^2 = 4.9 - 4.41 = \mathbf{0.49}$

**Problem 2**: If X has PDF $f(x) = 2x$ for $0 \leq x \leq 1$, find E[X].

**Solution**:
$$E[X] = \int_0^1 x \cdot 2x \, dx = 2\int_0^1 x^2 \, dx = 2 \cdot \frac{x^3}{3}\Big|_0^1 = \frac{2}{3}$$

**Problem 3**: If E[X] = 5 and Var(X) = 4, find E[(2X + 3)²].

**Solution**:
1. $E[(2X + 3)^2] = E[4X^2 + 12X + 9]$
2. $= 4E[X^2] + 12E[X] + 9$
3. $E[X^2] = Var(X) + (E[X])^2 = 4 + 25 = 29$
4. $= 4(29) + 12(5) + 9 = 116 + 60 + 9 = \mathbf{185}$

---

## Hardest GATE Questions

**Topic: CDF to PDF Conversion**

**Question (GATE 2017 Style)**:
A random variable X has CDF:
$$F(x) = \begin{cases} 0 & x < 0 \\ x^2 & 0 \leq x \leq 1 \\ 1 & x > 1 \end{cases}$$
Find P(0.5 < X < 0.8).

**Solution**:
1. $P(0.5 < X < 0.8) = F(0.8) - F(0.5)$
2. $= (0.8)^2 - (0.5)^2 = 0.64 - 0.25 = \mathbf{0.39}$

---

**Topic: Independence and Expectation**

**Question (GATE 2018 Variant)**:
X and Y are independent random variables with E[X] = 2, E[Y] = 3, Var(X) = 1, Var(Y) = 4. Find E[(X-Y)²].

**Solution**:
1. $E[(X-Y)^2] = Var(X-Y) + (E[X-Y])^2$
2. $Var(X-Y) = Var(X) + Var(Y) = 1 + 4 = 5$ (independent)
3. $E[X-Y] = E[X] - E[Y] = 2 - 3 = -1$
4. $E[(X-Y)^2] = 5 + 1 = \mathbf{6}$

---

**Topic: MGF Application**

**Question**:
If the MGF of X is $M_X(t) = e^{3t + 2t^2}$, find E[X] and Var(X).

**Solution**:
1. $M_X'(t) = (3 + 4t)e^{3t + 2t^2}$
2. $E[X] = M_X'(0) = 3 \cdot 1 = \mathbf{3}$
3. $M_X''(t) = 4e^{3t+2t^2} + (3+4t)^2 e^{3t+2t^2}$
4. $E[X^2] = M_X''(0) = 4 + 9 = 13$
5. $Var(X) = 13 - 9 = \mathbf{4}$

---

## References
- [Random variable (Wikipedia)](https://en.wikipedia.org/wiki/Random_variable)
- [Expected value (Wikipedia)](https://en.wikipedia.org/wiki/Expected_value)
- [Variance (Wikipedia)](https://en.wikipedia.org/wiki/Variance)
