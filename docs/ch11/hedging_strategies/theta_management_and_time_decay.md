# Theta Management and Time Decay


Theta measures the rate of decline in an option's value with the passage of time, holding all else constant. Managing theta exposure is central to options portfolio construction and P&L forecasting.

---

## Theta sign conventions


For a **long option** (call or put), theta is typically **negative**: the position loses value each day as the option approaches expiry and extrinsic value erodes.

For a **short option**, theta is **positive**: the position gains value as the sold option decays toward its intrinsic value.

This time decay accelerates as the option nears expiration, especially for **at-the-money** options where the extrinsic value is largest.

---

## Time decay by moneyness


### Call options

As time to maturity \(\tau = T - t\) decreases, the call price converges to its intrinsic value:

\[
C(S, t) \to \max(S - K, 0) \quad \text{as } \tau \to 0
\]

The rate of convergence depends on moneyness:

| Moneyness | Behavior | Theta magnitude |
|---|---|---|
| **ITM** (\(S \gg K\)) | Converges to \(S - K\); slow time value loss | Moderate |
| **ATM** (\(S \approx K\)) | Largest extrinsic value; decays fastest | Largest |
| **OTM** (\(S \ll K\)) | Already near zero; decays quickly but cheaply | Small (option is cheap) |

### Put options

Similarly:

\[
P(S, t) \to \max(K - S, 0) \quad \text{as } \tau \to 0
\]

ATM puts also exhibit the fastest time decay, mirroring the call behavior.

---

## Theta acceleration near expiry


The \(\sqrt{\tau}\) dependence in the Black–Scholes formula means that an ATM option's time value decays as

\[
V_{\text{extrinsic}} \propto \sigma S \sqrt{\tau}
\]

Taking the derivative with respect to \(\tau\):

\[
\Theta_{\text{ATM}} \propto -\frac{\sigma S}{2\sqrt{\tau}}
\]

This diverges as \(\tau \to 0\), reflecting the well-known acceleration of time decay in the final days before expiry. For an ATM option with 1 day to expiry, theta is approximately \(\sqrt{252}\) times larger than for a 1-year option (per unit of calendar time).

---

## Practical objectives of theta management


1. **Forecast time decay in P&L models** for long and short positions.
2. **Construct theta-neutral portfolios** by offsetting long and short options at different maturities.
3. **Harvest theta** through short option strategies while managing gamma risk.
4. **Minimize theta bleed** in directional option strategies.

---

## Calendar (time) spreads


A **calendar spread** involves buying a long-dated option and selling a short-dated option at the same strike.

**Example:** Buy a 6-month ATM call, sell a 1-month ATM call.

- The short-dated option has higher daily theta (faster decay).
- The long-dated option decays more slowly.
- **Net theta** can be positive: you earn the differential time decay.

The trade profits when:
- The underlying stays near the strike (both options are ATM).
- The short-dated option expires worthless, and the long-dated option retains value.
- Implied volatility increases (benefits the long leg more).

**Risk:** if the underlying moves far from the strike, both options lose extrinsic value and the spread collapses.

---

## Dynamic hedging with short gamma


### Strategy

Sell options to earn positive theta, then delta-hedge dynamically to manage directional exposure. The goal is to **harvest time decay** while staying market-neutral.

### P&L decomposition

For a short ATM call position that is delta-hedged:

\[
\text{Daily P\&L} \approx \underbrace{|\Theta|\,\Delta t}_{\text{theta income}} - \underbrace{\frac{1}{2}|\Gamma|(\Delta S)^2}_{\text{gamma cost from moves}}
\]

The strategy is profitable when realized volatility is **below** implied volatility:

\[
\mathbb{E}[\text{P\&L}] > 0 \iff \sigma_{\text{realized}} < \sigma_{\text{implied}}
\]

### Risks

- **Large moves**: if the underlying gaps significantly, gamma losses can overwhelm theta income.
- **Volatility spikes**: increasing implied vol raises the mark-to-market value of the short option, creating unrealized losses.
- **Tail events**: this is a concave P&L strategy — small gains most of the time, occasional large losses.

---

## Python: time decay visualization


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def bs_call_price(S, K, tau, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    return S * norm.cdf(d1) - K * np.exp(-r * tau) * norm.cdf(d2)

def bs_put_price(S, K, tau, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    return K * np.exp(-r * tau) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Parameters
r = 0.05
sigma = 0.2
K = 100
tau = np.linspace(0.01, 1.0, 200)

# Moneyness scenarios
spots = [120, 100, 80]
labels_call = ["ITM Call (S=120)", "ATM Call (S=100)", "OTM Call (S=80)"]
labels_put = ["OTM Put (S=120)", "ATM Put (S=100)", "ITM Put (S=80)"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for S, label in zip(spots, labels_call):
    axes[0].plot(tau, bs_call_price(S, K, tau, r, sigma), label=label, linewidth=2)
axes[0].set_xlabel("Time to Maturity (Years)")
axes[0].set_ylabel("Call Value ($)")
axes[0].set_title("European Call Price vs. Time to Maturity")
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].invert_xaxis()

for S, label in zip(spots, labels_put):
    axes[1].plot(tau, bs_put_price(S, K, tau, r, sigma), label=label, linewidth=2)
axes[1].set_xlabel("Time to Maturity (Years)")
axes[1].set_ylabel("Put Value ($)")
axes[1].set_title("European Put Price vs. Time to Maturity")
axes[1].legend()
axes[1].grid(True, alpha=0.3)
axes[1].invert_xaxis()

fig.suptitle("Time Decay: Option Prices Converge to Intrinsic Value", fontsize=14)
plt.tight_layout()
plt.show()
```

---

## Python: theta income from short call


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def bs_theta_call(S, K, tau, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(tau))
             - r * K * np.exp(-r * tau) * norm.cdf(d2))
    return theta

S, K = 100, 100
r, sigma = 0.01, 0.2
tau = np.linspace(0.01, 0.5, 200)

theta_call = bs_theta_call(S, K, tau, r, sigma)

plt.figure(figsize=(10, 5))
plt.plot(tau, -theta_call, label="Short Call Theta Income", color='darkorange', linewidth=2)
plt.xlabel("Time to Maturity (Years)")
plt.ylabel("Theta Income ($/year)")
plt.title("Theta Income from Short ATM Call Option")
plt.grid(True, alpha=0.3)
plt.legend()
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()
```

The plot shows theta income accelerating as expiry approaches — the short option earns the most theta in its final days.

---

## Theta hedging strategies summary


| Strategy | Mechanism | Risk profile |
|---|---|---|
| **Calendar spread** | Long far, short near at same strike | Profits from differential decay; loses on large moves |
| **Short gamma + delta hedge** | Sell options, hedge delta dynamically | Earns theta; loses on large moves and vol spikes |
| **Mixed maturity portfolio** | Combine long and short options across maturities | Can target net theta ≈ 0 |
| **Greeks optimization** | Minimize net theta subject to delta/gamma constraints | Systematic, requires full Greeks computation |

---

## What to remember


- Theta is most negative for long ATM options and accelerates near expiry as \(1/\sqrt{\tau}\).
- Short option positions earn theta but are exposed to gamma and vega risk.
- Calendar spreads exploit differential time decay between near and far maturities.
- The gamma-theta tradeoff is inescapable: earning theta always implies bearing some form of convexity risk.
