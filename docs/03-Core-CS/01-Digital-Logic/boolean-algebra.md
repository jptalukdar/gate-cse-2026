# Boolean Algebra

## Short Notes
Boolean algebra is the branch of algebra in which the values of the variables are the truth values true and false, usually denoted 1 and 0 respectively.

### Basic Logic Gates
- **AND**: Output is 1 only if all inputs are 1. ($Y = A \cdot B$)
- **OR**: Output is 1 if any input is 1. ($Y = A + B$)
- **NOT**: Inverts the input. ($Y = \overline{A}$)
- **NAND**: NOT of AND. Universal gate. ($Y = \overline{A \cdot B}$)
- **NOR**: NOT of OR. Universal gate. ($Y = \overline{A + B}$)
- **XOR**: Output is 1 if inputs are different. ($Y = A \oplus B = \overline{A}B + A\overline{B}$)
- **XNOR**: Output is 1 if inputs are same. ($Y = A \odot B = AB + \overline{A}\overline{B}$)

## Key Theories & Formulas

### 1. Basic Identities
- **Idempotent Law**: $A+A = A$; $A \cdot A = A$
- **Identity Law**: $A+0 = A$; $A \cdot 1 = A$
- **Null Law**: $A+1 = 1$; $A \cdot 0 = 0$
- **Distributive Law**: $A+(BC) = (A+B)(A+C)$  *(Extremely important for GATE)*

### 2. De Morgan's Theorems
- $\overline{A+B} = \overline{A} \cdot \overline{B}$
- $\overline{A \cdot B} = \overline{A} + \overline{B}$

### 3. Consensus Theorem
- $AB + \overline{A}C + BC = AB + \overline{A}C$
- $(A+B)(\overline{A}+C)(B+C) = (A+B)(\overline{A}+C)$

### 4. Shannon's Expansion Theorem
$f(A, B, C, ...) = A \cdot f(1, B, C, ...) + \overline{A} \cdot f(0, B, C, ...)$

---

## Example Problems

**Problem:** Simplify the expression $Y = AB + A(B+C) + B(B+C)$.

1.  Expand: $Y = AB + AB + AC + BB + BC$
2.  Simplify $BB = B$: $Y = AB + AC + B + BC$
3.  Combine $B + BC = B$: $Y = AB + AC + B$
4.  Combine $B + AB = B$: $Y = B + AC$
**Result:** $Y = B + AC$

---

## Hardest GATE Questions

**Topic: Functional Completeness**
*A set of gates is functionally complete if any Boolean function can be implemented using only those gates.*

**Tricky Question (GATE 2016 Variant):** 
Is the set $\{\oplus, 1\}$ functionally complete?

- **Analysis:** XOR ($\oplus$) and the constant 1.
- We can get NOT: $\overline{A} = A \oplus 1$.
- To get AND/OR, we need some way to create a product. XOR is a linear function. $\{ \oplus, 1 \}$ can only generate linear functions (functions of form $a_0 \oplus a_1 x_1 \oplus ...$). 
- AND is not linear. Therefore, $\{ \oplus, 1 \}$ is **NOT** functionally complete.
- **Why it's hard:** Many students confuse "Universal Gates" (NAND/NOR) with "Functionally Complete Sets". Identifying non-trivial sets requires checking if they can implement {NOT, AND} or {NOT, OR}.
