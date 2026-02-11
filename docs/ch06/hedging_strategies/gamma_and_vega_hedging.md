# Gamma and Vega Hedging


Delta hedging removes linear price risk but leaves the portfolio exposed to gamma (convexity) and vega (volatility) risks. Neutralizing these requires trading additional options.

---

## Gamma hedging


### Why gamma matters

After delta hedging, the residual P&L over an interval is

\[
P\&L_{\text{hedged}} \approx \frac{1}{2}\Gamma(\delta S)^2 + \Theta\,\delta t
\]

If \(\Gamma\) is large, even moderate price moves create significant P&L swings. **Gamma hedging** seeks

\[
\boxed{\Gamma_{\text{portfolio}} = 0}
\]

### Mechanics

Since the underlying asset has \(\Gamma = 0\) (its price is linear in itself), gamma can only be hedged with **other options**.

**Worked example.** You are long 100 calls with per-option \(\Gamma_{\text{call}} = 0.04\).

Total gamma: \(100 \times 0.04 = 4.0\).

To neutralize, find another option (e.g., an ATM put) with \(\Gamma_{\text{put}} = 0.05\). Short

\[
n = \frac{4.0}{0.05} = 80 \text{ puts}
\]

After adding 80 short puts:

\[
\Gamma_{\text{portfolio}} = 4.0 - 80 \times 0.05 = 0
\]

**Important.** Adding the puts changes the portfolio delta, so you must **re-delta-hedge** after the gamma adjustment.

### Sequential hedging procedure

1. **Gamma-neutralize** using options (match \(\Gamma\) with opposite-sign option positions).
2. **Re-delta-hedge** using shares to restore \(\Delta_{\text{portfolio}} = 0\).

This order matters: adjusting gamma with options changes delta, but adjusting delta with shares does not affect gamma.

---

## Vega hedging


### Why vega matters

In real markets, implied volatility changes over time. A portfolio with net vega exposure gains or loses value as implied vol shifts:

\[
\delta V \approx \nu \cdot \delta\sigma_{\text{implied}}
\]

A **vega-neutral** portfolio satisfies

\[
\boxed{\nu_{\text{portfolio}} = 0}
\]

### Mechanics

Like gamma, vega can only be hedged with **other options** (the underlying has zero vega). Vega hedging typically involves:

- **Buying/selling options** at different strikes or maturities to offset net vega.
- **Variance swaps**: provide direct exposure to realized variance, useful for hedging aggregate vega.
- **VIX options/futures**: trade implied volatility directly (for equity index portfolios).

### Vega-gamma interaction

In Black–Scholes, vega and gamma are proportional:

\[
\nu = \sigma S^2 \tau\,\Gamma
\]

This means gamma-hedging automatically addresses vega in the Black–Scholes world. However, in practice (stochastic volatility, term structure effects), vega and gamma are **not perfectly correlated**, and separate hedging is required.

---

## Joint gamma-vega hedging


When both gamma and vega must be neutralized, you need **at least two option instruments** (in addition to the underlying for delta). This creates a system of equations:

\[
\begin{cases}
n_1 \Gamma_1 + n_2 \Gamma_2 = -\Gamma_{\text{existing}} \\
n_1 \nu_1 + n_2 \nu_2 = -\nu_{\text{existing}}
\end{cases}
\]

Solve for \(n_1, n_2\), then re-delta-hedge with shares.

**Example.** Existing portfolio: \(\Gamma = +4\), \(\nu = +200\).

Available instruments:
- Option A: \(\Gamma_A = 0.05\), \(\nu_A = 3.0\)
- Option B: \(\Gamma_B = 0.02\), \(\nu_B = 5.0\)

Solve:

\[
\begin{pmatrix} 0.05 & 0.02 \\ 3.0 & 5.0 \end{pmatrix}
\begin{pmatrix} n_1 \\ n_2 \end{pmatrix}
= \begin{pmatrix} -4 \\ -200 \end{pmatrix}
\]

yielding the required positions in options A and B.

---

## The gamma-theta tradeoff


Gamma and theta are fundamentally linked through the Black–Scholes PDE:

\[
\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)
\]

This implies:

| Position | Gamma | Theta | Interpretation |
|---|---|---|---|
| **Long options** | \(\Gamma > 0\) | \(\Theta < 0\) | Benefit from moves, pay time decay |
| **Short options** | \(\Gamma < 0\) | \(\Theta > 0\) | Earn time decay, lose on moves |

You cannot have both positive gamma and positive theta simultaneously (in Black–Scholes). This tradeoff is the central tension in options portfolio management.

---

## Short gamma strategies


### Concept

Sell options to earn theta income while dynamically delta-hedging to manage directional risk. This is a **short volatility** strategy.

### Mechanics

1. **Sell short-dated ATM options** (high theta, high gamma).
2. **Delta-hedge frequently** to keep directional risk near zero.
3. **Profit source**: theta accumulation when realized volatility is below implied.
4. **Loss source**: gamma losses when large moves force unfavorable hedge adjustments.

### P&L structure

- **Profit = theta earned** (positive, accrues daily).
- **Loss = gamma cost** from rebalancing: approximately \(\frac{1}{2}|\Gamma|(\Delta S)^2\) per move.
- **Net P&L** depends on whether realized vol exceeds or falls below implied vol.

### Risk profile

Short gamma means the position's delta moves **against** you:

| When underlying rises | Delta decreases (you get shorter) |
|---|---|
| When underlying falls | Delta increases (you get longer) |

This forces the hedger to **buy high and sell low** when rebalancing — the fundamental cost of short gamma.

### When to use

- Market expected to remain range-bound (low realized vol).
- Fast execution capability for frequent rebalancing.
- Willingness to accept tail risk, or protective wings purchased to cap extreme losses.

---

## Python: computing hedge quantities


```python
import numpy as np

# Portfolio: long 100 calls
num_calls = 100
delta_call = 0.6
gamma_call = 0.04
vega_call = 2.5  # per option

# Total sensitivities
total_delta = num_calls * delta_call
total_gamma = num_calls * gamma_call
total_vega = num_calls * vega_call

print(f"Total Delta: {total_delta:.1f}")
print(f"Total Gamma: {total_gamma:.1f}")
print(f"Total Vega:  {total_vega:.1f}")

# Step 1: Gamma hedge using ATM puts (gamma = 0.05, vega = 3.0)
gamma_put = 0.05
delta_put = -0.5
vega_put = 3.0
num_puts = -total_gamma / gamma_put  # negative = short puts

print(f"\nShort {abs(num_puts):.0f} ATM puts to gamma-hedge")

# New portfolio Greeks after gamma hedge
new_delta = total_delta + num_puts * delta_put
new_gamma = total_gamma + num_puts * gamma_put
new_vega = total_vega + num_puts * vega_put

print(f"Post-gamma-hedge Delta: {new_delta:.1f}")
print(f"Post-gamma-hedge Gamma: {new_gamma:.4f}")
print(f"Post-gamma-hedge Vega:  {new_vega:.1f}")

# Step 2: Delta hedge with shares
shares = -new_delta
print(f"\nShort {shares:.1f} shares to delta-hedge")
print(f"Final Delta: {new_delta + shares:.4f}")
```

---

## What to remember


- Gamma can only be hedged with options, not with the underlying.
- After gamma-hedging with options, the portfolio must be re-delta-hedged with shares.
- The gamma-theta tradeoff is fundamental: you cannot simultaneously be long gamma and long theta.
- Short gamma earns theta but requires frequent rebalancing and exposes the portfolio to large moves.
- Joint gamma-vega hedging requires at least two option instruments plus shares.
