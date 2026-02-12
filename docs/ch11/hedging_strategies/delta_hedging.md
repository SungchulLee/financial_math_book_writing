# Delta Hedging


Delta hedging is the most fundamental options risk management technique: maintain a portfolio whose net delta is zero to eliminate first-order directional exposure.

---

## Principle


For a portfolio containing options, the **portfolio delta** measures total first-order sensitivity to the underlying price. A delta-neutral portfolio satisfies

\[
\boxed{\Delta_{\text{portfolio}} = 0}
\]

For a single long option with delta \(\Delta\), this requires holding \(-\Delta\) shares of the underlying.

---

## Static delta hedge: worked example


Suppose you hold **100 European call options** (each on 1 share) with delta \(\Delta = 0.6\).

**Portfolio delta** before hedging:

\[
\Delta_{\text{portfolio}} = 100 \times 0.6 = 60
\]

**Delta-neutral hedge**: short **60 shares** of the underlying.

\[
\Delta_{\text{hedged}} = 60 - 60 = 0
\]

After hedging, a \$1 move in the stock produces approximately zero change in portfolio value (to first order).

---

## Why delta hedging is imperfect


Delta hedging eliminates only the **linear** component of price risk. The residual P&L after delta hedging comes from:

**Gamma (convexity).** The delta itself changes as \(S\) moves. For a move \(\delta S\):

\[
\delta V_{\text{hedged}} \approx \frac{1}{2}\Gamma(\delta S)^2
\]

This term is always positive for long options (\(\Gamma > 0\)), meaning the hedged portfolio benefits from large moves — but the cost is theta.

**Theta (time decay).** The Black–Scholes PDE implies:

\[
\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)
\]

For a long gamma position, theta is negative: the portfolio loses value with the passage of time if the stock doesn't move.

**Discrete rebalancing.** In practice, hedges are adjusted at discrete intervals, not continuously. The error between discrete and continuous hedging is proportional to \(\Gamma \cdot \sigma^2 S^2 \cdot \Delta t\).

---

## Dynamic delta hedging


In practice, delta changes with \(S\), so the hedge must be **rebalanced** over time.

**Algorithm:**

1. At time \(t_0\): compute \(\Delta(t_0, S_0)\), hold \(-\Delta \cdot N_{\text{options}}\) shares.
2. At time \(t_1\): recompute \(\Delta(t_1, S_1)\), adjust share position.
3. Repeat at each rebalancing date.

**Rebalancing cost** per step is approximately \(|\Delta(t_{i+1}) - \Delta(t_i)| \times S \times \text{spread}\).

The tradeoff: more frequent rebalancing reduces hedging error but increases transaction costs.

---

## P&L decomposition


Over a rebalancing period \([t, t+\Delta t]\), the delta-hedged P&L decomposes as:

\[
P\&L \approx \underbrace{\Theta\,\Delta t}_{\text{time decay}} + \underbrace{\frac{1}{2}\Gamma(\Delta S)^2}_{\text{gamma P\&L}} + \underbrace{\nu\,\Delta\sigma}_{\text{vega P\&L}}
\]

where \(\Delta S = S_{t+\Delta t} - S_t\) and \(\Delta\sigma\) is any change in implied volatility. This decomposition is the workhorse of options P&L attribution.

---

## Python implementation


```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_S = 100
K = 100
delta = 0.6
num_options = 100
hedge_shares = -num_options * delta  # short shares

# Simulate range of stock price moves
price_moves = np.linspace(-20, 20, 200)
final_S = initial_S + price_moves

# Approximate option P&L (using delta only)
option_pnl = num_options * delta * price_moves

# Unhedged P&L
unhedged_pnl = option_pnl

# Hedged P&L
stock_pnl = hedge_shares * price_moves
hedged_pnl = option_pnl + stock_pnl  # ≈ 0 by construction

# Include gamma effect for more realistic hedged P&L
gamma = 0.04
hedged_pnl_with_gamma = (num_options * 0.5 * gamma * price_moves**2
                         + stock_pnl + option_pnl)

plt.figure(figsize=(10, 6))
plt.plot(final_S, unhedged_pnl, label='Unhedged P&L (Option Only)', linewidth=2)
plt.plot(final_S, hedged_pnl, label='Delta-Hedged P&L (linear)', linewidth=2, linestyle='--')
plt.plot(final_S, hedged_pnl_with_gamma, label='Delta-Hedged P&L (with gamma)',
         linewidth=2, linestyle='-.')
plt.axhline(0, color='gray', linestyle='--', alpha=0.5)
plt.title('P&L: Hedged vs. Unhedged')
plt.xlabel('Final Stock Price')
plt.ylabel('P&L ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

The plot shows: without hedging, P&L is linear in the stock move. With delta hedging, the linear component vanishes, leaving only the gamma (quadratic) term — positive for long options.

---

## When delta hedging works well


- **Low gamma** positions: delta changes slowly, infrequent rebalancing suffices.
- **Liquid underlyings**: tight spreads keep rebalancing costs manageable.
- **Moderate time to expiry**: far from expiry, gamma is smaller and delta is more stable.

---

## When delta hedging breaks down


- **Near expiry, near the strike**: gamma blows up (\(\Gamma \sim 1/(S\sigma\sqrt{\tau})\)), delta changes violently.
- **Jumps in the underlying**: delta hedging assumes continuous price paths; jumps cause unhedgeable losses.
- **Illiquid markets**: wide bid-ask spreads make frequent rebalancing prohibitively expensive.
- **Large moves**: the linear approximation \(\delta V \approx \Delta\,\delta S\) breaks down for moves where higher-order terms matter.

---

## What to remember


- Delta hedging removes first-order directional risk by holding \(-\Delta\) shares per option.
- Residual P&L after delta hedging is driven by gamma, theta, and vega — the higher-order Greeks.
- Dynamic rebalancing is necessary because delta changes with \(S\) and \(t\).
- The gamma-theta tradeoff is fundamental: long gamma earns on moves but pays theta; short gamma earns theta but loses on moves.
