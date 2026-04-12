# Gamma and Vega Hedging


Delta hedging removes linear price risk but leaves the portfolio exposed to gamma (convexity) and vega (volatility) risks. Neutralizing these requires trading additional options.

---

### Gamma hedging


#### Why gamma matters

After delta hedging, the residual P&L over an interval is

$$
P\&L_{\text{hedged}} \approx \frac{1}{2}\Gamma(\delta S)^2 + \Theta\,\delta t
$$

If $\Gamma$ is large, even moderate price moves create significant P&L swings. **Gamma hedging** seeks

$$
\boxed{\Gamma_{\text{portfolio}} = 0}
$$

#### Mechanics

Since the underlying asset has $\Gamma = 0$ (its price is linear in itself), gamma can only be hedged with **other options**.

**Worked example.** You are long 100 calls with per-option $\Gamma_{\text{call}} = 0.04$.

Total gamma: $100 \times 0.04 = 4.0$.

To neutralize, find another option (e.g., an ATM put) with $\Gamma_{\text{put}} = 0.05$. Short

$$
n = \frac{4.0}{0.05} = 80 \text{ puts}
$$

After adding 80 short puts:

$$
\Gamma_{\text{portfolio}} = 4.0 - 80 \times 0.05 = 0
$$

**Important.** Adding the puts changes the portfolio delta, so you must **re-delta-hedge** after the gamma adjustment.

#### Sequential hedging procedure

1. **Gamma-neutralize** using options (match $\Gamma$ with opposite-sign option positions).
2. **Re-delta-hedge** using shares to restore $\Delta_{\text{portfolio}} = 0$.

This order matters: adjusting gamma with options changes delta, but adjusting delta with shares does not affect gamma.

---

### Vega hedging


#### Why vega matters

In real markets, implied volatility changes over time. A portfolio with net vega exposure gains or loses value as implied vol shifts:

$$
\delta V \approx \nu \cdot \delta\sigma_{\text{implied}}
$$

A **vega-neutral** portfolio satisfies

$$
\boxed{\nu_{\text{portfolio}} = 0}
$$

#### Mechanics

Like gamma, vega can only be hedged with **other options** (the underlying has zero vega). Vega hedging typically involves:

- **Buying/selling options** at different strikes or maturities to offset net vega.
- **Variance swaps**: provide direct exposure to realized variance, useful for hedging aggregate vega.
- **VIX options/futures**: trade implied volatility directly (for equity index portfolios).

#### Vega-gamma interaction

In Black–Scholes, vega and gamma are proportional:

$$
\nu = \sigma S^2 \tau\,\Gamma
$$

This means gamma-hedging automatically addresses vega in the Black–Scholes world. However, in practice (stochastic volatility, term structure effects), vega and gamma are **not perfectly correlated**, and separate hedging is required.

---

### Joint gamma-vega hedging


When both gamma and vega must be neutralized, you need **at least two option instruments** (in addition to the underlying for delta). This creates a system of equations:

$$
\begin{cases}
n_1 \Gamma_1 + n_2 \Gamma_2 = -\Gamma_{\text{existing}} \\
n_1 \nu_1 + n_2 \nu_2 = -\nu_{\text{existing}}
\end{cases}
$$

Solve for $n_1, n_2$, then re-delta-hedge with shares.

**Example.** Existing portfolio: $\Gamma = +4$, $\nu = +200$.

Available instruments:
- Option A: $\Gamma_A = 0.05$, $\nu_A = 3.0$
- Option B: $\Gamma_B = 0.02$, $\nu_B = 5.0$

Solve:

$$
\begin{pmatrix} 0.05 & 0.02 \\ 3.0 & 5.0 \end{pmatrix}
\begin{pmatrix} n_1 \\ n_2 \end{pmatrix}
= \begin{pmatrix} -4 \\ -200 \end{pmatrix}
$$

yielding the required positions in options A and B.

---

### The gamma-theta tradeoff


Gamma and theta are fundamentally linked through the Black–Scholes PDE:

$$
\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)
$$

This implies:

