# Integrity Constraints

## Short Notes
Rules enforced on data to maintain quality and correctness.

### Types
- **Entity Integrity**: Primary key cannot be NULL.
- **Referential Integrity**: Foreign key must match a primary key in referenced table or be NULL.
- **Domain Integrity**: Values must fall within a defined set/range.

## Key Theories & Formulas

### 1. Key Constraints
- **Super Key**: Set of attributes that uniquely identifies a tuple.
- **Candidate Key**: Minimal super key.
- **Primary Key**: Selected candidate key.

---

## Example Problems

**Problem:** Can a foreign key be part of a primary key in the same table?
- **Result:** **YES**. This is common in weak entities or self-referencing tables.

---

## Hardest GATE Questions

**Topic: On Delete/Update Actions**
**Tricky Question (GATE 2011/2014):**
If table $S$ references $R$ with `ON DELETE CASCADE`, what happens when a row in $R$ is deleted?
- **Analysis:** All rows in $S$ that point to the deleted row in $R$ are also deleted.
- **The "Trap":** `SET NULL` vs `RESTRICT`. 
  - `RESTRICT` prevents deletion of $R$ if $S$ references it.
- **Hard Aspect:** Constraints in the presence of NULLs.
  - Primary key cannot have NULL, but a **Unique** constraint can have multiple NULLs in most SQL implementations (though standard varies).
- **Complexity:** Assertions and Triggers.
  - Identifying the firing order of triggers (Before/After, Row/Statement level)

---

## References
- [Data integrity (Wikipedia)](https://en.wikipedia.org/wiki/Data_integrity)
- [Referential integrity (Wikipedia)](https://en.wikipedia.org/wiki/Referential_integrity)
