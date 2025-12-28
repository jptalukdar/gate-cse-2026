# I/O Interface

## Short Notes
How the CPU communicates with external peripherals.

### Data Transfer Modes
- **Programmed I/O**: CPU polls the device in a loop. CPU is 100% busy.
- **Interrupt-driven I/O**: Device signals CPU via interrupt. CPU only interacts when needed.
- **DMA (Direct Memory Access)**: Device transfers data directly to/from memory without continuous CPU involvement.

## Key Theories & Formulas

### 1. Cycle Stealing in DMA
DMA "steals" a bus cycle from the CPU during the transfer.
- **DMA Time per character**: $T_{dma} = \text{Preparation Time} + \text{Transfer Time}$.
- **CPU stall time**: percentage of cycles stolen.

### 2. Interrupt latency
The time from the occurrence of an interrupt to the start of the execution of the Interrupt Service Routine (ISR).

---

## Example Problems

**Problem:** A disk transfers data at 1 Mbps. CPU clock is 1 GHz. DMA transfer is in 1-byte bursts. How many clock cycles are stolen per byte?
1. Time for 1 byte: $8 \text{ bits} / 10^6 \text{ bps} = 8 \mu\text{s}$.
2. CPU clock period: $1 / 10^9 = 1 \text{ ns}$.
3. If 1 DMA burst takes 1 memory cycle (10 ns typical):
   - Every $8 \mu\text{s}$, the CPU is stalled for $10 \text{ ns}$.
   - Stolen cycles = $10 \text{ cycles}$ per Byte.

---

## Hardest GATE Questions

**Topic: DMA Overhead and CPU Idle time**
**Tricky Question (GATE 2013/2015):**
A DMA controller transfers 64-character blocks from a device to memory. The device rate is 200 KBps. The CPU runs at 1 MHz. Each DMA transfer (of one character) steals one bus cycle. What is the percentage of time the CPU is busy?
- **Analysis:**
  - Device makes a request every $1/200K = 5 \mu\text{s}$.
  - CPU cycle time = $1 / 1M = 1 \mu\text{s}$.
  - Every $5 \mu\text{s}$, one cycle ($1 \mu\text{s}$) is stolen.
  - Stolen fraction = $1/5 = 0.20$ or $20\%$.
  - CPU Busy time = $100\% - 20\% = 80\%$.
- **The "Trap":** Sometimes the question mentions "Burst Mode" vs "Cycle Stealing Mode". In Burst Mode, the CPU is stalled for the duration of the *entire* block transfer.
- **Hard Aspect:** When multiple devices are connected, and you must calculate the aggregate stolen cycles or determine if the bus saturates.
