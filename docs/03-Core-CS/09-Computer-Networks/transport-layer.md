# Transport Layer

## Short Notes
The Transport Layer provides end-to-end communication between processes on different hosts.

### Major Protocols

- **TCP**: Reliable, byte-stream, connection-oriented.
- **UDP**: Unreliable, datagram, connectionless.

## Key Theories & Formulas

### 1. Port Numbers

- Standard range: 0-1023 (Well-known ports).
- Total range: 0-65535 (16 bits).

### 2. Error and Flow Control

- Uses checksums for error detection.
- Uses sliding window for flow control.

---

## Example Problems

**Problem:** Which protocol is used for real-time video streaming?

- **Result:** UDP (due to low latency requirements).

---

## Hardest GATE Questions

**Topic: Multiplexing and Socket Addressing**
**Tricky Question (GATE 2011/2015/2018):**
A host has one IP but multiple applications (HTTP, FTP, SMTP) running. How are incoming packets delivered to the correct application?

- **Analysis:** **Port Multiplexing**. Each application listens on a unique port number. The 5-tuple (Src IP, Src Port, Dest IP, Dest Port, Protocol) uniquely identifies a connection.
- **The "Trap":** UDP Checksum is **optional** in IPv4 but **mandatory** in IPv6.
- **Hard Aspect:** TCP Timers.
  - Retransmission Timeout (RTO) calculation using smoothed RTT (SRTT).
  - $SRTT = (1-\alpha)SRTT_{old} + \alpha RTT_{new}$.
- **Complexity:** Comparison of cumulative ACK (TCP) vs individual ACK.
  - TCP ACKs indicate the "next expected byte", not the "last received byte"

---

## References

- [Transport layer (Wikipedia)](https://en.wikipedia.org/wiki/Transport_layer)
- [User Datagram Protocol (Wikipedia)](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
