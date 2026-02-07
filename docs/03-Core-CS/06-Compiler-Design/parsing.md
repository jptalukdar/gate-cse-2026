# Parsing

## Short Notes
Parsing (Syntax Analysis) checks if the tokens follow the grammar rules and builds a **Parse Tree**.

### Types of Parsers

1.  **Top-Down**: Starts from root (Start symbol) and reaches leaves. (LL parsers, Recursive Descent).
2.  **Bottom-Up**: Starts from leaves (Tokens) and reduces to root. (LR parsers, Operator Precedence).

## Key Theories & Formulas

### 1. LL(1) Parsing

- Left-to-right scan, Leftmost derivation, 1 token lookahead.
- **Condition**: For $A \to \alpha \mid \beta$, $FIRST(\alpha) \cap FIRST(\beta) = \emptyset$.
- **Requirement**: No Left Recursion, No Left Factoring required.

### 2. LR Parsing

- Left-to-right scan, Reverse of Rightmost derivation.
- Power hierarchy: $LR(0) < SLR < LALR < CLR$.
- **Number of States**: $LR(0), SLR, LALR$ have the same number of states. $CLR$ has many more.

### 3. Operator Precedence Parsing

- Only works for "Operator Grammars". No $\epsilon$ or adjacent non-terminals.

---

## Example Problems

**Problem:** Find FIRST and FOLLOW for:
$S \to aAB$
$A \to b \mid \epsilon$
$B \to c$

- $FIRST(A) = \{b, \epsilon\}$
- $FIRST(S) = \{a\}$
- $FOLLOW(A) = FIRST(B) = \{c\}$

---

## Hardest GATE Questions

**Topic: Conflict Analysis in Parsing Tables**
**Tricky Question (GATE 2011/2013/2018):**
Given an LR item set, is there a shift-reduce (S-R) or reduce-reduce (R-R) conflict?

- **Analysis:** 
  - **S-R Conflict**: A state has $A \to \alpha \cdot a \beta$ and $B \to \gamma \cdot$ where $a \in FOLLOW(B)$ in SLR.
  - **R-R Conflict**: Two reductions in the same state for the same lookahead.
- **The "Trap":** "LALR vs CLR".
  - Merging two CLR states with same core but different lookaheads into one LALR state **can create R-R conflicts** but **never S-R conflicts**.
  - This is a very common theoretical question.
- **Hard Aspect:** Identifying if a grammar is LR(1) by manually building the item sets.
- **Complexity:** Parsing complexity $O(n^3)$ for any CFG (CYK algorithm), but $O(n)$ for LR/LL grammars

---

## References

- [Parsing (Wikipedia)](https://en.wikipedia.org/wiki/Parsing)
- [Recursive descent parser (Wikipedia)](https://en.wikipedia.org/wiki/Recursive_descent_parser)
- [LR parser (Wikipedia)](https://en.wikipedia.org/wiki/LR_parser)
