# Partial Orders and Lattices

## Short Notes

- **Relation**: Binary relation on set $S$.
- **POSET (Partially Ordered Set)**: A set $S$ with a relation $\preceq$ that is Reflexive, Anti-symmetric, and Transitive.
- **Hasse Diagram**: A graphical representation of a finite POSET, removing self-loops and implied transitive edges.

## Key Theories & Formulas

### 1. Elements in POSET

- **Maximal Element**: $m \in S$ s.t. no $x \in S$ has $m \preceq x$ (except $m$).
- **Maximum Element (Gratest)**: $g \in S$ s.t. $\forall x \in S, x \preceq g$. (Unique if exists).
- **Minimal** and **Minimum (Least)** defined analogously.
- **Upper Bound** of $A \subseteq S$: $x \in S$ s.t. $\forall a \in A, a \preceq x$.
- **LUB (Least Upper Bound / Supremum)**: The minimum of all upper bounds.
- **GLB (Greatest Lower Bound / Infimum)**: The maximum of all lower bounds.

### 2. Lattices

- **Lattice**: A POSET where every pair of elements $\{a, b\}$ has a unique LUB ($a \lor b$) and unique GLB ($a \land b$).
- **Bounded Lattice**: Has both a Greatest element (1) and Least element (0).
- **Complemented Lattice**: Bounded lattice where every element $a$ has a complement $a'$ such that $a \lor a' = 1$ and $a \land a' = 0$.
- **Distributive Lattice**: $a \lor (b \land c) = (a \lor b) \land (a \lor c)$.
- **Boolean Algebra**: A complemented distributive lattice.

---

## Example Problems

**Problem**: Is the set $D_{12}$ (divisors of 12) under divisibility a lattice?

- $D_{12} = \{1, 2, 3, 4, 6, 12\}$.
- For any $x, y \in D_{12}$:
  - $x \lor y = \text{LCM}(x, y) \in D_{12}$
  - $x \land y = \text{GCD}(x, y) \in D_{12}$
- Yes, this forms a lattice.
- Diagram (Bottom to Top):
  - 1 -> 2 -> 4 -> 12
  - 1 -> 3 -> 6 -> 12
  - 2 -> 6
  - 4 -> 12
- 1 is Bottom, 12 is Top.

---

## Hardest GATE Questions

**Topic: Counting Lattices**

**Tricky Question**:
Consider the set $A = \{a, b, c\}$. How many distinct Hasse diagrams are possible that represent a Lattice on $A$?
(i.e., How many Lattices on 3 labeled elements?)

- **Analysis**:
  - Lattice implies connected structure (conceptually).
  - Configurations:
    1. Linear chain: $x-y-z$. 3! permutations = 6.
    2. "V" shape? No, V shape ($a < c, b < c$) implies $a \lor b = c$, but $a \land b$ does not exist (undefined). So not a lattice.
    3. Wait, is that true? For $\{a, b, c\}$ to be a lattice, it must have top and bottom.
  - So, 3 elements must form a linear chain to be a lattice?
  - Let's check. If $a, b$ are incomparable, we need $a \land b$ (which must be $< a, b$) and $a \lor b$ (which must be $> a, b$).
  - If distinct bounds must exist, we need at least 4 elements for a "diamond" shape. With 3 elements, we simply cannot handle incomparable elements properly alongside bounds.
  - Exception: If $a < c, b < c$ and $a \land b$ is MISSING, it's not a lattice.
  - So on 3 elements, only a total ordering (Chain) is a lattice.
  - Number of total orders on 3 elements = $3! = 6$.
- **Result**: 6.
- **Why it's hard**: Requires testing small structures against Lattice axioms (LUB/GLB existence).

---

## References

- [Partially ordered set (Wikipedia)](https://en.wikipedia.org/wiki/Partially_ordered_set)
- [Lattice (order) (Wikipedia)](https://en.wikipedia.org/wiki/Lattice_(order))
