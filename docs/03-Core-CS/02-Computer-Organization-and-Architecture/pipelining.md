# Pipelining

## Short Notes
Pipelining is a technique where multiple instructions are overlapped in execution. The goal is to increase the throughput (instructions per second), not to decrease the execution time of a single instruction.

### Pipeline Stages (Standard 5-Stage RISC)
1.  **IF**: Instruction Fetch
2.  **ID**: Instruction Decode / Register Fetch
3.  **EX**: Execute / Address Calculation
4.  **MA**: Memory Access
5.  **WB**: Write Back

### Performance Metrics
- **Cycle Time ($t_p$)**: $max(\text{stage delays}) + \text{latch delay}$.
- **Speedup ($S$)**: $\frac{\text{Time without pipeline}}{\text{Time with pipeline}} = \frac{n \times k \times t}{n+(k-1)t_p}$, which approaches $k$ for large $n$ (where $k$ is number of stages).

## Key Theories & Formulas

### 1. Throughput
Throughput = $\frac{\text{Number of Instructions}}{\text{Total Time}}$.
For an ideal pipeline, Throughput = $\frac{1}{\text{Clock Cycle Time}}$.

### 2. Pipeline Hazards
- **Structural Hazard**: Hardware resource conflict (e.g., single memory for data and instructions).
- **Data Hazard**: Dependence on a result not yet written back (RAW, WAR, WAW).
  - *Solution*: Data Forwarding/Bypassing, Stalling.
- **Control Hazard**: Branch instructions.
  - *Solution*: Branch Prediction, Delayed Branching.

### 3. Efficiency ($\eta$)
$\eta = \frac{S}{k}$, where $S$ is speedup and $k$ is number of stages.

---

## Example Problems

**Problem:** A 4-stage pipeline has stage delays of 150, 120, 160, and 140 ns. Latch delay is 10 ns. Calculate the cycle time and speedup for 100 instructions.
1.  **Cycle Time ($t_p$)**: $max(150, 120, 160, 140) + 10 = 160 + 10 = 170$ ns.
2.  **Non-pipelined time ($T_{np}$)**: $(150+120+160+140) \times 100 = 570 \times 100 = 57,000$ ns.
3.  **Pipelined time ($T_p$)**: $[k + (n-1)] \times t_p = [4 + 99] \times 170 = 103 \times 170 = 17,510$ ns.
4.  **Speedup ($S$)**: $57,000 / 17,510 \approx 3.25$.

---

## Hardest GATE Questions

**Topic: Pipeline Performance with Stalls and Branch Penalties**
**Tricky Question (GATE 2014/2017):**
In a 5-stage pipeline, 20% of instructions are conditional branches. 60% of these branches are taken. A taken branch incurs a 2-cycle penalty. What is the average CPI?
- **Analysis:**
  - Base CPI = 1.
  - Penalty occurs only on **Taken** branches.
  - Probability(Branch) = 0.20.
  - Probability(Taken | Branch) = 0.60.
  - Probability(Taken Branch) = $0.20 \times 0.60 = 0.12$.
  - Average CPI = $Base CPI + (\text{Prob of Taken Branch} \times \text{Penalty})$
  - $Avg CPI = 1 + (0.12 \times 2) = 1.24$.
- **Result:** 1.24 CPI.
- **The "Trap":** Sometimes the branch penalty is given for *all* branches (if they aren't predicted), or specifically for *mispredictions*. You must read carefully whether the penalty applies to "Taken", "Not Taken", or "All" branch instructions.
