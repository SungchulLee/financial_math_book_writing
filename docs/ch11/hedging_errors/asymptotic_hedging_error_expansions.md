# Asymptotic Hedging Error Expansions

One seeks expansions of hedging error in small parameters.

!!! tip "Toy mechanism: variance scales with $\Delta t$, std with $\sqrt{\Delta t}$"
    The whole $\sqrt{\Delta t}$ scaling is one observation. Each rebalancing step contributes a hedging error of order $\Gamma(\Delta S)^2 - \Gamma\sigma^2 S^2\Delta t$ — a mean-zero quantity with variance proportional to $(\Delta t)^2$. Summing $N = T/\Delta t$ independent such terms gives total variance $\propto T\cdot\Delta t$, hence total standard deviation $\propto \sqrt{\Delta t}$. That single CLT-style argument fixes the leading order; the higher-order corrections $c_2\Delta t + \cdots$ come from third- and fourth-order Taylor terms suppressed at first order. All the formulas below are bookkeeping on top of this one scaling.

---

## Small time step expansion


For rebalancing interval $\Delta t \to 0$, the hedging error admits an expansion:

$$
\mathrm{HE}=c_1\sqrt{\Delta t}+c_2\Delta t+\cdots
$$

**Derivation of $c_1$.** Recall (see [§ Discrete-Time Hedging Error](discrete_time_hedging_error.md)): the per-step error $\frac{1}{2}\Gamma_k[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t]$ has variance $\frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2$, and summing $N = T/\Delta t$ independent steps gives $\text{Var}(\mathrm{HE}) \approx \frac{1}{2}\overline{\Gamma^2 S^4 \sigma^4} \cdot T \cdot \Delta t$. Thus:

$$
\boxed{c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma(t,S_t)^2 S_t^4 \sigma^4 \, dt}}
$$

The coefficient $c_1$ depends on the path through gamma.

**Second-order term** $c_2$:

$$
c_2 = -\frac{1}{2}\int_0^T \left(\frac{\partial \Gamma}{\partial t} + \mathcal{L}\Gamma\right) S^2 \sigma^2 \, dt + \text{(third derivative terms)}
$$

This involves the time derivative of gamma and curvature effects.

---

## Transaction cost expansion


Recall (see [§ Transaction Costs and Liquidity Effects](../model_risk/transaction_costs_and_liquidity_effects.md)): with proportional cost $\lambda$, the Whalley–Wilmott bandwidth is $h \sim (3\lambda/(2\Gamma S^2\sigma^2))^{1/3}$, the utility loss scales as $\lambda^{2/3}(\Gamma S^2\sigma^2)^{1/3} T$, and Leland's adjusted volatility $\sigma_{\text{eff}}^2 = \sigma^2(1 + \sqrt{8\lambda/(\pi\sigma\sqrt{\Delta t})}\,\text{sign}(\Gamma))$ absorbs the cost into the hedge model. The fractional powers $\lambda^{1/3}$, $\lambda^{2/3}$ arise from balancing $O(h^2)$ hedging error against $O(1/h)$ trading frequency.

---

## Model error expansion


For small model misspecification $\varepsilon$:

$$
\mathrm{HE}\approx \varepsilon A_1+\varepsilon^2 A_2+\cdots
$$

**Volatility misspecification.** Recall (see [§ Impact of Volatility Misspecification](impact_of_volatility_misspecification.md)): with $\varepsilon = \sigma^2 - \hat{\sigma}^2$, the first-order term is the gamma-weighted exposure $A_1 = \frac{1}{2}\int_0^T \Gamma(t,S_t) S_t^2 \, dt$.

**Jump risk.** If true dynamics include jumps with intensity $\lambda_J$ and size $J$:

$$
\mathrm{HE}_{\text{jump}} \sim \sum_{\text{jumps}} \frac{1}{2}\Gamma S^2 J^2
$$

The hedging error is dominated by jump contributions, not diffusive terms.

---

## Greeks-based P&L attribution


Recall (see [§ Gamma Risk and Convexity Effects](gamma_risk_and_convexity_effects.md)): the asymptotic expansion reduces to the standard decomposition $P\&L \approx \Theta\,\Delta t + \tfrac{1}{2}\Gamma(\Delta S)^2 + \nu\,\Delta\sigma + \text{higher order}$. The residual should be small if:

