# Finite Automata & Regular Expressions

## Short Notes
Finite Automata (FA) are the simplest machines used to recognize Regular Languages.

### Types
- **DFA (Deterministic)**: Unique transition for every (state, symbol).
- **NFA (Non-deterministic)**: Zero, one, or multiple transitions for a (state, symbol).
- **$\epsilon$-NFA**: NFA allowed to change state without consuming any input.
- **Equivalence**: DFA $\equiv$ NFA $\equiv$ $\epsilon$-NFA. All recognize the same set of languages (Regular).

## Key Theories & Formulas

### 1. NFA to DFA Conversion
- A DFA equivalent to an $n$-state NFA can have up to **$2^n$** states (Power Set Construction).

### 2. Regular Expressions (RE)
Algebraic description of a regular language. Basic operators: Union ($+$), Concatenation ($\cdot$), Kleene Closure ($^*$).
- **Identity**: $(a+b)^* = (a^*b^*)^* = (a^*+b^*)^*$

---

[... existing tutorials on ε-NFA to RE and Transition Tables ...]

---

## Example Problems

**Problem:** Find the minimum DFA for a language over $\{0, 1\}$ that ends with `01`.
- States:
  1. $q_0$ (Start/Neither)
  2. $q_1$ (Just saw `0`)
  3. $q_2$ (Final - Just saw `01`)
- **Result:** 3 states.

---

## Hardest GATE Questions

**Topic: DFA Minimization with Unreachable States**
**Tricky Question (GATE 2011/2013/2018):**
How many states are in the minimized DFA that accepts all strings over $\{a, b\}$ NOT containing the substring `aba`?
- **Analysis:** 
  1. Build DFA for "contains `aba`" (4 states: start, `a`, `ab`, `aba`).
  2. The 4th state is a trap state.
  3. Complement the DFA by swapping final and non-final states.
  4. Minimizing that DFA leads to **4 states**.
- **The "Trap":** Complementing a DFA only works if the DFA is **complete**. If you forget the trap state, the complement will be wrong.
- **Complexity:** Calculating the number of states in a DFA for "divisible by $N$" in binary.
  - Number of states = **$N$**. 
  - If the string is read MSB first, $q_i \xrightarrow{x} q_{(2i+x) \pmod N}$.
  - If LSB first, it's more complex and requires reversing the DFA.
