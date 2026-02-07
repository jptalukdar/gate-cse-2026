# Code Generation & Runtime Environments

## Short Notes
This topic covers the mapping of intermediate code to machine-specific code and the management of memory during execution.

### Runtime Storage

- **Activation Record (Stack Frame)**: Stores information for a single function call (Parameters, Return address, Local variables).
- **Static vs Dynamic Allocation**:
  - **Static**: Memory allocated at compile time. No recursion.
  - **Stack**: Support for recursion.
  - **Heap**: Used for dynamic data (e.g., `malloc`).

## Key Theories & Formulas

### 1. Intermediate Code (IR)

- **Three-Address Code (3AC)**: Each instruction has at most three operands. (e.g., $x = y + z$).
- **Quadruples**: (Op, Arg1, Arg2, Result).
- **Triples**: (Op, Arg1, Arg2). Result is implicit based on the instruction index.

### 2. Parameter Passing

- **Call by Name**: Substitution based (used in Algol).
- **Call by Value-Result**: Local copy is worked on, then copied back to actual argument upon return.

---

## Example Problems

**Problem:** Represent $a = b * -c + b * -c$ in 3AC.

1. $t_1 = -c$
2. $t_2 = b * t_1$
3. $t_3 = b * t_1$  *(Actually $t_3 = t_2$ if optimized)*
4. $t_4 = t_2 + t_3$
5. $a = t_4$

---

## Hardest GATE Questions

**Topic: Reference passing and non-local access (Static/Dynamic Links)**
**Tricky Question (GATE 2011/2015/2018):**
In a language with nested functions, how does an inner function access a variable declared in an outer function?

- **Analysis:** Using **Static Links**. A static link in an activation record points to the activation record of the function's static (lexical) parent.
- **The "Trap":** Dynamic Scoping vs Static Scoping.
  - **Static Scoping**: Search in lexical parent.
  - **Dynamic Scoping**: Search in calling function (stack parent).
- **Hard Aspect:** Differentiating between "Triple" and "Indirect Triple" record counts.
- **Complexity:** Code generation logic for specific hardware.
  - Question: "Minimum number of registers needed to evaluate $(a+b)*(c+d)$?"
  - Use **Sethi-Ullman** numbering: Label leaves 1/0, parent is $max(l, r)$ or $max(l, r)+1$ if equal.
  - For $(a+b)*(c+d)$, label $a, b, c, d$ as 1. $a+b$ is 2, $c+d$ is 2. The root is $2+1 = 3$. Registers needed: **2** (if we can store high results back to memory) or **3**

---

## References

- [Code generation (compiler) (Wikipedia)](https://en.wikipedia.org/wiki/Code_generation_(compiler))
- [Call stack (Wikipedia)](https://en.wikipedia.org/wiki/Call_stack)
