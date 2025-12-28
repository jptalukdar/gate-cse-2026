# Data Link Layer

## Short Notes
Responsible for node-to-node delivery, error control, and flow control.

### Flow Control
- **Stop-and-Wait**: Send one frame, wait for ACK.
- **Sliding Window**: Send multiple frames.
  - Go-Back-N (GBN)
  - Selective Repeat (SR)

## Key Theories & Formulas

### 1. Efficiency ($\eta$)
$\eta = \frac{T_{trans}}{T_{trans} + 2 T_{prop}}$
- Let $a = T_{prop} / T_{trans}$.
- **Stop-and-Wait**: $\eta = 1 / (1 + 2a)$.
- **Sliding Window**: $\eta = W / (1 + 2a)$ (where $W$ is window size).

### 2. CSMA/CD (Ethernet)
Used for collision detection in shared channels.
- **Minimum Frame Size ($L$)**: $L \ge 2 \times T_{prop} \times B$ (where $B$ is bandwidth).
- $T_{trans} \ge 2 \times T_{prop}$.

---

## Example Problems

**Problem:** A 1 Mbps link has $T_{prop} = 25$ ms. Frame size is 1000 bits. Find efficiency of Stop-and-Wait.
1. $T_{trans} = 1000 / 10^6 = 1$ ms.
2. $a = 25 / 1 = 25$.
3. $\eta = 1 / (1 + 2 \times 25) = 1/51 \approx 2\%$.

---

## Hardest GATE Questions

**Topic: Window Size and Sequence Numbers**
**Tricky Question (GATE 2011/2013/2016):**
What is the minimum number of sequence bits for Selective Repeat with window size $W$?
- **Analysis:** $Max\_Seq\_No \ge 2W$. 
- **Bits** = $\lceil log_2(2W) \rceil$.
- **The "Trap":** GBN vs SR window sizes.
  - GBN: $W_{sender} = N-1, W_{receiver} = 1$.
  - SR: $W_{sender} = W_{receiver} = N/2$.
- **Hard Aspect:** Efficiency with errors.
  - $\eta = (1-p) \times (\eta_{ideal})$ where $p$ is probability of frame error.
- **Complexity:** Binary Exponential Backoff in CSMA/CD.
  - After $n$ collisions, wait for $K \times 512$ bit-times where $K \in [0, 2^n - 1]$.
  - Max $n$ is 10 (range $[0, 1023]$).
