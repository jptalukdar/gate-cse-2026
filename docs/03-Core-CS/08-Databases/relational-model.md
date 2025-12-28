# Relational Model (Algebra & Calculus)

## Short Notes
The relational model represents data as tables (relations).

### Relational Algebra (Procedural)
- **Selection ($\sigma$)**: Filter rows.
- **Projection ($\pi$)**: Filter columns.
- **Union ($\cup$)**, **Intersect ($\cap$)**, **Set Difference ($-$)**.
- **Cartesian Product ($\times$)**.
- **Join ($\bowtie$)**: $\sigma(R \times S)$.

## Key Theories & Formulas

### 1. Relational Calculus (Non-procedural)
- Tuple Relational Calculus (TRC).
- Domain Relational Calculus (DRC).
- **Safety**: An expression is safe if it produces a finite set of tuples.

### 2. Join Types
- **Natural Join**: Join on common attributes.
- **Outer Joins (Left, Right, Full)**: Include unmatched tuples from one or both tables.

### 3. Degree and Cardinality
- **Degree**: Number of columns. ($\text{Deg}(R \times S) = \text{Deg}(R) + \text{Deg}(S)$).
- **Cardinality**: Number of rows. ($\text{Card}(R \times S) = \text{Card}(R) \times \text{Card}(S)$).

---

## Example Problems

**Problem:** What is the result of $\pi_{\text{Name}}(\sigma_{\text{Age}>20}(R))$?
- **Result:** Names of all persons in R with age greater than 20.

---

## Hardest GATE Questions

**Topic: Division Operator and "Every" Queries**
**Tricky Question (GATE 2011/2013/2017):**
Translate "Find students who have taken **every** course offered by the CS department" into Relational Algebra.
- **Analysis:** This requires the **Division ($\div$)** operator.
- Expression: $\pi_{\text{SID, CID}}(\text{Enroll}) \div \pi_{\text{CID}}(\sigma_{\text{Dept}='CS'}(\text{Course}))$.
- **The "Trap":** SQL doesn't have a division operator. You must use `NOT EXISTS (NOT EXISTS ...)` or compare `COUNT` with a subquery.
- **Hard Aspect:** TRC expressions involving universal ($\forall$) and existential ($\exists$) quantifiers.
  - $\forall x (P(x)) \equiv \neg \exists x (\neg P(x))$.
- **Complexity:** Tuple count in multiple joins. 
  - Max and Min tuples in a natural join of $R(A, B)$ and $S(B, C)$ given their sizes.
  - If $B$ is a primary key in $S$, max tuples is $|R|$.
  - If $B$ is not a key in either, max tuples is $|R| \times |S|$

---

## References
- [Relational model (Wikipedia)](https://en.wikipedia.org/wiki/Relational_model)
