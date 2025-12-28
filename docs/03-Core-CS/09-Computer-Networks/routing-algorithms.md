# Routing Algorithms

## Short Notes
How the network layer decides the path from source to destination.

### Major Types
- **Distance Vector (DV)**: Uses Bellman-Ford. Nodes exchange tables with neighbors. (e.g., RIP).
- **Link State (LS)**: Uses Dijkstra. Nodes have global knowledge of the topology. (e.g., OSPF).
- **Path Vector**: Uses BGP. For inter-domain routing.

## Key Theories & Formulas

### 1. Count-to-Infinity Problem (DV)
Occurs when a link fails and neighbors update each other recursively.
- **Solutions**: Split Horizon, Poison Reverse, Triggered Updates.

### 2. Hierarchical Routing
Divides the network into regions (Autonomous Systems) to reduce routing table size.

---

## Example Problems

**Problem:** In DV, if A has distance 5 to C, and B has distance 2 to A. What is B's distance to C through A?
- $D(B, C) = D(B, A) + D(A, C) = 2 + 5 = 7$.

---

## Hardest GATE Questions

**Topic: Convergence Time and Loop Detection**
**Tricky Question (GATE 2011/2014/2017):**
If three nodes A, B, C are in a line (A-B-C) using DV, and the link A-B fails, how many updates until the system realizes A is unreachable?
- **Analysis:** This tests the Count-to-Infinity speed. If infinity is defined as 16, it might take 16 exchanges.
- **The "Trap":** "Poison Reverse". 
  - If B tells C "my distance to A is $\infty$" because B reached A through C, C won't bounce the info back to B.
- **Hard Aspect:** BGP (Border Gateway Protocol) path attributes.
  - BGP avoids loops by including the entire AS path in the update.
- **Complexity:** OSPF Link State Advertisements (LSA) and flood control.
  - Question: "Total number of packets sent in a network of $N$ nodes to flood a new link state information?"
