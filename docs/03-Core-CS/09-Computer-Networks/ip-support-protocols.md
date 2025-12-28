# IP Support Protocols

## Short Notes
Helper protocols that enable the functionality of the Network layer.

### Protocols
- **ARP (Address Resolution Protocol)**: Resolve IPv4 $\to$ MAC. (Broadcast request, Unicast reply).
- **DHCP (Dynamic Host Configuration Protocol)**: Assigns IP addresses dynamically. (DORA process).
- **ICMP (Internet Control Message Protocol)**: Error reporting and queries (Ping, Traceroute).
- **NAT (Network Address Translation)**: Maps private IPs to public IPs.

## Key Theories & Formulas

### 1. Traceroute Logic
Uses ICMP Time Exceeded messages. Sets TTL=1, then 2, then 3... to identify routers on the path.

### 2. ARP Cache
Stores resolved MAC addresses for a limited time to reduce broadcast overhead.

---

## Example Problems

**Problem:** How does a node find the MAC address of its default gateway?
- **Result:** Uses ARP with the gateway's IP address.

---

## Hardest GATE Questions

**Topic: ARP Across Multiple Subnets**
**Tricky Question (GATE 2012/2015/2018):**
If Host A in Subnet 1 wants to send a packet to Host B in Subnet 2, whose MAC address does Host A request in the ARP broadcast?
- **Analysis:** **MAC of the Router (Default Gateway)**. Host A realizes B is in a different network and sends the frame to the router.
- **The "Trap":** "Gratuitous ARP". 
  - Used for duplicate IP detection or updating caches when a MAC changes.
- **Hard Aspect:** ICMP error message structure.
  - ICMP error packets include the IP header + first 8 bytes of the original datagram to help the sender identify the error.
- **Complexity:** DHCP Relay Agents.
  - How a client gets an IP if the DHCP server is in a different subnet (Router forwards the broadcast as a unicast).
