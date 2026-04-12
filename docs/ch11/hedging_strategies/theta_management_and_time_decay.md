# Theta Management and Time Decay


Theta measures the rate of decline in an option's value with the passage of time, holding all else constant. Managing theta exposure is central to options portfolio construction and P&L forecasting.

---

### Theta sign conventions


For a **long option** (call or put), theta is typically **negative**: the position loses value each day as the option approaches expiry and extrinsic value erodes.

For a **short option**, theta is **positive**: the position gains value as the sold option decays toward its intrinsic value.

This time decay accelerates as the option nears expiration, especially for **at-the-money** options where the extrinsic value is largest.

---

### Time decay by moneyness


#### Call options

As time to maturity $\tau = T - t$ decreases, the call price converges to its intrinsic value:

$$
C(S, t) \to \max(S - K, 0) \quad \text{as } \tau \to 0
$$

The rate of convergence depends on moneyness:

| Moneyness | Behavior | Theta magnitude |
|---|---|---|
| **ITM** ($S \gg K$) | Converges to $S - K$; slow time value loss | Moderate |
| **ATM** ($S \approx K$) | Largest extrinsic value; decays fastest | Largest |
| **OTM** ($S \ll K$) | Already near zero; decays quickly but cheaply | Small (option is cheap) |

#### Put options

Similarly:

$$
P(S, t) \to \max(K - S, 0) \quad \text{as } \tau \to 0
$$

ATM puts also exhibit the fastest time decay, mirroring the call behavior.

---

### Theta acceleration near expiry


The $\sqrt{\tau}$ dependence in the Black–Scholes formula means that an ATM option's time value decays as

$$
V_{\text{extrinsic}} \propto \sigma S \sqrt{\tau}
$$

Taking the derivative with respect to $\tau$:

$$
\Theta_{\text{ATM}} \propto -\frac{\sigma S}{2\sqrt{\tau}}
$$

This diverges as $\tau \to 0$, reflecting the well-known acceleration of time decay in the final days before expiry. For an ATM option with 1 day to expiry, theta is approximately $\sqrt{252}$ times larger than for a 1-year option (per unit of calendar time).

---

### Practical objectives of theta management


1. **Forecast time decay in P&L models** for long and short positions.
2. **Construct theta-neutral portfolios** by offsetting long and short options at different maturities.
3. **Harvest theta** through short option strategies while managing gamma risk.
4. **Minimize theta bleed** in directional option strategies.

---

### Calendar (time) spreads


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

### Dynamic hedging with short gamma


#### Strategy

Sell options to earn positive theta, then delta-hedge dynamically to manage directional exposure. The goal is to **harvest time decay** while staying market-neutral.

#### P&L decomposition

For a short ATM call position that is delta-hedged:

$$
\text{Daily P\&L} \approx \underbrace{|\Theta|\,\Delta t}_{\text{theta income}} - \underbrace{\frac{1}{2}|\Gamma|(\Delta S)^2}_{\text{gamma cost from moves}}
$$

The strategy is profitable when realized volatility is **below** implied volatility:

$$
\mathbb{E}[\text{P\&L}] > 0 \iff \sigma_{\text{realized}} < \sigma_{\text{implied}}
$$

#### Risks

- **Large moves**: if the underlying gaps significantly, gamma losses can overwhelm theta income.
- **Volatility spikes**: increasing implied vol raises the mark-to-market value of the short option, creating unrealized losses.
- **Tail events**: this is a concave P&L strategy — small gains most of the time, occasional large losses.

---

### Python: time decay visualization


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

### Python: theta income from short call


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

### Theta hedging strategies summary


| Strategy | Mechanism | Risk profile |
|---|---|---|
| **Calendar spread** | Long far, short near at same strike | Profits from differential decay; loses on large moves |
| **Short gamma + delta hedge** | Sell options, hedge delta dynamically | Earns theta; loses on large moves and vol spikes |
| **Mixed maturity portfolio** | Combine long and short options across maturities | Can target net theta ≈ 0 |
| **Greeks optimization** | Minimize net theta subject to delta/gamma constraints | Systematic, requires full Greeks computation |

