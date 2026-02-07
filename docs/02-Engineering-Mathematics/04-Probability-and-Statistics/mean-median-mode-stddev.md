# Mean, Median, Mode & Standard Deviation

## Short Notes
These are **measures of central tendency** and **measures of dispersion** that summarize data distributions.

- **Mean (μ)**: Average value — sensitive to outliers
- **Median**: Middle value — robust to outliers
- **Mode**: Most frequent value — can be multiple or none
- **Standard Deviation (σ)**: Measure of spread around the mean

## Key Theories & Formulas

### 1. Mean (Arithmetic Mean)
**For raw data**:
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

**For frequency distribution**:
$$\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$

**For grouped data** (using class marks):
$$\bar{x} = \frac{\sum f_i m_i}{\sum f_i}$$ where $m_i$ = class mark

**Properties**:

- $\sum(x_i - \bar{x}) = 0$
- If every value increases by k, mean increases by k
- If every value multiplied by k, mean multiplied by k

### 2. Median
**For ungrouped data**:

- Arrange in order
- If n is odd: Median = $x_{(n+1)/2}$
- If n is even: Median = $\frac{x_{n/2} + x_{n/2+1}}{2}$

**For grouped data**:
$$Median = L + \frac{(N/2 - CF)}{f} \times h$$

where:

- L = lower boundary of median class
- N = total frequency
- CF = cumulative frequency before median class
- f = frequency of median class
- h = class width

### 3. Mode
**For ungrouped data**: Most frequently occurring value

**For grouped data**:
$$Mode = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \times h$$

where:

- L = lower boundary of modal class
- f₁ = frequency of modal class
- f₀ = frequency of class before modal class
- f₂ = frequency of class after modal class
- h = class width

### 4. Relationship Between Mean, Median, Mode
For **moderately skewed** distributions:
$$Mode \approx 3 \times Median - 2 \times Mean$$

| Skewness | Relationship |
|----------|-------------|
| Symmetric | Mean = Median = Mode |
| Right skewed | Mode < Median < Mean |
| Left skewed | Mean < Median < Mode |

### 5. Variance and Standard Deviation
**Population Variance**:
$$\sigma^2 = \frac{\sum(x_i - \mu)^2}{N} = \frac{\sum x_i^2}{N} - \mu^2$$

**Sample Variance**:
$$s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$$ (Bessel's correction)

**Standard Deviation**: $\sigma = \sqrt{Var}$

### 6. Other Measures of Dispersion
| Measure | Formula |
|---------|---------|
| Range | max - min |
| Coefficient of Variation | $CV = \frac{\sigma}{\mu} \times 100\%$ |
| Interquartile Range (IQR) | Q₃ - Q₁ |

### 7. Combined Mean & Variance
For two groups with means $\bar{x}_1, \bar{x}_2$, sizes $n_1, n_2$:

**Combined Mean**:
$$\bar{x}_{combined} = \frac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$$

**Combined Variance**:
$$\sigma_{combined}^2 = \frac{n_1(\sigma_1^2 + d_1^2) + n_2(\sigma_2^2 + d_2^2)}{n_1 + n_2}$$

where $d_1 = \bar{x}_1 - \bar{x}_{combined}$, $d_2 = \bar{x}_2 - \bar{x}_{combined}$

---

## Example Problems

**Problem 1**: Find mean, median, mode: 2, 3, 3, 4, 5, 5, 5, 6, 7

**Solution**:

- **Mean**: (2+3+3+4+5+5+5+6+7)/9 = 40/9 ≈ **4.44**
- **Median**: 9 values → 5th value = **5**
- **Mode**: 5 appears most (3 times) → **5**

**Problem 2**: Data: 10, 20, 30, 40, 50. Find variance and standard deviation.

**Solution**:

1. Mean = 150/5 = 30
2. $\sum(x_i - 30)^2 = 400 + 100 + 0 + 100 + 400 = 1000$
3. Variance = 1000/5 = **200**
4. Standard Deviation = $\sqrt{200}$ = **14.14**

**Problem 3**: If the mean of 5 numbers is 8 and one number is removed, the mean becomes 7. Find the removed number.

**Solution**:

1. Sum of 5 numbers = 5 × 8 = 40
2. Sum of 4 numbers = 4 × 7 = 28
3. Removed number = 40 - 28 = **12**

---

## Hardest GATE Questions

**Topic: Combined Statistics**

**Question (GATE 2019 Style)**:
Group A: 50 students, mean = 60, standard deviation = 8
Group B: 100 students, mean = 75, standard deviation = 10
Find the combined standard deviation.

**Solution**:

1. Combined mean: $\bar{x}_c = \frac{50(60) + 100(75)}{150} = \frac{10500}{150} = 70$
2. $d_1 = 60 - 70 = -10$, $d_2 = 75 - 70 = 5$
3. Combined variance:
   $\sigma_c^2 = \frac{50(64 + 100) + 100(100 + 25)}{150} = \frac{50(164) + 100(125)}{150}$
   $= \frac{8200 + 12500}{150} = \frac{20700}{150} = 138$

4. Combined SD = $\sqrt{138}$ ≈ **11.75**

---

**Topic: Effect of Linear Transformation**

**Question (GATE 2016 Variant)**:
If the mean and variance of a dataset are 20 and 16, what are the mean and variance if each value is transformed by Y = 3X - 5?

**Solution**:

1. E[Y] = E[3X - 5] = 3E[X] - 5 = 3(20) - 5 = **55**
2. Var(Y) = Var(3X - 5) = 9·Var(X) = 9(16) = **144**
3. New SD = 12

---

**Topic: Coefficient of Variation**

**Question**:
Stock A has mean return 15% with SD 6%. Stock B has mean return 20% with SD 10%. Which stock is more consistent (less risky)?

**Solution**:

1. CV(A) = 6/15 × 100 = **40%**
2. CV(B) = 10/20 × 100 = **50%**
3. **Stock A is more consistent** (lower CV)

---

**Topic: Median from Grouped Data**

**Question**:
Find the median from:
| Class | 0-10 | 10-20 | 20-30 | 30-40 |
|-------|------|-------|-------|-------|
| Freq  | 5    | 15    | 20    | 10    |

**Solution**:

1. N = 50, N/2 = 25
2. Cumulative frequencies: 5, 20, 40, 50
3. Median class: 20-30 (CF just exceeds 25)
4. L = 20, CF = 20, f = 20, h = 10
5. Median = 20 + $\frac{25-20}{20}$ × 10 = 20 + 2.5 = **22.5**

---

## References

- [Arithmetic mean (Wikipedia)](https://en.wikipedia.org/wiki/Arithmetic_mean)
- [Median (Wikipedia)](https://en.wikipedia.org/wiki/Median)
- [Mode (statistics) (Wikipedia)](https://en.wikipedia.org/wiki/Mode_(statistics))
- [Standard deviation (Wikipedia)](https://en.wikipedia.org/wiki/Standard_deviation)
