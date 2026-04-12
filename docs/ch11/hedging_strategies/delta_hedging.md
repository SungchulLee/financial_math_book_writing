# Delta Hedging


Delta hedging is the most fundamental options risk management technique: maintain a portfolio whose net delta is zero to eliminate first-order directional exposure.

---

### Principle


For a portfolio containing options, the **portfolio delta** measures total first-order sensitivity to the underlying price. A delta-neutral portfolio satisfies

$$
\boxed{\Delta_{\text{portfolio}} = 0}
$$

For a single long option with delta $\Delta$, this requires holding $-\Delta$ shares of the underlying.

---

### Static delta hedge: worked example


Suppose you hold **100 European call options** (each on 1 share) with delta $\Delta = 0.6$.

**Portfolio delta** before hedging:

$$
\Delta_{\text{portfolio}} = 100 \times 0.6 = 60
$$

**Delta-neutral hedge**: short **60 shares** of the underlying.

$$
\Delta_{\text{hedged}} = 60 - 60 = 0
$$

After hedging, a \$1 move in the stock produces approximately zero change in portfolio value (to first order).

---

### Why delta hedging is imperfect


Delta hedging eliminates only the **linear** component of price risk. The residual P&L after delta hedging comes from:

**Gamma (convexity).** The delta itself changes as $S$ moves. For a move $\delta S$:

$$
\delta V_{\text{hedged}} \approx \frac{1}{2}\Gamma(\delta S)^2
$$

This term is always positive for long options ($\Gamma > 0$), meaning the hedged portfolio benefits from large moves — but the cost is theta.

**Theta (time decay).** The Black–Scholes PDE implies:

$$
\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)
$$

For a long gamma position, theta is negative: the portfolio loses value with the passage of time if the stock doesn't move.

**Discrete rebalancing.** In practice, hedges are adjusted at discrete intervals, not continuously. The error between discrete and continuous hedging is proportional to $\Gamma \cdot \sigma^2 S^2 \cdot \Delta t$.

---

### Dynamic delta hedging


In practice, delta changes with $S$, so the hedge must be **rebalanced** over time.

**Algorithm:**

1. At time $t_0$: compute $\Delta(t_0, S_0)$, hold $-\Delta \cdot N_{\text{options}}$ shares.
2. At time $t_1$: recompute $\Delta(t_1, S_1)$, adjust share position.
3. Repeat at each rebalancing date.

**Rebalancing cost** per step is approximately $|\Delta(t_{i+1}) - \Delta(t_i)| \times S \times \text{spread}$.

The tradeoff: more frequent rebalancing reduces hedging error but increases transaction costs.

---

### P&L decomposition


Over a rebalancing period $[t, t+\Delta t]$, the delta-hedged P&L decomposes as:

$$
P\&L \approx \underbrace{\Theta\,\Delta t}_{\text{time decay}} + \underbrace{\frac{1}{2}\Gamma(\Delta S)^2}_{\text{gamma P\&L}} + \underbrace{\nu\,\Delta\sigma}_{\text{vega P\&L}}
$$

where $\Delta S = S_{t+\Delta t} - S_t$ and $\Delta\sigma$ is any change in implied volatility. This decomposition is the workhorse of options P&L attribution.

---

### Python implementation


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

### When delta hedging works well


- **Low gamma** positions: delta changes slowly, infrequent rebalancing suffices.
- **Liquid underlyings**: tight spreads keep rebalancing costs manageable.
- **Moderate time to expiry**: far from expiry, gamma is smaller and delta is more stable.

---

### When delta hedging breaks down


- **Near expiry, near the strike**: gamma blows up ($\Gamma \sim 1/(S\sigma\sqrt{\tau})$), delta changes violently.
- **Jumps in the underlying**: delta hedging assumes continuous price paths; jumps cause unhedgeable losses.
- **Illiquid markets**: wide bid-ask spreads make frequent rebalancing prohibitively expensive.
- **Large moves**: the linear approximation $\delta V \approx \Delta\,\delta S$ breaks down for moves where higher-order terms matter.

---

### What to remember


- Delta hedging removes first-order directional risk by holding $-\Delta$ shares per option.
- Residual P&L after delta hedging is driven by gamma, theta, and vega — the higher-order Greeks.
- Dynamic rebalancing is necessary because delta changes with $S$ and $t$.
- The gamma-theta tradeoff is fundamental: long gamma earns on moves but pays theta; short gamma earns theta but loses on moves.

---

## Exercises

**Exercise 1.** A trader holds 200 European put options with $\Delta_{\text{put}} = -0.40$. Compute the portfolio delta and the number of shares needed to delta-hedge. After hedging, what is the approximate P&L from a $\$2$ increase in the underlying?

