# Layering Concepts (OSI & TCP/IP)

## Short Notes
Layering is a design principle to divide network functionality into manageable pieces.

### Models
- **OSI (7 Layers)**: Physical, Data Link, Network, Transport, Session, Presentation, Application.
- **TCP/IP (4/5 Layers)**: Network Access (Link), Internet (Network), Transport, Application.

## Key Theories & Formulas

### 1. Data Units (PDU)
- Application: Message
- Transport: **Segment** (TCP) / **Datagram** (UDP)
- Network: **Packet**
- Data Link: **Frame**
- Physical: **Bits**

### 2. Encapsulation
Headers are added as data moves down the stack; stripped as it moves up.

---

## Example Problems

**Problem:** At which layer is the IP address added?
- **Result:** Network Layer.

---

## Hardest GATE Questions

**Topic: Functions per Layer and Multi-layer interactions**
**Tricky Question (GATE 2011/2015/2018):**
Which layer is responsible for Dialog Control and Token Management?
- **Analysis:** **Session Layer**.
- **The "Trap":** "Routing vs Forwarding".
  - Routing (finding the path) and Forwarding (moving packet from input to output) are both **Network Layer** functions.
- **Hard Aspect:** Identifying the layer of a specific device.
  - Hub: Physical.
  - Bridge/Switch: Data Link.
  - Router: Network.
  - Gateway: All layers.
- **Complexity:** Comparison of OSI and TCP/IP philosophies. (OSI is a reference model, TCP/IP is the implementation).
