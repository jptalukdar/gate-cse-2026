# Local Optimization

## Short Notes
Local optimization occurs within a **Basic Block**. A Basic Block is a sequence of instructions with one entry and one exit.

### Basic Block Identification
1. **Leaders**: 
   - First instruction.
   - Any instruction that is a target of a jump.
   - Any instruction following a jump.
2. **Block**: From one leader to just before the next.

## Key Theories & Formulas

### 1. Directed Acyclic Graph (DAG)
Used to represent basic blocks for optimization.
- Leaves: Initial values of variables.
- Internal Nodes: Operations.
- **Benefits**: Eliminates Common Sub-expressions, Identifies Dead Code.

### 2. Common Optimizations
- **Constant Folding**: Evaluating `2 * 3` as `6` at compile time.
- **Constant Propagation**: Replacing a variable with its known constant value.
- **Strength Reduction**: Replacing expensive ops (e.g., `* 2`) with cheaper ones (e.g., `<< 1`).

---

## Example Problems

**Problem:** How many basic blocks in a loop `for(i=0; i<10; i++) { a[i] = 0; }`?
- Block 1: `i=0`
- Block 2: `if i < 10 goto B3 else B4`
- Block 3: `a[i]=0; i++`
- Block 4: Exit.
**Result:** Usually 3 or 4 blocks depending on the IR representation.

---

## Hardest GATE Questions

**Topic: Dead Code and Unreachable Code**
**Tricky Question (GATE 2011/2016):**
Is `if(0) { x = 10; }` dead code or unreachable code?
- **Analysis:** **Unreachable Code**. The control flow will never reach those instructions. **Dead Code** is code that is executed but its result is never used.
- **The "Trap":** Sub-expression matching in DAGs.
  - In $a = b + c; d = b + c$, the DAG will have only one node for $b+c$.
- **Hard Aspect:** Identifying the minimum number of instructions after optimization.
  - Question: "The following code can be minimized to how many 3AC instructions?"
  - Requires manually applying folding, propagation, and common sub-expression elimination.
