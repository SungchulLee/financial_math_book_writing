# Gamma Risk and Convexity Effects


For a small move $\delta S$,

$$
\delta V \approx \Delta\,\delta S + \frac{1}{2}\Gamma(\delta S)^2
$$


Delta-hedging removes the linear term, leaving

$$
\boxed{\delta V_{\text{delta-hedged}}\approx \frac{1}{2}\Gamma(\delta S)^2}
$$


Thus gamma exposure links delta-hedged P&L to realized variance.

---

## Continuous-time P&L decomposition


For a delta-hedged option position over time interval $[t, t+dt]$, the instantaneous P&L is:

$$
dP\&L = dV - \Delta \, dS
$$

Using Itô's lemma on $V(t,S)$:

$$
dV = \Theta \, dt + \Delta \, dS + \frac{1}{2}\Gamma (dS)^2
$$

After delta-hedging:

$$
\boxed{dP\&L_{\text{hedged}} = \Theta \, dt + \frac{1}{2}\Gamma (dS)^2}
$$

Since $(dS)^2 = \sigma^2 S^2 dt$ (in expectation):

$$
\mathbb{E}[dP\&L_{\text{hedged}}] = \left(\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma\right) dt
$$

By the Black–Scholes PDE, this equals $r(V - S\Delta)dt$, the cost of financing.

---

## Theta-gamma relationship


The fundamental identity:

$$
\boxed{\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)}
$$

**Interpretation:**

- Long gamma positions earn from realized volatility ($\frac{1}{2}\Gamma(dS)^2$)
- But pay theta (time decay) to maintain the position
- These exactly offset when realized vol equals implied vol

**For ATM options:**

$$
\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma
$$

since $V - S\Delta \approx 0$ for ATM.

---

## Gamma P&L over discrete intervals


Over a finite interval $\Delta t$, with spot move $\Delta S = S_{t+\Delta t} - S_t$:

$$
P\&L_{\text{hedged}} \approx \Theta \Delta t + \frac{1}{2}\Gamma (\Delta S)^2
$$

In terms of returns $R = \Delta S/S$:

$$
P\&L_{\text{hedged}} \approx \Theta \Delta t + \frac{1}{2}\Gamma S^2 R^2
$$

**Expected P&L** (assuming correct model):

$$
\mathbb{E}[P\&L_{\text{hedged}}] = \Theta \Delta t + \frac{1}{2}\Gamma S^2 \sigma^2 \Delta t = r(V - S\Delta)\Delta t
$$

**Variance of P&L:**

$$
\text{Var}(P\&L_{\text{hedged}}) \approx \frac{1}{2}\Gamma^2 S^4 \sigma^4 \Delta t^2
$$

(using $\text{Var}(R^2) \approx 2\sigma^4 \Delta t$ for normal returns)

---

## Long gamma vs short gamma


**Long gamma** (positive $\Gamma$):

- Benefits from large moves: $\frac{1}{2}\Gamma(\Delta S)^2 > 0$
- Pays theta: $\Theta < 0$ typically
- Profits when realized volatility exceeds implied volatility
- "Buy low, sell high" rebalancing: as $S$ rises, sell; as $S$ falls, buy

**Short gamma** (negative $\Gamma$):

- Earns theta: $\Theta > 0$ (collecting premium)
- Loses on large moves: $\frac{1}{2}\Gamma(\Delta S)^2 < 0$
- Profits when realized volatility is below implied volatility
- "Buy high, sell low" rebalancing: adverse rebalancing

---

## Realized vs implied volatility trading


The P&L from delta-hedging over $[0,T]$ is:

$$
P\&L = \frac{1}{2}\int_0^T \Gamma(t,S_t) S_t^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2) dt
$$

where $\sigma_{\text{realized}}^2 dt = (dS/S)^2$ is instantaneous realized variance.

**Trading strategy:**

- If you expect $\sigma_{\text{realized}} > \sigma_{\text{implied}}$: buy options (long gamma)
- If you expect $\sigma_{\text{realized}} < \sigma_{\text{implied}}$: sell options (short gamma)

---

## Dollar gamma


Practitioners often use **dollar gamma**:

