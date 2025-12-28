# Memory Hierarchy

## Short Notes
Memory hierarchy is an enhancement to the cache concept, extending it to the entire storage system of a computer.

### Levels
1.  **Registers**: CPU internal.
2.  **Cache (L1, L2, L3)**: High speed SRAM.
3.  **Main Memory**: DRAM.
4.  **Secondary Storage**: HDD, SSD (Magnetic/Flash).

### Parameters
- **Access Time**: Decreases as we go up.
- **Cost per Bit**: Increases as we go up.
- **Capacity**: Increases as we go down.

## Key Theories & Formulas

### 1. Hierarchical vs Simultaneous Access
- **Simultaneous Access**: All levels are accessed at once (e.g., L1 and L2).
  $T_{avg} = H \times T_1 + (1-H) \times T_2$
- **Hierarchical Access**: Level $i+1$ is only accessed if there is a miss in level $i$.
  $T_{avg} = H \times T_1 + (1-H) \times (T_1 + T_2)$

---

## Example Problems

**Problem:** A memory system has L1 cache and RAM. $T_{L1} = 2$ ns, $T_{RAM} = 100$ ns. Hit ratio is 0.9. Find effective access time for hierarchical access.
- $T_{avg} = 0.9(2) + 0.1(2 + 100) = 1.8 + 10.2 = 12$ ns.

---

## Hardest GATE Questions

**Topic: Multilevel Cache with Inclusive vs Exclusive properties**
**Tricky Question (GATE 2011):**
In a 2-level cache system, L1 has a local hit rate of 0.8 and L2 has a local hit rate of 0.9. What is the global hit rate?
- **Analysis:**
  - Global Hit Rate = Probability of hitting in L1 OR (Missing in L1 AND hitting in L2).
  - $P(H_{global}) = P(H_1) + P(M_1)P(H_2)$
  - $P(H_{global}) = 0.8 + (1 - 0.8)(0.9) = 0.8 + (0.2)(0.9) = 0.8 + 0.18 = 0.98$.
- **The "Trap":** Confusing "Local Hit Rate" (hit rate within that cache level for requests reaching it) with "Global Hit Rate" (hit rate relative to the total CPU requests).
- **Hard Aspect:** When inclusive properties are used. In an **Inclusive Cache**, L2 must contain everything in L1. This affects eviction policies and coherence

---

## References
- [Memory hierarchy (Wikipedia)](https://en.wikipedia.org/wiki/Memory_hierarchy)
