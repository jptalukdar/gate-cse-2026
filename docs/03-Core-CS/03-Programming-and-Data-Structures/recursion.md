# Recursion

## Short Notes
Recursion is a process where a function calls itself. A recursive function must have a base case to terminate.

### Components

- **Base Case**: The condition that stops the recursion.
- **Recursive Step**: The part where the function calls itself with a modified argument.

## Key Theories & Formulas

### 1. Tail Recursion
A function is tail-recursive if the recursive call is the last action in the function. Tail recursion can be optimized by the compiler into a loop.

### 2. Stack Depth
The number of simultaneous function calls that can exist on the activation stack. For a recursion of depth $n$, memory complexity is $O(n)$ unless optimized.

---

## Example Problems

**Problem:** How many times is `f` called for `f(5)`?
```c
int f(int n) {
    if (n <= 1) return 1;
    return f(n-1) + f(n-2);
}
```

- This is a Fibonacci tree. Number of calls follows the recurrence $T(n) = T(n-1) + T(n-2) + 1$.
- For $n=5$, calls = 15.

---

## Hardest GATE Questions

**Topic: Static Variables in Recursion**
**Tricky Question (GATE 2014):**
```c
int f(int n) {
    static int r = 0;
    if (n <= 0) return 1;
    if (n > 3) {
        r = n;
        return f(n-2) + 2;
    }
    return f(n-1) + r;
}
```
What is `f(5)`?

- **Analysis:**
  1. `f(5)`: $n=5 > 3$. Sets `r = 5`. Returns `f(3) + 2`.
  2. `f(3)`: $n=3 \le 3$. Returns `f(2) + r`. (Current `r` is 5). Returns `f(2) + 5`.
  3. `f(2)`: Returns `f(1) + 5`.
  4. `f(1)`: Returns `f(0) + 5`.
  5. `f(0)`: Returns 1.
  - Backtrack: `f(1) = 1 + 5 = 6`. `f(2) = 6 + 5 = 11`. `f(3) = 11 + 5 = 16`.
  - Final: `f(5) = 16 + 2 = 18`.
- **The "Trap":** `static r` is shared across all recursive calls. Its value updates mid-recursion and persists.
- **Complexity:** Nested recursion like `f(f(n-1))`. Requires very careful manual tracing of the stack

---

## References

- [Recursion (computer science) (Wikipedia)](https://en.wikipedia.org/wiki/Recursion_(computer_science))
