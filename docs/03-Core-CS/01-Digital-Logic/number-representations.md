# Number Representations

## Short Notes
Number systems define how values are stored in binary. GATE focuses heavily on signed integers and floating-point representations.

### Integer Representations ($n$ bits)
- **Unsigned**: Range $[0, 2^n - 1]$.
- **Signed Magnitude**: Range $[-(2^{n-1} - 1), 2^{n-1} - 1]$. Two representations for zero (+0 and -0).
- **1's Complement**: Range $[-(2^{n-1} - 1), 2^{n-1} - 1]$. Two representations for zero.
- **2's Complement**: Range $[-2^{n-1}, 2^{n-1} - 1]$. Unique representation for zero. Most efficient for hardware (subtraction is just addition).

## Key Theories & Formulas

### 1. Overflow Detection in 2's Complement
Overflow occurs when adding two numbers of the same sign results in a different sign.
- **Hardware Logic**: $Overflow = C_{n} \oplus C_{n-1}$ (Carry into MSB XOR Carry out of MSB).

### 2. IEEE 754 Floating Point (Single Precision - 32 bits)
- **Sign Bit (1 bit)**: 0 for +, 1 for -.
- **Exponent (8 bits)**: Biased by 127. Store $E + 127$.
- **Mantissa (23 bits)**: Normalized form $1.M$. Only the fractional part $M$ is stored (Hidden bit '1').
- **Value**: $(-1)^S \times 1.M \times 2^{E-127}$.

---

## Example Problems

**Problem:** Represent -5 in 8-bit 2's complement.
1. Binary of +5: `0000 0101`
2. 1's complement: `1111 1010`
3. Add 1 for 2's complement: `1111 1011`
**Result:** `0xFB`

**Problem:** What is the range of 8-bit 2's complement?
- Min: $-2^7 = -128$
- Max: $2^7 - 1 = 127$

---

## Hardest GATE Questions

**Topic: IEEE 754 Precision and Min/Max values**
**Tricky Question (GATE 2018):**
Consider a floating-point system with 1 bit sign, 3 bit biased exponent (bias=3), and 2 bit mantissa. What is the smallest positive normalized number?
- **Analysis:**
  - Smallest normalized number has Exponent = 1 (actual exponent $E = 1 - 3 = -2$).
  - Mantissa is $1.00_b$ (hidden bit is 1, fraction is 00).
  - Value = $+1.00 \times 2^{-2} = 0.25$.
- **The "Trap":** Exponent bits `000` and `111` are reserved for Denormalized numbers and NaN/Infinity respectively. Using $E_{stored}=0$ would lead to a denormalized number, which is a different category.
- **Hard Aspect:** Differentiating between the "Smallest Normalized" and "Smallest Denormalized" value.
  - Smallest Denormalized (for same system): $0.01_b \times 2^{1-3} = 0.25 \times 2^{-2} = 0.0625$.