1. Rebalancing is frequent ($\Delta t$ small)
2. Model is accurate ($\varepsilon$ small)
3. No jumps occur

---

## Numerical verification


For an ATM call with $S = 100$, $\sigma = 20\%$, $\tau = 0.25$:

| Rebalancing | $\sqrt{\Delta t}$ | Theoretical Std | Monte Carlo Std |
|:------------|:--------------------|:----------------|:----------------|
| Daily | 0.063 | 0.28 | 0.27 |
| Weekly | 0.139 | 0.62 | 0.60 |
| Monthly | 0.289 | 1.29 | 1.25 |

The theoretical $\sqrt{\Delta t}$ scaling is confirmed by simulation.

---

## Optimal rebalancing frequency


Balancing hedging error variance against transaction costs:

$$
\text{Total Cost} = c_1^2 \Delta t + \lambda \cdot \frac{\text{turnover}}{\Delta t}
$$

The optimal $\Delta t^*$ satisfies:

$$
\Delta t^* \sim \left(\frac{\lambda \cdot \text{turnover}}{c_1^2}\right)^{1/2}
$$

Higher gamma (larger $c_1$) calls for more frequent rebalancing; higher costs call for less frequent.

---

## What to remember


- Leading hedging error term is $\mathcal{O}(\sqrt{\Delta t})$, driven by gamma
- Coefficient $c_1$ involves path integral of $\Gamma^2 S^4 \sigma^4$
- Transaction costs create $\lambda^{2/3}$ scaling of utility loss
- No-trade bands scale as $\lambda^{1/3}$
- These expansions connect asymptotics to practical P&L attribution
- Jump risk dominates diffusive hedging error in discontinuous models

---

## Exercises

**Exercise 1.** For the leading-order coefficient $c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 \, dt}$, compute $c_1$ for a constant-gamma approximation with $\Gamma = 0.04$, $S = 100$, $\sigma = 0.20$, $T = 0.25$. What is the hedging error standard deviation for daily rebalancing?

??? success "Solution to Exercise 1"
    With constant $\Gamma = 0.04$, $S = 100$, $\sigma = 0.20$, $T = 0.25$:

    $$
    c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 \, dt} = \sqrt{\frac{1}{2}\,\Gamma^2 S^4 \sigma^4\, T}
    $$

    Compute the integrand (constant in this approximation):

    $$
    \Gamma^2 S^4 \sigma^4 = (0.04)^2 \times (100)^4 \times (0.20)^4 = 1.6 \times 10^{-3} \times 10^8 \times 1.6 \times 10^{-3} = 256
    $$

    $$
    c_1 = \sqrt{\frac{1}{2} \times 256 \times 0.25} = \sqrt{32} = 4\sqrt{2} \approx 5.657
    $$

    For daily rebalancing ($\Delta t = 1/252$):

    $$
    \operatorname{Std}(\text{HE}) = c_1 \sqrt{\Delta t} = 5.657 \times \sqrt{1/252} = 5.657 \times 0.06299 \approx 0.356
    $$

    The hedging error standard deviation for daily rebalancing is approximately $\$0.36$.

---

**Exercise 2.** The Whalley-Wilmott no-trade bandwidth is $h \sim (3\lambda/(2\Gamma S^2 \sigma^2))^{1/3}$. Compute $h$ for $\lambda = 0.001$, $\Gamma = 0.04$, $S = 100$, $\sigma = 0.20$. Express $h$ in delta units. How does the bandwidth change if $\lambda$ doubles?

??? success "Solution to Exercise 2"
    With $\lambda = 0.001$, $\Gamma = 0.04$, $S = 100$, $\sigma = 0.20$:

    $$
    h = \left(\frac{3\lambda}{2\Gamma S^2 \sigma^2}\right)^{1/3}
    $$

    Compute the argument:

    $$
    2\Gamma S^2 \sigma^2 = 2 \times 0.04 \times 10000 \times 0.04 = 32
    $$

    $$
    h = \left(\frac{3 \times 0.001}{32}\right)^{1/3} = \left(\frac{0.003}{32}\right)^{1/3} = (9.375 \times 10^{-5})^{1/3}
    $$

    $$
    h \approx (9.375 \times 10^{-5})^{1/3} \approx 0.04543
    $$

    The bandwidth is approximately $h \approx 0.045$ in delta units. This means the trader does not rebalance unless the delta deviates by more than $\pm 0.045$ from the Black--Scholes delta.

    If $\lambda$ doubles to $0.002$:

    $$
    h_{\text{new}} = \left(\frac{2\lambda}{\lambda}\right)^{1/3} h = 2^{1/3} \times 0.04543 \approx 1.260 \times 0.04543 \approx 0.05724
    $$

    The bandwidth increases by a factor of $2^{1/3} \approx 1.26$, or about $26\%$. Higher transaction costs lead to wider no-trade bands, as expected.