$$
\Gamma_{\$} = \frac{1}{2}\Gamma S^2
$$

This measures the dollar P&L from a 1% move:

$$
P\&L \approx \Gamma_{\$} \cdot (R \times 100)^2 / 10000 = \Gamma_{\$} R^2
$$

---

## Numerical example


Consider an ATM call with $S = K = 100$, $\sigma = 20\%$, $\tau = 30$ days, $r = 5\%$:

- $\Gamma = 0.055$
- $\Theta = -0.044$ per day
- $\Gamma_{\$} = \frac{1}{2} \times 0.055 \times 100^2 = 275$

**Scenario: 2% daily move**

$$
\text{Gamma P&L} = \frac{1}{2} \times 0.055 \times (2)^2 = 0.11
$$

$$
\text{Theta P&L} = -0.044
$$

$$
\text{Net P&L} = 0.11 - 0.044 = 0.066
$$

The position profits because the realized move (2%) exceeds the implied daily vol ($\sigma\sqrt{1/252} \approx 1.26\%$).

---

## What to remember


- Long gamma benefits from volatility (large squared moves)
- Short gamma earns carry but is exposed to large moves
- Theta and gamma are linked: $\Theta + \frac{1}{2}\sigma^2 S^2\Gamma = r(V - S\Delta)$
- Delta-hedged P&L depends on realized vs implied volatility
- Dollar gamma $\Gamma_{\$} = \frac{1}{2}\Gamma S^2$ measures dollar exposure to variance

---

## Exercises

**Exercise 1.** For an ATM put with $S = K = 100$, $\sigma = 0.25$, $\tau = 60/252$, $r = 0.03$, compute $\Gamma$, $\Theta$, and dollar gamma $\Gamma_{\$}$. Verify the theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = r(V - S\Delta)$ using the Black--Scholes put price and delta.

??? success "Solution to Exercise 1"
    We use the Black--Scholes formulas for an ATM put with $S = K = 100$, $\sigma = 0.25$, $\tau = 60/252 \approx 0.2381$, $r = 0.03$.

    First compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)\tau}{\sigma\sqrt{\tau}} = \frac{(0.03 + 0.03125)(0.2381)}{0.25\sqrt{0.2381}} = \frac{0.01460}{0.12191} \approx 0.1198
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{\tau} = 0.1198 - 0.12191 \approx -0.0021
    $$

    **Gamma** (same for puts and calls):

    $$
    \Gamma = \frac{\phi(d_1)}{S\sigma\sqrt{\tau}} = \frac{0.3953}{100 \times 0.25 \times 0.4880} \approx 0.0324
    $$

    **Theta** for a put:

    $$
    \Theta_{\text{put}} = -\frac{S\sigma\phi(d_1)}{2\sqrt{\tau}} + rKe^{-r\tau}N(-d_2) \approx -\frac{100 \times 0.25 \times 0.3953}{2 \times 0.4880} + 0.03 \times 100 \times 0.9929 \times 0.5008
    $$

    $$
    \Theta_{\text{put}} \approx -10.146 + 1.491 \approx -8.655 \text{ per year} \approx -0.0344 \text{ per day}
    $$

    **Dollar gamma:**

    $$
    \Gamma_{\$} = \frac{1}{2}\Gamma S^2 = \frac{1}{2}(0.0324)(10000) = 162
    $$

    **Verification of theta-gamma identity.** The Black--Scholes put price is approximately $P \approx 3.64$ and the put delta is $\Delta_{\text{put}} = N(d_1) - 1 \approx -0.4523$.

    $$
    \Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = -8.655 + \frac{1}{2}(0.0625)(10000)(0.0324) = -8.655 + 10.125 = 1.470
    $$

    $$
    r(V - S\Delta) = 0.03(3.64 - 100 \times (-0.4523)) = 0.03(3.64 + 45.23) = 0.03(48.87) = 1.466
    $$

    These are approximately equal (the small difference is due to rounding), confirming the identity.

---

**Exercise 2.** A trader is long gamma with $\Gamma = 0.06$ and pays daily theta of $\$0.05$. If the realized daily move is $|\Delta S| = 1.5$, compute the gamma P&L and the net daily P&L. What is the minimum daily move needed for the position to break even?

