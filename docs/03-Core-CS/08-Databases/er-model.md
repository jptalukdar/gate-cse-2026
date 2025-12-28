# ER Model

## Short Notes
The Entity-Relationship (ER) model is a high-level conceptual data model.

### Components
- **Entity**: An object or concept (e.g., `Employee`).
- **Attribute**: A property of an entity (e.g., `Name`).
- **Relationship**: Association between entities.
- **Cardinality**: 1:1, 1:N, M:N relationships.

## Key Theories & Formulas

### 1. ER to Relational Mapping
- **1:1**: Can be merged into one table or use foreign key.
- **1:N**: Foreign key on the 'N' side.
- **M:N**: Requires a **new table** with primary keys of both participating entities as foreign keys.

### 2. Participation Constraints
- **Total Participation**: Every entity in the set must be involved in the relationship. (Double line).
- **Partial Participation**: Entities can exist without a relationship.

---

## Example Problems

**Problem:** How many tables are needed for an M:N relationship between two entities $E_1$ and $E_2$?
- **Result:** **3 tables**. One for $E_1$, one for $E_2$, and one for the relationship.

---

## Hardest GATE Questions

**Topic: Identification of Minimum Tables in Complex ER Diagrams**
**Tricky Question (GATE 2011/2015/2018):**
Given an ER diagram with multiple relationships, some being 1:N and some total participation, find the minimum number of tables.
- **Analysis:** 
  - 1:1 and 1:N with total participation on the 'N' side can usually be merged with the 'N' side entity table.
  - Multi-valued attributes always require a **new table**.
- **The "Trap":** Binary vs Ternary relationships.
  - A ternary relationship (among 3 entities) always needs its own table, regardless of cardinality.
- **Hard Aspect:** Weak Entities.
  - A Weak Entity depends on its identifying owner. The Identifying Relationship and the Weak Entity are merged into one table.
- **Complexity:** ER diagrams with attributes on the relationships themselves.