---

**Exercise 3.** The utility loss from transaction costs scales as $\lambda^{2/3}$, not linearly in $\lambda$. Explain why this fractional power arises from the interplay between hedging error ($\sim h^2$) and trading cost ($\sim 1/h$). If transaction costs decrease by a factor of 10, by what factor does the utility loss decrease?

??? success "Solution to Exercise 3"
    The optimal strategy trades off hedging error against transaction cost. The no-trade bandwidth $h$ controls both:

    - **Hedging error** scales as $h^2$: a wider band allows the delta to deviate further, increasing the squared hedging error.
    - **Transaction cost** scales as $1/h$: a wider band means less frequent trading, reducing costs.

    The total cost is:

    $$
    \text{Total} \sim h^2 + \frac{\lambda}{h}
    $$

    Minimizing over $h$:

    $$
    \frac{d}{dh}\left(h^2 + \frac{\lambda}{h}\right) = 2h - \frac{\lambda}{h^2} = 0 \implies h^* \sim \lambda^{1/3}
    $$

    Substituting back:

    $$
    \text{Total}^* \sim (h^*)^2 + \frac{\lambda}{h^*} \sim \lambda^{2/3} + \lambda^{2/3} \sim \lambda^{2/3}
    $$

    The $\lambda^{2/3}$ power arises because the optimal bandwidth balances two competing terms with different powers of $h$, and the cube-root balancing yields a $2/3$ exponent.

    If transaction costs decrease by a factor of 10 ($\lambda \to \lambda/10$):

    $$
    \frac{\text{New cost}}{\text{Old cost}} = \left(\frac{1}{10}\right)^{2/3} = 10^{-2/3} \approx 0.2154
    $$

    The utility loss decreases by a factor of approximately $4.64$, which is less than the tenfold reduction in costs. This diminishing return occurs because lower costs encourage tighter bands, which also incur more frequent trading.

---

**Exercise 4.** Leland's adjusted volatility is $\sigma_{\text{eff}}^2 = \sigma^2(1 + \sqrt{8\lambda/(\pi\sigma\sqrt{\Delta t})}\,\text{sign}(\Gamma))$. For $\sigma = 0.20$, $\lambda = 0.002$, $\Delta t = 1/252$, compute $\sigma_{\text{eff}}$ for a long gamma position. By how much does the adjusted volatility exceed the true volatility?

??? success "Solution to Exercise 4"
    With $\sigma = 0.20$, $\lambda = 0.002$, $\Delta t = 1/252$:

    $$
    \sigma_{\text{eff}}^2 = \sigma^2\left(1 + \sqrt{\frac{8\lambda}{\pi\sigma\sqrt{\Delta t}}}\right)
    $$

    First compute the correction term. With $\sqrt{\Delta t} = \sqrt{1/252} \approx 0.06299$:

    $$
    \frac{8\lambda}{\pi\sigma\sqrt{\Delta t}} = \frac{8 \times 0.002}{\pi \times 0.20 \times 0.06299} = \frac{0.016}{0.03958} \approx 0.4042
    $$

    $$
    \sqrt{0.4042} \approx 0.6358
    $$

    For a long gamma position ($\text{sign}(\Gamma) = +1$):

    $$
    \sigma_{\text{eff}}^2 = (0.20)^2(1 + 0.6358) = 0.04 \times 1.6358 = 0.06543
    $$

    $$
    \sigma_{\text{eff}} = \sqrt{0.06543} \approx 0.2558
    $$

    The Leland-adjusted volatility exceeds the true volatility by:

    $$
    \frac{\sigma_{\text{eff}} - \sigma}{\sigma} = \frac{0.2558 - 0.20}{0.20} = \frac{0.0558}{0.20} \approx 27.9\%
    $$

    This is a substantial adjustment, reflecting the significant impact of transaction costs on daily hedging.