??? success "Solution to Exercise 1"
    The trader holds 200 European puts with $\Delta_{\text{put}} = -0.40$ per option.

    **Portfolio delta:**

    $$
    \Delta_{\text{portfolio}} = 200 \times (-0.40) = -80
    $$

    **Shares needed to delta-hedge.** To neutralize the negative delta, the trader must buy shares. The hedge requires $+80$ shares (long 80 shares):

    $$
    \Delta_{\text{hedged}} = -80 + 80 = 0
    $$

    **P&L from a $\$2$ increase.** After delta hedging, the first-order P&L is zero. The residual comes from gamma:

    $$
    \text{P\&L} \approx \frac{1}{2}\Gamma_{\text{portfolio}}(\delta S)^2
    $$

    Since the trader is long puts, $\Gamma > 0$, so the P&L is positive but small for a $\$2$ move. Without knowing the exact gamma, the approximate P&L from the linear (delta) component alone is zero by construction.

---

**Exercise 2.** Starting with a delta-neutral position on a long call ($\Delta = 0.55$, $\Gamma = 0.03$), the underlying moves from $S = 100$ to $S = 104$. Compute: (a) the new approximate delta using $\Delta_{\text{new}} \approx \Delta + \Gamma \cdot \delta S$; (b) the number of shares the hedger must trade to rebalance; (c) the gamma P&L from this move.

??? success "Solution to Exercise 2"
    Starting position: delta-neutral on a long call with $\Delta = 0.55$, $\Gamma = 0.03$, and the underlying moves from $S = 100$ to $S = 104$, so $\delta S = 4$.

    **(a) New approximate delta:**

    $$
    \Delta_{\text{new}} \approx \Delta + \Gamma \cdot \delta S = 0.55 + 0.03 \times 4 = 0.67
    $$

    **(b) Shares to rebalance.** The initial hedge held $-0.55$ shares per option. The new delta-neutral hedge requires $-0.67$ shares per option. The hedger must sell an additional

    $$
    0.67 - 0.55 = 0.12 \text{ shares per option}
    $$

    to restore delta neutrality (i.e., short 0.12 additional shares per option).

    **(c) Gamma P&L from this move:**

    $$
    \text{Gamma P\&L} = \frac{1}{2}\Gamma(\delta S)^2 = \frac{1}{2}(0.03)(4)^2 = \frac{1}{2}(0.03)(16) = 0.24 \text{ per option}
    $$

    The positive gamma P&L reflects the convexity benefit of the long option position.

---

**Exercise 3.** The P&L decomposition gives $\text{P\&L} \approx \Theta\,\Delta t + \frac{1}{2}\Gamma(\Delta S)^2 + \nu\,\Delta\sigma$. For a delta-hedged long call with $\Theta = -0.05$/day, $\Gamma = 0.04$, $\nu = 15$, compute the daily P&L if: (a) $\Delta S = 0$, $\Delta\sigma = 0$; (b) $\Delta S = 3$, $\Delta\sigma = 0$; (c) $\Delta S = 0$, $\Delta\sigma = +0.02$.

??? success "Solution to Exercise 3"
    Given: $\Theta = -0.05$/day, $\Gamma = 0.04$, $\nu = 15$.

    **(a) $\Delta S = 0$, $\Delta\sigma = 0$:**

    $$
    \text{P\&L} = (-0.05)(1) + \frac{1}{2}(0.04)(0)^2 + 15(0) = -0.05
    $$

    Pure theta loss of $\$0.05$ per option per day.

    **(b) $\Delta S = 3$, $\Delta\sigma = 0$:**

    $$
    \text{P\&L} = (-0.05)(1) + \frac{1}{2}(0.04)(3)^2 + 15(0) = -0.05 + 0.18 = +0.13
    $$

    The gamma P&L from the move more than offsets the theta loss.

    **(c) $\Delta S = 0$, $\Delta\sigma = +0.02$:**

    $$
    \text{P\&L} = (-0.05)(1) + \frac{1}{2}(0.04)(0)^2 + 15(0.02) = -0.05 + 0.30 = +0.25
    $$

    The implied vol increase generates a vega profit that dominates the theta loss.

---

**Exercise 4.** Explain why delta hedging breaks down near expiry for ATM options. For $S = K = 100$, $\sigma = 0.20$, $\tau = 1/252$, compute the delta at $S = 99.5$ and $S = 100.5$. How many shares must the hedger trade for a $\$1$ move? Compare this to the same calculation at $\tau = 30/252$.

