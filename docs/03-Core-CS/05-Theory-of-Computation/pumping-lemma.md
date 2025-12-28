# Pumping Lemma

## Short Notes
The Pumping Lemma is a property common to all languages in a specific class (Regular or CFL). It is primarily used to prove that a language is **NOT** in that class.

## Key Theories & Formulas

### 1. Pumping Lemma for Regular Languages (PL-R)
For any regular $L$, there exists $p$ such that any $w \in L$ with $|w| \ge p$ can be split into $w = xyz$:
1. $y \neq \epsilon$
2. $|xy| \le p$
3. $xy^iz \in L$ for all $i \ge 0$.

### 2. Pumping Lemma for Context-Free Languages (PL-CFL)
For any CFL $L$, there exists $p$ such that any $w \in L$ with $|w| \ge p$ can be split into $w = uvwxy$:
1. $vx \neq \epsilon$
2. $|vwx| \le p$
3. $uv^iwx^iy \in L$ for all $i \ge 0$.

---

## Example Problems

**Problem:** Prove $L = \{a^n b^n \mid n \ge 0\}$ is not regular.
1. Assume $L$ is regular. Let pumping length be $p$.
2. Choose $w = a^p b^p$. Note $|w| = 2p \ge p$.
3. Split $w=xyz$. Since $|xy| \le p$, $y$ must contain only $a$s.
4. Pump $y$: $xy^2z$ will have more $a$s than $b$s ($p+k$ vs $p$).
5. $xy^2z \notin L$, contradiction.

---

## Hardest GATE Questions

**Topic: Correct application of quantifier logic in PL**
**Tricky Question (GATE 2012/2014):**
Which of the following conditions is necessary for a language to be proven non-regular using PL?
- **Analysis:** You must show that **no matter how** one splits the string into $xyz$ (as long as it fits the 3 conditions), there is **some** $i$ such that $xy^iz \notin L$.
- **The "Trap":** "I found ONE split that fails, so it's not regular." **Wrong.** You must show it fails for **ALL** valid splits. 
- **Complexity:** Pumping $i=0$ (Pumping down).
  - Sometimes $xy^2z$ still stays in the language, but $xy^0z$ (which is $xz$) falls out. This is a common tactic for languages like $L = \{ a^n b^m \mid n > m \}$.
- **Hard Aspect:** Using PL for CFL to disprove $a^n b^n c^n$. 
  - $vwx$ can span at most two different symbols (like $a$s and $b$s). 
  - Pumping $v$ and $x$ will increase $a$s and $b$s but the number of $c$s will remain $p$.
  - This breaks the $n=m=k$ equality.
