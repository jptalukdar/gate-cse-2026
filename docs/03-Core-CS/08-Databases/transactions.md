# Transactions and Concurrency Control

## Short Notes
A transaction is a unit of program execution that accesses and updates data.

### ACID Properties
- **Atomicity**: All or nothing.
- **Consistency**: Correct state transition.
- **Isolation**: Concurrent transactions don't interfere.
- **Durability**: Success persists after failures.

## Key Theories & Formulas

### 1. Serializability
- **Conflict Serializability**: Can the schedule be transformed into a serial schedule by swapping non-conflicting actions?
  - Conflict: 2 actions on same data by different transactions, at least one is a Write.
- **View Serializability**: More relaxed than conflict. Every Conflict Serial schedule is View Serial.

### 2. Concurrency Protocols
- **2PL (Two-Phase Locking)**: Growing and Shrinking phases. Ensures Conflict Serializability.
- **Strict 2PL**: Holds all locks until commit. Ensures **Recoverable** and **Cascaless** schedules.
- **Timestamp Ordering**: Uses read/write timestamps ($TS$).

---

## Example Problems

**Problem:** $T_1: R(x), W(x)$; $T_2: R(x), W(x)$. Is this conflict serializable if interleaved?
- If $T_1 R(x) \to T_2 R(x) \to T_1 W(x)$, there's a cycle in the precedence graph.
**Result:** Not conflict serializable.

---

## Hardest GATE Questions

**Topic: Recoverability and Cascading Rollbacks**
**Tricky Question (GATE 2012/2015/2019):**
Which property is guaranteed by Strict 2PL?
- **Analysis:** **Conflict Serializability** and **Strictness** (which implies Recoverability and Absence of Cascading Rollbacks).
- **The "Trap":** Deadlocks in 2PL.
  - 2PL ensures serializability but **does NOT prevent deadlocks**.
- **Hard Aspect:** View Serializability calculation.
  - If a schedule is NOT conflict serializable, it might still be view serial if it has "blind writes" (writing without reading).
- **Complexity:** Thomas Write Rule.
  - Allows $W(x)$ even if $TS(T) < WTS(X)$ by ignoring the write (since a later value is already written)

---

## References
- [Database transaction (Wikipedia)](https://en.wikipedia.org/wiki/Database_transaction)
- [Concurrency control (Wikipedia)](https://en.wikipedia.org/wiki/Concurrency_control)
