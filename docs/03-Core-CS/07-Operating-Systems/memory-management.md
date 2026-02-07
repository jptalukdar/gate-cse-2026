# Memory Management

## Short Notes
Managing the movement of processes between main memory and disk.

### Techniques

- **Paging**: Fixed-size blocks. No external fragmentation. Suffers from Internal Fragmentation.
- **Segmentation**: Variable-size logical blocks. Suffers from External Fragmentation.

## Key Theories & Formulas

### 1. Paging Address Translation

- **Logical Address**: [ Page Number ($p$) | Offset ($d$) ]
- **Physical Address**: [ Frame Number ($f$) | Offset ($d$) ]
- **Page Table Entry (PTE)**: Stores Frame Number + Control bits (Valid, Dirty, etc.).

### 2. Multi-level Paging
Reduces page table size in memory.

- Total Address bits = $p_1 + p_2 + ... + d$.

### 3. Page Replacement Algorithms

- **FIFO**: Belady's Anomaly (more frames $\to$ more faults).
- **LRU**: Stack algorithm. No anomaly.
- **Optimal (OPT)**: Smallest number of faults.

---

## Example Problems

**Problem:** 32-bit address, 4 KB page. Page table entry is 4 bytes. Find Page Table size.

1. Pages = $2^{32} / 2^{12} = 2^{20}$.
2. Size = $2^{20} \times 4 \text{ bytes} = 4 \text{ MB}$.

---

## Hardest GATE Questions

**Topic: TLB and Multi-level Page Table Overhead**
**Tricky Question (GATE 2014/2015/2021):**
Calculate Effective Memory Access Time (EMAT) with TLB and 2-level paging.

- **Formula:** $EMAT = T_{tlb} + P_{hit}(T_{mem}) + (1-P_{hit})(2 \cdot T_{mem} + T_{mem})$
- **Analysis:**
  - TLB hit: 1 memory access (data).
  - TLB miss: 2 memory accesses (PT1, PT2) + 1 memory access (data) = 3 total.
- **The "Trap":** Does the TLB lookup occur in **parallel** or **serial** with the memory access?
  - Parallel: $EMAT = P_{hit}(T_{tlb} + T_{mem}) + (1-P_{hit})(\dots)$.
- **Hard Aspect:** Inverted Page Tables.
  - Page Table size = $O(\text{Number of Physical Frames}) \times PTE$.
- **Complexity:** Segmentation with Paging.
  - Seg Table $\to$ Page Table $\to$ Frame. 
  - Number of memory accesses for a single logical address is significantly higher

---

## References

- [Memory management (Wikipedia)](https://en.wikipedia.org/wiki/Memory_management)
- [Paging (Wikipedia)](https://en.wikipedia.org/wiki/Paging)
- [Virtual memory (Wikipedia)](https://en.wikipedia.org/wiki/Virtual_memory)
