# Cache Memory

## Short Notes
Cache memory is a small, high-speed memory placed between the CPU and Main Memory to reduce the average access time.

### Localities of Reference

- **Temporal Locality**: Accessing the same memory location repeatedly in a short time.
- **Spatial Locality**: Accessing memory locations close to each other (e.g., arrays).

### Mapping Techniques

- **Direct Mapping**: Each block of main memory maps to exactly one cache line. (Line = Block % No. of Lines).
- **Fully Associative Mapping**: Any block can map to any line.
- **Set Associative Mapping**: Each block maps to any line within a specific set. (Set = Block % No. of Sets).

## Key Theories & Formulas

### 1. Address Breakdown

- **Direct**: [ Tag | Line | Word Offset ]
- **Fully Associative**: [ Tag | Word Offset ]
- **$k$-way Set Associative**: [ Tag | Set | Word Offset ]
- *Note:* Word Offset bits = $log_2(\text{Block Size})$.

### 2. Average Memory Access Time ($T_{avg}$)
$T_{avg} = H \times T_{cache} + (1-H) \times T_{main}$
where $H$ is Hit Ratio.

### 3. Cache Replacement Policies

- **LRU (Least Recently Used)**: Replace the block not used for the longest time.
- **FIFO (First-In-First-Out)**: Replace the oldest block.
- **Optimal**: Replace the block that won't be used for the longest time in the future.

---

## Example Problems

**Problem:** A system has 64 KB cache with 16 B blocks. Main memory is 1 MB. Find the Tag, Set, and Offset bits for a 4-way set-associative cache.

1.  **Block Size**: 16 B = $2^4 \implies$ Offset = **4 bits**.
2.  **Number of Blocks in Cache**: $64 KB / 16 B = 2^{16} / 2^4 = 2^{12}$ blocks.
3.  **Number of Sets**: $2^{12} / 4 = 2^{12} / 2^2 = 2^{10}$ sets $\implies$ Set = **10 bits**.
4.  **Main Memory Size**: 1 MB = $2^{20} \implies$ Total Address = **20 bits**.
5.  **Tag Bits**: $20 - (10 + 4) =$ **6 bits**.

---

## Hardest GATE Questions

**Topic: Write-Through vs Write-Back and No-Write-Allocate**
**Tricky Question (GATE 2011/2014):**
Compare the number of memory accesses for a Write-Through vs Write-Back cache for a sequence of write operations.

- **Analysis:**
  - **Write-Through**: Every write updates cache **and** main memory. If there are $W$ writes, there are $W$ memory accesses.
  - **Write-Back**: Updates only cache. Memory is updated only when a **dirty** block is evicted.
- **The "Trap":** Questions often involve a "Write Miss".
  - **Write-Allocate**: Bring the block from memory to cache on a write miss.
  - **No-Write-Allocate**: Update memory directly without bringing the block to cache.
- **Complexity:** Calculating average access time when the dirty block eviction probability is given.
  $T_{avg} = H \times T_c + (1-H) \times [T_m + P_{dirty} \times T_m]$
  (If the missed block is replaced by a dirty block, we pay for two memory accesses)

---

## References

- [CPU cache (Wikipedia)](https://en.wikipedia.org/wiki/CPU_cache)
- [Cache replacement policies (Wikipedia)](https://en.wikipedia.org/wiki/Cache_replacement_policies)
