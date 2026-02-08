# ⚡ Cheatsheet: Theory of Computation

## Closure Properties Table

| Operation | Regular | DCFL | CFL | CSL | Recursive | RE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Union** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Intersection** | ✅ Yes | ❌ No | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes |
| **Complement** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| **Concatenation**| ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Kleene Star** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Homomorphism** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Reverse** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

### Operation Definitions

| Operation | Definition | Intuition |
| :--- | :--- | :--- |
| **Union** | $L_1 \cup L_2 = \{w \mid w \in L_1 \text{ or } w \in L_2\}$ | Strings in either language |
| **Intersection** | $L_1 \cap L_2 = \{w \mid w \in L_1 \text{ and } w \in L_2\}$ | Strings in both languages |
| **Complement** | $\bar{L} = \Sigma^* - L = \{w \mid w \notin L\}$ | All strings NOT in $L$ |
| **Concatenation** | $L_1 \cdot L_2 = \{xy \mid x \in L_1, y \in L_2\}$ | Append strings from $L_2$ to $L_1$ |
| **Kleene Star** | $L^* = \bigcup_{i=0}^{\infty} L^i = \{\epsilon\} \cup L \cup LL \cup LLL \cup \ldots$ | Zero or more concatenations |
| **Homomorphism** | $h(L) = \{h(w) \mid w \in L\}$ where $h: \Sigma \to \Gamma^*$ | Substitute each symbol with a string |
| **Reverse** | $L^R = \{w^R \mid w \in L\}$ | Mirror each string in $L$ |

### When Closure Fails (❌ Cases)

When a language class is **not closed** under an operation, the result may belong to a **larger class**:

| Language | Operation | Result Could Be |
| :--- | :--- | :--- |
| **DCFL** | Union | CFL (e.g., $\{a^n b^n\} \cup \{a^n b^{2n}\}$ is CFL, not DCFL) |
| **DCFL** | Intersection | CFL or CSL |
| **DCFL** | Concatenation | CFL |
| **DCFL** | Kleene Star | CFL |
| **DCFL** | Homomorphism | CFL |
| **CFL** | Intersection | CSL (e.g., $\{a^n b^n c^m\} \cap \{a^m b^n c^n\} = \{a^n b^n c^n\}$) |
| **CFL** | Complement | CSL or Recursive |
| **Recursive** | Homomorphism | RE (can encode halting problem) |
| **RE** | Complement | May be **Not RE** (e.g., $\overline{L_{HALT}}$ is not RE) |

> **Key Insight**: DCFL operations often yield CFL. CFL intersection/complement yield CSL. RE complement can fall outside RE entirely (co-RE).

### Language Abbreviations

| Abbreviation | Full Name |
| :--- | :--- |
| **Regular** | Regular Languages |
| **DCFL** | Deterministic Context-Free Languages |
| **CFL** | Context-Free Languages |
| **CSL** | Context-Sensitive Languages |
| **Recursive** | Recursive (Decidable) Languages |
| **RE** | Recursively Enumerable (Recognizable) Languages |

## Decidability Table
(D = Decidable, U = Undecidable)

| Problem | Regular | DCFL | CFL | CSL | Recursive | RE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Membership $w \in L$** | ✅ D | ✅ D | ✅ D | ✅ D | ✅ D | ❌ U |
| **Emptiness $L = \phi$** | ✅ D | ✅ D | ✅ D | ❌ U | ❌ U | ❌ U |
| **Finiteness** | ✅ D | ✅ D | ✅ D | ❌ U | ❌ U | ❌ U |
| **Equality $L_1 = L_2$** | ✅ D | ✅ D | ❌ U | ❌ U | ❌ U | ❌ U |
| **Subset $L_1 \subseteq L_2$**| ✅ D | ❌ U | ❌ U | ❌ U | ❌ U | ❌ U |
| **Disjointness** | ✅ D | ❌ U | ❌ U | ❌ U | ❌ U | ❌ U |

## Determining Language


