# Limits, Continuity, Differentiability

## Short Notes

### Limits
The **limit** of a function f(x) as x approaches a point c is the value that f(x) approaches as x gets arbitrarily close to c.

$$\lim_{x \to c} f(x) = L$$

- **Left-hand limit (LHL)**: $\lim_{x \to c^-} f(x)$
- **Right-hand limit (RHL)**: $\lim_{x \to c^+} f(x)$
- Limit exists iff LHL = RHL

### Continuity
A function f(x) is **continuous** at x = c if:

1. f(c) is defined
2. $\lim_{x \to c} f(x)$ exists
3. $\lim_{x \to c} f(x) = f(c)$

### Differentiability
A function is **differentiable** at x = c if:
$$f'(c) = \lim_{h \to 0} \frac{f(c+h) - f(c)}{h}$$ exists.

**Key Relationship**: 
$$\text{Differentiable} \Rightarrow \text{Continuous} \Rightarrow \text{Limit exists}$$
(Converse is NOT always true!)

## Key Theories & Formulas

### 1. Standard Limits
| Limit | Value |
|-------|-------|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | 1 |
| $\lim_{x \to 0} \frac{\tan x}{x}$ | 1 |
| $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ |
| $\lim_{x \to 0} \frac{e^x - 1}{x}$ | 1 |
| $\lim_{x \to 0} \frac{\ln(1+x)}{x}$ | 1 |
| $\lim_{x \to 0} \frac{a^x - 1}{x}$ | $\ln a$ |
| $\lim_{x \to 0} (1 + x)^{1/x}$ | $e$ |
| $\lim_{x \to \infty} (1 + \frac{1}{x})^x$ | $e$ |
| $\lim_{x \to 0} \frac{\sin^{-1} x}{x}$ | 1 |
| $\lim_{x \to 0} \frac{\tan^{-1} x}{x}$ | 1 |

### 2. L'Hôpital's Rule
For indeterminate forms $\frac{0}{0}$ or $\frac{\infty}{\infty}$:
$$\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)}$$

**Other indeterminate forms**: $0 \cdot \infty$, $\infty - \infty$, $0^0$, $1^\infty$, $\infty^0$ (convert to $\frac{0}{0}$ or $\frac{\infty}{\infty}$)

### 3. Types of Discontinuity
| Type | Description |
|------|-------------|
| Removable | Limit exists but ≠ f(c), or f(c) undefined |
| Jump | LHL ≠ RHL (both finite) |
| Infinite | At least one limit is infinite |
| Oscillatory | Limit doesn't exist (e.g., $\sin(1/x)$ at x=0) |

### 4. Derivative Formulas
| Function | Derivative |
|----------|-----------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |

### 5. Non-Differentiable Cases
A function is NOT differentiable at x = c if:

- There's a corner/cusp (e.g., |x| at x = 0)
- There's a vertical tangent
- There's a discontinuity
- Left and right derivatives differ

---

## Example Problems

**Problem 1**: Evaluate $\lim_{x \to 0} \frac{\sin 5x}{3x}$

**Solution**:
$$\lim_{x \to 0} \frac{\sin 5x}{3x} = \lim_{x \to 0} \frac{\sin 5x}{5x} \cdot \frac{5}{3} = 1 \cdot \frac{5}{3} = \mathbf{\frac{5}{3}}$$

**Problem 2**: Check continuity of $f(x) = \begin{cases} \frac{\sin x}{x} & x \neq 0 \\ k & x = 0 \end{cases}$ at x = 0

**Solution**:

- $\lim_{x \to 0} \frac{\sin x}{x} = 1$
- For continuity: k = 1

**Problem 3**: Is $f(x) = |x|$ differentiable at x = 0?

**Solution**:

- Left derivative: $\lim_{h \to 0^-} \frac{|h| - 0}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$
- Right derivative: $\lim_{h \to 0^+} \frac{|h| - 0}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1$
- Left ≠ Right → **Not differentiable** at x = 0

---

## Hardest GATE Questions

**Topic: L'Hôpital's Rule with $1^\infty$ Form**

**Question (GATE 2018 Style)**:
Evaluate $\lim_{x \to 0} (\cos x)^{1/x^2}$

**Solution**:

1. Form: $1^\infty$ (indeterminate)
2. Let $y = (\cos x)^{1/x^2}$
3. $\ln y = \frac{\ln(\cos x)}{x^2}$
4. Apply L'Hôpital's Rule:
   $$\lim_{x \to 0} \frac{\ln(\cos x)}{x^2} = \lim_{x \to 0} \frac{-\tan x}{2x} = -\frac{1}{2}$$

5. $\ln y = -\frac{1}{2}$
6. $y = e^{-1/2} = \mathbf{\frac{1}{\sqrt{e}}}$

**Why it's hard**: Requires recognizing $1^\infty$ form and using logarithmic transformation.

---

**Topic: Differentiability at a Point**

**Question (GATE 2016 Variant)**:
For what value of n is $f(x) = x^n \sin(1/x)$ for $x \neq 0$, and $f(0) = 0$, differentiable at x = 0?

**Solution**:

1. Check derivative at x = 0:
   $$f'(0) = \lim_{h \to 0} \frac{h^n \sin(1/h)}{h} = \lim_{h \to 0} h^{n-1} \sin(1/h)$$

2. For this limit to exist:
   - $|h^{n-1} \sin(1/h)| \leq |h|^{n-1}$
   - Need $n - 1 > 0$, i.e., **n > 1**
3. For n = 2: limit = 0 (derivative exists)
4. For n = 1: limit oscillates (derivative doesn't exist)

**Answer**: $\mathbf{n > 1}$ (or n ≥ 2 for integer n)

---

**Topic: Continuity with Floor Function**

**Question**:
Find the number of points where $f(x) = [x] + \sqrt{x - [x]}$ is discontinuous in [0, 3].

**Solution**:

1. $f(x) = [x] + \sqrt{\{x\}}$ where {x} is the fractional part
2. $\sqrt{\{x\}}$ is continuous everywhere
3. [x] is discontinuous at integers: 1, 2, 3
4. At x = 1: LHL = 0 + 1 = 1, RHL = 1 + 0 = 1 → Continuous
5. At x = 2: LHL = 1 + 1 = 2, RHL = 2 + 0 = 2 → Continuous
6. At x = 3: LHL = 2 + 1 = 3, RHL = 3 + 0 = 3 → Continuous
7. **0 discontinuities** in [0, 3]

---

## References

- [Limit of a function (Wikipedia)](https://en.wikipedia.org/wiki/Limit_of_a_function)
- [Continuous function (Wikipedia)](https://en.wikipedia.org/wiki/Continuous_function)
- [Derivative (Wikipedia)](https://en.wikipedia.org/wiki/Derivative)
- [L'Hôpital's rule (Wikipedia)](https://en.wikipedia.org/wiki/L%27H%C3%B4pital%27s_rule)
