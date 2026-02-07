# Sets, Relations, and Functions

## Short Notes

- **Power Set**: The set of all subsets. $|P(S)| = 2^{|S|}$.
- **Relation**: A subset of $A \times B$.
- **Reflexive**: $\forall a \in A, (a,a) \in R$.
- **Symmetric**: if $(a,b) \in R \implies (b,a) \in R$.
- **Transitive**: if $(a,b) \in R \land (b,c) \in R \implies (a,c) \in R$.
- **Equivalence Relation**: Reflexive + Symmetric + Transitive.
- **Partial Order**: Reflexive + Anti-Symmetric + Transitive.
- **Function**: mapping where every element in Domain maps to unique element in Codomain.

## Key Theories & Formulas

### 1. Number of Relations
For $|A| = n$:

- Total Relations on $A$: $2^{n^2}$
- Reflexive Relations: $2^{n^2 - n}$
- Symmetric Relations: $2^{n(n+1)/2}$
- Anti-Symmetric Relations: $2^n \cdot 3^{n(n-1)/2}$

### 2. Function Properties

- **Injective (One-to-One)**: $f(x) = f(y) \implies x = y$.
- **Surjective (Onto)**: Range = Codomain.
- **Bijective**: Injective + Surjective.
- Number of functions from set A ($m$) to set B ($n$): $n^m$.
- Number of Injective functions ($n \ge m$): $P(n, m) = \frac{n!}{(n-m)!}$.
- Number of Surjective functions ($m \ge n$): $n^m - \binom{n}{1}(n-1)^m + \binom{n}{2}(n-2)^m - ...$

### 3. Countability

- **Countable**: Finite or matches cardinality of Integers (e.g., $\mathbb{Z}, \mathbb{Q}$, set of all C programs).
- **Uncountable**: Matches cardinality of Reals (e.g., $\mathbb{R}, P(\mathbb{N})$).
- Diagonalization argument is used to prove uncountability.

---

## Example Problems

**Problem**: How many equivalence relations are there on a set with 3 elements $\{1, 2, 3\}$?

- Based on **Bell Numbers** ($B_n$).
- $B_3$: Partitions of {1, 2, 3}.
  - {{1}, {2}, {3}} - 1 way
  - {{1, 2}, {3}}, {{1, 3}, {2}}, {{2, 3}, {1}} - 3 ways
  - {{1, 2, 3}} - 1 way
- Total = $1 + 3 + 1 = 5$.

---

## Hardest GATE Questions

**Topic: Properties of Relations**

**Tricky Question**:
Let $R$ be a non-empty relation on a set $A$. Use quantifiers to say $R$ is NOT symmetric.

- **Definition of Symmetric**: $\forall x \forall y ((x,y) \in R \to (y,x) \in R)$.
- **Negation (NOT Symmetric)**: $\neg (\forall x \forall y ((x,y) \in R \to (y,x) \in R))$.
- $\equiv \exists x \exists y \neg ((x,y) \in R \to (y,x) \in R)$.
- recall $\neg(p \to q) \equiv p \land \neg q$.
- **Result**: $\exists x \exists y ((x,y) \in R \land (y,x) \notin R)$.
- **Why it's hard**: Understanding that "Not Symmetric" does *not* mean "Anti-symmetric". It simply means the symmetry property fails for at least one pair.

**Topic: Countability**
**Question**: Is the set of all functions from $\mathbb{N}$ to $\{0, 1\}$ countable?

- This is equivalent to determining the cardinality of infinite binary strings.
- This is $2^{|\mathbb{N}|} = |\mathbb{R}|$.
- **Result**: Uncountable. (Cantor's Diagonalization).

---

## References

- [Set theory (Wikipedia)](https://en.wikipedia.org/wiki/Set_theory)
- [Binary relation (Wikipedia)](https://en.wikipedia.org/wiki/Binary_relation)
- [Function (mathematics) (Wikipedia)](https://en.wikipedia.org/wiki/Function_(mathematics))
