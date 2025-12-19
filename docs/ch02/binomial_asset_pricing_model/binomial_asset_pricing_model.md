# Binomial Asset Pricing Model

## Introduction

The **binomial model**, developed by **Cox, Ross, and Rubinstein (1979)**, provides a discrete-time framework for modeling stock price evolution and pricing derivative securities. In this model, a stock price can take only two possible values at each time step — it can either **rise** or **fall** by predetermined factors. Despite its apparent simplicity, the binomial model serves as the foundation for understanding continuous-time models, particularly the **Black–Scholes framework**.

The model's discrete nature offers several advantages:

- **Computational tractability**: The step-by-step representation makes it well-suited for numerical implementation
- **Flexibility**: It naturally handles American-style options (early exercise), dividends, and time-varying parameters
- **Path-dependent options**: The model accommodates complex payoffs that depend on the price path (barrier options, lookback options)
- **Pedagogical clarity**: It illustrates key pricing principles — no-arbitrage, replication, risk-neutral valuation — in a finite, algebraic setting before moving to stochastic calculus

More fundamentally, the binomial model reveals the essential logic of arbitrage-free pricing:

- **No-arbitrage** restrictions on prices,
- **Replication** and **uniqueness** of prices,
- Emergence of a **risk-neutral probability**,
- **Martingale pricing** for discounted assets,
- The **binomial-to-Black–Scholes limit**.

We proceed deliberately through the discrete-time, finite-state framework to understand this pricing logic *before* confronting continuous time.

---

## 1. Market Setup

We work on a time grid $t=0,1$ (later extended to many steps).

- **Risk-free asset** (bank account):  
  $$
  B_0 = 1, \qquad B_1 = 1+r, \quad r>-1.
  $$

- **Risky asset** (stock):  
  $$
  S_0>0, \qquad
  S_1 =
  \begin{cases}
  uS_0 & \text{(up)} \\
  dS_0 & \text{(down)}
  \end{cases}
  \quad \text{with } u>d>0.
  $$

A **(self-financing) portfolio** is described by holdings $(\Delta,\beta)$, meaning:

- $\Delta$: number of shares of stock
- $\beta$: units of the bank account

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

> What is the fair price $V_0$ of $H$ at time 0?

We will answer this in multiple, equivalent ways:

1. **No-arbitrage bounds** (and existence of risk-neutral probability),
2. **Replication** (and uniqueness of price),
3. **Risk-neutral expectation** (martingale pricing).