| Position | Gamma | Theta | Interpretation |
|---|---|---|---|
| **Long options** | $\Gamma > 0$ | $\Theta < 0$ | Benefit from moves, pay time decay |
| **Short options** | $\Gamma < 0$ | $\Theta > 0$ | Earn time decay, lose on moves |

You cannot have both positive gamma and positive theta simultaneously (in Black–Scholes). This tradeoff is the central tension in options portfolio management.

---

### Short gamma strategies


#### Concept

Sell options to earn theta income while dynamically delta-hedging to manage directional risk. This is a **short volatility** strategy.

#### Mechanics

1. **Sell short-dated ATM options** (high theta, high gamma).
2. **Delta-hedge frequently** to keep directional risk near zero.
3. **Profit source**: theta accumulation when realized volatility is below implied.
4. **Loss source**: gamma losses when large moves force unfavorable hedge adjustments.

#### P&L structure

- **Profit = theta earned** (positive, accrues daily).
- **Loss = gamma cost** from rebalancing: approximately $\frac{1}{2}|\Gamma|(\Delta S)^2$ per move.
- **Net P&L** depends on whether realized vol exceeds or falls below implied vol.

#### Risk profile

Short gamma means the position's delta moves **against** you:

| When underlying rises | Delta decreases (you get shorter) |
|---|---|
| When underlying falls | Delta increases (you get longer) |

This forces the hedger to **buy high and sell low** when rebalancing — the fundamental cost of short gamma.

#### When to use

- Market expected to remain range-bound (low realized vol).
- Fast execution capability for frequent rebalancing.
- Willingness to accept tail risk, or protective wings purchased to cap extreme losses.

---

### Python: computing hedge quantities


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

### What to remember


- Gamma can only be hedged with options, not with the underlying.
- After gamma-hedging with options, the portfolio must be re-delta-hedged with shares.
- The gamma-theta tradeoff is fundamental: you cannot simultaneously be long gamma and long theta.
- Short gamma earns theta but requires frequent rebalancing and exposes the portfolio to large moves.
- Joint gamma-vega hedging requires at least two option instruments plus shares.

---

## Exercises

**Exercise 1.** A portfolio has $\Gamma = +3.0$ and $\Delta = +45$. An ATM put with $\Gamma_{\text{put}} = 0.04$ and $\Delta_{\text{put}} = -0.50$ is available for gamma hedging. Compute: (a) the number of puts to short for gamma neutrality; (b) the new portfolio delta after adding the puts; (c) the number of shares to trade for delta neutrality.

??? success "Solution to Exercise 1"
    The portfolio has $\Gamma = +3.0$ and $\Delta = +45$. The hedging put has $\Gamma_{\text{put}} = 0.04$ and $\Delta_{\text{put}} = -0.50$.

    **(a) Number of puts to short for gamma neutrality:**

    $$
    n_{\text{put}} = -\frac{\Gamma_{\text{portfolio}}}{\Gamma_{\text{put}}} = -\frac{3.0}{0.04} = -75
    $$

    Short 75 puts.

    **(b) New portfolio delta after adding the puts:**

    $$
    \Delta_{\text{new}} = 45 + (-75)(-0.50) = 45 + 37.5 = 82.5
    $$

    **(c) Shares to trade for delta neutrality.** Short 82.5 shares of the underlying:

    $$
    \Delta_{\text{final}} = 82.5 - 82.5 = 0
    $$

    The final portfolio is both gamma-neutral and delta-neutral.

---

**Exercise 2.** Using the formula $\nu = \sigma S^2 \tau \Gamma$ in Black--Scholes, verify that gamma-hedging an ATM option with another ATM option at the same maturity automatically hedges vega. Why does this relationship break down when the hedging option has a different maturity?

