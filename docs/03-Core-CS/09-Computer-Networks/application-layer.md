# Application Layer

## Short Notes
The layer closest to the end user. It contains protocols for specific services.

### Protocols
- **HTTP**: For web browsing. (Port 80).
- **DNS**: Resolves Domain Name $\to$ IP. (Port 53).
- **SMTP**: Sending email. (Port 25).
- **POP3/IMAP**: Receiving email.
- **FTP**: File transfer. (Ports 20/21).

## Key Theories & Formulas

### 1. DNS Resolution
- **Recursive**: The server finds the result for you.
- **Iterative**: The server gives you the address of the next server to ask.

### 2. HTTP Types
- **Non-persistent**: One TCP connection per object.
- **Persistent**: Multiple objects over one TCP connection (can be pipelined or not).

---

## Example Problems

**Problem:** How many RTTs to fetch 1 base HTML and 10 images over non-persistent HTTP?
- 1 RTT for TCP + 1 RTT for Object = 2 RTTs per object.
- Total = $2 + (10 \times 2) = 22$ RTTs.

---

## Hardest GATE Questions

**Topic: Email Protocol Interactions**
**Tricky Question (GATE 2011/2014):**
Which protocol is used between the Sender's Mail Server and the Receiver's Mail Server?
- **Analysis:** **SMTP**. 
- **The "Trap":** Thinking POP3 is used for server-to-server transfer. POP3/IMAP are only for the **Client** to pull mail from its own server.
- **Hard Aspect:** DNS Caching and TTL.
  - If a DNS record is cached for 1 hour, updates won't be visible until it expires.
- **Complexity:** HTTP Conditional GET using `If-Modified-Since`.
  - Allows the browser to check if a cached copy is still valid without downloading the whole object again.
