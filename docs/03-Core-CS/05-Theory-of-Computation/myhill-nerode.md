## Myhill–Nerode Theorem: Short Notes

The **Myhill–Nerode theorem** provides a characterization of regular languages. It states that a language $L$ is regular if and only if the number of equivalence classes of the relation $\equiv_L$ (where $x \equiv_L y$ if for all $z$, $xz \in L \iff yz \in L$) is finite. This theorem is useful for proving whether a language is regular and for minimizing deterministic finite automata (DFA).

### Example

Consider the language $L = \{ w \in \{0,1\}^* \mid w \text{ ends with } 01 \}$.

#### DFA Transition Table

| State | Input 0 | Input 1 |
| :--- | :--- | :--- |
| $q_0$ | $q_1$ | $q_2$ |
| $q_1$ | $q_3$ | $q_4$ |
| $q_2$ | $q_4$ | $q_3$ |
| $q_3$ | $q_5$ | $q_5$ |
| $q_4$ | $q_5$ | $q_5$ |
| $q_5$ | $q_5$ | $q_5$ |

Each state represents an equivalence class under $\equiv_L$. Since there are finitely many states, $L$ is regular.

---

## References

- [Myhill–Nerode theorem (Wikipedia)](https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem)
