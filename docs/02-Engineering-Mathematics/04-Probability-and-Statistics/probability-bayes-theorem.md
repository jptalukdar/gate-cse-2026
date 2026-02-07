# Probability & Bayes' Theorem

## Short Notes
**Probability** quantifies the likelihood of an event occurring, ranging from 0 (impossible) to 1 (certain).

- **Sample Space (S)**: Set of all possible outcomes
- **Event (E)**: A subset of the sample space
- **Classical Probability**: $P(E) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$

**Bayes' Theorem** relates conditional probabilities and is fundamental for updating beliefs based on new evidence.

## Key Theories & Formulas

### 1. Probability Axioms
1. $P(E) \geq 0$ for any event E
2. $P(S) = 1$ (S = sample space)
3. If $E_1, E_2, ...$ are mutually exclusive: $P(\bigcup E_i) = \sum P(E_i)$

### 2. Basic Probability Rules
| Rule | Formula |
|------|---------|
| Complement | $P(A') = 1 - P(A)$ |
| Addition | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Mutually Exclusive | $P(A \cup B) = P(A) + P(B)$ (if $A \cap B = \emptyset$) |
| De Morgan's Laws | $P((A \cup B)') = P(A' \cap B')$ |

### 3. Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

**Multiplication Rule**: $P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$

### 4. Independence
Two events A and B are **independent** if:
$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalently: $P(A|B) = P(A)$ and $P(B|A) = P(B)$

### 5. Total Probability Theorem
If $B_1, B_2, ..., B_n$ partition the sample space:
$$P(A) = \sum_{i=1}^{n} P(A|B_i) \cdot P(B_i)$$

### 6. Bayes' Theorem
$$P(B_j|A) = \frac{P(A|B_j) \cdot P(B_j)}{\sum_{i=1}^{n} P(A|B_i) \cdot P(B_i)}$$

**Simplified form** (two hypotheses):
$$P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A|B) \cdot P(B) + P(A|B') \cdot P(B')}$$

### 7. Odds Form of Bayes' Theorem
$$\frac{P(B|A)}{P(B'|A)} = \frac{P(A|B)}{P(A|B')} \cdot \frac{P(B)}{P(B')}$$

Posterior Odds = Likelihood Ratio × Prior Odds

---

## Example Problems

**Problem 1**: A bag has 3 red and 2 blue balls. Two balls are drawn without replacement. Find P(second is red | first is red).

**Solution**:
- After first red: 2 red, 2 blue remain (4 balls)
- P(second red | first red) = $\frac{2}{4} = \mathbf{0.5}$

**Problem 2**: For independent events A and B, if P(A) = 0.4 and P(B) = 0.3, find P(A ∪ B).

**Solution**:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.4 + 0.3 - 0.12 = \mathbf{0.58}$$

**Problem 3** (Classic Bayes): A test for disease D has:
- Sensitivity: P(+|D) = 0.99 (true positive rate)
- Specificity: P(-|D') = 0.95 (true negative rate)
- Prevalence: P(D) = 0.01

Find P(D|+) (probability of disease given positive test).

**Solution**:
1. P(+|D') = 1 - 0.95 = 0.05 (false positive rate)
2. P(+) = P(+|D)P(D) + P(+|D')P(D')
   = 0.99(0.01) + 0.05(0.99) = 0.0099 + 0.0495 = 0.0594
3. $P(D|+) = \frac{0.99 \times 0.01}{0.0594} = \frac{0.0099}{0.0594} = \mathbf{0.167}$ (about 17%)

---

## Hardest GATE Questions

**Topic: Triple Event Probability**

**Question (GATE 2019 Style)**:
Events A, B, C are independent with P(A) = 0.5, P(B) = 0.3, P(C) = 0.2. Find P(exactly two events occur).

**Solution**:
1. P(exactly A and B, not C) = P(A)P(B)P(C') = 0.5 × 0.3 × 0.8 = 0.12
2. P(exactly A and C, not B) = P(A)P(B')P(C) = 0.5 × 0.7 × 0.2 = 0.07
3. P(exactly B and C, not A) = P(A')P(B)P(C) = 0.5 × 0.3 × 0.2 = 0.03
4. P(exactly two) = 0.12 + 0.07 + 0.03 = **0.22**

---

**Topic: Bayes with Multiple Hypotheses**

**Question (GATE 2016 Variant)**:
Box 1 has 4 red, 6 blue balls. Box 2 has 7 red, 3 blue balls. A box is chosen randomly, and a ball is drawn. If the ball is red, what is the probability it came from Box 2?

**Solution**:
1. P(Box 1) = P(Box 2) = 0.5
2. P(Red|Box 1) = 4/10 = 0.4
3. P(Red|Box 2) = 7/10 = 0.7
4. P(Red) = 0.4(0.5) + 0.7(0.5) = 0.55
5. $P(Box 2|Red) = \frac{0.7 \times 0.5}{0.55} = \frac{0.35}{0.55} = \mathbf{\frac{7}{11}}$

---

**Topic: Conditional Independence Trap**

**Question**:
Events A and B are conditionally independent given C, i.e., P(A ∩ B | C) = P(A|C)P(B|C). Does this imply A and B are (unconditionally) independent?

**Solution**:
**NO!** Conditional independence does not imply unconditional independence.

**Counter-example**: Fair coin flipped twice.
- A = "first flip is heads"
- B = "second flip is heads"  
- C = "both flips same"

A and B are independent, but given C, they become dependent!

---

## References
- [Probability (Wikipedia)](https://en.wikipedia.org/wiki/Probability)
- [Bayes' theorem (Wikipedia)](https://en.wikipedia.org/wiki/Bayes%27_theorem)
- [Conditional probability (Wikipedia)](https://en.wikipedia.org/wiki/Conditional_probability)
