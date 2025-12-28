# Addressing Modes

## Short Notes
Addressing modes specify how the operand of an instruction is located.

### Common Modes
- **Implied/Implicit**: Operand is hidden in instruction (e.g., `CLS`, `CMA`).
- **Immediate**: Operand is part of instruction (e.g., `MOV R1, #5`).
- **Register**: Operand is in a register (e.g., `MOV R1, R2`).
- **Register Indirect**: Register contains the memory address of the operand.
- **Direct/Absolute**: Instruction contains the memory address of the operand.
- **Indirect**: Instruction contains address of the address of the operand.
- **Relative**: Effective Address ($EA$) = $PC$ + displacement.
- **Indexed**: $EA$ = Index Register + displacement.
- **Base Register**: $EA$ = Base Register + displacement.
- **Auto-Increment/Decrement**: Address in register is used, then the register is incremented/decremented.

## Key Theories & Formulas

### 1. Effective Address (EA)
The actual memory address where the data is stored.
- Direct: $EA = Address\_in\_Instruction$.
- Indirect: $EA = Memory[Address\_in\_Instruction]$.

### 2. Instruction Cycles
- **Immediate**: Fastest (no memory access for operand).
- **Indirect**: Slowest (two memory accesses: one for pointer, one for data).

---

## Example Problems

**Problem:** Match the addressing mode with the typical usage:
- Pointer/Variable: **Direct/Indirect**
- Array Access: **Indexed**
- Constant values: **Immediate**
- Relocatable code: **Relative**
- Parameter passing in stack: **Base-Register**

---

## Hardest GATE Questions

**Topic: Memory Access Count in Complex Pointers**
**Tricky Question (GATE 2015):**
An instruction `LOAD R1, @(R2)` uses indirect addressing through a pointer stored in R2. How many memory accesses are needed to execute this instruction (including fetch)?
- **Analysis:**
  1. **Instruction Fetch**: $1$ memory access (assuming 1 word instruction).
  2. **Operand Address Fetch**: R2 holds the address $A$. Memory at address $A$ holds the operand address $B$. So, $1$ memory access to read $B$.
  3. **Data Fetch**: Register content $B$ is the effective address. $1$ memory access to read the actual data.
- **Total**: $3$ memory accesses.
- **The "Trap":** Sometimes the question specifies that the instruction is already in the Instruction Register (IR). In that case, exclude the fetch cycle.
- **Hard Aspect:** Differentiating between "Register Indirect" (R2 contains address of data) and "Memory Indirect" (Instruction contains address $A$, which contains address $B$, which contains data)

---

## References
- [Addressing mode (Wikipedia)](https://en.wikipedia.org/wiki/Addressing_mode)
