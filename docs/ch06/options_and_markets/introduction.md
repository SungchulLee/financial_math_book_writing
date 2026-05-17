# Introduction

Long before options were traded electronically on modern exchanges, their basic idea was already understood in practice. One of the earliest recorded examples is attributed to Thales of Miletus (circa 600 BCE), who reportedly paid deposits to secure the **right — but not the obligation —** to use olive presses after the harvest. When demand surged, he exercised his rights and profited. This arrangement closely resembles a call option.

Centuries later, option-like contracts appeared in European markets. During the 17th-century Dutch Tulip Mania, traders bought agreements granting the right to purchase tulip bulbs at a fixed price — effectively early call options. These contracts were informal and often poorly enforced, but they captured the essential idea of optionality.

Modern listed options emerged much later. The Chicago Board Options Exchange (CBOE), founded in 1973, introduced standardized equity options and centralized clearing. In the same year, Black, Scholes, and Merton developed the mathematical framework that made systematic option pricing possible — transforming options from ad hoc agreements into a rigorously understood financial instrument.

In the [previous section](../futures_and_forwards/introduction.md), forwards and futures were defined by **obligation** — both parties must perform, payoffs are linear, and no premium changes hands. Options introduce **choice**: the holder decides whether to exercise, creating a nonlinear payoff. This single difference — from obligation to optionality — is what makes option pricing fundamentally harder and mathematically richer.

Options serve three economic roles: **hedging** (a farmer buys a put to floor a crop price), **speculation** (leveraged directional exposure with downside capped at the premium), and **price discovery** (market quotes encode the implied distribution of future returns). The fair price is not observable; it must be *computed* under a no-arbitrage constraint. The development of that constraint into a usable formula is the subject of the rest of this chapter (see [§ Why Pricing Matters](why_pricing_matters.md)).

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

## Exercises

**Exercise 1.** A European call option on stock XYZ has strike price K = 100 and expires in 3 months. If the stock price at expiration is S_T = 112, what is the payoff? What if S_T = 95?

??? success "Solution to Exercise 1"
    For S_T = 112: payoff = max(S_T - K, 0) = max(112 - 100, 0) = 12. For S_T = 95: payoff = max(95 - 100, 0) = 0. The call expires worthless when the stock finishes below the strike.

---

**Exercise 2.** Explain the difference between intrinsic value and time value of an option. If a call with strike 100 is trading at 8 when the stock price is 105, what is the intrinsic value and what is the time value?

??? success "Solution to Exercise 2"
    Intrinsic value is the payoff if the option were exercised immediately: max(S - K, 0) = max(105 - 100, 0) = 5. Time value is the difference between the option price and intrinsic value: 8 - 5 = 3. The time value reflects the possibility that the stock may move further in the money before expiration.

---

**Exercise 3.** A forward contract obligates both parties to transact at a fixed price $K$ at maturity, while a call option gives the holder a right but no obligation. Explain why this single difference makes the call payoff $(S_T - K)^+$ nonlinear, whereas the forward payoff $S_T - K$ is linear.

??? success "Solution to Exercise 3"
    Under a forward, the holder must pay $K$ and receive the asset regardless of $S_T$, so the payoff $S_T - K$ is an affine (linear) function of $S_T$.

    Under a call, the holder exercises only when $S_T > K$ and walks away otherwise. The payoff has a kink at $S_T = K$: it is $0$ to the left and $S_T - K$ to the right. The piecewise nature — a direct consequence of optionality — destroys linearity and is the source of the time value, the volatility dependence, and ultimately the convex Black-Scholes pricing problem.

---

**Exercise 4.** Suppose the market quotes the same European call at \$8 on Monday and at \$11 on Friday, with no change in the underlying stock price, strike, or interest rate. What single factor could most plausibly explain the increase in premium?

??? success "Solution to Exercise 4"
    With $S$, $K$, $r$, and time-to-maturity essentially unchanged, the most plausible driver is an increase in **implied volatility** $\sigma$. Higher volatility widens the distribution of possible terminal prices, which raises the option's time value because the holder benefits from upside while the downside payoff remains floored at zero. This sensitivity to volatility — vega — is one of the defining empirical features of option markets.

