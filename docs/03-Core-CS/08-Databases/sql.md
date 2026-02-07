# SQL

## Short Notes
Structured Query Language (SQL) is the standard for managing relational data.

### Commands

- **DDL**: `CREATE`, `DROP`, `ALTER`, `TRUNCATE`.
- **DML**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL**: `GRANT`, `REVOKE`.

## Key Theories & Formulas

### 1. Aggregate Functions
`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.

- `COUNT(*)` counts all rows including NULLs.
- `COUNT(column)` ignores NULLs.

### 2. Group By and Having

- `WHERE` filters rows *before* grouping.
- `HAVING` filters groups *after* grouping.

### 3. Set Operators
`UNION`, `INTERSECT`, `EXCEPT`.

- SQL `UNION` removes duplicates by default. Use `UNION ALL` to keep them.

---

## Example Problems

**Problem:** Find second highest salary.
```sql
SELECT MAX(Salary) 
FROM Employee 
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
```

---

## Hardest GATE Questions

**Topic: Nested Queries with Correlation and NULLs**
**Tricky Question (GATE 2014/2015/2019):**
What is the result of `WHERE X NOT IN (SELECT Y FROM T)` if the subquery returns a NULL?

- **Analysis:** **Empty Set**. 
  - `X NOT IN (NULL, 1, 2)` $\implies$ `X <> NULL AND X <> 1 AND X <> 2`.
  - In 3-valued logic, `X <> NULL` is UNKNOWN. Since the WHERE clause needs TRUE, the whole condition fails for every row.
- **The "Trap":** "Find names of students who have NO grade 'A'."
  - `SELECT Name FROM Students WHERE SID NOT IN (SELECT SID FROM Grades WHERE Grade = 'A')`. This logic is different from `WHERE Grade <> 'A'`.
- **Hard Aspect:** Correlated subqueries. The inner query executes for every row of the outer query. Finding the time complexity or number of times the inner query runs.
- **Complexity:** SQL Joins with `GROUP BY`.
  - Identifying which set of names is returned by a query involving self-joins and `ANY / ALL` operators

---

## References

- [SQL (Wikipedia)](https://en.wikipedia.org/wiki/SQL)
