# Introduction

Long before options were traded electronically on modern exchanges, their basic idea was already understood in practice. One of the earliest recorded examples is attributed to Thales of Miletus (circa 600 BCE), who reportedly paid deposits to secure the **right — but not the obligation —** to use olive presses after the harvest. When demand surged, he exercised his rights and profited. This arrangement closely resembles a call option.

Centuries later, option-like contracts appeared in European markets. During the 17th-century Dutch Tulip Mania, traders bought agreements granting the right to purchase tulip bulbs at a fixed price — effectively early call options. These contracts were informal and often poorly enforced, but they captured the essential idea of optionality.

Modern listed options emerged much later. The Chicago Board Options Exchange (CBOE), founded in 1973, introduced standardized equity options and centralized clearing. In the same year, Black, Scholes, and Merton developed the mathematical framework that made systematic option pricing possible — transforming options from ad hoc agreements into a rigorously understood financial instrument.

Suppose you own a stock worth \$100 and want to guarantee that you can sell it for at least \$95 over the next three months, no matter what happens in the market. How much should you pay for that protection? The surprising answer: it does not depend on what you think the stock will do. This is, at its core, an option pricing problem.

Options are among the most important financial instruments in modern markets. They provide a mechanism for transferring risk, speculating on price movements, and — most critically for this text — they pose a deep mathematical question: **what is the correct price?**

Unlike stocks or bonds, whose values are determined directly by cash flows, an option's value depends on the *future behavior* of an underlying asset. This makes option pricing inherently probabilistic and leads naturally to the theory of stochastic processes, partial differential equations, and measure-theoretic probability.

In the [previous section](../futures_and_forwards/introduction.md), forwards and futures were defined by **obligation** — both parties must perform, payoffs are linear, and no premium changes hands. Options introduce **choice**: the holder decides whether to exercise, creating a nonlinear payoff. This single difference — from obligation to optionality — is what makes option pricing fundamentally harder and mathematically richer.

---

## Why Options Exist

Options serve three fundamental economic purposes:

1. **Hedging**: A farmer can buy a put option to guarantee a minimum sale price for a crop, eliminating downside risk while retaining upside potential
2. **Speculation**: A trader who believes a stock will rise can buy a call option, gaining leveraged exposure with limited downside (the premium paid)
3. **Price discovery**: Option prices encode the market's collective view of future volatility and the probability distribution of asset returns

---

## Why Pricing Is Hard

A stock's current price is observable. An option's fair price is not — it must be *computed*. The difficulty arises from three sources:

- The payoff depends on the **future** stock price, which is random
- The option holder has a **choice** (exercise or not), introducing nonlinearity
- The price must be **arbitrage-free**, consistent with the prices of all other traded instruments

Resolving these difficulties requires a mathematical framework that connects probability, differential equations, and no-arbitrage economics. The **Black–Scholes model**, developed in the subsequent sections of this chapter, provides exactly this framework.

---

## What This Section Covers

This section introduces the language and concepts of options markets:

- **What is an option**: formal definitions of calls and puts, contract terms
- **Payoffs**: the mathematical functions that determine an option's value at maturity
- **Premium**: the price paid for an option and its decomposition into intrinsic and time value
- **Market structure**: how options are traded, standardized, and margined
- **Basic strategies**: elementary combinations of options and stock
- **Why pricing matters**: the no-arbitrage principle that motivates the entire theory

These concepts provide the foundation for the Black–Scholes formula and its extensions.