### 1. Regular Languages (Finite Automata)
- **The Shortcut**: If you only need a finite amount of memory to track the state.
- **Look for**: Pattern matching, "ends with," "contains," or "divisible by $k$."
- **The "No-Go"**: If the language requires comparing two infinite variables (e.g., "number of $a$'s equals number of $b$'s").
- **Examples**:
    - $\{w \mid w \text{ has an even number of 1s}\}$ — parity check
    - $a^*b^*$ — any number of $a$'s followed by any number of $b$'s
    - $\{w \mid w \text{ ends with } 01\}$ — suffix matching
    - $\{w \mid w \text{ contains } 110 \text{ as a substring}\}$ — substring matching
    - $\{w \mid |w| \mod 3 = 0\}$ — length divisibility
    - $\{w \mid w \text{ represents a binary number divisible by } 5\}$ — modular arithmetic
    - $(a+b)^*aba(a+b)^*$ — contains pattern
    - $\{w \mid \#a(w) \mod 2 = \#b(w) \mod 2\}$ — finite modular comparison
    - $\Sigma^*$ (all strings) and $\emptyset$ (empty language)

### 2. Context-Free Languages (Pushdown Automata)
- **The Shortcut**: If you need to perform one stack-based comparison (LIFO).
- **Look for**: One "nested" or "matching" dependency.
- **The "No-Go"**: Comparing three things ($a^n b^n c^n$) or cross-serial dependencies ($a^n b^m a^n b^m$).
- **Examples**:
    - $\{a^n b^n \mid n \ge 0\}$ — classic balanced matching
    - $\{ww^R \mid w \in \Sigma^*\}$ — even-length palindromes
    - $\{w \mid w = w^R\}$ — all palindromes
    - $\{a^i b^j \mid i \le j \le 2i\}$ — bounded inequality
    - $\{a^m b^n \mid m \ne n\}$ — inequality (union of $m > n$ and $m < n$)
    - $\{a^i b^j c^k \mid i = j \text{ or } j = k\}$ — one comparison at a time
    - Balanced parentheses: `(()(()))` — nested matching
    - $\{a^n b^{2n} \mid n \ge 0\}$ — linear relationship
    - Arithmetic expressions with proper nesting

### 3. Context-Sensitive Languages (Linear Bound Automata)
- **The Shortcut**: Memory needed is proportional to the input length (stays within bounds).
- **Look for**: Multiple comparisons or non-context-free patterns.
- **Examples**:
    - $\{a^n b^n c^n \mid n \ge 1\}$ — triple comparison
    - $\{ww \mid w \in \Sigma^*\}$ — copy language (non-palindrome match)
    - $\{a^{n^2} \mid n \ge 1\}$ — perfect squares
    - $\{a^{2^n} \mid n \ge 0\}$ — powers of 2
    - $\{a^p \mid p \text{ is prime}\}$ — prime length strings
    - $\{a^n b^m c^n d^m \mid n, m \ge 1\}$ — cross-serial dependency
    - $\{a^i b^j c^k \mid i < j < k\}$ — strict ordering

### 4. Recursive / RE (Turing Machines)
- **The Shortcut**: If it's computable by any algorithm or involves the Halting Problem.
- **Recursive**: Decidable; an algorithm exists that always halts.
- **RE (Recursively Enumerable)**: Recognizable; an algorithm exists that accepts valid strings but might loop forever on invalid ones.
- **Recursive Examples**:
    - All CSL, CFL, and Regular languages
    - $\{<M> \mid M \text{ is a valid TM encoding}\}$ — syntax checking
    - $\{<G> \mid G \text{ is a CFG and } L(G) = \emptyset\}$ — CFG emptiness
- **RE (but not Recursive) Examples**:
    - $L_{HALT} = \{<M, w> \mid M \text{ halts on } w\}$ — Halting problem
    - $L_U = \{<M, w> \mid M \text{ accepts } w\}$ — Universal TM language
    - $\{<M> \mid L(M) \ne \emptyset\}$ — TM non-emptiness
- **Not RE Examples** (complement of RE but not Recursive):
    - $\overline{L_{HALT}}$ — TM does not halt on input
    - $\{<M> \mid L(M) = \Sigma^*\}$ — TM accepts all strings


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
