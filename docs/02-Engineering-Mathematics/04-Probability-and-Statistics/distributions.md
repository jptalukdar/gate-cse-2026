# Distributions

## Short Notes
A **probability distribution** describes how probabilities are distributed over the values of a random variable. Key distributions for GATE CSE include Uniform, Binomial, Poisson, Exponential, and Normal.

## Key Theories & Formulas

### 1. Discrete Distributions

#### Uniform Distribution (Discrete)
$X \sim Uniform\{1, 2, ..., n\}$

- PMF: $P(X = k) = \frac{1}{n}$
- Mean: $E[X] = \frac{n+1}{2}$
- Variance: $Var(X) = \frac{n^2 - 1}{12}$

#### Bernoulli Distribution
$X \sim Bernoulli(p)$ — single trial with success probability p

- PMF: $P(X = 1) = p$, $P(X = 0) = 1-p$
- Mean: $E[X] = p$
- Variance: $Var(X) = p(1-p)$

#### Binomial Distribution
$X \sim Binomial(n, p)$ — number of successes in n independent trials

- PMF: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- Mean: $E[X] = np$
- Variance: $Var(X) = np(1-p)$

#### Geometric Distribution
$X \sim Geometric(p)$ — number of trials until first success

- PMF: $P(X = k) = (1-p)^{k-1} p$, $k = 1, 2, ...$
- Mean: $E[X] = \frac{1}{p}$
- Variance: $Var(X) = \frac{1-p}{p^2}$
- **Memoryless Property**: $P(X > m+n | X > m) = P(X > n)$

#### Poisson Distribution
$X \sim Poisson(\lambda)$ — number of events in fixed interval

- PMF: $P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$
- Mean: $E[X] = \lambda$
- Variance: $Var(X) = \lambda$
- Sum of Poissons: $Poisson(\lambda_1) + Poisson(\lambda_2) = Poisson(\lambda_1 + \lambda_2)$

### 2. Continuous Distributions

#### Uniform Distribution (Continuous)
$X \sim Uniform(a, b)$

- PDF: $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$
- Mean: $E[X] = \frac{a+b}{2}$
- Variance: $Var(X) = \frac{(b-a)^2}{12}$

#### Exponential Distribution
$X \sim Exponential(\lambda)$

- PDF: $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$
- CDF: $F(x) = 1 - e^{-\lambda x}$
- Mean: $E[X] = \frac{1}{\lambda}$
- Variance: $Var(X) = \frac{1}{\lambda^2}$
- **Memoryless Property**: $P(X > s+t | X > s) = P(X > t)$

#### Normal (Gaussian) Distribution
$X \sim N(\mu, \sigma^2)$

- PDF: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
- Mean: $E[X] = \mu$
- Variance: $Var(X) = \sigma^2$
- **Standard Normal**: $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$

**68-95-99.7 Rule**:

- P(μ - σ < X < μ + σ) ≈ 68%
- P(μ - 2σ < X < μ + 2σ) ≈ 95%
- P(μ - 3σ < X < μ + 3σ) ≈ 99.7%

### 3. Key Relationships
| Approximation | Condition |
|--------------|-----------|
| $Binomial(n,p) \approx Poisson(np)$ | n large, p small, np moderate |
| $Binomial(n,p) \approx Normal(np, np(1-p))$ | n large, np ≥ 5, n(1-p) ≥ 5 |
| $Poisson(\lambda) \approx Normal(\lambda, \lambda)$ | λ large (≥ 20) |

---

## Example Problems

**Problem 1**: X ~ Binomial(10, 0.3). Find P(X = 3).

**Solution**:
$$P(X=3) = \binom{10}{3}(0.3)^3(0.7)^7 = 120 \times 0.027 \times 0.0824 = \mathbf{0.267}$$

**Problem 2**: Cars arrive at a toll booth at rate 3 per minute (Poisson). Find P(no cars in 30 seconds).

**Solution**:

1. Rate for 30 sec = 3/2 = 1.5
2. $P(X=0) = \frac{e^{-1.5}(1.5)^0}{0!} = e^{-1.5} = \mathbf{0.223}$

**Problem 3**: X ~ Exponential(0.5). Find P(X > 3 | X > 1).

**Solution** (using memoryless property):
$$P(X > 3 | X > 1) = P(X > 2) = e^{-0.5 \times 2} = e^{-1} = \mathbf{0.368}$$

---

## Hardest GATE Questions

**Topic: Poisson Distribution Applications**

**Question (GATE 2018 Style)**:
A computer system crashes on average 2 times per week (Poisson). Find the probability of at least 3 crashes in 2 weeks.

**Solution**:

1. Rate for 2 weeks: λ = 4
2. P(X ≥ 3) = 1 - P(X ≤ 2)
3. P(X ≤ 2) = $e^{-4}(1 + 4 + 8) = 13e^{-4} \approx 0.238$
4. P(X ≥ 3) = 1 - 0.238 = **0.762**

---

**Topic: Normal Distribution with Z-scores**

**Question (GATE 2017 Variant)**:
Exam scores are N(70, 100). What percentage of students score between 60 and 85? (Given: Φ(1.5) = 0.9332, Φ(1) = 0.8413)

**Solution**:

1. Z₁ = (60-70)/10 = -1
2. Z₂ = (85-70)/10 = 1.5
3. P(60 < X < 85) = Φ(1.5) - Φ(-1) = 0.9332 - (1 - 0.8413)
4. = 0.9332 - 0.1587 = **77.45%**

---

**Topic: Distribution Identification**

**Question**:
X has MGF $M_X(t) = e^{3(e^t - 1)}$. Identify the distribution and find P(X ≥ 2).

**Solution**:

1. MGF of Poisson(λ) is $e^{\lambda(e^t - 1)}$
2. Comparing: λ = 3, so $X \sim Poisson(3)$
3. P(X ≥ 2) = 1 - P(X = 0) - P(X = 1)
4. = 1 - e⁻³ - 3e⁻³ = 1 - 4e⁻³ ≈ 1 - 0.199 = **0.801**

---

**Topic: Sum of Random Variables**

**Question**:
X₁ ~ Poisson(2), X₂ ~ Poisson(3), X₃ ~ Poisson(5) independent. Find Var(X₁ + X₂ + X₃).

**Solution**:

1. Sum of independent Poissons: X₁ + X₂ + X₃ ~ Poisson(2+3+5) = Poisson(10)
2. For Poisson: Var = λ
3. **Var(X₁ + X₂ + X₃) = 10**

---

## References

- [Probability distribution (Wikipedia)](https://en.wikipedia.org/wiki/Probability_distribution)
- [Normal distribution (Wikipedia)](https://en.wikipedia.org/wiki/Normal_distribution)
- [Poisson distribution (Wikipedia)](https://en.wikipedia.org/wiki/Poisson_distribution)
