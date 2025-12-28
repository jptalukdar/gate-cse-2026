# Inter-Process Communication (IPC)

## Short Notes
Mechanisms that allow processes to communicate and synchronize.

### Synchronization Tools
- **Semaphores**: Integer variables used for signaling.
- **Mutex**: Binary semaphore (lock).
- **Monitors**: High-level synchronization construct.

## Key Theories & Formulas

### 1. Semaphores
- **P(S) (wait)**: `while(S <= 0); S--;`
- **V(S) (signal)**: `S++;`
- **Binary Semaphore**: Range $[0, 1]$.
- **Counting Semaphore**: Range $[-\infty, \infty]$ or $[0, N]$. (Negative value represents number of blocked processes).

### 2. Classical Problems
- **Producer-Consumer**: Uses `empty`, `full`, and `mutex`.
- **Readers-Writers**: Multiple readers allowed, only one writer.
- **Dining Philosophers**: Deadlock prevention using asymmetry or resource hierarchy.

---

## Example Problems

**Problem:** A semaphore $S$ is initialized to 5. 10 $P$ operations and 4 $V$ operations are performed. What is the value of $S$?
- $5 - 10 + 4 = -1$.
**Result:** -1 (Indicates 1 process is blocked).

---

## Hardest GATE Questions

**Topic: Semaphore logic to prevent race conditions in complex code**
**Tricky Question (GATE 2013/2016/2019):**
Two processes P1 and P2 share a variable `x` initialized to 0. Both execute `x = x + 1`. What are the possible values of `x`?
- **Analysis:**
  - If synchronized: 2.
  - If interleaved (Race): 1.
    1. P1 reads `x` (0).
    2. P2 reads `x` (0).
    3. P1 increments and writes (1).
    4. P2 increments and writes (1).
- **The "Trap":** Questions where $n$ processes perform $k$ increments.
  - Max value: $n \times k$.
  - Min value: 2 (if properly interleaved).
- **Hard Aspect:** Binary semaphore implementation of a Counting semaphore.
- **Complexity:** Peterson's Algorithm and TSL (Test-and-Set Lock) properties.
  - Peterson's: Satisfies Mutual Exclusion, Progress, and Bounded Waiting for 2 processes.