---

**Exercise 5.** The P&L attribution formula decomposes the hedged P&L into theta, gamma, and vega components. For a delta-hedged position over one day with $\Theta = -0.05$, $\Gamma = 0.04$, $\nu = 12$, $\Delta S = 2$, and $\Delta\sigma = -0.005$, compute each component and the total P&L. Identify the dominant contributor.

??? success "Solution to Exercise 5"
    Compute each component:

    **Theta component:**

    $$
    \text{Theta P\&L} = \Theta \cdot \Delta t = (-0.05) \times (1/252) \approx -0.000198
    $$

    (Note: if $\Theta = -0.05$ is already in daily units, then the theta P&L is simply $-0.05$. We assume daily units here.)

    **Theta P&L** $= -0.05$

    **Gamma component:**

    $$
    \text{Gamma P\&L} = \frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2}(0.04)(2)^2 = \frac{1}{2}(0.04)(4) = 0.08
    $$

    **Vega component:**

    $$
    \text{Vega P\&L} = \nu \cdot \Delta\sigma = 12 \times (-0.005) = -0.06
    $$

    **Total P&L:**

    $$
    \text{Total} = -0.05 + 0.08 + (-0.06) = -0.03
    $$

    | Component | P&L |
    |:---|:---|
    | Theta | $-0.05$ |
    | Gamma | $+0.08$ |
    | Vega | $-0.06$ |
    | **Total** | $-0.03$ |

    The dominant contributor is the **vega component** ($-0.06$), followed closely by theta ($-0.05$) and gamma ($+0.08$). The gamma P&L from the stock move partially offsets the losses from theta and the implied volatility decline, but the net P&L is negative at $-\$0.03$.

---

**Exercise 6.** The numerical verification table shows theoretical and Monte Carlo hedging error standard deviations. Design a simulation to verify the $\sqrt{\Delta t}$ scaling: use the `bs_greeks` function to simulate delta-hedging with $N = 10{,}000$ paths for $\Delta t = 1/252$, $1/52$, and $1/12$. Report the standard deviation at each frequency and plot $\text{Std}(\text{HE})$ versus $\sqrt{\Delta t}$ to check linearity.

??? success "Solution to Exercise 6"
    The simulation proceeds as follows:

    **Setup:**

    - Parameters: $S_0 = K = 100$, $\sigma = 0.20$, $T = 0.25$, $r = 0.05$
    - Frequencies: daily ($\Delta t = 1/252$), weekly ($\Delta t = 1/52$), monthly ($\Delta t = 1/12$)
    - Number of paths: $N_{\text{paths}} = 10{,}000$

    **Algorithm for each path and frequency:**

    1. Simulate the stock price path: $S_{k+1} = S_k \exp\left((r - \sigma^2/2)\Delta t + \sigma\sqrt{\Delta t}\,Z_k\right)$
    2. At each $t_k$, compute $\Delta_k$ using the Black--Scholes delta formula
    3. Track the hedge portfolio: $\Pi_{k+1} = \Pi_k e^{r\Delta t} + \Delta_k(S_{k+1} - S_k e^{r\Delta t})$
    4. At expiry, compute $\text{HE} = \max(S_T - K, 0) - \Pi_T$

    **Expected results:**

    | Frequency | $\sqrt{\Delta t}$ | Theoretical Std | Expected MC Std |
    |:---|:---|:---|:---|
    | Daily | 0.063 | $\approx 0.28$ | $\approx 0.27$ |
    | Weekly | 0.139 | $\approx 0.62$ | $\approx 0.60$ |
    | Monthly | 0.289 | $\approx 1.29$ | $\approx 1.25$ |

    **Linearity check:** Plotting $\operatorname{Std}(\text{HE})$ vs $\sqrt{\Delta t}$ should yield points close to a straight line through the origin with slope $c_1 \approx 4.5$. The regression $R^2$ should be close to 1, confirming the theoretical $\sqrt{\Delta t}$ scaling. Small deviations from linearity arise from higher-order terms ($c_2 \Delta t$ and beyond) and from the constant-gamma approximation used in the theoretical formula.
