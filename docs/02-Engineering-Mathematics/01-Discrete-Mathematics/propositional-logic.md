# Propositional Logic

## Short Notes
Propositional logic deals with propositions (statements that are either true or false) and their connectivity using logical operators.
- **Tautology**: A formula that is always TRUE.
- **Contradiction**: A formula that is always FALSE.
- **Contingency**: A formula that is neither a tautology nor a contradiction.
- **Satisfiability**: A formula is satisfiable if there exists at least one truth assignment that makes it TRUE.

## Key Theories & Formulas

### 1. Logical Equivalences
- **Implication**: $p \to q \equiv \neg p \lor q$
- **Contrapositive**: $p \to q \equiv \neg q \to \neg p$
- **Bi-conditional**: $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$
- **De Morgan’s Laws**:
    - $\neg (p \land q) \equiv \neg p \lor \neg q$
    - $\neg (p \lor q) \equiv \neg p \land \neg q$

### 2. Valid Inference Rules
- **Modus Ponens**: $(p \to q) \land p \implies q$
- **Modus Tollens**: $(p \to q) \land \neg q \implies \neg p$
- **Hypothetical Syllogism**: $(p \to q) \land (q \to r) \implies (p \to r)$

### 3. First-Order Logic (Predicates)
- $\forall x (P(x) \land Q(x)) \equiv \forall x P(x) \land \forall x Q(x)$
- $\exists x (P(x) \lor Q(x)) \equiv \exists x P(x) \lor \exists x Q(x)$
- **Negation of Quantifiers**:
    - $\neg \forall x P(x) \equiv \exists x \neg P(x)$
    - $\neg \exists x P(x) \equiv \forall x \neg P(x)$

---

## Example Problems

**Problem**: Check if $((p \to q) \land (q \to r)) \to (p \to r)$ is a tautology.
1. Let $A = (p \to q) \land (q \to r)$.
2. We want to check $A \to (p \to r)$.
3. This is the **Hypothetical Syllogism** rule, which is a known tautology.
4. Alternatively, assume it's FALSE. Then $A$ is True and $(p \to r)$ is False.
   - $p \to r$ is False $\implies p=T, r=F$.
   - $A$ is LHS: $(T \to q) \land (q \to F)$.
   - For $A$ to be True, both parts must be True.
   - $T \to q$ is True $\implies q=T$.
   - $q \to F$ (i.e., $T \to F$) is False.
   - Contradiction! Since assuming it's False leads to a contradiction, the statement is a **Tautology**.

---

## Hardest GATE Questions

**Topic: Nested Quantifiers**

**Question (GATE 2014 Variant)**:
Which of the following is logically valid?
1. $\forall x (P(x) \to Q(x)) \implies (\forall x P(x) \to \forall x Q(x))$
2. $(\forall x P(x) \to \forall x Q(x)) \implies \forall x (P(x) \to Q(x))$

**Analysis**:
- **Statement 1**: TRUE.
  - If $P(x) \to Q(x)$ is true for all $x$, and if $P(x)$ is true for all $x$, then naturally $Q(x)$ must be true for all $x$ (by Modus Ponens for each instance).
- **Statement 2**: FALSE.
  - LHS: "If everyone is P, then everyone is Q".
  - RHS: "For everyone, if they are P, then they are Q".
  - Counter-example: Domain = {a, b}. P(a)=T, P(b)=F. Q(a)=T, Q(b)=F.
  - LHS: $\forall x P(x)$ is False, so LHS implication is True.
  - RHS: Check $x=b$. $P(b) \to Q(b)$ involves $F \to F$ (True). Wait, let's pick a better counter-example.
  - **Counter-example**: Integers. P(x): x is even. Q(x): x is odd.
  - LHS: Is "If all integers are even imply all integers are odd" True? Yes, because antecedent "all integers are even" is False. Implication is True.
  - RHS: $\forall x (Even(x) \to Odd(x))$. This is False (e.g., x=2, $T \to F$ is F).
  - So, True $\implies$ False is False.

**Result**: Only Statement 1 is valid.

**Why it's hard**: Nested quantifiers and the direction of implication ($A \implies B$ vs $B \implies A$) often confuse test-takers. You must construct concrete counter-examples.

---

## References
- [Propositional calculus (Wikipedia)](https://en.wikipedia.org/wiki/Propositional_calculus)
