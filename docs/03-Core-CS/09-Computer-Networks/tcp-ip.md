# TCP/IP Suite

## Short Notes
The protocol suite used for the modern internet.

### Key Components

- **TCP**: Connection-oriented, Reliable, Flow & Congestion control.
- **UDP**: Connectionless, Fast, No overhead, Best-effort delivery.
- **IP**: Addressing and Routing.

## Key Theories & Formulas

### 1. TCP Header

- **Source/Dest Port (16 bits each)**.
- **Sequence Number (32 bits)**: Byte number of the first byte in the segment.
- **ACK Number (32 bits)**: Next expected byte number.
- **Window Size (16 bits)**: Flow control (Receiver's buffer space).

### 2. TCP Congestion Control

- **Slow Start**: Window size doubles every RTT until `ssthresh`.
- **Congestion Avoidance**: Window increases linearly (+1 every RTT).
- **Fast Retransmit/Recovery**: Triggered by 3 duplicate ACKs.

---

## Example Problems

**Problem:** If `ssthresh` is 16 and a timeout occurs at window size 24, what is the new `ssthresh` and window size?

1. New `ssthresh` = $24 / 2 = 12$.
2. New window size = 1 (Slow start begins).
**Result:** ssthresh=12, cwnd=1.

---

## Hardest GATE Questions

**Topic: Connection Establishment and State Transition**
**Tricky Question (GATE 2011/2015/2019):**
During 3-way handshake, if client sends SEQ=100 and server responds with ACK=101, SEQ=500, what is the next SEQ and ACK from client?

- **Analysis:**
  - Client sends ACK=501 (Server's SEQ + 1) and SEQ=101 (since the first packet used 1 sequence number for the SYN flag).
- **The "Trap":** "Byte stream orientation". 
  - If a packet has 100 bytes and starts with SEQ=1000, its last byte is 1099. The ACK for this packet will be 1100.
- **Hard Aspect:** Bandwidth-Delay Product (BDP) effect on window size.
  - To saturate a link: $W \ge \text{Link Capacity} \times RTT$.
- **Complexity:** Silly Window Syndrome and its prevention (Nagle's algorithm and Clark's solution)

---

## References

- [Transmission Control Protocol (Wikipedia)](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [TCP congestion control (Wikipedia)](https://en.wikipedia.org/wiki/TCP_congestion_control)
