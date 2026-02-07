# ⚡ Cheatsheet: Digital Logic

| Topic | Formula / Concept | Note |
| :--- | :--- | :--- |
| **Boolean Algebra** | $A + \bar{A}B = A + B$ | Absorbption |
| | $AB + \bar{A}C + BC = AB + \bar{A}C$ | Consensus Theorem |
| | $f(A,B) = A \cdot f(1,B) + \bar{A} \cdot f(0,B)$ | Shannon Expansion |
| **XOR Properties** | $A \oplus A = 0$, $A \oplus 1 = \bar{A}$ | Odd function |
| | $A \oplus B = \bar{A}B + A\bar{B}$ | Inequality detector |
| **Logic Gates** | NAND/NOR are Universal | Can implement any function |
| | $\{ \oplus, 1 \}$ is NOT functional complete | Cannot implement AND/OR |
| **Number Rep** | Range of $n$-bit 2's Comp: $[-2^{n-1}, 2^{n-1}-1]$ | Asymmetric range |
| | Float Value: $(-1)^S \times 1.M \times 2^{E-Bias}$ | Bias = 127 (Single), 1023 (Double) |
| **Mux** | Formula to build $N \times 1$ using $M \times 1$: $\lceil \frac{N-1}{M-1} \rceil$ | Useful for cascading |
| **Counters** | Mod-$N$ counter freq: $f_{out} = f_{clk} / N$ | Frequency division |
| | Ring Counter states: $N$ | Johnson Counter states: $2N$ |
| **Delays** | Ripple Adder Delay: $N \times t_{FA}$ | Very slow for large $N$ |
| | Lookahead Adder Delay: Constant ($O(1)$ theoretically) | Larger area cost |

## ⚠️ Common Traps

- **minterm vs Maxterm**: $\sum m(1, 3)$ is equivalent to $\Pi M(0, 2)$. Don't mix them up.
- **2's Complement**: To negate a number, flip all bits and add 1. Negating $0$ gives $0$. Negating $-2^{n-1}$ results in overflow.
- **Overflow**: In 2's comp addition, overflow occurs if adding two positives gives negative, or two negatives gives positive. $V = C_{in} \oplus C_{out}$ (for MSB).
