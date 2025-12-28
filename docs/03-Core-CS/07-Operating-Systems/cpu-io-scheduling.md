# CPU & I/O Scheduling

## Short Notes
Selection of which process in the ready queue gets the CPU.

### Algorithms
- **FCFS**: Non-preemptive. Suffers from Convoy Effect.
- **SJF**: Shortest Job First. Optimal for average waiting time.
- **SRTF**: Shortest Remaining Time First (Preemptive SJF).
- **Round Robin (RR)**: Preemptive. Good for response time.
- **Priority**: Can result in starvation. (Solution: Aging).

## Key Theories & Formulas

### 1. Metrics
- **Arrival Time ($AT$)**
- **Burst Time ($BT$)**
- **Completion Time ($CT$)**
- **Turnaround Time ($TAT$)** = $CT - AT$
- **Waiting Time ($WT$)** = $TAT - BT$
- **Response Time ($RT$)** = (First time got CPU) - $AT$

---

## Example Problems

**Problem:** RR with time quantum 2. Processes: P1(BT=5), P2(BT=3).
- 0-2: P1 (rem 3)
- 2-4: P2 (rem 1)
- 4-6: P1 (rem 1)
- 6-7: P2 (done)
- 7-8: P1 (done)
**Result:** Gantt chart shows context switches.

---

## Hardest GATE Questions

**Topic: Context Switch Overhead and Adaptive Scheduling**
**Tricky Question (GATE 2012/2015/2019):**
In RR, if context switch time is $C$ and time quantum is $Q$, what is the percentage of CPU wasted if $BT \gg Q$?
- **Analysis:**
  - Every $Q$ work, we spend $C$ switching.
  - Overhead = $\frac{C}{Q+C} \times 100$.
- **The "Trap":** Choosing an extremely small $Q$ to minimize $WT$. This increases context switch overhead drastically, making the system inefficient.
- **Hard Aspect:** SRTF with tie-breaking rules.
  - If two processes have same remaining time, use PID or Arrival time? GATE usually specifies.
- **Complexity:** Multi-level Queue vs Multi-level Feedback Queue (MLFQ). MLFQ is more complex as processes can move between queues based on their behavior (I/O bound vs CPU bound).
