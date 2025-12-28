# File Systems

## Short Notes
Storage and retrieval of data on disk.

### Allocation Methods
- **Contiguous**: Fast, but external fragmentation.
- **Linked**: No fragmentation, but slow (sequential access).
- **Indexed**: Fast random access. Uses **Inodes** (Unix).

## Key Theories & Formulas

### 1. Inode Structure (Unix)
- Direct Pointers: Points to data blocks.
- Single Indirect: Points to a block of pointers.
- Double Indirect: Points to a block of single indirect pointers.
- Triple Indirect: ...

### 2. Disk Scheduling Algorithms
- **FCFS**: Fair but inefficient.
- **SSTF**: Shortest Seek Time First. Starvation possible.
- **SCAN (Elevator)**: Continuous back and forth.
- **C-SCAN**: One-way circular scan. More uniform wait time.
- **LOOK/C-LOOK**: Scan only as far as the last request.

---

## Example Problems

**Problem:** Disk with 200 tracks (0-199). Current head at 50. Requests: 10, 180, 20. Find seek distance for SCAN (towards 0).
1. 50 $\to$ 20.
2. 20 $\to$ 10.
3. 10 $\to$ 0. (Always goes to 0 in SCAN).
4. 0 $\to$ 180.
**Total:** $(50-0) + (180-0) = 50 + 180 = 230$ tracks.

---

## Hardest GATE Questions

**Topic: Max File size in Inode system**
**Tricky Question (GATE 2012/2015/2018):**
A disk has 1 KB blocks and 4-byte pointers. An Inode has 10 direct, 1 single indirect, and 1 double indirect pointer. What is the max file size?
- **Analysis:**
  - Pointers per block = $1024 / 4 = 256$.
  - Direct: $10 \times 1 \text{ KB} = 10 \text{ KB}$.
  - Single Indirect: $256 \times 1 \text{ KB} = 256 \text{ KB}$.
  - Double Indirect: $256 \times 256 \times 1 \text{ KB} = 65536 \text{ KB} = 64 \text{ MB}$.
- **Result:** $\approx 64.2$ MB.
- **The "Trap":** Forgetting to add the direct and single indirect parts to the double indirect part.
- **Hard Aspect:** Disk rotational latency and transfer time calculation.
  - $Time = \text{Seek Time} + \text{Rotational Latency} + \text{Transfer Time}$.
  - Avg Rotational Latency = $0.5 \times \text{Time for one rotation}$.
- **Complexity:** File systems with bitmapped free-space management and the overhead of storing the bitmap

---

## References
- [File system (Wikipedia)](https://en.wikipedia.org/wiki/File_system)
- [Inode (Wikipedia)](https://en.wikipedia.org/wiki/Inode)
