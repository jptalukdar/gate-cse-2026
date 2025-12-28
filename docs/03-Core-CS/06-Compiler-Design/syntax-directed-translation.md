# Syntax-Directed Translation

## Short Notes
Syntax-Directed Translation (SDT) attaches "semantic actions" or "rules" to grammar productions to compute values during parsing.

### Attribute Types
- **Synthesized**: Value computed from children in the parse tree. ($E = E_1 + T$).
- **Inherited**: Value computed from parent or siblings.

## Key Theories & Formulas

### 1. Categories of SDD
- **S-Attributed**: Uses only synthesized attributes. Can be evaluated during bottom-up parsing.
- **L-Attributed**: Uses synthesized and specific inherited attributes (only from parent or siblings to the **left**).

### 2. Implementation
- S-attributed is naturally implemented on the LR parser stack.
- L-attributed requires a traversal (often Depth-First).

---

## Example Problems

**Problem:** For $E \to E_1 + T \{ E.val = E_1.val + T.val \}$. What type of attribute is `val`?
- **Result:** Synthesized.

---

## Hardest GATE Questions

**Topic: Evaluation Order and Side-Effects**
**Tricky Question (GATE 2012/2014/2019):**
Can a given SDT be evaluated in a single pass during a Top-Down or Bottom-Up parse?
- **Analysis:** 
  - Single pass Top-Down: Grammar must be LL(1) and SDT must be L-attributed.
  - Single pass Bottom-Up: SDT must be S-attributed.
- **The "Trap":** "Post-fix SDT". 
  - If actions are only at the end of productions (e.g., $A \to XYZ \{ action \}$), it's a post-fix SDT.
- **Hard Aspect:** Calculating the values of a complex SDT with both inherited and synthesized attributes.
  - Example: $T \to F T'$, $T' \to * F T'_1$ where values are passed down through $T'$.
- **Complexity:** Dependency Graphs. A cycle in the dependency graph means the attribute values cannot be computed.
