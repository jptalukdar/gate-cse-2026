# Turing Machines & Undecidability

## Short Notes
Turing Machines (TM) are the most powerful computational models. Undecidability deals with problems that cannot be solved by any algorithm (TM).

### Chomsky Hierarchy & Power
Regular $\subset$ CFL $\subset$ CSL $\subset$ Recursive (Rec) $\subset$ Recursively Enumerable (RE).

| Language Class | Recognizer |
| :--- | :--- |
| Regular | Finite Automata |
| CFL | Pushdown Automata |
| CSL | Linear Bounded Automata |
| Recursive | TM which always halts |
| RE | TM which halts for YES, may loop for NO |

## Key Theories & Formulas

### 1. Halting Problem
The problem of determining whether a TM $M$ will halt on input $w$ is **undecidable** and **RE**.

### 2. Rice's Theorem
Every non-trivial property of the **languages** recognized by TMs is undecidable.
- "Is $L(M)$ empty?" - Undecidable.
- "Is $M$ starting with 5 states?" - **Decidable** (it's a property of the machine, not its language).

---

## Example Problems

**Problem:** Is it decidable if a Regular Language is finite?
- **Result:** **YES**. All properties of Regular languages are decidable.

---

## Hardest GATE Questions

**Topic: Decidability Table (The "Master Chart")**
**Tricky Question (GATE 2013/2016/2020):**
Is $\{ \langle M \rangle \mid M \text{ is a TM and } |L(M)| \ge 2 \}$ recursively enumerable?
- **Analysis:** **YES**. We can non-deterministically guess two different strings and run $M$ on them. If both halt/accept, we accept. 
- **The "Trap":** Checking if it is **Recursive**. It's not. If $M$ recognizes a language with only 1 string, we might loop forever.
- **Hard Aspect:** Identifying "Trivial" vs "Non-trivial" in Rice's Theorem.
  - Trivial: Property is true for all RE languages or none.
- **Complexity:** Post Correspondence Problem (PCP).
  - PCP is undecidable for alphabet size $\ge 2$.
  - Modified PCP is also undecidable

---

## References
- [Turing machine (Wikipedia)](https://en.wikipedia.org/wiki/Turing_machine)
- [Undecidable problem (Wikipedia)](https://en.wikipedia.org/wiki/Undecidable_problem)
- [Rice's theorem (Wikipedia)](https://en.wikipedia.org/wiki/Rice%27s_theorem)
