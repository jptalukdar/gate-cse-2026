# Sequential Circuits

## Short Notes
Sequential circuits are circuits where the output depends on both present inputs and past outputs (memory).

### Core Components (Flip-Flops)
- **SR**: Set-Reset. Invalid state if $S=R=1$.
- **JK**: Universal FF. Toggles if $J=K=1$.
- **D**: Data. $Q_{next} = D$.
- **T**: Toggle. $Q_{next} = T \oplus Q$.

### Characteristics Equations
- **JK**: $Q_{n+1} = J\overline{Q}_n + \overline{K}Q_n$
- **D**: $Q_{n+1} = D$
- **T**: $Q_{n+1} = T\overline{Q}_n + \overline{T}Q_n$

## Key Theories & Formulas

### 1. Excitation Tables (For Design)
Necessary input to get a specific transition:
- $0 \to 0$: $D=0, J=0, K=X, T=0$
- $0 \to 1$: $D=1, J=1, K=X, T=1$
- $1 \to 0$: $D=0, J=X, K=1, T=1$
- $1 \to 1$: $D=1, J=X, K=0, T=0$

### 2. Counters
- **Asynchronous (Ripple)**: Clock of one FF is the output of the previous. $T_{total} = n \times T_{pd}$.
- **Synchronous**: All FFs share the same clock. $T_{total} = T_{pd} + T_{comb}$.
- **Modulo-$N$**: A counter that has $N$ distinct states.

---

## Example Problems

**Problem:** Design a Toggle (T) FF using a JK Flip-Flop.
- Equation for T: $Q_{n+1} = T\overline{Q}_n + \overline{T}Q_n$
- Equation for JK: $Q_{n+1} = J\overline{Q}_n + \overline{K}Q_n$
- Compare: $J = T$ and $\overline{K} = \overline{T} \implies K = T$.
**Result:** Connect $J$ and $K$ inputs together and label as $T$.

---

## Hardest GATE Questions

**Topic: Self-Starting Counters and Invalid States**
**Tricky Question (GATE CS 2011/2015 type):**
A 3-bit synchronous counter is designed for $0 \to 1 \to 2 \to 0$. What happens if the counter starts at state $3 (011)$?
- **Analysis:**
  1. Write the circuit excitation equations for $D_2, D_1, D_0$ based on the $0,1,2$ sequence.
  2. Plug the inputs $(0, 1, 1)$ into those equations to find the next state.
  3. If the next state eventually leads back to the $0 \to 1 \to 2$ cycle, it is **self-starting**.
  4. If it enters a lock-out (e.g., $3 \to 4 \to 3$), it is **not self-starting**.
- **Why it's hard:** Requires rigorous calculation for states NOT mentioned in the primary sequence. Often, questions ask for the frequency of the MSB in such a degraded cycle.

**Frequency Division:**
In a ripple counter with $n$ flip-flops, the output frequency of the $n$-th FF is $f_{out} = \frac{f_{clk}}{2^n}$.
For Mod-$N$ counters, $f_{out} = \frac{f_{clk}}{N}$.