??? success "Solution to Exercise 2"
    In Black--Scholes, the relationship is $\nu = \sigma S^2 \tau \Gamma$. For two ATM options at the same maturity $\tau$ and the same underlying $S$, both options share the same $\sigma$, $S$, and $\tau$.

    If we gamma-hedge using Option B to neutralize Option A's gamma:

    $$
    n_B \Gamma_B = -\Gamma_A
    $$

    The resulting vega is:

    $$
    \nu_A + n_B \nu_B = \sigma S^2 \tau \Gamma_A + n_B \sigma S^2 \tau \Gamma_B = \sigma S^2 \tau (\Gamma_A + n_B \Gamma_B) = \sigma S^2 \tau \cdot 0 = 0
    $$

    So gamma-hedging automatically hedges vega when both options are at the same maturity.

    **Why this breaks down for different maturities.** If the hedging option has maturity $\tau'$ instead of $\tau$, then $\nu_B = \sigma S^2 \tau' \Gamma_B$. The resulting vega after gamma-hedging is:

    $$
    \sigma S^2 \tau \Gamma_A + n_B \sigma S^2 \tau' \Gamma_B = \sigma S^2 (\tau \Gamma_A + \tau' n_B \Gamma_B) = \sigma S^2 (\tau - \tau') \Gamma_A \neq 0
    $$

    since $n_B \Gamma_B = -\Gamma_A$, giving $\sigma S^2 \tau \Gamma_A - \sigma S^2 \tau' \Gamma_A = \sigma S^2 (\tau - \tau')\Gamma_A$. The proportionality constant $\tau$ differs between the two options, so gamma neutrality no longer implies vega neutrality.

---

**Exercise 3.** Solve the joint gamma-vega hedging system for: existing portfolio $\Gamma = +4$, $\nu = +200$; Option A: $\Gamma_A = 0.05$, $\nu_A = 3.0$; Option B: $\Gamma_B = 0.02$, $\nu_B = 5.0$. Find the positions $n_1$, $n_2$ in Options A and B that neutralize both gamma and vega.

??? success "Solution to Exercise 3"
    The system of equations is:

    $$
    \begin{cases} 0.05\,n_1 + 0.02\,n_2 = -4 \\ 3.0\,n_1 + 5.0\,n_2 = -200 \end{cases}
    $$

    From the first equation: $n_1 = \frac{-4 - 0.02\,n_2}{0.05} = -80 - 0.4\,n_2$.

    Substituting into the second equation:

    $$
    3.0(-80 - 0.4\,n_2) + 5.0\,n_2 = -200
    $$

    $$
    -240 - 1.2\,n_2 + 5.0\,n_2 = -200
    $$

    $$
    3.8\,n_2 = 40 \implies n_2 = \frac{40}{3.8} \approx 10.526
    $$

    $$
    n_1 = -80 - 0.4(10.526) = -80 - 4.211 \approx -84.211
    $$

    **Verification:**

    - Gamma: $0.05(-84.211) + 0.02(10.526) = -4.211 + 0.211 = -4.0$ (neutralizes $\Gamma = +4$)
    - Vega: $3.0(-84.211) + 5.0(10.526) = -252.63 + 52.63 = -200.0$ (neutralizes $\nu = +200$)

    The trader should short approximately 84.2 units of Option A and go long approximately 10.5 units of Option B, then re-delta-hedge with shares.

---

**Exercise 4.** A short gamma strategy sells 50 ATM calls ($\Gamma = -0.04$ per option, $\Theta = +0.08$ per option per day) and delta-hedges daily. Compute: (a) the portfolio gamma and daily theta income; (b) the breakeven daily move $|\Delta S|^*$ such that $\frac{1}{2}|\Gamma_{\text{port}}|(\Delta S^*)^2 = \Theta_{\text{port}} \cdot 1\text{ day}$; (c) the implied daily volatility corresponding to this breakeven move.

??? success "Solution to Exercise 4"
    The trader sells 50 ATM calls with per-option $\Gamma = -0.04$ and $\Theta = +0.08$/day.

    **(a) Portfolio gamma and daily theta income:**

    $$
    \Gamma_{\text{port}} = 50 \times (-0.04) = -2.0
    $$

    $$
    \Theta_{\text{port}} = 50 \times 0.08 = +4.0 \text{ per day}
    $$

    **(b) Breakeven daily move.** Setting gamma loss equal to theta income:

    $$
    \frac{1}{2}|\Gamma_{\text{port}}|(\Delta S^*)^2 = \Theta_{\text{port}}
    $$

    $$
    \frac{1}{2}(2.0)(\Delta S^*)^2 = 4.0
    $$

    $$
    (\Delta S^*)^2 = 4.0 \implies \Delta S^* = 2.0
    $$

    The breakeven daily move is $\$2.00$.

    **(c) Implied daily volatility.** If the underlying is at $S = 100$ (typical for ATM), the breakeven move as a percentage is $2.0/100 = 2.0\%$. The annualized volatility corresponding to a daily move of $2\%$ is:

    $$
    \sigma_{\text{annual}} = 0.02 \times \sqrt{252} \approx 0.02 \times 15.87 \approx 31.7\%
    $$

    The strategy is profitable when the realized daily volatility is below $2\%$ (annualized $\approx 31.7\%$).

