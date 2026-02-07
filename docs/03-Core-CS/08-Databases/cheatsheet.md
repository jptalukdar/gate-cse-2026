# ⚡ Cheatsheet: Databases

## Normalization
| Form | Rule | Problem fixed |
| :--- | :--- | :--- |
| **1NF** | Atomic values | Multi-valued attributes |
| **2NF** | No Partial Dependency | Redundancy from composite keys |
| **3NF** | No Transitive Dependency | Redundancy from non-prime attributes |
| **BCNF** | For $X \to Y$, $X$ is Super Key | All anomalies from FDs |

## Transactions (ACID)

- **Atomicity**: All or nothing. (Recovery Manager/Log).
- **Consistency**: DB remains valid. (Integrity Constraints).
- **Isolation**: Transactions execute independently. (Concurrency Control).
- **Durability**: Changes are permanent. (Log/Write-ahead).

## Concurrency

- **Serial Schedule**: One txn after another.
- **Conflict Serializable**: Equivalent to a serial schedule via swaps. Check via Precedence Graph (Cycle = NOT serializable).
- **2PL (Two Phase Locking)**: Growing and Shrinking phase. Guarantees Conflict Serializability.
- **Strict 2PL**: Hold locks till commit. Avoids Cascading Rollback.

## Indexing (B+ Trees)

- Order $p$. Key size $k$, Pointer sizes $P$ (node) and $R$ (record), Block size $B$.
- **Internal Node**: $p \times P + (p-1) \times k \le B$.
- **Leaf Node**: $p \times (k + R) + P \le B$.

## ⚠️ Common Traps

- **Candidate Key**: Minimal Super Key. A table can have multiple CKs.
- **Primary Key**: One of the CKs chosen by designer. Cannot be NULL.
- **Clustered Index**: Only one per table (sorts the data).
- **Natural Join**: Joins on common attributes with same name. Removes duplicate columns.
- **SQL Counting**: `COUNT(*)` counts NULLs. `COUNT(col)` does NOT count NULLs.
