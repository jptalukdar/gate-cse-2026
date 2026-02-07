# Conditional Probability

## Short Notes
**Conditional probability** is the probability of an event occurring given that another event has already occurred.

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

This is fundamental to probabilistic reasoning and forms the basis for Bayes' theorem and probabilistic inference.

## Key Theories & Formulas

### 1. Multiplication Rule
$$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

**Chain Rule** for multiple events:
$$P(A_1 \cap A_2 \cap ... \cap A_n) = P(A_1) \cdot P(A_2|A_1) \cdot P(A_3|A_1 \cap A_2) \cdots$$

### 2. Conditional Probability Properties
- $P(A|B) + P(A'|B) = 1$
- $P(A \cup B | C) = P(A|C) + P(B|C) - P(A \cap B | C)$
- $P(\emptyset | B) = 0$, $P(S|B) = 1$

### 3. Law of Total Probability
If $B_1, B_2, ..., B_n$ form a partition of S:
$$P(A) = \sum_{i=1}^{n} P(A|B_i) \cdot P(B_i)$$

### 4. Independence vs Conditional Probability
- **Independent**: $P(A|B) = P(A)$ (B gives no information about A)
- **Dependent**: $P(A|B) \neq P(A)$

### 5. Conditional Expectation
$$E[X|Y=y] = \sum_x x \cdot P(X=x|Y=y)$$

**Tower Property**: $E[E[X|Y]] = E[X]$

### 6. Conditional Variance
$$Var(X|Y) = E[X^2|Y] - (E[X|Y])^2$$

**Total Variance Formula**:
$$Var(X) = E[Var(X|Y)] + Var(E[X|Y])$$

---

## Example Problems

**Problem 1**: A fair die is rolled. If the result is even, find P(result ≥ 4 | result is even).

**Solution**:
- Even outcomes: {2, 4, 6}
- Outcomes ≥ 4 among even: {4, 6}
- $P(\geq 4 | even) = \frac{2}{3}$

**Problem 2**: In a class, 60% are boys. 70% of boys and 80% of girls passed an exam. A student passed. Find the probability the student is a boy.

**Solution**:
1. P(Boy) = 0.6, P(Girl) = 0.4
2. P(Pass|Boy) = 0.7, P(Pass|Girl) = 0.8
3. P(Pass) = 0.7(0.6) + 0.8(0.4) = 0.42 + 0.32 = 0.74
4. $P(Boy|Pass) = \frac{0.7 \times 0.6}{0.74} = \frac{0.42}{0.74} = \mathbf{\frac{21}{37}} \approx 0.568$

**Problem 3**: Three machines M1, M2, M3 produce 30%, 45%, 25% of items. Defect rates: 2%, 3%, 2%. An item is defective. Find P(from M2).

**Solution**:
1. P(D) = 0.02(0.3) + 0.03(0.45) + 0.02(0.25)
   = 0.006 + 0.0135 + 0.005 = 0.0245
2. $P(M2|D) = \frac{0.03 \times 0.45}{0.0245} = \frac{0.0135}{0.0245} = \mathbf{\frac{27}{49}} \approx 0.551$

---

## Hardest GATE Questions

**Topic: Sequential Drawing**

**Question (GATE 2018 Style)**:
An urn has 5 white and 3 black balls. Balls are drawn one by one without replacement. Find P(third ball is white | first two are of different colors).

**Solution**:
1. Given: first two are different colors (one white, one black)
2. After drawing: 4 white, 2 black OR 5 white, 2 black remain? 
3. Either way: 4 white + 2 black = 6 balls remain
4. Case 1 (WB first): 4W, 2B remain → P(W) = 4/6
5. Case 2 (BW first): 4W, 2B remain → P(W) = 4/6
6. Both cases give same result: $P(3rd = W | different) = \mathbf{\frac{2}{3}}$

---

**Topic: Markov Property**

**Question (GATE 2017 Variant)**:
Rain on consecutive days has probability 0.7. Rain following no-rain has probability 0.4. Today is Monday with rain. Find P(rain on Wednesday).

**Solution**:
1. Let R = rain, N = no rain
2. P(Tue=R | Mon=R) = 0.7, P(Tue=N | Mon=R) = 0.3
3. P(Wed=R | Tue=R) = 0.7, P(Wed=R | Tue=N) = 0.4
4. P(Wed=R) = P(Wed=R|Tue=R)P(Tue=R) + P(Wed=R|Tue=N)P(Tue=N)
5. = 0.7(0.7) + 0.4(0.3) = 0.49 + 0.12 = **0.61**

---

**Topic: Conditional Independence**

**Question**:
Given $P(A|C) = 0.6$, $P(B|C) = 0.4$, and A, B are conditionally independent given C. Find $P(A \cup B | C)$.

**Solution**:
1. Conditional independence: $P(A \cap B | C) = P(A|C) \cdot P(B|C)$
2. $P(A \cap B | C) = 0.6 \times 0.4 = 0.24$
3. $P(A \cup B | C) = P(A|C) + P(B|C) - P(A \cap B | C)$
4. $= 0.6 + 0.4 - 0.24 = \mathbf{0.76}$

---

**Topic: Simpson's Paradox**

**Question**:
Hospital A treats 100 mild (90% success) and 100 severe (50% success) cases.
Hospital B treats 50 mild (80% success) and 150 severe (40% success) cases.

Which hospital has better overall success rate? Better conditional rates?

**Solution**:
**Hospital A**:
- Mild: 90, Severe: 50, Total: 140/200 = **70%**

**Hospital B**:
- Mild: 40, Severe: 60, Total: 100/200 = **50%**

**Paradox**: A has 70% overall vs B's 50%. But:
- For mild: A = 90% > B = 80% (A better)
- For severe: A = 50% > B = 40% (A better)

A is better in both categories AND overall! (No paradox here actually, but demonstrates conditional analysis importance)

---

## References
- [Conditional probability (Wikipedia)](https://en.wikipedia.org/wiki/Conditional_probability)
- [Law of total probability (Wikipedia)](https://en.wikipedia.org/wiki/Law_of_total_probability)