---

### What to remember


- Theta is most negative for long ATM options and accelerates near expiry as $1/\sqrt{\tau}$.
- Short option positions earn theta but are exposed to gamma and vega risk.
- Calendar spreads exploit differential time decay between near and far maturities.
- The gamma-theta tradeoff is inescapable: earning theta always implies bearing some form of convexity risk.

---

## Exercises

**Exercise 1.** An ATM call with $S = K = 100$, $\sigma = 0.20$, $r = 0.03$ has price $C = \$4.50$ at $\tau = 0.25$ and $C = \$3.80$ at $\tau = 0.20$. Estimate the average daily theta over this 12.6-trading-day interval. Compare with the instantaneous theta from the Black--Scholes formula at $\tau = 0.25$.

??? success "Solution to Exercise 1"
    The call price drops from $C = \$4.50$ at $\tau = 0.25$ to $C = \$3.80$ at $\tau = 0.20$. The time interval is $\Delta\tau = 0.25 - 0.20 = 0.05$ years, which corresponds to $0.05 \times 252 = 12.6$ trading days.

    **Average daily theta:**

    $$
    \bar{\Theta}_{\text{daily}} = \frac{C(\tau = 0.20) - C(\tau = 0.25)}{\Delta\tau / (1/252)} = \frac{3.80 - 4.50}{12.6} = \frac{-0.70}{12.6} \approx -\$0.0556 \text{ per day}
    $$

    **Instantaneous theta from Black--Scholes at $\tau = 0.25$.** Using the ATM approximation:

    $$
    \Theta_{\text{ATM}} \approx -\frac{S\sigma}{2\sqrt{2\pi\tau}}
    $$

    With $S = 100$, $\sigma = 0.20$, $\tau = 0.25$:

    $$
    \Theta_{\text{annual}} \approx -\frac{100 \times 0.20}{2\sqrt{2\pi \times 0.25}} = -\frac{20}{2\sqrt{1.5708}} = -\frac{20}{2 \times 1.2533} = -\frac{20}{2.5066} \approx -7.979 \text{ per year}
    $$

    Converting to daily (dividing by 252):

    $$
    \Theta_{\text{daily}} \approx \frac{-7.979}{252} \approx -\$0.0317 \text{ per day}
    $$

    The average theta over the interval ($-\$0.056$/day) is larger in magnitude than the instantaneous theta at $\tau = 0.25$ ($-\$0.032$/day) because theta accelerates as $\tau$ decreases, so the average over $[0.20, 0.25]$ reflects the higher decay rates near $\tau = 0.20$.

---

**Exercise 2.** A calendar spread consists of selling a 1-month ATM call and buying a 3-month ATM call at $K = 100$. Using the theta formula $\Theta_{\text{ATM}} \approx -\frac{S\sigma}{2\sqrt{2\pi\tau}}$, compute the net theta of this spread for $\sigma = 0.20$. Under what conditions does the spread earn positive net theta?

??? success "Solution to Exercise 2"
    Using the ATM theta approximation $\Theta_{\text{ATM}} \approx -\frac{S\sigma}{2\sqrt{2\pi\tau}}$ with $S = 100$ and $\sigma = 0.20$:

    **Short 1-month call** ($\tau_1 = 1/12$): the trader earns the negative of the long theta, so

    $$
    \Theta_{\text{short}} = +\frac{100 \times 0.20}{2\sqrt{2\pi/12}} = +\frac{20}{2\sqrt{0.5236}} = +\frac{20}{2 \times 0.7236} = +\frac{20}{1.4472} \approx +13.82 \text{ per year}
    $$

    **Long 3-month call** ($\tau_2 = 3/12 = 0.25$):

    $$
    \Theta_{\text{long}} = -\frac{20}{2\sqrt{2\pi \times 0.25}} = -\frac{20}{2.5066} \approx -7.98 \text{ per year}
    $$

    **Net theta of the calendar spread:**

    $$
    \Theta_{\text{net}} = 13.82 + (-7.98) = +5.84 \text{ per year} \approx +\$0.023 \text{ per day}
    $$

    The spread earns positive net theta because the short-dated option decays faster than the long-dated option. This positive net theta occurs when both options are near the money. If the underlying moves far from the strike, both options become deep ITM or deep OTM, their thetas converge toward zero, and the differential decay advantage disappears.

