# Deadlocks

## Short Notes
A situation where a set of processes are blocked because each is holding a resource and waiting for another resource held by another process in the set.

### 4 Necessary Conditions (Coffman)
1. **Mutual Exclusion**
2. **Hold and Wait**
3. **No Preemption**
4. **Circular Wait**

## Key Theories & Formulas

### 1. Banker's Algorithm (Avoidance)
Uses `Available`, `Allocation`, `Max`, and `Need` matrices.
- $Need = Max - Allocation$.
- System is in a **Safe State** if there exists a sequence to satisfy all needs.

### 2. Resource Allocation Graph (RAG)
- Single instance of resource: Cycle $\iff$ Deadlock.
- Multiple instances: Cycle $\implies$ Potentially Deadlock.

---

## Example Problems

**Problem:** A system has 10 units of $R$. 3 processes need 4 each. Can deadlock occur?
- Max resources for no deadlock: $\sum (Need_i - 1) + 1$.
- $(4-1) \times 3 + 1 = 9 + 1 = 10$.
- Since we have 10 units, no deadlock possible.

---

## Hardest GATE Questions

**Topic: Minimum Resources for Deadlock Prevention**
**Tricky Question (GATE 2013/2016):**
Find the range of $m$ (resources) such that the system is never in deadlock for $n$ processes with $k$ peak demands.
- **Formula**: $m \ge \sum (k_i - 1) + 1$.
- **The "Trap":** Problems where resources are of different types ($R1, R2, R3$). You must calculate the condition for each or find a combination that breaks safety.
- **Hard Aspect:** Deadlock Recovery in Distributed Systems.
- **Complexity:** Banker's Algorithm with multiple requests.
  - Question: "If process P1 requests (1, 0, 2), should it be granted immediately?"
  - Requires running the safety algorithm on the *post-grant* state.
