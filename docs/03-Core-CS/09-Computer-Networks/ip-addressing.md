# IP Addressing (IPv4)

## Short Notes
IPv4 addresses are 32-bit unique identifiers for network interfaces.

### Classful Addressing

- **Class A**: `0...` (1-126). 8-bit Network ID.
- **Class B**: `10...` (128-191). 16-bit Network ID.
- **Class C**: `110...` (192-223). 24-bit Network ID.
- **Class D**: `1110...` (Multicast).
- **Class E**: `1111...` (Experimental).

## Key Theories & Formulas

### 1. CIDR (Classless Inter-Domain Routing)
Represented as `IP/Prefix`.

- Number of addresses in `/n` block = $2^{32-n}$.
- **Netmask**: $n$ bits of 1 followed by $(32-n)$ bits of 0.

### 2. Subnetting
Borrowing bits from Host ID to create Subnet ID.

- Number of subnets = $2^{\text{borrowed bits}}$.
- Usable hosts per subnet = $2^{\text{remaining bits}} - 2$. (Exclude Network ID and Directed Broadcast Address).

---

## Example Problems

**Problem:** How many hosts in a `192.168.1.0/24` network?

- $32 - 24 = 8$ bits for hosts.
- $2^8 - 2 = 254$ hosts.

---

## Hardest GATE Questions

**Topic: Variable Length Subnet Masking (VLSM) and Aggregation**
**Tricky Question (GATE 2014/2015/2019):**
An ISP has block `10.1.1.0/24`. It needs to divide this for 3 companies needing 100, 50, and 50 addresses respectively. Give the prefixes.

- **Analysis:**
  1. 100 needs 7 bits ($2^7=128$). Prefix: `/25`. Range: `10.1.1.0 - 10.1.1.127`.
  2. 50 needs 6 bits ($2^6=64$). Prefix: `/26`. Range: `10.1.1.128 - 10.1.1.191`.
  3. 50 needs 6 bits ($2^6=64$). Prefix: `/26`. Range: `10.1.1.192 - 10.1.1.255`.
- **The "Trap":** Route Aggregation (Supernetting).
  - Given four /26 blocks, can they be summarized into one /24? (Only if they are contiguous and start at a /24 boundary).
- **Hard Aspect:** Fragment size calculation in IPv4.
  - Offset = (Bytes from start) / 8.
  - Data must be a multiple of 8 (except last fragment).
- **Complexity:** Private IP ranges (10.x, 172.16-31.x, 192.168.x) and Loopback (127.0.0.1)

---

## References

- [IP address (Wikipedia)](https://en.wikipedia.org/wiki/IP_address)
- [IPv4 (Wikipedia)](https://en.wikipedia.org/wiki/IPv4)
- [Classless Inter-Domain Routing (Wikipedia)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
