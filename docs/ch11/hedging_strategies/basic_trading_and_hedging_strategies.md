# Basic Trading and Hedging Strategies


Options trading strategies are built on Greek exposures. Each strategy expresses a specific view on direction, volatility, or time decay.

---

### Delta-neutral hedging


Continuously rebalance shares to offset directional moves. This is the foundation of all other strategies.

Key properties:

- Requires frequent adjustment in high-gamma positions.
- Transaction costs from rebalancing scale with gamma and realized volatility.
- Perfect only in the continuous-time, zero-cost limit of Black–Scholes.

---

### Gamma-theta tradeoff


#### Long gamma (buying options)

Position: buy calls/puts or straddles. Greek profile: \(\Gamma > 0\), \(\Theta < 0\), \(\nu > 0\).

Profit when the underlying makes large moves (realized vol exceeds implied vol). The cost is daily theta bleed when the market is quiet. Best used ahead of anticipated events.

#### Short gamma (selling options)

Position: sell calls/puts or straddles. Greek profile: \(\Gamma < 0\), \(\Theta > 0\), \(\nu < 0\).

Profit when the market stays calm (realized vol below implied vol). Risk: large, sudden moves cause disproportionate losses (concave P&L). Best suited for range-bound markets with elevated implied vol.

---

### Vega trades


**Long vega:** buy options when expecting implied volatility to increase. Common before anticipated volatility events. Theta decay works against you while waiting.

**Short vega:** sell options when expecting implied volatility to decrease. Common after volatility spikes expected to mean-revert. Risk: further vol increases lead to mark-to-market losses.

---

### Risk reversal


**Construction:** long OTM call + short OTM put (same expiry).

**Greek profile:** positive delta (bullish directional bet), typically positive net vega, can be structured for near-zero premium.

**Use case:** express a directional and volatility view simultaneously. The skew (puts typically more expensive than equidistant calls) means you receive premium from the rich put to fund the cheap call.

**Risk:** the short put creates downside exposure if the underlying falls significantly.

---

### Straddle


#### Long straddle

**Construction:** buy call and put at the same strike (typically ATM) and expiry.

**Greek profile:**

- \(\Delta \approx 0\) (initially neutral).
- \(\Gamma > 0\) (benefits from moves in either direction).
- \(\Theta < 0\) (pays significant time decay).
- \(\nu > 0\) (benefits from vol increases).

**Profit when:** the underlying moves substantially in either direction, or implied vol rises. The move must be large enough to offset the premium paid (which includes time value for both options).

**Breakeven:** \(S_T > K + \text{premium}\) or \(S_T < K - \text{premium}\).

#### Short straddle

**Construction:** sell call and put at the same strike.

**Greek profile:** \(\Gamma < 0\), \(\Theta > 0\), \(\nu < 0\).

**Profit when:** the market stays calm and near the strike. Earn premium from time decay. Risk is unlimited in both directions.

---

### Strangle


#### Long strangle

**Construction:** buy OTM call (strike \(K_2\)) and OTM put (strike \(K_1 < K_2\)).

Similar to long straddle but cheaper (both options are OTM), with wider breakeven points. Requires a larger move to profit, but costs less in theta.

#### Short strangle

**Construction:** sell OTM call and OTM put.

Earns premium if the underlying stays between the two strikes. Wider profit zone than a short straddle, but less premium collected.

---

### Greek summary of common strategies


| Strategy | \(\Delta\) | \(\Gamma\) | \(\Theta\) | \(\nu\) | View |
|---|---|---|---|---|---|
| Long call | + | + | − | + | Bullish + long vol |
| Short call | − | − | + | − | Bearish + short vol |
| Long straddle | ≈ 0 | + | − | + | Big move expected |
| Short straddle | ≈ 0 | − | + | − | Range-bound |
| Risk reversal | + | mixed | mixed | mixed | Directional + skew |
| Calendar spread | ≈ 0 | mixed | + | mixed | Differential decay |

---

### Python: advanced P&L simulator


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

### What to remember


- Every option strategy is a combination of Greek exposures expressing a specific market view.
- The gamma-theta tradeoff is inescapable: long gamma costs theta, short gamma earns theta.
- Straddles and strangles provide symmetric exposure to large moves (or calm markets).
- Risk reversals combine directional and volatility views, often exploiting skew.
- Understanding the Greek profile of each strategy is essential before entering any position.

---

## Exercises

**Exercise 1.** A trader constructs a long straddle by buying an ATM call and an ATM put, each priced at $\$5.00$. The combined premium is $\$10.00$. Compute the breakeven stock prices at expiry. If the underlying finishes at $S_T = 115$ with $K = 100$, what is the profit or loss?