??? success "Solution to Exercise 2"
    The gamma P&L from a move $|\Delta S| = 1.5$ is:

    $$
    \text{Gamma P\&L} = \frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2}(0.06)(1.5)^2 = \frac{1}{2}(0.06)(2.25) = 0.0675
    $$

    The net daily P&L is:

    $$
    \text{Net P\&L} = \text{Gamma P\&L} - |\Theta| = 0.0675 - 0.05 = 0.0175
    $$

    The position is profitable because the gamma gain exceeds the theta cost.

    For breakeven, we need:

    $$
    \frac{1}{2}\Gamma(\Delta S_{\text{BE}})^2 = |\Theta|
    $$

    $$
    (\Delta S_{\text{BE}})^2 = \frac{2|\Theta|}{\Gamma} = \frac{2(0.05)}{0.06} = \frac{5}{3} \approx 1.6667
    $$

    $$
    |\Delta S_{\text{BE}}| = \sqrt{5/3} \approx 1.291
    $$

    The stock must move at least $\$1.29$ per day for the long gamma position to break even.

---

**Exercise 3.** The hedging P&L identity states $\text{P\&L} = \frac{1}{2}\int_0^T \Gamma(t,S_t)S_t^2(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,dt$. If a trader sells an ATM call at $\sigma_{\text{implied}} = 0.25$ and realized volatility turns out to be $\sigma_{\text{realized}} = 0.20$, estimate the cumulative P&L using $\Gamma \approx 0.03$, $S = 100$, $T = 0.5$.

??? success "Solution to Exercise 3"
    The trader sells the call (short gamma, $\Gamma < 0$ from the trader's perspective), so the hedging P&L for the seller is:

    $$
    \text{P\&L} = -\frac{1}{2}\int_0^T \Gamma(t,S_t)S_t^2(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,dt
    $$

    where the negative sign reflects the short position. Using the constant approximations $\Gamma \approx 0.03$, $S \approx 100$, and $T = 0.5$:

    $$
    \sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2 = 0.20^2 - 0.25^2 = 0.04 - 0.0625 = -0.0225
    $$

    The long-gamma (buyer's) P&L would be:

    $$
    \frac{1}{2}(0.03)(10000)(-0.0225)(0.5) = 150 \times (-0.0225) \times 0.5 = -1.6875
    $$

    Since the trader is short, their P&L is:

    $$
    \text{P\&L}_{\text{seller}} = +1.6875
    $$

    The seller profits approximately $\$1.69$ because realized volatility ($20\%$) was below the implied volatility ($25\%$) at which the option was sold. This is the essence of a short volatility strategy: collecting premium when realized vol is lower than implied vol.

---

**Exercise 4.** Explain the "buy low, sell high" rebalancing pattern for a long gamma position. If a delta-neutral trader is long calls with $\Gamma = 0.04$ and the stock rises from $100$ to $105$, by how much does delta change? Does the trader buy or sell shares to rebalance, and at what price level?

??? success "Solution to Exercise 4"
    A long gamma position has $\Gamma > 0$, meaning the option's delta increases as the stock rises and decreases as the stock falls. When the trader is delta-neutral:

    - **Stock rises**: Delta increases, so the portfolio becomes net long. The trader must **sell shares** to return to delta-neutral, selling at the higher price.
    - **Stock falls**: Delta decreases, so the portfolio becomes net short. The trader must **buy shares** to return to delta-neutral, buying at the lower price.

    This creates a natural "buy low, sell high" pattern that generates P&L proportional to $(\Delta S)^2$.

    For the specific scenario with $\Gamma = 0.04$ and a move from $100$ to $105$:

    $$
    \Delta\text{(delta change)} = \Gamma \times \Delta S = 0.04 \times 5 = 0.20
    $$

    The delta increases by $0.20$ (i.e., 20 shares per option contract). Since the trader was delta-neutral and is now long delta, the trader must **sell 0.20 units of stock** (per unit of option) to rebalance. The shares are sold at $S = 105$, which is above the initial price -- illustrating the favorable "sell high" rebalancing.

    The approximate gamma P&L from this move is:

    $$
    \text{Gamma P\&L} = \frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2}(0.04)(25) = 0.50
    $$

---

**Exercise 5.** Dollar gamma is defined as $\Gamma_{\$} = \frac{1}{2}\Gamma S^2$. For a portfolio with $\Gamma_{\$} = 500$, compute the P&L from a $1\%$ daily return, a $2\%$ daily return, and a $5\%$ daily return. Show that the P&L is quadratic in the return and identify the coefficient.

??? success "Solution to Exercise 5"
    Dollar gamma is $\Gamma_{\$} = \frac{1}{2}\Gamma S^2 = 500$. The P&L from a return $R$ is:

    $$
    \text{P\&L} = \Gamma_{\$} \cdot R^2
    $$

    **For a 1% return** ($R = 0.01$):

    $$
    \text{P\&L} = 500 \times (0.01)^2 = 500 \times 0.0001 = 0.05
    $$

    **For a 2% return** ($R = 0.02$):

    $$
    \text{P\&L} = 500 \times (0.02)^2 = 500 \times 0.0004 = 0.20
    $$

    **For a 5% return** ($R = 0.05$):

    $$
    \text{P\&L} = 500 \times (0.05)^2 = 500 \times 0.0025 = 1.25
    $$

    The P&L is quadratic in $R$: $\text{P\&L} = 500 \cdot R^2$. The coefficient is $\Gamma_{\$} = 500$. The quadratic scaling means that a 5% move produces 25 times the P&L of a 1% move, not 5 times. This convexity is the defining feature of gamma exposure.

---

**Exercise 6.** Compare the risk profiles of two portfolios: (A) long 100 ATM calls with $\tau = 1$ month; (B) long 100 ATM calls with $\tau = 6$ months. Both are delta-hedged. Using the scaling laws ($\Gamma \sim \tau^{-1/2}$, $\Theta \sim -\tau^{-1/2}$), determine which portfolio has (a) higher daily P&L volatility; (b) higher daily theta bleed; (c) higher sensitivity to a volatility change of $+2\%$.

??? success "Solution to Exercise 6"
    Using the ATM scaling laws $\Gamma \sim 1/(\sigma S \sqrt{2\pi\tau})$ and $\Theta \sim -\sigma S/(2\sqrt{2\pi\tau})$:

    Let $\tau_A = 1/12$ (1 month) and $\tau_B = 6/12 = 0.5$ (6 months). The ratio $\sqrt{\tau_B/\tau_A} = \sqrt{6} \approx 2.449$.

    **(a) Daily P&L volatility.** The delta-hedged P&L variance per day is proportional to $\Gamma^2 S^4 \sigma^4 (\Delta t)^2$. Since $\Gamma \sim \tau^{-1/2}$:

    $$
    \frac{\text{P\&L vol}_A}{\text{P\&L vol}_B} = \frac{\Gamma_A}{\Gamma_B} = \sqrt{\frac{\tau_B}{\tau_A}} = \sqrt{6} \approx 2.45
    $$

    **Portfolio A has higher daily P&L volatility** by a factor of about 2.45. Short-dated options have higher gamma, leading to larger daily fluctuations.

    **(b) Daily theta bleed.** Since $\Theta \sim -\tau^{-1/2}$:

    $$
    \frac{|\Theta_A|}{|\Theta_B|} = \sqrt{\frac{\tau_B}{\tau_A}} = \sqrt{6} \approx 2.45
    $$

    **Portfolio A has higher daily theta bleed** by the same factor. The theta-gamma relationship ensures that higher gamma comes with proportionally higher time decay.

    **(c) Sensitivity to volatility change.** The vega of an ATM option scales as $\nu \sim S\sqrt{\tau}$, so:

    $$
    \frac{\nu_B}{\nu_A} = \sqrt{\frac{\tau_B}{\tau_A}} = \sqrt{6} \approx 2.45
    $$

    **Portfolio B has higher sensitivity to a volatility change** by a factor of about 2.45. Longer-dated options have more vega exposure, making them more sensitive to shifts in implied volatility.
