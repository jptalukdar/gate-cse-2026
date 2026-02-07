# Threads

## Short Notes
A thread is a basic unit of CPU utilization, following a process model but sharing memory space.

### Types

- **User-level Threads (ULT)**: Managed by a library. Kernel is unaware. Faster switching but one blocked thread blocks the whole process.
- **Kernel-level Threads (KLT)**: Managed by OS. Slower switching but supports parallel execution on multiple CPUs.

## Key Theories & Formulas

### 1. Thread Sharing

- **Shared**: Code, Data, Heap, OS Resources (files, signals).
- **Private**: Stack, Registers, Program Counter (PC), State.

---

## Example Problems

**Problem:** What is shared between threads of the same process?

- **Result:** Global variables (data), code section, and heap memory.

---

## Hardest GATE Questions

**Topic: ULT vs KLT blocking behavior**
**Tricky Question (GATE 2011/2015/2021):**
If a User-level thread performs a blocking I/O operation, what happens to other threads in the same process?

- **Analysis:** **All threads are blocked**. Since the kernel only sees the process, it puts the whole process in the Wait state.
- **The "Trap":** Thinking that ULTs can run on different CPUs. They cannot; they are scheduled within a single kernel thread/process.
- **Hard Aspect:** Context switch overhead differences.
  - Context switch between threads is faster than between processes because it doesn't involve changing the Page Table (CR3 register in x86).
- **Complexity:** Many-to-Many vs One-to-One threading models

---

## References

- [Thread (computing) (Wikipedia)](https://en.wikipedia.org/wiki/Thread_(computing))