??? success "Solution to Exercise 1"
    The long straddle consists of a long ATM call and a long ATM put, each costing $\$5.00$, so the total premium is $\$10.00$ with $K = 100$.

    **Breakeven at expiry.** The position profits when the intrinsic value exceeds the premium paid.

    - Upper breakeven: the call is in the money and the put expires worthless, so

    $$
    S_T - K = 10 \implies S_T = K + 10 = 110
    $$

    - Lower breakeven: the put is in the money and the call expires worthless, so

    $$
    K - S_T = 10 \implies S_T = K - 10 = 90
    $$

    **P&L at $S_T = 115$.** The call pays $115 - 100 = 15$ and the put expires worthless, so

    $$
    \text{P\&L} = 15 - 10 = +\$5.00
    $$

    The position is profitable because $S_T = 115$ lies above the upper breakeven of $110$.

---

**Exercise 2.** For a short strangle with $K_1 = 90$ (put) and $K_2 = 110$ (call), both OTM, the trader collects a total premium of $\$3.50$. Determine the breakeven levels and the maximum profit. Compute the P&L at $S_T = 85$ and $S_T = 120$.

??? success "Solution to Exercise 2"
    The short strangle collects a total premium of $\$3.50$ by selling an OTM put at $K_1 = 90$ and an OTM call at $K_2 = 110$.

    **Breakeven levels.** The seller loses money when the payoff on either short option exceeds the premium collected.

    - Upper breakeven: the short call is exercised, so

    $$
    S_T - K_2 = 3.50 \implies S_T = 110 + 3.50 = 113.50
    $$

    - Lower breakeven: the short put is exercised, so

    $$
    K_1 - S_T = 3.50 \implies S_T = 90 - 3.50 = 86.50
    $$

    **Maximum profit.** This occurs when both options expire worthless, i.e., $K_1 \leq S_T \leq K_2$. The maximum profit is the full premium: $\$3.50$.

    **P&L at $S_T = 85$.** The put is in the money: payoff $= 90 - 85 = 5$, and the call expires worthless.

    $$
    \text{P\&L} = 3.50 - 5.00 = -\$1.50
    $$

    **P&L at $S_T = 120$.** The call is in the money: payoff $= 120 - 110 = 10$, and the put expires worthless.

    $$
    \text{P\&L} = 3.50 - 10.00 = -\$6.50
    $$

---

**Exercise 3.** Using the Greek summary table, explain why a long straddle has $\Delta \approx 0$ initially but $\Gamma > 0$. As the underlying moves from $S = 100$ to $S = 108$, how does the portfolio delta change? What must the trader do to maintain delta neutrality?

??? success "Solution to Exercise 3"
    **Why $\Delta \approx 0$ initially.** A long straddle at the money consists of a long call with $\Delta_{\text{call}} \approx +0.5$ and a long put with $\Delta_{\text{put}} \approx -0.5$. The portfolio delta is

    $$
    \Delta_{\text{straddle}} = \Delta_{\text{call}} + \Delta_{\text{put}} \approx 0.5 + (-0.5) = 0
    $$

    **Why $\Gamma > 0$.** Both long options have positive gamma. Since gamma is always non-negative for long vanilla options:

    $$
    \Gamma_{\text{straddle}} = \Gamma_{\text{call}} + \Gamma_{\text{put}} > 0
    $$

    **Delta change as $S$ moves from 100 to 108.** As the underlying rises, both the call delta and the put delta increase (both move toward $+1$ and $0$, respectively). The rate of change is governed by gamma. With $\delta S = 8$:

    $$
    \Delta_{\text{new}} \approx \Delta_{\text{old}} + \Gamma_{\text{straddle}} \cdot \delta S = 0 + \Gamma_{\text{straddle}} \cdot 8 > 0
    $$

    The portfolio becomes net long delta. The call delta increases toward $1$ while the put delta moves toward $0$, so the positive gamma ensures the straddle picks up positive delta on an up-move.

    **Maintaining delta neutrality.** The trader must sell $\Gamma_{\text{straddle}} \times 8$ shares of the underlying to offset the newly acquired positive delta and restore $\Delta_{\text{portfolio}} = 0$.

---

**Exercise 4.** A risk reversal is constructed by buying a call at $K = 110$ and selling a put at $K = 90$ with $S_0 = 100$. If the call costs $\$3.00$ and the put premium received is $\$3.50$, what is the net premium? Compute the P&L at $S_T = 80$, $100$, and $120$. Explain why this strategy expresses both a directional and a volatility view.

