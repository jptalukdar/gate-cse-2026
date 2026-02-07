# ALU, Data-path & Control Unit

## Short Notes
This topic covers the internal structure of the Processor.

### Components

- **ALU (Arithmetic Logic Unit)**: Performs calculations and logical operations.
- **Datapath**: The pathway (buses, registers) where data flows between CPU components.
- **Control Unit (CU)**: Directs the operation of the processor. It tells the datapath what to do.

### Control Unit Types

- **Hardwired**: Uses logic gates, flip-flops. Fixed, fast, but difficult to modify.
- **Microprogrammed**: Stores control signals in a "Control Memory" (ROM) as microinstructions. Slower but flexible.

## Key Theories & Formulas

### 1. Control Memory (ROM) Size
Size = (Number of microinstructions) $\times$ (Length of microinstruction).

- **Horizontal Microprogramming**: Many control bits (unencoded). High parallelism, large memory.
- **Vertical Microprogramming**: Encoded bits (require decoders). Smaller memory, slower.

### 2. Control Signal Encoding
If a group of $N$ control signals are **mutually exclusive** (never active together), they can be encoded using $log_2(N+1)$ bits.

---

## Example Problems

**Problem:** A processor has 64 distinct control signals. If they are all active together (worst case), how many bits are needed for horizontal microprogramming?

- **Result:** 64 bits.
- If they are grouped into 8 mutually exclusive groups of 7 signals each:
  - Each group needs $log_2(7+1) = 3$ bits.
  - Total = $8 \times 3 = 24$ bits. (Vertical/Encoded)

---

## Hardest GATE Questions

**Topic: Micro-instruction Sequencing**
**Tricky Question (GATE 2005/2016):**
Calculate the size of control memory for a processor with 128 micro-instructions, each requiring 20 control signals and a 7-bit branch address. Control signals are grouped into 4 groups of size 5, 4, 6, and 5 respectively (mutually exclusive within groups).

- **Analysis:**
  - Group 1 (5): $log_2(5+1) \uparrow = 3$ bits.
  - Group 2 (4): $log_2(4+1) \uparrow = 3$ bits.
  - Group 3 (6): $log_2(6+1) \uparrow = 3$ bits.
  - Group 4 (5): $log_2(5+1) \uparrow = 3$ bits.
  - Control Signal bits = $3+3+3+3 = 12$ bits.
  - Branch bits = $7$ bits.
  - Total bits per word = $12 + 7 = 19$.
  - Control Memory Size = $128 \times 19$ bits.
- **The "Trap":** Forgetting the $+1$ in $log_2(N+1)$. The $+1$ represents the "No-op" state where none of the $N$ signals are active

---

## References

- [Arithmetic logic unit (Wikipedia)](https://en.wikipedia.org/wiki/Arithmetic_logic_unit)
- [Control unit (Wikipedia)](https://en.wikipedia.org/wiki/Control_unit)
