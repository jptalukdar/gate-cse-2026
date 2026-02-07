# Regular Languages

## Short Notes
Regular Languages are recognized by Finite Automata. They are the lowest level in the Chomsky Hierarchy.

### Closure Properties
| Operation | Regular |
| :--- | :--- |
| Union | YES |
| Intersect | YES |
| Complementation | YES |
| Concatenation | YES |
| Kleene Star | YES |
| Reverse | YES |
| Homomorphism | YES |
| Inverse Homomorphism | YES |
| Subset | **NO** |

## Key Theories & Formulas

### 1. Decision Properties
We can check (using algorithms) if a regular language is:

- **Empty**: Is there a path from start to any final state?
- **Finite**: Does the DFA have a cycle on any path to a final state?
- **Equal**: Do two DFAs recognize the same language?

### 2. Pumping Lemma for Regular Languages
Used to prove a language is **NOT** regular.
If $L$ is regular, there exists $p$ such that any string $w \in L$ with $|w| \ge p$ can be split $w=xyz$ such that:

1. $|xy| \le p$
2. $|y| > 0$
3. $xy^iz \in L$ for all $i \ge 0$.

---

## Example Problems

**Problem:** Is $L = \{0^n1^n \mid n \ge 0\}$ regular?

- **Analysis:** No. Finite automata cannot "count" $n$. Pumping Lemma: choose $w = 0^p1^p$. $y$ must consist only of $0$s. Pumping $y$ will result in $0^{p+k}1^p \notin L$.

---

## Hardest GATE Questions

**Topic: Identification of Regularity in Complex Sets**
**Tricky Question (GATE 2011/2015/2021):**
Is $L = \{a^n b^m \mid n+m \text{ is even}\}$ regular?

- **Analysis:** Yes. $n+m$ being even means both are even or both are odd. This is equivalent to $(aa)^* (bb)^* + a(aa)^* b(bb)^*$. 
- **The "Trap":** Comparing a language that "looks like" counting.
  - $L_1 = \{a^n b^n \mid n \le 10^{100}\}$ is **REGULAR** because $n$ is bounded.
  - $L_2 = \{a^n b^m \mid n=m\}$ is **NOT REGULAR**.
- **Complexity:** Regularity of languages involving prime numbers.
  - $L = \{a^p \mid p \text{ is prime}\}$ is **NOT REGULAR**.
  - No regular expression can generate prime sequence gaps

---

## References

- [Regular language (Wikipedia)](https://en.wikipedia.org/wiki/Regular_language)
- [Regular expression (Wikipedia)](https://en.wikipedia.org/wiki/Regular_expression)
