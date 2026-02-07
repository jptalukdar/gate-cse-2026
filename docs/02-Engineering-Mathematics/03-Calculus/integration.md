# Integration

## Short Notes
**Integration** is the inverse of differentiation. It's used to find areas, volumes, and accumulated quantities.

- **Indefinite Integral**: $\int f(x) \, dx = F(x) + C$ where F'(x) = f(x)
- **Definite Integral**: $\int_a^b f(x) \, dx = F(b) - F(a)$ (Fundamental Theorem of Calculus)

## Key Theories & Formulas

### 1. Basic Integration Formulas
| Function | Integral |
|----------|----------|
| $\int x^n \, dx$ | $\frac{x^{n+1}}{n+1} + C$ (n ≠ -1) |
| $\int \frac{1}{x} \, dx$ | $\ln|x| + C$ |
| $\int e^x \, dx$ | $e^x + C$ |
| $\int a^x \, dx$ | $\frac{a^x}{\ln a} + C$ |
| $\int \sin x \, dx$ | $-\cos x + C$ |
| $\int \cos x \, dx$ | $\sin x + C$ |
| $\int \sec^2 x \, dx$ | $\tan x + C$ |
| $\int \csc^2 x \, dx$ | $-\cot x + C$ |
| $\int \sec x \tan x \, dx$ | $\sec x + C$ |
| $\int \frac{1}{1+x^2} \, dx$ | $\tan^{-1} x + C$ |
| $\int \frac{1}{\sqrt{1-x^2}} \, dx$ | $\sin^{-1} x + C$ |

### 2. Integration Techniques

#### Substitution (u-substitution)
$$\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du$$

#### Integration by Parts
$$\int u \, dv = uv - \int v \, du$$
**LIATE Rule** for choosing u: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential

#### Partial Fractions
For rational functions P(x)/Q(x):
- Factor Q(x)
- Decompose into simpler fractions
- Integrate each part

### 3. Special Integrals
| Integral | Result |
|----------|--------|
| $\int \frac{dx}{x^2 + a^2}$ | $\frac{1}{a} \tan^{-1}(\frac{x}{a}) + C$ |
| $\int \frac{dx}{x^2 - a^2}$ | $\frac{1}{2a} \ln|\frac{x-a}{x+a}| + C$ |
| $\int \frac{dx}{\sqrt{a^2 - x^2}}$ | $\sin^{-1}(\frac{x}{a}) + C$ |
| $\int \frac{dx}{\sqrt{x^2 + a^2}}$ | $\ln|x + \sqrt{x^2 + a^2}| + C$ |
| $\int \sqrt{a^2 - x^2} \, dx$ | $\frac{x}{2}\sqrt{a^2-x^2} + \frac{a^2}{2}\sin^{-1}(\frac{x}{a}) + C$ |

### 4. Properties of Definite Integrals
- $\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$
- $\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$
- $\int_a^b f(x) \, dx = \int_a^b f(a+b-x) \, dx$
- If f(-x) = f(x) (even): $\int_{-a}^a f(x) \, dx = 2\int_0^a f(x) \, dx$
- If f(-x) = -f(x) (odd): $\int_{-a}^a f(x) \, dx = 0$
- $\int_0^{2a} f(x) \, dx = 2\int_0^a f(x) \, dx$ if f(2a-x) = f(x)

### 5. Leibniz Rule (Differentiation under Integral)
$$\frac{d}{dx} \int_{a(x)}^{b(x)} f(t) \, dt = f(b(x)) \cdot b'(x) - f(a(x)) \cdot a'(x)$$

---

## Example Problems

**Problem 1**: Evaluate $\int_0^1 x e^{x^2} \, dx$

**Solution**:
1. Let u = x², du = 2x dx
2. $\int_0^1 x e^{x^2} \, dx = \frac{1}{2} \int_0^1 e^u \, du$
3. $= \frac{1}{2}[e^u]_0^1 = \frac{1}{2}(e - 1) = \mathbf{\frac{e-1}{2}}$

**Problem 2**: Evaluate $\int \frac{x}{x^2 + 4} \, dx$

**Solution**:
1. Let u = x² + 4, du = 2x dx
2. $= \frac{1}{2} \int \frac{du}{u} = \frac{1}{2} \ln|u| + C$
3. $= \mathbf{\frac{1}{2} \ln(x^2 + 4) + C}$

**Problem 3**: Evaluate $\int_0^\pi x \sin x \, dx$

**Solution** (Integration by Parts):
1. u = x, dv = sin x dx
2. du = dx, v = -cos x
3. $= [-x \cos x]_0^\pi + \int_0^\pi \cos x \, dx$
4. $= [-\pi(-1) - 0] + [\sin x]_0^\pi$
5. $= \pi + 0 = \mathbf{\pi}$

---

## Hardest GATE Questions

**Topic: Integration by Parts with Recursive Pattern**

**Question (GATE 2018 Style)**:
If $I_n = \int_0^{\pi/2} \sin^n x \, dx$, find the reduction formula.

**Solution**:
1. $I_n = \int_0^{\pi/2} \sin^{n-1} x \cdot \sin x \, dx$
2. Using IBP: u = sin^(n-1)x, dv = sin x dx
3. $I_n = [-\sin^{n-1}x \cos x]_0^{\pi/2} + (n-1)\int_0^{\pi/2} \sin^{n-2}x \cos^2 x \, dx$
4. $= 0 + (n-1)\int_0^{\pi/2} \sin^{n-2}x (1-\sin^2 x) \, dx$
5. $= (n-1)I_{n-2} - (n-1)I_n$
6. $I_n + (n-1)I_n = (n-1)I_{n-2}$
7. **$I_n = \frac{n-1}{n} I_{n-2}$**

**Wallis's Formula**:
- $I_n = \frac{(n-1)!!}{n!!} \times \begin{cases} \frac{\pi}{2} & n \text{ even} \\ 1 & n \text{ odd} \end{cases}$

---

**Topic: Leibniz Rule Application**

**Question (GATE 2016 Variant)**:
If $F(x) = \int_0^{x^2} e^{t^2} \, dt$, find F'(x).

**Solution**:
Using Leibniz Rule:
$$F'(x) = e^{(x^2)^2} \cdot 2x - e^0 \cdot 0 = \mathbf{2x \cdot e^{x^4}}$$

---

**Topic: Even/Odd Function Properties**

**Question**:
Evaluate $\int_{-\pi}^{\pi} (x^3 \cos x + x^2 \sin x) \, dx$

**Solution**:
1. Let f(x) = x³cos x + x²sin x
2. Check: f(-x) = (-x)³cos(-x) + (-x)²sin(-x) = -x³cos x - x²sin x = -f(x)
3. f(x) is **odd**!
4. $\int_{-\pi}^{\pi} f(x) \, dx = \mathbf{0}$

---

## References
- [Integral (Wikipedia)](https://en.wikipedia.org/wiki/Integral)
- [Integration by parts (Wikipedia)](https://en.wikipedia.org/wiki/Integration_by_parts)
- [Leibniz integral rule (Wikipedia)](https://en.wikipedia.org/wiki/Leibniz_integral_rule)
