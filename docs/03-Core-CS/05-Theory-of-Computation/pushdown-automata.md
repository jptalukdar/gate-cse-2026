# Pushdown Automata

## Short Notes
A Pushdown Automaton (PDA) is a finite automaton with an additional **Stack** for infinite memory (LIFO). 

### Acceptance Criteria
1. **Final State Acceptance**: The machine reaches a final state.
2. **Empty Stack Acceptance**: The stack becomes empty.
*Note:* Both methods are equivalent for Non-deterministic PDAs (NPDA).

## Key Theories & Formulas

### 1. NPDA vs DPDA
- **NPDA**: Recognizes all Context-Free Languages (CFL).
- **DPDA**: Recognizes only Deterministic Context-Free Languages (DCFL).
- **Power**: NPDA > DPDA. (Unlike FA where DFA = NFA).

### 2. Transition Function
$\delta(q, a, X) = \{(p, Y)\}$
- $q$: Current state.
- $a$: Input symbol (or $\epsilon$).
- $X$: Symbol at top of stack.
- $p$: Next state.
- $Y$: String to replace $X$ with on the stack.

---

## Example Problems

**Problem:** How to implement $a^n b^{2n}$ using a PDA?
1. For every 'a' read, push **two** 'X's onto the stack.
2. For every 'b' read, pop **one** 'X' from the stack.
3. If stack is empty when input ends, accept.

---

## Hardest GATE Questions

**Topic: Determinism and Conflict in Stack Operations**
**Tricky Question (GATE 2011/2016):**
Is a PDA that allows either an $\epsilon$-transition OR an input transition from the same state (with same stack top) deterministic?
- **Analysis:** **NO**. This is a "Shift-Reduce" style conflict. For a PDA to be deterministic, if $\delta(q, \epsilon, X)$ is defined, then $\delta(q, a, X)$ must be undefined for all $a \in \Sigma$.
- **The "Trap":** Thinking all CFLs have a DPDA.
  - $L = \{ww^R\}$ does NOT have a DPDA.
  - $L = \{a^n b^n \cup a^n b^{2n}\}$ does NOT have a DPDA (requires guessing which $n$ to check).
- **Hard Aspect:** Number of states in a PDA vs an equivalent CFG.
- **Complexity:** PDAs with multiple stacks.
  - 1 Stack PDA = CFL.
  - 2 Stack PDA = **Turing Machine** (Full Power).
  - This is because two stacks can simulate a TM tape.