---

**Exercise 3.** Theta acceleration near expiry scales as $1/\sqrt{\tau}$. Compute the ratio $\Theta(\tau = 1\text{ day})/\Theta(\tau = 30\text{ days})$ for an ATM option. A short-dated option writer earns more theta per day --- explain why this does not constitute a "free lunch" by discussing the corresponding gamma risk.

??? success "Solution to Exercise 3"
    The ATM theta scales as $\Theta \propto -1/\sqrt{\tau}$, so:

    $$
    \frac{|\Theta(\tau = 1\text{ day})|}{|\Theta(\tau = 30\text{ days})|} = \frac{1/\sqrt{1/252}}{1/\sqrt{30/252}} = \frac{\sqrt{30/252}}{\sqrt{1/252}} = \sqrt{\frac{30}{1}} = \sqrt{30} \approx 5.48
    $$

    The 1-day option decays approximately 5.5 times faster per day than the 30-day option.

    **Why this is not a free lunch.** The gamma of an ATM option also scales as $\Gamma \propto 1/\sqrt{\tau}$ (in fact, $\Gamma_{\text{ATM}} \propto 1/(S\sigma\sqrt{\tau})$). So the short-dated option has gamma that is $\sqrt{30} \approx 5.5$ times larger as well. The gamma-theta tradeoff is preserved: the higher theta income earned by selling the short-dated option is exactly offset by the higher gamma risk. A single large move near expiry can wipe out many days of accumulated theta, and the probability of such a move (relative to the option's remaining life) is not negligible. The short-dated option seller earns more theta per day but faces proportionally more rebalancing cost and tail risk.

---

**Exercise 4.** For a short ATM call position that is delta-hedged, the daily P&L is approximately $|\Theta|\Delta t - \frac{1}{2}|\Gamma|(\Delta S)^2$. If $\Theta = -0.08$/day and $\Gamma = 0.04$ per option, and the trader is short 100 options, compute the net daily P&L for realized daily moves of $|\Delta S| = 0$, $1$, $2$, and $3$ dollars. What is the breakeven daily move?

??? success "Solution to Exercise 4"
    The trader is short 100 ATM calls with $\Theta = -0.08$/day and $\Gamma = 0.04$ per option. Since the position is short, the portfolio-level values are:

    $$
    \Theta_{\text{port}} = 100 \times 0.08 = +8.0 \text{ per day}
    $$

    $$
    |\Gamma_{\text{port}}| = 100 \times 0.04 = 4.0
    $$

    The daily P&L formula is:

    $$
    \text{P\&L} = |\Theta_{\text{port}}| - \frac{1}{2}|\Gamma_{\text{port}}|(\Delta S)^2 = 8.0 - \frac{1}{2}(4.0)(\Delta S)^2 = 8.0 - 2.0(\Delta S)^2
    $$

    | $|\Delta S|$ | Gamma cost | Net P&L |
    |:---:|:---:|:---:|
    | $0$ | $0$ | $+\$8.00$ |
    | $1$ | $2.0$ | $+\$6.00$ |
    | $2$ | $8.0$ | $\$0.00$ |
    | $3$ | $18.0$ | $-\$10.00$ |

    **Breakeven daily move:**

    $$
    2.0(\Delta S^*)^2 = 8.0 \implies (\Delta S^*)^2 = 4.0 \implies \Delta S^* = \$2.00
    $$

    Any daily move exceeding $\$2.00$ causes a net loss.

---

**Exercise 5.** A trader wants to construct a theta-neutral portfolio using ATM options at $\tau_1 = 1$ month and $\tau_2 = 6$ months. If $\Theta_1 = -0.12$/day and $\Theta_2 = -0.04$/day per option, how many of each option should the trader hold (long or short) to achieve net theta $\approx 0$ with 100 options at the shorter maturity? What is the resulting gamma exposure?

??? success "Solution to Exercise 5"
    The trader holds 100 short options at $\tau_1 = 1$ month with $\Theta_1 = -0.12$/day per option (short position earns $+0.12$/day per option). To achieve net theta $\approx 0$, they need to go long options at $\tau_2 = 6$ months with $\Theta_2 = -0.04$/day per option.

    Net theta condition:

    $$
    -100 \times \Theta_1 + n_2 \times \Theta_2 = 0
    $$

    Note: shorting 100 options at maturity 1 gives portfolio theta $= -100 \times (-0.12) = +12.0$/day. Going long $n_2$ options at maturity 2 gives portfolio theta contribution $= n_2 \times (-0.04)$/day.

    $$
    +12.0 + n_2(-0.04) = 0 \implies n_2 = \frac{12.0}{0.04} = 300
    $$

    The trader should go long 300 options at the 6-month maturity.

    **Resulting gamma exposure.** ATM gamma scales as $\Gamma \propto 1/(S\sigma\sqrt{\tau})$. Let $\Gamma_1$ and $\Gamma_2$ denote the per-option gammas. Since $\Theta_{\text{ATM}} \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$ (in annual terms), we have $\Gamma \propto |\Theta|/(\sigma^2 S^2)$. The ratio of gammas is:

    $$
    \frac{\Gamma_1}{\Gamma_2} = \frac{|\Theta_1|}{|\Theta_2|} = \frac{0.12}{0.04} = 3
    $$

    The net gamma is:

    $$
    \Gamma_{\text{net}} = -100\Gamma_1 + 300\Gamma_2 = -100\Gamma_1 + 300 \times \frac{\Gamma_1}{3} = -100\Gamma_1 + 100\Gamma_1 = 0
    $$

    In this idealized case (same $\sigma$, $S$, $K$), the theta-neutral portfolio is also gamma-neutral. This is a consequence of the $\Theta$-$\Gamma$ proportionality in Black--Scholes. In practice, differences in moneyness, implied vol levels, or skew effects would create residual gamma.

---

**Exercise 6.** Using the Python theta visualization code, add a plot showing the **daily theta P&L** of a calendar spread (short 1-month call, long 6-month call) as a function of the underlying price $S$ at inception. Identify the spot range where the spread earns positive daily theta and explain why the spread loses money when $S$ moves far from the strike.

??? success "Solution to Exercise 6"
    This is a computational exercise. The key idea is to compute the net theta of the calendar spread as a function of the spot price $S$.

    For each value of $S$, compute the Black--Scholes theta of both legs:

    - Short 1-month call at $K = 100$: $\Theta_{\text{short}}(S) = -\Theta_{\text{BS}}(S, K, \tau_1)$ (positive, since we are short)
    - Long 6-month call at $K = 100$: $\Theta_{\text{long}}(S) = \Theta_{\text{BS}}(S, K, \tau_2)$ (negative)

    The net daily theta is $\Theta_{\text{net}}(S) = \Theta_{\text{short}}(S) + \Theta_{\text{long}}(S)$.

    **Expected shape.** The net theta is positive (earning) near $S = K = 100$ because the short-dated option has higher absolute theta than the long-dated option when both are near the money. As $S$ moves far from $K$ in either direction:

    - Both options become deep ITM or deep OTM.
    - The extrinsic value of both options shrinks toward zero.
    - Both thetas approach zero, and the net theta also approaches zero or may turn slightly negative.

    The positive-theta region is approximately $S \in [85, 115]$ for typical parameters. Outside this range, the spread provides negligible theta income. The spread loses money when $S$ moves far from the strike because the long 6-month option loses more value (in absolute terms) than the short 1-month option, as the longer-dated option has more extrinsic value exposed to the spot move. Additionally, far from the strike, the short option may already be worthless, so no further theta income accrues from it while the long option continues to bleed.
