# Combinational Circuits

## Short Notes
Combinational circuits are circuits where the output at any time depends only on the present inputs.

### Core Components
- **Half Adder**: Adds two bits. Sum $S = A \oplus B$, Carry $C = AB$.
- **Full Adder**: Adds three bits. $S = A \oplus B \oplus C_{in}$, $C_{out} = AB + BC_{in} + AC_{in}$.
- **Multiplexer (MUX)**: $2^n$ inputs, $n$ selection lines, 1 output. Acts as a data selector.
- **Decoder**: $n$ inputs, $2^n$ outputs. Only one output is active based on binary input.

## Key Theories & Formulas

### 1. Multiplexer as a Universal Logic Module
- A $2^n \times 1$ MUX can implement any Boolean function of $n+1$ variables.
- One variable is used as input (along with 0, 1), and $n$ variables are used as select lines.

### 2. Decoder with OR Gates
- An $n$-to-$2^n$ decoder followed by OR gates can implement any set of Boolean functions by summing the minterms.

### 3. Look-Ahead Carry (LAC) Logic
- Reduces carry propagation delay in ripple carry adders.
- **Generate**: $G_i = A_i B_i$; **Propagate**: $P_i = A_i \oplus B_i$.
- $C_{i+1} = G_i + P_i C_i$.

---

## Example Problems

**Problem:** How many $2 \times 1$ MUX are needed to implement a $16 \times 1$ MUX?
- Level 1: $16/2 = 8$ MUX
- Level 2: $8/2 = 4$ MUX
- Level 3: $4/2 = 2$ MUX
- Level 4: $2/2 = 1$ MUX
- **Total:** $8 + 4 + 2 + 1 = 15$
- **Formula:** For a $N \times 1$ MUX using $M \times 1$ MUX: $\frac{N-1}{M-1}$. Here: $(16-1)/(2-1) = 15$.

---

## Hardest GATE Questions

**Topic: MUX Cascade with Variable Transformation**
**Tricky Question (GATE CS 2014):**
Given a $4 \times 1$ MUX with select lines $S_1, S_0$ as $A, B$. Inputs are $I_0=C, I_1=\overline{C}, I_2=\overline{C}, I_3=C$. What is the realized function $f(A, B, C)$?

- **Analysis:**
  $f = \overline{A}\overline{B}(C) + \overline{A}B(\overline{C}) + A\overline{B}(\overline{C}) + AB(C)$
  $f = C(\overline{A}\overline{B} + AB) + \overline{C}(\overline{A}B + A\overline{B})$
  $f = C(A \odot B) + \overline{C}(A \oplus B)$
  Since $(A \odot B) = \overline{A \oplus B}$, let $X = A \oplus B$.
  $f = C\overline{X} + \overline{C}X = X \oplus C$
- **Result:** $f = A \oplus B \oplus C$ (3-variable XOR).
- **Why it's hard:** Requires identifying the XOR structure within the MUX expansion terms efficiently. Mistakes in Shannon expansion are common.
