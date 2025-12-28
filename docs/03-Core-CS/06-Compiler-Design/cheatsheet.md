# ⚡ Cheatsheet: Compiler Design

## Parsing Power
$$LL(1) \subset SLR(1) \subset LALR(1) \subset CLR(1)$$
- **LL(1)**: Top-Down, NO Left Recursion, NO Left Factoring. Uses First & Follow.
- **LR(0)**: Bottom-Up. Uses Closure & Goto. Items: $A \to \alpha \cdot \beta$.
- **SLR(1)**: Extends LR(0). Reduce on Follow(A). Problem: Shift-Reduce conflicts if Follow sets overlap.
- **CLR(1)**: Canonical LR. Items include lookahead: $[A \to \alpha \cdot \beta, a]$. Most powerful. Large tables.
- **LALR(1)**: Merges states of CLR(1) with same core. Same table size as SLR. Can generate Reduce-Reduce conflicts during merge.

## Syntax Directed Translation (SDT)
- **Synthesized Attribute**: Computed from children. `S.val = A.val + B.val`.
- **Inherited Attribute**: Computed from parent or siblings. `A.in = S.in`.
- **S-Attributed**: Only synthesized attributes. Bottom-up evaluation.
- **L-Attributed**: Synthesized + Inherited (only from left siblings/parent). Depth-first evaluation.

## Code Optimization
- **Basic Block**: Sequence of instructions with single entry and single exit.
- **Flow Graph**: Nodes = Basic Blocks. Edges = Control flow.
- **DAG**: Used for local optimization (Common Subexpression Elimination, Dead Code Elimination).

## Runtime Environment
- **Activation Record**: Return val, Actual params, Control link (dynamic), Access link (static), Saved machine status, Local data, Temporaries.

## ⚠️ Common Traps
- **Left Recursion**: $A \to A\alpha | \beta$ becomes $A \to \beta A'$, $A' \to \alpha A' | \epsilon$. (Eliminate for LL(1)).
- **Ambiguity**: Ambiguous grammars are NEVER LR(k). But can be parsed using operator precedence or by resolving conflicts (e.g., else-if).
- **Conflict Types**:
  - **SR (Shift-Reduce)**: Should I shift input or reduce stack?
  - **RR (Reduce-Reduce)**: Multiple productions match for reduction.
