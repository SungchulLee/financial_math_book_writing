# Basic Trading and Hedging Strategies


Options trading strategies are built on Greek exposures. Each strategy expresses a specific view on direction, volatility, or time decay.

---

## Delta-neutral hedging


Continuously rebalance shares to offset directional moves. This is the foundation of all other strategies.

Key properties:

- Requires frequent adjustment in high-gamma positions.
- Transaction costs from rebalancing scale with gamma and realized volatility.
- Perfect only in the continuous-time, zero-cost limit of Black–Scholes.

---

## Gamma-theta tradeoff


### Long gamma (buying options)

Position: buy calls/puts or straddles. Greek profile: \(\Gamma > 0\), \(\Theta < 0\), \(\nu > 0\).

Profit when the underlying makes large moves (realized vol exceeds implied vol). The cost is daily theta bleed when the market is quiet. Best used ahead of anticipated events.

### Short gamma (selling options)

Position: sell calls/puts or straddles. Greek profile: \(\Gamma < 0\), \(\Theta > 0\), \(\nu < 0\).

Profit when the market stays calm (realized vol below implied vol). Risk: large, sudden moves cause disproportionate losses (concave P&L). Best suited for range-bound markets with elevated implied vol.

---

## Vega trades


**Long vega:** buy options when expecting implied volatility to increase. Common before anticipated volatility events. Theta decay works against you while waiting.

**Short vega:** sell options when expecting implied volatility to decrease. Common after volatility spikes expected to mean-revert. Risk: further vol increases lead to mark-to-market losses.

---

## Risk reversal


**Construction:** long OTM call + short OTM put (same expiry).

**Greek profile:** positive delta (bullish directional bet), typically positive net vega, can be structured for near-zero premium.

**Use case:** express a directional and volatility view simultaneously. The skew (puts typically more expensive than equidistant calls) means you receive premium from the rich put to fund the cheap call.

**Risk:** the short put creates downside exposure if the underlying falls significantly.

---

## Straddle


### Long straddle

**Construction:** buy call and put at the same strike (typically ATM) and expiry.

**Greek profile:**

- \(\Delta \approx 0\) (initially neutral).
- \(\Gamma > 0\) (benefits from moves in either direction).
- \(\Theta < 0\) (pays significant time decay).
- \(\nu > 0\) (benefits from vol increases).

**Profit when:** the underlying moves substantially in either direction, or implied vol rises. The move must be large enough to offset the premium paid (which includes time value for both options).

**Breakeven:** \(S_T > K + \text{premium}\) or \(S_T < K - \text{premium}\).

### Short straddle

**Construction:** sell call and put at the same strike.

**Greek profile:** \(\Gamma < 0\), \(\Theta > 0\), \(\nu < 0\).

**Profit when:** the market stays calm and near the strike. Earn premium from time decay. Risk is unlimited in both directions.

---

## Strangle


### Long strangle

**Construction:** buy OTM call (strike \(K_2\)) and OTM put (strike \(K_1 < K_2\)).

Similar to long straddle but cheaper (both options are OTM), with wider breakeven points. Requires a larger move to profit, but costs less in theta.

### Short strangle

**Construction:** sell OTM call and OTM put.

Earns premium if the underlying stays between the two strikes. Wider profit zone than a short straddle, but less premium collected.

---

## Greek summary of common strategies


| Strategy | \(\Delta\) | \(\Gamma\) | \(\Theta\) | \(\nu\) | View |
|---|---|---|---|---|---|
| Long call | + | + | − | + | Bullish + long vol |
| Short call | − | − | + | − | Bearish + short vol |
| Long straddle | ≈ 0 | + | − | + | Big move expected |
| Short straddle | ≈ 0 | − | + | − | Range-bound |
| Risk reversal | + | mixed | mixed | mixed | Directional + skew |
| Calendar spread | ≈ 0 | mixed | + | mixed | Differential decay |

---

## Python: advanced P&L simulator


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
S0 = 100
K = 100
T = 1.0
r = 0.05
sigma0 = 0.2
num_options = 100
num_steps = 200

# Range of final stock prices
S_final = np.linspace(70, 130, num_steps)
dS = S_final - S0

# Simulate a volatility perturbation
dsigma = 0.05 * np.sin(np.pi * (S_final - 70) / 60)  # vol smile effect

# Compute Greeks at initial point
d1_0 = (np.log(S0 / K) + (r + 0.5 * sigma0**2) * T) / (sigma0 * np.sqrt(T))
delta_0 = norm.cdf(d1_0)
gamma_0 = norm.pdf(d1_0) / (S0 * sigma0 * np.sqrt(T))
vega_0 = S0 * np.sqrt(T) * norm.pdf(d1_0)

# Option value change (Taylor expansion)
option_pnl = num_options * (delta_0 * dS
                            + 0.5 * gamma_0 * dS**2
                            + vega_0 * dsigma)

# Hedging strategies
# 1. No hedge
unhedged = option_pnl

# 2. Static delta hedge
static_hedge = option_pnl - num_options * delta_0 * dS

# 3. Dynamic delta hedge (approximate: delta varies with S)
d1_final = (np.log(S_final / K) + (r + 0.5 * sigma0**2) * T) / (sigma0 * np.sqrt(T))
delta_final = norm.cdf(d1_final)
avg_delta = 0.5 * (delta_0 + delta_final)
dynamic_hedge = option_pnl - num_options * avg_delta * dS

# Plot
plt.figure(figsize=(12, 7))
plt.plot(S_final, unhedged, label='Unhedged', linewidth=2)
plt.plot(S_final, static_hedge, label='Static Delta Hedge', linewidth=2)
plt.plot(S_final, dynamic_hedge, label='Dynamic Delta Hedge (approx)', linewidth=2)
plt.axhline(0, color='gray', linestyle='--', alpha=0.5)
plt.xlabel('Final Stock Price')
plt.ylabel('P&L ($)')
plt.title('P&L Under Different Hedging Strategies (with Gamma + Vega Effects)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

This demonstrates: unhedged P&L is dominated by directional moves, static delta hedging removes the linear component but leaves gamma and vega effects, and dynamic hedging further reduces the residual.

---

## What to remember


- Every option strategy is a combination of Greek exposures expressing a specific market view.
- The gamma-theta tradeoff is inescapable: long gamma costs theta, short gamma earns theta.
- Straddles and strangles provide symmetric exposure to large moves (or calm markets).
- Risk reversals combine directional and volatility views, often exploiting skew.
- Understanding the Greek profile of each strategy is essential before entering any position.
