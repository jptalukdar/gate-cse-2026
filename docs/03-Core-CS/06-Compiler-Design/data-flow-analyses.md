# Data Flow Analyses

## Short Notes
Data Flow Analysis (DFA) collects information about the values of variables at different points in the program.

### Key Types
- **Liveness Analysis**: Is a variable "live" (will it be used in the future)? Used for Register Allocation.
- **Reaching Definitions**: Which definitions of a variable can reach a certain point?
- **Available Expressions**: Which expressions have already been computed?

## Key Theories & Formulas

### 1. Data Flow Equations
Typically solved using iterative fixed-point algorithms.
- **Forward Analysis**: $Out[B] = f_B(In[B])$
- **Backward Analysis**: $In[B] = f_B(Out[B])$ (e.g., Liveness).

### 2. Loop Optimizations (Global)
- **Code Motion (Loop Invariant Code Motion)**: Move code outside the loop if its result doesn't change during iterations.
- **Induction Variable Elimination**: Removing redundant counters.

---

## Example Problems

**Problem:** Which analysis is used for Register Allocation?
- **Result:** Liveness Analysis. We want to know if a register can be reused because the variable it currently holds is "dead".

---

## Hardest GATE Questions

**Topic: Iterative Convergence and Lattice Theory**
**Tricky Question (GATE CS 2014):**
Given a flow graph and definitions, find the set of reaching definitions at the entry of a block.
- **Analysis:** Requires building the $Gen[B]$ and $Kill[B]$ sets for each block and iterating until $In[B]$ and $Out[B]$ values stop changing.
- **The "Trap":** "Very Busy Expressions" vs "Available Expressions".
- **Hard Aspect:** Loop Invariant Code Motion with side-effects.
  - Question: "Can `x = y + z` be moved out of a loop if `x` is redefined later in the same loop?" (No).
- **Complexity:** Data flow for pointers and arrays (Alias Analysis). Pointers make data flow significantly more complex as one write could affect multiple variables

---

## References
- [Data-flow analysis (Wikipedia)](https://en.wikipedia.org/wiki/Data-flow_analysis)
