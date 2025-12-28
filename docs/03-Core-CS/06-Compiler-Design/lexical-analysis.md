# Lexical Analysis

## Short Notes
Lexical Analysis is the first phase of a compiler. It reads the source code as a stream of characters and converts it into a sequence of **Tokens**.

### Basic Terms
- **Token**: A meaningful unit (e.g., `id`, `num`, `if`, `+`).
- **Lexeme**: The actual text in the source code (e.g., `count`, `123`).
- **Pattern**: A rule (often a Regular Expression) describing a token.

## Key Theories & Formulas

### 1. Token Counting
GATE often asks to count tokens in a C-snippet.
- **Rules**: 
  - Strings `"..."` are 1 token.
  - Multi-character operators like `++`, `<<`, `->` are 1 token.
  - Keywords, Identifiers, Numbers are separate tokens.
- **Whitespace**: Ignored unless in a string.

### 2. Regular Expressions in Lexical Analysis
Lexical analyzers use Regular Expressions to define tokens and Finite Automata (DFA) to recognize them.

---

## Example Problems

**Problem:** Count tokens in `printf("Sum = %d", a + b);`
1. `printf` (id)
2. `(` (symbol)
3. `"Sum = %d"` (string)
4. `,` (symbol)
5. `a` (id)
6. `+` (symbol)
7. `b` (id)
8. `)` (symbol)
9. `;` (symbol)
**Result:** 9 tokens.

---

## Hardest GATE Questions

**Topic: Longest Prefix Match (Maximal Munch Strategy)**
**Tricky Question (GATE 2011/2016):**
If a lexer sees `count++`, why is it not `count`, `+`, `+`?
- **Analysis:** The lexer uses the **Longest Prefix Match** rule. It keeps reading as long as the current string matches a valid pattern. `count+` is not a pattern (usually), but `++` is. So it groups `++`.
- **The "Trap":** Questions with nested comments or strings.
  - `/* comments /* inside */` - Lexical analyzer might treat the first `*/` as the end unless it handles nested comments (standard C doesn't).
- **Hard Aspect:** Regular Expression for C-style identifiers.
  - Must start with `[a-zA-Z_]` and followed by `[a-zA-Z0-9_]*`.
- **Complexity:** DFA for recognizing specific number types (Hex, Octal, Floating point).