??? success "Solution to Exercise 4"
    For an ATM call at $S = K = 100$, $\sigma = 0.20$, the delta is computed via $\Delta = N(d_1)$ where

    $$
    d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = \frac{\frac{1}{2}\sigma^2\tau}{\sigma\sqrt{\tau}} = \frac{\sigma\sqrt{\tau}}{2}
    $$

    (using $r \approx 0$ for simplicity and $S = K$).

    **At $\tau = 1/252$ (1 day):** $\sigma\sqrt{\tau} = 0.20\sqrt{1/252} = 0.20 \times 0.0630 = 0.01260$.

    - At $S = 99.5$: $d_1 = \frac{\ln(99.5/100)}{0.01260} + \frac{0.01260}{2} \approx \frac{-0.00501}{0.01260} + 0.0063 = -0.3976 + 0.0063 = -0.391$, so $\Delta(99.5) = N(-0.391) \approx 0.348$.
    - At $S = 100.5$: $d_1 = \frac{\ln(100.5/100)}{0.01260} + 0.0063 \approx \frac{0.00499}{0.01260} + 0.0063 = 0.396 + 0.0063 = 0.402$, so $\Delta(100.5) = N(0.402) \approx 0.656$.

    The delta changes by $0.656 - 0.348 = 0.308$ for a $\$1$ move. For 100 options, the hedger must trade approximately $30.8$ shares.

    **At $\tau = 30/252$:** $\sigma\sqrt{\tau} = 0.20\sqrt{30/252} = 0.20 \times 0.3450 = 0.06901$.

    - At $S = 99.5$: $d_1 \approx \frac{-0.00501}{0.06901} + 0.0345 = -0.0726 + 0.0345 = -0.0381$, so $\Delta(99.5) \approx N(-0.038) \approx 0.485$.
    - At $S = 100.5$: $d_1 \approx \frac{0.00499}{0.06901} + 0.0345 = 0.0723 + 0.0345 = 0.107$, so $\Delta(100.5) \approx N(0.107) \approx 0.543$.

    The delta changes by only $0.543 - 0.485 = 0.058$ for the same $\$1$ move, requiring only about $5.8$ shares traded per 100 options.

    **Conclusion.** Near expiry, gamma is approximately $\frac{0.308}{1} = 0.308$ versus $\frac{0.058}{1} = 0.058$ at 30 days. The near-expiry gamma is over $5\times$ larger, making the delta extremely unstable and forcing costly, frequent rebalancing. This is why delta hedging breaks down near expiry for ATM options.

---

**Exercise 5.** A portfolio manager holds a delta-neutral book with $\Gamma = 5.0$ (portfolio) and $\Theta = -0.80$/day. Using the theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$, and assuming the delta-neutral book has $V - S\Delta \approx 0$, verify the consistency of $\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma$ with $S = 100$ and $\sigma = 0.20$.

??? success "Solution to Exercise 5"
    The theta-gamma identity for a delta-neutral portfolio ($\Delta = 0$) with $V - S\Delta \approx 0$ gives:

    $$
    \Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    Substituting $S = 100$, $\sigma = 0.20$, $\Gamma = 5.0$:

    $$
    -\frac{1}{2}(0.20)^2(100)^2(5.0) = -\frac{1}{2}(0.04)(10000)(5.0) = -\frac{1}{2}(2000) = -1000 \text{ per year}
    $$

    Converting to daily theta (dividing by 252 trading days):

    $$
    \Theta_{\text{daily}} \approx \frac{-1000}{252} \approx -3.97 \text{ per day}
    $$

    Wait --- the given theta is $\Theta = -0.80$/day. Let us check whether the stated values are portfolio-level or per-option. If $\Gamma = 5.0$ is the total portfolio gamma and $\Theta = -0.80$/day is the total portfolio theta, then the identity predicts $|\Theta_{\text{daily}}| \approx 3.97$, which is larger than $0.80$.

    The discrepancy arises because the assumption $V - S\Delta \approx 0$ is an approximation. For a portfolio with nonzero net option value, the right-hand side $r(V - S\Delta)$ contributes a correction. Alternatively, if the portfolio gamma is expressed per unit (not total) or the convention differs, the magnitudes may align. The key point is that the identity confirms the **sign** relationship: positive gamma necessitates negative theta, and the magnitudes are linked through $\sigma^2 S^2$. The stated values are consistent in sign but the exact magnitudes depend on the $r(V - S\Delta)$ term that was approximated as zero.

---

**Exercise 6.** Modify the Python delta-hedging code to rebalance only when the delta deviation exceeds a threshold of $0.05$ (i.e., only trade when $|\Delta_{\text{new}} - \Delta_{\text{current}}| > 0.05$). Simulate 1000 paths and compare the hedged P&L standard deviation with the continuous rebalancing strategy. How much does the threshold reduce the number of trades?

??? success "Solution to Exercise 6"
    This is a computational exercise. The key steps are:

    1. **Simulate 1000 GBM paths** for the underlying over the option's life with daily steps.
    2. **Continuous rebalancing strategy:** At each time step, compute $\Delta(t_i, S_i)$ using Black--Scholes and adjust the share position.
    3. **Threshold rebalancing strategy:** Only adjust shares when $|\Delta_{\text{new}} - \Delta_{\text{current}}| > 0.05$.

    For each path, the hedging P&L is:

    $$
    \text{P\&L} = \text{option payoff} - \text{premium received} - \sum_{i} (\Delta_{i} - \Delta_{i-1})(S_i)
    $$

    **Expected results:**

    - The continuous strategy has lower P&L standard deviation because the hedge is always up to date.
    - The threshold strategy produces moderately higher P&L volatility (perhaps 10--30% more, depending on parameters) but significantly fewer trades.
    - For typical parameters ($\sigma = 0.20$, daily rebalancing, $\tau = 1$ year with 252 steps), continuous rebalancing requires 252 trades per path. The threshold strategy might require 100--150 trades (a reduction of 40--60%), with the savings concentrated during low-volatility periods when delta changes slowly.
    - The trade reduction is most significant when the underlying is far from the strike (delta is flat and changes slowly) and least significant near the strike close to expiry (where gamma is high and delta moves rapidly).
