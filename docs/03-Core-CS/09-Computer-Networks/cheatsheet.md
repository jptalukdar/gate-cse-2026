# ⚡ Cheatsheet: Computer Networks

## Delays

- **Transmission ($T_t$)**: $L / B$ (Length / Bandwidth).
- **Propagation ($T_p$)**: $Distance / Speed$.
- **Round Trip Time (RTT)**: $2 \times T_p$.
- **Total Time**: $T_t + T_p + T_{queue} + T_{proc}$.

## Flow Control
| Protocol | Efficiency ($\eta$) | Window Sizes ($W_s, W_r$) |
| :--- | :--- | :--- |
| **Stop & Wait** | $\frac{1}{1+2a}$ | $1, 1$ |
| **GBN** | $\frac{N}{1+2a}$ | $N, 1$ |
| **SR** | $\frac{N}{1+2a}$ | $N, N$ |

- Here $a = T_p / T_t$. Max throughput = Efficiency $\times$ Bandwidth.

## IP Addressing (IPv4)

- **Class A**: 0... (NetID: 8 bits)
- **Class B**: 10... (NetID: 16 bits)
- **Class C**: 110... (NetID: 24 bits)
- **Subnetting**: Borrow $x$ bits from Host ID. Subnets = $2^x$. Hosts = $2^h - 2$.
- **CIDR**: /24 means 24 bits Network, 8 bits Host (254 hosts).

## TCP/UDP

- **TCP Header**: Min 20 Bytes, Max 60 Bytes.
- **UDP Header**: 8 Bytes (Source Port, Dest Port, Len, Checksum).
- **Sequence Numbers**: Byte-stream based. $Ack \# = Next Expected Byte$.
- **Congestion**:
  - Slow start: Doubles CWND every RTT.
  - Congestion Avoidance: Linear increase (+1 MSS).
  - Threshold: On timeout, $Threshold = CWND/2$, $CWND = 1$.

## ⚠️ Common Traps

- **Bandwidth-Delay Product**: $B \times RTT$. Amount of data "in flight". Vital for window sizing.
- **Manchester Encoding**: Used in Ethernet. Baud rate = $2 \times$ Bit rate.
- **Fragment Offset**: Measured in 8-byte blocks. $Offset = 100 \implies 800$ bytes skipped.
- **Checksum**: Detects errors, does NOT correct them. CRC is usually Link Layer.