---

**Exercise 5.** Explain why the order of operations matters: gamma-hedge first with options, then delta-hedge with shares. What goes wrong if you delta-hedge first and then gamma-hedge? Specifically, does adding options after delta-hedging with shares change the delta?

??? success "Solution to Exercise 5"
    **Order: gamma-hedge first, then delta-hedge.**

    - Step 1 (gamma-hedge with options): Adding options changes both the gamma and the delta of the portfolio.
    - Step 2 (delta-hedge with shares): Adding shares changes the delta but does not affect gamma (shares have $\Gamma = 0$).

    This sequence works because the delta adjustment in Step 2 does not undo the gamma neutralization achieved in Step 1.

    **What goes wrong in the reverse order:**

    - Step 1 (delta-hedge with shares): The portfolio is delta-neutral but still has nonzero gamma.
    - Step 2 (gamma-hedge with options): Adding options changes gamma toward zero, but also changes delta away from zero. The delta hedge from Step 1 is now invalidated.

    The trader would need to go back and re-delta-hedge with shares, making the initial delta hedge redundant. If the trader does not re-delta-hedge after Step 2, the portfolio has the correct gamma but incorrect delta.

    In summary: adding options always changes delta, so delta-hedging must come last. Adding shares never changes gamma, so the gamma hedge is preserved regardless of subsequent share trades.

---

**Exercise 6.** A portfolio has the following Greeks: $\Delta = 100$, $\Gamma = 6.0$, $\nu = 350$, $\Theta = -1.20$/day. Only one hedging option is available with $\Delta_H = 0.55$, $\Gamma_H = 0.04$, $\nu_H = 2.8$. The trader can gamma-hedge but not simultaneously vega-hedge. Compute the position in the hedging option for gamma neutrality, the resulting net vega, and discuss whether the residual vega exposure is acceptable.

??? success "Solution to Exercise 6"
    The portfolio has $\Gamma = 6.0$ and the hedging option has $\Gamma_H = 0.04$, $\nu_H = 2.8$, $\Delta_H = 0.55$.

    **Position for gamma neutrality:**

    $$
    n_H = -\frac{\Gamma_{\text{port}}}{\Gamma_H} = -\frac{6.0}{0.04} = -150
    $$

    Short 150 units of the hedging option.

    **Resulting net vega:**

    $$
    \nu_{\text{new}} = 350 + (-150)(2.8) = 350 - 420 = -70
    $$

    The portfolio goes from long vega ($+350$) to short vega ($-70$). The gamma hedge overshoots the vega neutralization because the hedging option's vega-to-gamma ratio ($2.8/0.04 = 70$) exceeds the portfolio's vega-to-gamma ratio ($350/6.0 \approx 58.3$).

    **Resulting delta (before share hedge):**

    $$
    \Delta_{\text{new}} = 100 + (-150)(0.55) = 100 - 82.5 = 17.5
    $$

    The trader then shorts 17.5 shares to restore delta neutrality.

    **Acceptability of residual vega.** The residual $\nu = -70$ means the portfolio loses $\$70$ for each 1 percentage point increase in implied volatility. Whether this is acceptable depends on:

    - The magnitude relative to the portfolio value and risk limits.
    - The trader's view on volatility direction (if they expect vol to decline, short vega is tolerable).
    - The volatility regime: in a low-vol environment, the risk of a vol spike may make this exposure unacceptable.

    If the residual vega is too large, the trader needs a second hedging instrument to independently target vega, creating the two-instrument system required for joint gamma-vega neutralization.
