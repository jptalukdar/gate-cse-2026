# Hashing

## Short Notes
Hashing maps data of arbitrary size to fixed-size values using a hash function $h(x)$.

### Collision Resolution
- **Chaining**: Use linked lists at each hash index.
- **Open Addressing**: Find another empty slot (Linear Probing, Quadratic Probing, Double Hashing).

## Key Theories & Formulas

### 1. Load Factor ($\alpha$)
$\alpha = \frac{\text{Number of elements}}{\text{Table size}}$.
- Chaining: $T_{search} = 1 + \alpha$.
- Open Addressing: $T_{search} = \frac{1}{1-\alpha}$ (assuming uniform hashing).

### 2. Probing Formulas
- Linear: $h(x, i) = (h(x) + i) \pmod m$
- Quadratic: $h(x, i) = (h(x) + c_1 i + c_2 i^2) \pmod m$
- Double: $h(x, i) = (h_1(x) + i \cdot h_2(x)) \pmod m$

---

## Example Problems

**Problem:** Insert 11 into a table of size 10 using Linear Probing with $h(x) = x \pmod{10}$.
1. $h(11) = 1$.
2. If index 1 is full, check index 2.
**Result:** First available slot among $(1, 2, 3...)$.

---

## Hardest GATE Questions

**Topic: Clustering and Search Performance**
**Tricky Question (GATE 2011/2015/2019):**
Which collision resolution technique suffers from Primary Clustering?
- **Analysis:** **Linear Probing**. Long runs of occupied slots build up, increasing search time.
- **The "Trap":** "Search Time in Chaining".
  - Question: "Worst case time for a search in a hash table with $n$ elements using chaining?"
  - Answer: **$O(n)$**. This happens if all $n$ elements hash to the same slot (chain length $= n$).
- **Hard Aspect:** Calculating the expected number of probes for a successful/unsuccessful search with specific $\alpha$. 
  - For $\alpha = 0.5$ in Linear Probing: $E[S] = \frac{1}{2}(1 + \frac{1}{1-0.5}) = 1.5$.
- **Complexity:** Double Hashing requirements. $h_2(x)$ must be relatively prime to $m$ to ensure all slots are checked.
