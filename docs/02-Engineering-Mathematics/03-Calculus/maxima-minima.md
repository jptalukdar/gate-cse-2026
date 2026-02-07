# Maxima & Minima

## Short Notes
**Maxima and Minima** (extrema) are the largest and smallest values of a function. Finding extrema is crucial for optimization problems.

- **Local Maximum**: f(c) ≥ f(x) for all x near c
- **Local Minimum**: f(c) ≤ f(x) for all x near c
- **Global (Absolute) Maximum/Minimum**: Largest/smallest value over the entire domain
- **Critical Point**: Where f'(x) = 0 or f'(x) doesn't exist

## Key Theories & Formulas

### 1. First Derivative Test
At a critical point c where f'(c) = 0:
| Sign Change of f'(x) | Conclusion |
|--------------------|------------|
| + to − (increasing to decreasing) | **Local Maximum** |
| − to + (decreasing to increasing) | **Local Minimum** |
| No sign change | **Neither** (inflection point) |

### 2. Second Derivative Test
At a critical point c where f'(c) = 0:
| f''(c) | Conclusion |
|--------|------------|
| f''(c) < 0 | **Local Maximum** (concave down) |
| f''(c) > 0 | **Local Minimum** (concave up) |
| f''(c) = 0 | **Inconclusive** (use first derivative test) |

### 3. Global Extrema on Closed Interval [a, b]
1. Find all critical points in (a, b)
2. Evaluate f at critical points and endpoints
3. Compare: largest = global max, smallest = global min

### 4. Multivariable Optimization (Two Variables)
For f(x, y), find critical points where $f_x = 0$ and $f_y = 0$.

**Second Derivative Test** using Hessian determinant:
$$D = f_{xx} \cdot f_{yy} - (f_{xy})^2$$

| Condition | Conclusion |
|-----------|------------|
| D > 0 and $f_{xx}$ < 0 | **Local Maximum** |
| D > 0 and $f_{xx}$ > 0 | **Local Minimum** |
| D < 0 | **Saddle Point** |
| D = 0 | **Inconclusive** |

### 5. Constrained Optimization (Lagrange Multipliers)
To optimize f(x, y) subject to constraint g(x, y) = 0:
$$\nabla f = \lambda \nabla g$$

Solve: $f_x = \lambda g_x$, $f_y = \lambda g_y$, $g(x, y) = 0$

---

## Example Problems

**Problem 1**: Find local extrema of f(x) = x³ - 3x + 2

**Solution**:
1. f'(x) = 3x² - 3 = 0 ⟹ x = ±1
2. f''(x) = 6x
3. At x = 1: f''(1) = 6 > 0 → **Local Minimum**, f(1) = 0
4. At x = -1: f''(-1) = -6 < 0 → **Local Maximum**, f(-1) = 4

**Problem 2**: Find global extrema of f(x) = x³ - 3x on [-2, 2]

**Solution**:
1. Critical points: f'(x) = 3x² - 3 = 0 ⟹ x = ±1
2. Evaluate:
   - f(-2) = -8 + 6 = -2
   - f(-1) = -1 + 3 = 2
   - f(1) = 1 - 3 = -2
   - f(2) = 8 - 6 = 2
3. **Global Max = 2** at x = -1 and x = 2
4. **Global Min = -2** at x = -2 and x = 1

**Problem 3**: Classify critical points of f(x, y) = x² + y² - 2x - 4y + 5

**Solution**:
1. $f_x = 2x - 2 = 0$ ⟹ x = 1
2. $f_y = 2y - 4 = 0$ ⟹ y = 2
3. Critical point: (1, 2)
4. $f_{xx} = 2$, $f_{yy} = 2$, $f_{xy} = 0$
5. D = 2 × 2 - 0 = 4 > 0 and $f_{xx}$ > 0
6. **Local Minimum** at (1, 2), f(1, 2) = 1 + 4 - 2 - 8 + 5 = **0**

---

## Hardest GATE Questions

**Topic: Second Derivative Test Failure**

**Question (GATE 2019 Style)**:
Classify the critical point of f(x) = x⁴ at x = 0.

**Solution**:
1. f'(x) = 4x³ = 0 ⟹ x = 0
2. f''(x) = 12x², f''(0) = 0 → Inconclusive!
3. Use first derivative test:
   - For x < 0: f'(x) = 4x³ < 0 (decreasing)
   - For x > 0: f'(x) = 4x³ > 0 (increasing)
4. Sign changes from − to + → **Local Minimum**
5. Alternative: f(x) = x⁴ ≥ 0 and f(0) = 0 → **Global Minimum**

**Why it's hard**: Second derivative test fails; must use first derivative test.

---

**Topic: Multivariable Saddle Point**

**Question (GATE 2017 Variant)**:
Classify all critical points of f(x, y) = x³ - 3xy + y³

**Solution**:
1. $f_x = 3x² - 3y = 0$ ⟹ y = x²
2. $f_y = -3x + 3y² = 0$ ⟹ x = y²
3. Substitute: x = (x²)² = x⁴ ⟹ x⁴ - x = 0 ⟹ x(x³ - 1) = 0
4. x = 0 or x = 1
5. Critical points: (0, 0) and (1, 1)
6. Hessian analysis:
   - $f_{xx} = 6x$, $f_{yy} = 6y$, $f_{xy} = -3$
   - At (0, 0): D = 0 - 9 = -9 < 0 → **Saddle Point**
   - At (1, 1): D = 36 - 9 = 27 > 0, $f_{xx}$ = 6 > 0 → **Local Minimum**

---

**Topic: Lagrange Multipliers**

**Question**:
Find the maximum value of f(x, y) = xy subject to x² + y² = 8.

**Solution**:
1. $\nabla f = (y, x)$, $\nabla g = (2x, 2y)$ where g = x² + y² - 8
2. $y = 2\lambda x$ and $x = 2\lambda y$
3. From these: $y = 2\lambda(2\lambda y) = 4\lambda² y$
4. Either y = 0 or λ² = 1/4 ⟹ λ = ±1/2
5. If λ = 1/2: y = x, so 2x² = 8 ⟹ x = ±2
6. Points: (2, 2), (-2, -2), (2, -2), (-2, 2)
7. f(2, 2) = 4, f(-2, -2) = 4, f(2, -2) = -4, f(-2, 2) = -4
8. **Maximum = 4** at (2, 2) and (-2, -2)

---

## References
- [Maxima and minima (Wikipedia)](https://en.wikipedia.org/wiki/Maxima_and_minima)
- [Lagrange multiplier (Wikipedia)](https://en.wikipedia.org/wiki/Lagrange_multiplier)
