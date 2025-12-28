# Normalization

## Short Notes
Normalization is the process of organizing data to reduce redundancy and improve data integrity.

### Functional Dependency (FD)
$X \to Y$ means the value of $X$ uniquely determines $Y$.
- **Closure of attributes ($X^+$)**: Set of all attributes determined by $X$.
- **Candidate Key**: $K$ is a candidate key if $K^+ = \text{All attributes}$ and no subset of $K$ is a key.

## Key Theories & Formulas

### 1. Normal Forms
- **1NF**: Atomic values. No multi-valued attributes.
- **2NF**: In 1NF + No **Partial Functional Dependency**. (Non-prime attribute depends on full candidate key).
- **3NF**: In 2NF + No **Transitive Functional Dependency**. ($X \to A$ where $X$ is not a superkey and $A$ is not prime).
- **BCNF**: For every $X \to A$, $X$ must be a superkey.

### 2. Properties
- **Lossless Join Decomposition**: $R_1 \cap R_2 \to R_1$ or $R_1 \cap R_2 \to R_2$.
- **Dependency Preserving**: $(F_1 \cup F_2)^+ = F^+$.

---

## Example Problems

**Problem:** $R(A, B, C, D)$, $F = \{A \to B, B \to C, C \to D\}$. Find Key and NF.
1. $A^+ = \{A, B, C, D\} \implies$ Key is $A$.
2. $B \to C$ is a Transitive Dependency ($B$ is not a key).
**Result:** 2NF (since no partial dependency on $A$) but not 3NF.

---

## Hardest GATE Questions

**Topic: Dependency Preservation for BCNF**
**Tricky Question (GATE 2011/2013/2018):**
Is it always possible to decompose a relation into BCNF that is both lossless and dependency preserving?
- **Analysis:** **NO**. 3NF always allows lossless + dependency preserving. BCNF always allows lossless, but **might not allow dependency preservation**.
- **The "Trap":** Minimal Cover calculation.
  - Finding the Canonical Cover requires removing extraneous attributes and redundant FDs.
- **Hard Aspect:** Counting the number of Candidate Keys for a given set of FDs.
  - Example: $R(A, B, C, D)$, $F = \{AB \to CD, CD \to AB\}$. Keys: $\{AB, CD\}$.
- **Complexity:** Higher Normal Forms (4NF for Multi-valued dependencies, 5NF for Join dependencies). Rarely asked but important to know definitions.
