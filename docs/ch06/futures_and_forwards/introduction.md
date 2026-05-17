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
is pedagogical. Recall (see [§ Payoff of Forwards and Futures](payoff.md)): the forward payoff $S_T - K$ is **linear**, with no optionality and no volatility parameter. Recall (see [§ No-Arbitrage Pricing of Forwards](no_arbitrage_pricing.md)): pricing reduces to one equation $F_0 = S_0 e^{rT}$ — the prototype for every pricing argument that follows, including Black-Scholes.

## How to Read This Section

Every page that follows is built on the same three-step pattern:

1. **A tiny concrete scene** — one farmer, one barrel of oil, one numerical arbitrage — that exposes the mechanism on a single page.
2. **The abstract principle** the toy reveals — no-arbitrage, replication, cost of carry — stated in symbols only after the reader has *seen* it work.
3. **The general formula and its extensions** — dividends, storage, convexity, daily settlement — each obtained by perturbing the toy.

Read the concrete scene first; treat the formulas as compressions of the scene, not as definitions to memorize. The same pattern reappears in later chapters when we replace the linear payoff $S_T - K$ with the nonlinear payoff $(S_T - K)^+$ and rebuild the pricing argument for options.

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

Mastering forward pricing is not merely a prerequisite — it is the foundation. Every concept introduced here (no-arbitrage, replication, cost of carry, risk-neutral valuation) reappears in more complex form when we price options. The bridge from this linear world to the nonlinear world of options is developed in [§ From Forwards to Options](bridge_to_options.md).

## Exercises

**Exercise 1.** A forward contract on stock ABC is struck at F = 50 with delivery in 6 months. If the spot price at delivery is S_T = 55, what is the payoff to the long party? What is the payoff to the short party?

??? success "Solution to Exercise 1"
    The long party's payoff is S_T - F = 55 - 50 = 5. The short party's payoff is F - S_T = 50 - 55 = -5. Forward contracts are zero-sum: the long party's gain equals the short party's loss.

---

**Exercise 2.** Explain why the forward price of a non-dividend-paying stock satisfies F = S_0 * exp(rT), where r is the risk-free rate and T is the time to delivery.

??? success "Solution to Exercise 2"
    Consider two portfolios: (A) enter a long forward at price F, and (B) buy the stock now at S_0, funded by borrowing at rate r. Portfolio B costs S_0 * exp(rT) at delivery. Both portfolios deliver one share at time T. By no-arbitrage, they must have the same cost, so F = S_0 * exp(rT).

---

**Exercise 3.** In one sentence each, state the role of (a) replication, (b) cost of carry, and (c) daily settlement in the theory of forwards and futures. For each, name the section of this chapter where the concept is developed.

??? success "Solution to Exercise 3"
    (a) **Replication** constructs a portfolio of traded assets whose payoff matches the forward's, pinning down the forward price via no-arbitrage — see [§ No-Arbitrage Pricing of Forwards](no_arbitrage_pricing.md).

    (b) **Cost of carry** generalizes the replication argument to include dividends, storage costs, and convenience yields — see [§ Cost of Carry](cost_of_carry.md).

    (c) **Daily settlement** converts the forward's single terminal payment into a sequence of daily margin flows, exchanging credit risk for liquidity risk — see [§ Margin and Marking to Market](margin_mark_to_market.md).

---

**Exercise 4.** Forwards and futures have linear payoffs, while options have nonlinear payoffs. In one sentence, explain why this distinction matters for the *complexity of pricing*.

??? success "Solution to Exercise 4"
    Linear payoffs can be replicated by a one-time **static** portfolio of stock and bond, so pricing is algebraic and depends only on $r$; nonlinear payoffs require **dynamic** rebalancing whose cost depends on volatility $\sigma$, leading to the Black-Scholes machinery — see [§ From Forwards to Options](bridge_to_options.md).

---

**Exercise 5.** Name three real-world futures contracts and identify, for each, whether it is settled by physical delivery or in cash.

??? success "Solution to Exercise 5"
    Examples (recall, see [§ What is a Forward and a Future?](what_is_forward_future.md)):

    - **WTI Crude Oil (CL)**: physical delivery at Cushing, Oklahoma.
    - **Gold (GC)**: physical delivery (100 troy oz).
    - **S&P 500 E-mini (ES)** and **KOSPI 200**: cash-settled against the final index level.

    VIX futures are also cash-settled — against a special VIX settlement value.

---

**Exercise 6.** Two practitioners disagree: one says "the forward price is what the market expects the stock to be worth at $T$"; the other says "the forward price is just $S_0$ carried at the risk-free rate." Which is correct, and why?

??? success "Solution to Exercise 6"
    The second is correct under the standard no-arbitrage assumption: $F_0 = S_0 e^{rT}$ depends only on $S_0$, $r$, and $T$, not on the real-world drift $\mu$ of the stock. Any market expectation is already embedded in $S_0$.

    The first statement is only correct under the **risk-neutral measure** $\mathbb{Q}$: $F_0 = \mathbb{E}^{\mathbb{Q}}[S_T]$ — the expected price under $\mathbb{Q}$, not under the real-world probability $\mathbb{P}$ — see [§ No-Arbitrage Pricing of Forwards](no_arbitrage_pricing.md).

