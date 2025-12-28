# Programming in C

## Short Notes
C is a procedural programming language. For GATE, focus is on pointers, scope, storage classes, and operator precedence.

### Key Concepts
- **Storage Classes**: `auto`, `extern`, `static`, `register`.
  - `static`: Variables retain value between function calls.
- **Pointers**: Variables that store memory addresses. `*p` is value at address; `&x` is address of variable.
- **Arrays & Pointers**: `a[i]` is equivalent to `*(a + i)`.
- **Operator Precedence**: Postfix (`++`, `--`) > Unary (`*`, `&`) > Multiplicative > Additive.

## Key Theories & Formulas

### 1. Pointer Arithmetic
If `p` is a pointer to type `T`, then `p + 1` increments the address by `sizeof(T)` bytes.

### 2. Parameter Passing
- **Call by Value**: Local copy is modified; actual arguments remain unchanged.
- **Call by Reference**: Address is passed; actual arguments are modified.
- *Note:* C only supports call-by-value, but passing a pointer simulates call-by-reference.

---

## Example Problems

**Problem:** What is the output?
```c
int a = 10;
void f(int *p) {
    static int a = 5;
    a += *p;
    *p = a;
}
int main() {
    f(&a);
    f(&a);
    printf("%d", a);
}
```
1.  **First call**: `static a` (local to `f`) becomes $5 + 10 = 15$. Global `a` becomes 15.
2.  **Second call**: `static a` is 15. It becomes $15 + 15 = 30$. Global `a` becomes 30.
**Result:** 30.

---

## Hardest GATE Questions

**Topic: Multi-dimensional Arrays and Pointer Decay**
**Tricky Question (GATE 2011/2016):**
Given `int a[3][4][5]`, what is the value of `a[1] - a[0]`?
- **Analysis:**
  - `a` is an array of 3 elements, where each element is a $4 \times 5$ array.
  - `a[0]` and `a[1]` are pointers to $4 \times 5$ arrays.
  - In pointer subtraction, the result is the number of elements of the "pointed-to" type between the pointers.
  - Since `a[0]` and `a[1]` are consecutive elements of type `int[4][5]`, the difference is **1**.
- **The "Trap":** Many students calculate the byte difference ($4 \times 5 \times 4 \text{ bytes} = 80$ bytes). But pointer subtraction scales by the size of the element.
- **Complexity:** `*(*(*(a+i)+j)+k)` vs `*(*(a+i)+j)`. Understanding where the "pointer" turns into a "value" is crucial

---

## References
- [C (programming language) (Wikipedia)](https://en.wikipedia.org/wiki/C_(programming_language))
