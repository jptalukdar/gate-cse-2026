# ⚡ Cheatsheet: Theory of Computation

## Closure Properties Table
| Operation | Regular | DCFL | CFL | CSL | Recursive | RE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Union** | Yes | No | Yes | Yes | Yes | Yes |
| **Intersection** | Yes | No | No | Yes | Yes | Yes |
| **Complement** | Yes | Yes | No | Yes | Yes | No |
| **Concatenation**| Yes | No | Yes | Yes | Yes | Yes |
| **Kleene Star** | Yes | No | Yes | Yes | Yes | Yes |
| **Homomorphism** | Yes | No | Yes | Yes | No | Yes |
| **Reverse** | Yes | Yes | Yes | Yes | Yes | Yes |

## Decidability Table
(D = Decidable, U = Undecidable)
| Problem | Regular | DCFL | CFL | CSL | Recursive | RE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Membership $w \in L$** | D | D | D | D | D | U |
| **Emptiness $L = \phi$** | D | D | D | U | U | U |
| **Finiteness** | D | D | D | U | U | U |
| **Equality $L_1 = L_2$** | D | D | U | U | U | U |
| **Subset $L_1 \subseteq L_2$**| D | U | U | U | U | U |
| **Disjointness** | D | U | U | U | U | U |

## Key Concepts

- **Chomsky Hierarchy**: Regular $\subset$ DCFL $\subset$ CFL $\subset$ CSL $\subset$ Recursive $\subset$ RE.
- **Pumping Lemma (Regular)**: If $L$ is regular, $\exists p$ s.t. $\forall w \in L, |w| \ge p$, $w$ can be split into $xyz$:
  1. $|xy| \le p$
  2. $|y| \ge 1$
  3. $xy^iz \in L$ for all $i \ge 0$.
- **Countability**:
  - set of Regular languages is **Countable**.
  - set of Turing Machines is **Countable**.
  - set of all languages over $\Sigma$ is **Uncountable**.

## ⚠️ Common Traps

- **Subset Construction**: NFA with $n$ states converts to DFA with at most $2^n$ states.
- **Ambiguity**: Checking if a CFG is ambiguous is **Undecidable**. Checking if a CFL is inherently ambiguous is **Undecidable**.
- **CFL Complement**: Complement of CFL is NOT necessarily CFL (it's CSL/Recursive). BUT, Complement of DCFL is DCFL.
