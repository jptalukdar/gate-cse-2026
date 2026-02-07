# Process Management

## Short Notes
A process is a program in execution.

### Process States

1. **New**: Created.
2. **Ready**: Waiting in main memory for CPU.
3. **Running**: Executing on CPU.
4. **Waiting**: Blocked (waiting for I/O).
5. **Terminated**: Finished.
- **Suspended Ready/Wait**: Moved to secondary memory (swap).

### Process Control Block (PCB)
Stores PID, State, PC, Registers, Memory limits, Open files list.

## Key Theories & Formulas

### 1. Operations

- **fork()**: Creates a child process. Returns 0 to child, PID of child to parent.
- **exec()**: Replaces current process image with a new program.

---

## Example Problems

**Problem:** How many processes are created?
```c
fork();
fork();
fork();
```

- Formula: $2^n$ processes (including parent). 
- **Result:** $2^3 = 8$.

---

## Hardest GATE Questions

**Topic: fork() loops and variable values**
**Tricky Question (GATE 2011/2014/2021):**
```c
int x = 10;
if(fork() == 0) {
    x = x + 5;
    printf("%d", x);
} else {
    wait(NULL);
    x = x - 5;
    printf("%d", x);
}
```

- **Analysis:**
  - `fork()` creates a **copy** of the address space.
  - Child sets local copy of `x` to 15. Prints 15.
  - Parent waits, then sets its local `x` to 5. Prints 5.
- **The "Trap":** Thinking `x` is shared. It is NOT shared between parent and child (copy-on-write).
- **Complexity:** Calculating the total number of "hello" prints in a loop of `fork()`.
- **Hard Aspect:** Orphan vs Zombie processes.
  - Orphan: Parent dies, init inherits.
  - Zombie: Child dies, parent hasn't read exit status

---

## References

- [Process management (computing) (Wikipedia)](https://en.wikipedia.org/wiki/Process_management_(computing))
