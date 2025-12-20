# Why Measure Change Removes Arbitrage

A central insight of modern financial mathematics is that **absence of arbitrage**
is equivalent to the existence of a probability measure under which discounted asset
prices are martingales.

This section explains *why* changing the probability measure removes arbitrage
opportunities, without introducing new technical results.

---

## Arbitrage and Predictable Drift

Under the physical (real-world) probability measure \(\mathbb{P}\), asset prices
typically exhibit a drift reflecting risk preferences, growth expectations, and
economic forces. For a risky asset \(S_t\),
\[
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}}.
\]

If the drift \(\mu_t\) were exploitable without risk, arbitrage would arise.
However, the presence of risk means that drift alone does not create arbitrage
unless it can be hedged away.

---

## Discounting and Martingales

Let \(B_t\) denote the money market account (numéraire),
\[
B_t = \exp\!\left(\int_0^t r_s\,ds\right).
\]

Absence of arbitrage requires that **discounted asset prices**
\[
\tilde S_t := \frac{S_t}{B_t}
\]
do not admit predictable gains. Mathematically, this means that \(\tilde S_t\)
should be a martingale under some probability measure.

---

## Role of Measure Change

Girsanov’s theorem provides the mechanism to remove drift terms by changing the
probability measure. Under a suitable equivalent measure \(\mathbb{Q}\),
the discounted asset price satisfies
\[
d\tilde S_t = \sigma_t \tilde S_t\, dW_t^{\mathbb{Q}},
\]
with zero drift.

This transformation does not alter the possible price paths, but **reweights their
probabilities** so that systematic gains disappear.

---

## Economic Interpretation

Changing the measure does not change reality. Instead, it changes the *lens*
through which uncertainty is evaluated. Under the risk-neutral measure:
- Expected returns are adjusted for risk,
- Only the time value of money remains,
- Arbitrage opportunities are eliminated by construction.

This explains why pricing can be performed under \(\mathbb{Q}\) even though the
world evolves under \(\mathbb{P}\).

---

## Key Principle

> Arbitrage-free pricing is possible because risk can be absorbed into the
> probability measure.

This principle underlies all modern pricing theory and will be used repeatedly
in later chapters.
