# Binomial Asset Pricing Model

The **binomial asset pricing model** is the simplest complete-market model for a risky asset.  
It explains, in a finite and algebraic setting, the key ideas that later reappear in Black–Scholes:

- **no-arbitrage** restrictions on prices,
- **replication** and **uniqueness** of prices,
- emergence of a **risk-neutral probability**,
- **martingale pricing** for discounted assets,
- and the **binomial-to-Black–Scholes limit**.

This section is deliberately discrete-time and finite-state. The goal is to understand the logic of pricing *before* moving to continuous time.

---

## 1. Market Setup

We work on a time grid \(t=0,1\) (later extended to many steps).

- Risk-free asset (bank account):  

  $$
  B_0 = 1, \qquad B_1 = 1+r, \quad r>-1.
  $$



- Risky asset (stock):  

  $$
  S_0>0, \qquad
  S_1 =
  \begin{cases}
  uS_0 & \text{(up)} \\
  dS_0 & \text{(down)}
  \end{cases}
  \quad \text{with } u>d>0.
  $$



A (self-financing) portfolio is described by holdings \((\Delta,\beta)\), meaning:

- \(\Delta\): number of shares of stock
- \(\beta\): units of the bank account

Its value is:

$$
V_0 = \Delta S_0 + \beta B_0,\qquad
V_1 = \Delta S_1 + \beta B_1.
$$



---

## 2. Claims and Pricing Question

A **contingent claim** (derivative payoff) is any random variable measurable w.r.t. the terminal state:

$$
H = H(S_1).
$$



The central question is:

> What is the fair price \(V_0\) of \(H\) at time 0?

We will answer this in multiple, equivalent ways:

1. **No-arbitrage bounds** (and existence of risk-neutral probability),
2. **Replication** (and uniqueness of price),
3. **Risk-neutral expectation** (martingale pricing).