??? success "Solution to Exercise 4"
    **Net premium.** The trader buys the call for $\$3.00$ and receives $\$3.50$ from selling the put:

    $$
    \text{Net premium} = -3.00 + 3.50 = +\$0.50 \text{ (credit)}
    $$

    **P&L at $S_T = 80$.** The call expires worthless. The short put is exercised: the trader must buy at $K = 90$ while the stock is worth $80$, costing $90 - 80 = 10$.

    $$
    \text{P\&L} = 0.50 - 10.00 = -\$9.50
    $$

    **P&L at $S_T = 100$.** Both options expire worthless (call strike 110, put strike 90).

    $$
    \text{P\&L} = +\$0.50
    $$

    **P&L at $S_T = 120$.** The call pays $120 - 110 = 10$. The put expires worthless.

    $$
    \text{P\&L} = 0.50 + 10.00 = +\$10.50
    $$

    **Directional and volatility view.** The risk reversal expresses a bullish directional view because it profits when the underlying rises and loses when it falls. It also exploits the volatility skew: OTM puts are typically more expensive than equidistant OTM calls due to the skew, so the trader receives a net credit by selling the "rich" put and buying the "cheap" call. The strategy implicitly takes a view that the skew overstates downside risk relative to upside potential.

---

**Exercise 5.** Explain the gamma-theta tradeoff for a short gamma position. If a trader sells an ATM straddle with $\Gamma = -0.08$ (portfolio) and $\Theta = +0.15$ per day, compute the P&L after one day if the underlying: (a) does not move; (b) moves by $2\%$; (c) moves by $5\%$. At what daily move does the gamma loss exceed the theta gain?

??? success "Solution to Exercise 5"
    The portfolio is short gamma with $\Gamma = -0.08$ and earns $\Theta = +0.15$ per day. Let $S_0 = 100$ for concreteness.

    **(a) Underlying does not move ($\delta S = 0$).**

    $$
    \text{P\&L} = \Theta \cdot 1 + \frac{1}{2}\Gamma(\delta S)^2 = 0.15 + 0 = +\$0.15
    $$

    Pure theta gain.

    **(b) Underlying moves by 2% ($\delta S = 2$).**

    $$
    \text{P\&L} = 0.15 + \frac{1}{2}(-0.08)(2)^2 = 0.15 - 0.16 = -\$0.01
    $$

    The gamma loss nearly offsets the theta gain.

    **(c) Underlying moves by 5% ($\delta S = 5$).**

    $$
    \text{P\&L} = 0.15 + \frac{1}{2}(-0.08)(5)^2 = 0.15 - 1.00 = -\$0.85
    $$

    A large move produces a substantial loss.

    **Breakeven move.** Set the gamma loss equal to the theta gain:

    $$
    \frac{1}{2}|\Gamma|(\delta S^*)^2 = \Theta \implies \frac{1}{2}(0.08)(\delta S^*)^2 = 0.15
    $$

    $$
    (\delta S^*)^2 = \frac{0.30}{0.08} = 3.75 \implies \delta S^* = \sqrt{3.75} \approx 1.94
    $$

    Any daily move exceeding approximately $\$1.94$ (or $1.94\%$ of $S_0 = 100$) causes the gamma loss to exceed the theta gain.

---

**Exercise 6.** Extend the P&L simulator to include a **long strangle** strategy. Compute and plot the P&L as a function of the final stock price for $K_1 = 90$, $K_2 = 110$, with both options having $\tau = 0.5$, $\sigma = 0.25$, $r = 0.03$. How does the profile compare to a long straddle at $K = 100$?

??? success "Solution to Exercise 6"
    Using Black--Scholes pricing with $S_0 = 100$, $r = 0.03$, $\sigma = 0.25$, and $\tau = 0.5$:

    **Long strangle:** Buy an OTM put at $K_1 = 90$ and an OTM call at $K_2 = 110$. The total cost is $P(90) + C(110)$.

    **Long straddle at $K = 100$:** Buy a call and a put at $K = 100$. The total cost is $C(100) + P(100)$.

    The P&L at expiry for each strategy is:

    - Long strangle: $\max(K_1 - S_T, 0) + \max(S_T - K_2, 0) - \text{premium}_{\text{strangle}}$
    - Long straddle: $|S_T - K| - \text{premium}_{\text{straddle}}$

    **Comparison.** The strangle is cheaper because both options are OTM, but it requires a larger move to reach profitability. The straddle has narrower breakeven points but costs more. Specifically:

    - The straddle has breakevens at $K \pm \text{premium}_{\text{straddle}}$, while the strangle has breakevens at $K_1 - \text{premium}_{\text{strangle}}$ and $K_2 + \text{premium}_{\text{strangle}}$.
    - For moves within the strangle's strikes ($90 < S_T < 110$), the straddle still generates intrinsic payoff while the strangle generates none.
    - For very large moves, both strategies converge to the same slope ($\pm 1$ per dollar of underlying move), but the straddle's P&L is shifted up by the difference in strikes minus the difference in premiums.
    - The strangle is preferred when the trader expects a very large move but wants to minimize the upfront cost and theta bleed.
