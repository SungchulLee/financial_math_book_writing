# Introduction

Long before the first option was traded on an exchange, merchants and farmers were
already locking in future prices. Forward-like agreements appear in Mesopotamian
clay tablets dating to roughly 1750 BCE, where grain delivery contracts specified
quantities and fixed prices under the Code of Hammurabi. Around 600 BCE, Thales of
Miletus reportedly paid deposits to secure future access to olive presses before the
harvest — often cited as the first recorded derivatives trade. By the 1630s, Dutch
merchants were trading forward contracts on tulip bulbs during the famous Tulip
Mania, though these lacked standardization and carried substantial default risk.

The transition from informal forwards to true futures occurred in Japan. The Dojima
Rice Exchange in Osaka (circa 1730) introduced standardized rice contracts traded on
an organized exchange with rudimentary clearing — widely regarded as the first
genuine futures market. The modern system of standardized contracts, fixed delivery
dates, margin requirements, and a central clearinghouse was established at the
Chicago Board of Trade (CBOT) in 1848 and remains the template for exchanges
worldwide.

Forwards and futures are, quite literally, the oldest derivatives — and they remain
among the most actively traded instruments today, covering commodities, currencies,
interest rates, and equity indices worth trillions of dollars.

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
F = S_0 \, e^{rT}
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
