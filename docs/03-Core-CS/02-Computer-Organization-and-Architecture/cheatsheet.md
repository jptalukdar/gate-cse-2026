# ⚡ Cheatsheet: Computer Organization

| Topic | Formula / Concept | Note |
| :--- | :--- | :--- |
| **Performance** | $Execution Time = \frac{IC \times CPI}{Clock Rate}$ | Iron Law of Performance |
| | $Speedup = \frac{T_{old}}{T_{new}}$ | Amdahl's Law also applies |
| **Pipelining** | $Speedup = \frac{N \cdot k}{k + (N-1)}$ | $k$=stages, $N$=instructions |
| | Ideal CPI = 1 | Stalls increase CPI > 1 |
| | Hazards: Structural (Hardware), Data (Dependency), Control (Branch) |
| **Cache** | $AMAT = H_{time} + (MissRate \times MissPenalty)$ | Hierarchy performance |
| | $Index = \log_2(\frac{CacheSize}{BlockSize \times Assoc})$ | Set Index bits |
| | $Offset = \log_2(BlockSize)$ | Byte offset bits |
| | $Tag = AddrBits - Index - Offset$ |
| **Addressing** | **PC-Relative**: $Target = PC + Offset$ | Used in Branch/Jumps |
| | **Base-Register**: $Target = Base + Offset$ | Used in Array/Struct access |
| **I/O** | **Memory Mapped**: Registers have memory addresses | Same instructions for Mem/IO |
| | **Isolated I/O**: Separate address space | Special `IN`/`OUT` instructions |
| **DMA** | CPU initializes, DMA transfers block, Interrupts on completion | Cycle Stealing vs Burst Mode |

## ⚠️ Common Traps
- **Byte vs Word Addressing**: Always check if the memory is byte-addressable. If word-addressable (e.g., 32-bit words), addresses increment by 1 for next word, not 4.
- **Write Back vs Write Through**: Write Back needs a "Dirty Bit". Write Through doesn't.
- **Pipeline Stalls**: A conditional branch often causes more penalty than a data dependency. Branch Prediction reduces this.
- **Capacity**: "Cache Size" usually refers to *Data* capacity, not including Tag/Valid/Dirty overhead bits. Read specific questions carefully.
