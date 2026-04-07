# Introduction

Long before the first option was traded on an exchange, merchants and farmers were
already locking in future prices. Forward contracts appear in Mesopotamian clay
tablets dating to roughly 1750 BCE, and organized futures markets emerged in
seventeenth-century Japan with the Dojima Rice Exchange. Forwards and futures are,
quite literally, the oldest derivatives — and they remain among the most actively
traded instruments today, covering commodities, currencies, interest rates, and
equity indices worth trillions of dollars.

## Why Forwards Come Before Options

This section deliberately precedes our treatment of options pricing, and the reason
is pedagogical. A forward contract has a **linear payoff**: the profit or loss at
maturity is simply the difference between the spot price and the agreed-upon forward
price. There is no optionality, no early-exercise decision, and no volatility
parameter to estimate. Pricing a forward reduces to a single, clean application of
the no-arbitrage principle combined with static replication.

Concretely, if the forward price on a non-dividend-paying asset is $F$ and the
current spot price is $S_0$, the relationship enforced by arbitrage is

$$
F = S_0 \, e^{rT},
$$

where $r$ is the continuously compounded risk-free rate and $T$ is the time to
maturity. This one equation — and the reasoning behind it — is the prototype for
every pricing argument that follows, including Black-Scholes.

## What This Section Covers

We build the theory of forwards and futures in a sequence of short, self-contained
topics:

- **What is a Forward and a Future** — contract definitions, obligations of each party, and the role of the delivery date.
- **Payoff of Forwards and Futures** — linear payoff diagrams, long versus short positions, and the zero-sum nature of these contracts.
- **No-Arbitrage Pricing** — the core argument: how replication with a spot position and borrowing/lending pins down the forward price.
- **Cost of Carry and Extensions** — generalizing the pricing formula to assets that pay dividends, coupons, or incur storage costs.
- **Futures vs Forwards** — how daily settlement, standardization, and exchange clearing distinguish futures from their over-the-counter cousins.
- **Margin and Marking to Market** — initial margin, maintenance margin, and the mechanics of daily profit-and-loss settlement.
- **Why Forwards Are Easy and Options Are Hard** — the conceptual bridge from linear payoffs to the nonlinear world of options, motivating the need for the Black-Scholes framework.

## The Key Takeaway

Mastering forward pricing is not merely a prerequisite — it is the foundation.
Every concept introduced here (no-arbitrage, replication, cost of carry, risk-neutral
valuation) reappears, in a more complex form, when we price options. If you
understand *why* the forward price must equal $S_0 \, e^{rT}$, you already
possess the core intuition behind the Black-Scholes formula. The rest is
generalization.
