# P&L Explanation Under Heston

## Introduction

In the Black--Scholes world, a delta-hedged portfolio's profit and loss decomposes neatly into three terms: theta (time decay), gamma (realized versus implied variance), and financing. Because volatility is constant, this decomposition is **exact** --- every dollar of P&L is explained. The Heston model breaks this simplicity. Variance $v_t$ is now a second stochastic factor, so the option price $V(t, S_t, v_t)$ depends on three variables instead of two. Applying Ito's lemma to this two-factor system introduces additional terms --- a **vega P&L** from variance moves and a **vanna P&L** from the correlation between stock and variance --- that have no analogue in Black--Scholes. Understanding these terms is essential for any practitioner who delta-hedges under stochastic volatility.

This section derives the full P&L decomposition for a delta-hedged option in the Heston model, identifies each contributing term, and explains the sources of **unexplained P&L** that arise in practice.

!!! info "Prerequisites"
    - [Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md) (the bivariate SDE system)
    - [Greeks via Characteristic Function Differentiation](greeks_via_cf_differentiation.md) (delta, gamma, vega definitions)
    - [Vega Surface and Vol-of-Vol](vega_surface_and_vol_of_vol.md) (variance sensitivities)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the instantaneous P&L of a delta-hedged option under the Heston model using two-dimensional Ito's lemma
    2. Identify the theta, gamma, vega, vanna, and volga contributions to P&L
    3. Explain why unexplained P&L arises from vol-of-vol, discrete rehedging, and correlation
    4. Compare the Heston P&L decomposition with its Black--Scholes counterpart

---

## The Heston Pricing PDE

### Two-Factor Dynamics

Recall the Heston model under the risk-neutral measure $\mathbb{Q}$:

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho \, dt$, where $r$ is the risk-free rate, $q$ is the continuous dividend yield, $\kappa$ is the mean-reversion speed, $\theta$ is the long-run variance, $\xi$ is the vol-of-vol, and $\rho$ is the correlation.

### The PDE

The European option price $V(t, S, v)$ satisfies the **Heston PDE**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} v S^2 \frac{\partial^2 V}{\partial S^2} + \rho \xi v S \frac{\partial^2 V}{\partial S \, \partial v} + \frac{1}{2} \xi^2 v \frac{\partial^2 V}{\partial v^2} + (r - q) S \frac{\partial V}{\partial S} + \kappa(\theta - v) \frac{\partial V}{\partial v} - r V = 0
$$

This PDE encodes the no-arbitrage condition under $\mathbb{Q}$. Each term in the PDE will correspond to a specific component of the P&L decomposition.

---

## Two-Dimensional Ito Expansion

### Applying Ito's Lemma

To understand P&L, we work under the **physical measure** $\mathbb{P}$, where the dynamics may differ from $\mathbb{Q}$ through the market price of risk. The option price $V(t, S_t, v_t)$ is a function of three variables. By two-dimensional Ito's lemma:

$$
dV = \frac{\partial V}{\partial t} \, dt + \frac{\partial V}{\partial S} \, dS_t + \frac{\partial V}{\partial v} \, dv_t + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (dS_t)^2 + \frac{\partial^2 V}{\partial S \, \partial v} \, dS_t \, dv_t + \frac{1}{2} \frac{\partial^2 V}{\partial v^2} (dv_t)^2
$$

Substituting the quadratic variation terms:

$$
(dS_t)^2 = v_t S_t^2 \, dt, \qquad dS_t \, dv_t = \rho \xi v_t S_t \, dt, \qquad (dv_t)^2 = \xi^2 v_t \, dt
$$

we obtain the **full Ito expansion**:

$$
dV = \frac{\partial V}{\partial t} \, dt + \frac{\partial V}{\partial S} \, dS_t + \frac{\partial V}{\partial v} \, dv_t + \frac{1}{2} v_t S_t^2 \frac{\partial^2 V}{\partial S^2} \, dt + \rho \xi v_t S_t \frac{\partial^2 V}{\partial S \, \partial v} \, dt + \frac{1}{2} \xi^2 v_t \frac{\partial^2 V}{\partial v^2} \, dt
$$

### Greek Notation

We introduce standard notation for the partial derivatives (Greeks):

| Greek | Symbol | Definition |
|-------|--------|------------|
| Delta | $\Delta$ | $\partial V / \partial S$ |
| Gamma | $\Gamma$ | $\partial^2 V / \partial S^2$ |
| Theta | $\Theta$ | $\partial V / \partial t$ |
| Vega (variance) | $\mathcal{V}$ | $\partial V / \partial v$ |
| Vanna (cross) | $\mathcal{A}$ | $\partial^2 V / (\partial S \, \partial v)$ |
| Volga (variance gamma) | $\mathcal{G}$ | $\partial^2 V / \partial v^2$ |

!!! warning "Vega Convention"
    In the Heston model, vega is naturally defined as the sensitivity to the **variance** $v$, not to the **volatility** $\sigma = \sqrt{v}$. The relationship is $\partial V / \partial \sigma = 2\sqrt{v} \cdot \partial V / \partial v$. Market practitioners often quote vega with respect to implied volatility, so care is needed when comparing.

Using this notation, the Ito expansion becomes:

$$
dV = \Theta \, dt + \Delta \, dS_t + \mathcal{V} \, dv_t + \frac{1}{2} \Gamma \, v_t S_t^2 \, dt + \mathcal{A} \, \rho \xi v_t S_t \, dt + \frac{1}{2} \mathcal{G} \, \xi^2 v_t \, dt
$$

---

## Delta-Hedged P&L Decomposition

### The Hedged Portfolio

A trader holds the option $V$ and delta-hedges by shorting $\Delta$ shares of the underlying. The portfolio value is:

$$
\Pi_t = V(t, S_t, v_t) - \Delta \, S_t
$$

The instantaneous P&L of the hedged portfolio is:

$$
d\Pi_t = dV - \Delta \, dS_t - r \Pi_t \, dt
$$

where the last term accounts for the financing cost of the portfolio. Substituting the Ito expansion and cancelling the $\Delta \, dS_t$ terms:

$$
d\Pi_t = \Theta \, dt + \mathcal{V} \, dv_t + \frac{1}{2} \Gamma \, v_t S_t^2 \, dt + \mathcal{A} \, \rho \xi v_t S_t \, dt + \frac{1}{2} \mathcal{G} \, \xi^2 v_t \, dt - r(V - \Delta S_t) \, dt
$$

### Decomposition Into Named Components

!!! note "Theorem (Heston P&L Decomposition)"
    The instantaneous P&L of a continuously delta-hedged option under the Heston model decomposes as:

    $$
    d\Pi_t = \underbrace{\Theta \, dt}_{\text{theta}} + \underbrace{\frac{1}{2} \Gamma \, v_t S_t^2 \, dt}_{\text{gamma}} + \underbrace{\mathcal{V} \, dv_t}_{\text{vega}} + \underbrace{\mathcal{A} \, \rho \xi v_t S_t \, dt}_{\text{vanna}} + \underbrace{\frac{1}{2} \mathcal{G} \, \xi^2 v_t \, dt}_{\text{volga}} - \underbrace{r(V - \Delta S_t) \, dt}_{\text{financing}}
    $$

Each term captures a distinct source of risk:

1. **Theta P&L** ($\Theta \, dt$): Time decay. For a long option position, $\Theta < 0$ --- the option loses value as time passes, all else equal.

2. **Gamma P&L** ($\frac{1}{2} \Gamma v_t S_t^2 \, dt$): Convexity. The delta-hedged portfolio benefits from realized variance exceeding the level priced into the option. For a long gamma position ($\Gamma > 0$), this term is always non-negative.

3. **Vega P&L** ($\mathcal{V} \, dv_t$): Sensitivity to variance moves. This is the key term absent from Black--Scholes. When variance increases ($dv_t > 0$) and the trader is long vega ($\mathcal{V} > 0$), this contributes positively.

4. **Vanna P&L** ($\mathcal{A} \rho \xi v_t S_t \, dt$): Cross-sensitivity between spot and variance. This term captures the interaction between the two risk factors through their correlation and the cross-partial derivative.

5. **Volga P&L** ($\frac{1}{2} \mathcal{G} \xi^2 v_t \, dt$): The "gamma of vega." This term captures the convexity of the option price with respect to variance, scaled by the vol-of-vol squared.

6. **Financing** ($r(V - \Delta S_t) \, dt$): Cost of carrying the hedged position.

---

## Theta-Gamma Relationship Under Heston

### Using the PDE

In the Black--Scholes model, the theta-gamma relationship $\Theta + \frac{1}{2} \sigma^2 S^2 \Gamma + r S \Delta - r V = 0$ links theta, gamma, delta, and the option value. Under Heston, the analogous relationship comes directly from the pricing PDE:

$$
\Theta = -\frac{1}{2} v S^2 \Gamma - \rho \xi v S \, \mathcal{A} - \frac{1}{2} \xi^2 v \, \mathcal{G} - (r - q) S \Delta - \kappa(\theta - v) \mathcal{V} + r V
$$

Substituting into the P&L decomposition, the deterministic terms simplify.

!!! note "Theorem (Theta-Gamma-Vega Identity)"
    Under continuous delta hedging and risk-neutral pricing, the deterministic component of the delta-hedged P&L satisfies:

    $$
    \Theta + \frac{1}{2} v S^2 \Gamma + \rho \xi v S \, \mathcal{A} + \frac{1}{2} \xi^2 v \, \mathcal{G} + (r - q) S \Delta + \kappa(\theta - v) \mathcal{V} - r V = 0
    $$

    This is simply a restatement of the Heston PDE with Greek notation. The deterministic terms in the P&L cancel exactly if the option is priced consistently with the Heston model.

### Residual P&L

After using the PDE to eliminate the deterministic terms, the remaining P&L is purely stochastic:

$$
d\Pi_t = \mathcal{V}\left[dv_t - \kappa(\theta - v_t) \, dt\right] = \mathcal{V} \, \xi \sqrt{v_t} \, dW_t^{(2)}
$$

Under the risk-neutral measure with continuous hedging and correct model, the expected P&L is zero. Under the physical measure, or with model misspecification, this residual drives the **unexplained P&L**.

---

## Comparison with Black--Scholes P&L

### The Black--Scholes Decomposition

In the Black--Scholes model ($v_t = \sigma^2$ constant), the delta-hedged P&L is:

$$
d\Pi_t^{\text{BS}} = \Theta^{\text{BS}} \, dt + \frac{1}{2} \Gamma^{\text{BS}} S_t^2 \, (dS_t / S_t)^2 - r(V^{\text{BS}} - \Delta^{\text{BS}} S_t) \, dt
$$

Using the Black--Scholes PDE ($\Theta^{\text{BS}} + \frac{1}{2} \sigma^2 S^2 \Gamma^{\text{BS}} + rS\Delta^{\text{BS}} - rV^{\text{BS}} = 0$), this reduces to the well-known **gamma P&L**:

$$
d\Pi_t^{\text{BS}} = \frac{1}{2} \Gamma^{\text{BS}} S_t^2 \left[\left(\frac{dS_t}{S_t}\right)^2 - \sigma^2 \, dt\right]
$$

The P&L is driven solely by the difference between **realized** and **implied** variance.

### Additional Terms in Heston

The Heston model introduces three extra terms relative to Black--Scholes:

| Term | Source | Hedgeable? |
|------|--------|------------|
| $\mathcal{V} \, dv_t$ | Stochastic variance | Only with variance swaps or VIX options |
| $\mathcal{A} \, \rho \xi v_t S_t \, dt$ | Spot-variance correlation | Partially, through delta adjustment |
| $\frac{1}{2} \mathcal{G} \, \xi^2 v_t \, dt$ | Vol-of-vol convexity | Only with second-order variance instruments |

!!! tip "Practical Implication"
    A trader who delta-hedges an option using the Heston model but does not hedge variance risk will have P&L driven by $\mathcal{V} \, dv_t$. The magnitude of this unhedged term depends on the option's vega and the realized variance path. For long-dated options with large $\mathcal{V}$, variance moves can dominate the gamma P&L.

---

## Sources of Unexplained P&L

### Defining Unexplained P&L

In practice, the theoretical P&L decomposition never perfectly matches the actual P&L of a trading book. The difference is called **unexplained P&L** (sometimes "P&L leakage" or "P&L noise"):

$$
\text{Unexplained P\&L} = \text{Actual P\&L} - \sum_{\text{Greeks}} \text{Greek} \times \text{Risk factor move}
$$

### Sources Under Heston

Several factors contribute to unexplained P&L when hedging under the Heston model:

**1. Discrete Rehedging.** The decomposition assumes continuous delta hedging. In practice, rehedging occurs at discrete intervals $\Delta t$. The discretization error scales as $\mathcal{O}(\Delta t)$ for each Greek term:

$$
\text{Discrete error} \approx \frac{1}{2} \frac{\partial^2 V}{\partial S^2} S^2 v \left[(\Delta S / S)^2 - v \, \Delta t\right]
$$

This "gamma slippage" depends on the realized path and is non-diversifiable across time steps.

**2. Higher-Order Terms.** The Ito expansion truncates at second order. Third-order terms in $\Delta S$ and $\Delta v$ contribute $\mathcal{O}((\Delta t)^{3/2})$ errors that become visible in volatile markets or for highly convex instruments.

**3. Model Misspecification.** If the true data-generating process differs from Heston --- for example, if jumps are present or if the vol-of-vol is itself stochastic --- the P&L decomposition based on Heston Greeks will leave a residual. The Heston model cannot capture:

- Jump-induced P&L (requires Bates or Merton extensions)
- Rough volatility effects ($H < 0.5$ Hurst parameter)
- Regime changes in mean-reversion speed $\kappa$

**4. Correlation Instability.** The parameter $\rho$ is assumed constant, but empirical correlation between spot returns and variance changes fluctuates. When $\rho$ varies, the vanna term $\mathcal{A} \, \rho \xi v S \, dt$ generates unexplained P&L proportional to $\Delta\rho$.

**5. Vol-of-Vol Contribution.** The volga term $\frac{1}{2} \mathcal{G} \xi^2 v \, dt$ is often small for vanilla options but becomes significant for:

- Variance options (where $\mathcal{G}$ is large)
- Deep out-of-the-money options (where convexity in $v$ is high)
- Long-dated options (where accumulated vol-of-vol exposure is large)

!!! warning "Vol-of-Vol and Unexplained P&L"
    The vol-of-vol parameter $\xi$ controls the curvature of the implied volatility smile. When a trader hedges using a model with incorrect $\xi$, the volga P&L is systematically misestimated. This is a common source of persistent unexplained P&L in equity derivatives desks.

---

## Worked Example

### Setup

Consider a European call option under the Heston model with the following parameters:

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Spot price | $S_0$ | \$100 |
| Strike | $K$ | \$100 |
| Risk-free rate | $r$ | 3% |
| Dividend yield | $q$ | 0% |
| Initial variance | $v_0$ | 0.04 |
| Mean reversion | $\kappa$ | 2.0 |
| Long-run variance | $\theta$ | 0.04 |
| Vol-of-vol | $\xi$ | 0.5 |
| Correlation | $\rho$ | $-0.7$ |
| Time to maturity | $T$ | 0.5 years |

### Greeks at Inception

Using Fourier inversion (e.g., the COS method), the option price and Greeks at $t = 0$ are approximately:

| Greek | Value | Units |
|-------|-------|-------|
| $V$ | \$6.42 | dollars |
| $\Delta$ | 0.567 | per dollar of $S$ |
| $\Gamma$ | 0.0298 | per dollar$^2$ of $S$ |
| $\Theta$ | $-0.0215$ | per day (calendar) |
| $\mathcal{V}$ | 17.8 | per unit of variance |
| $\mathcal{A}$ | $-0.48$ | cross-sensitivity |
| $\mathcal{G}$ | 62.5 | per unit of variance$^2$ |

### One-Day P&L Attribution

Suppose over one trading day ($\Delta t = 1/252$):

- The stock moves from \$100.00 to \$101.20 ($\Delta S = +1.20$)
- Variance moves from 0.0400 to 0.0385 ($\Delta v = -0.0015$)

The P&L components are:

$$
\text{Theta P\&L} = \Theta \times \Delta t = -0.0215 \times (1/252) \approx -\$0.0001
$$

$$
\text{Delta P\&L} = \Delta \times \Delta S = 0.567 \times 1.20 = +\$0.680
$$

$$
\text{Gamma P\&L} = \frac{1}{2} \Gamma (\Delta S)^2 = \frac{1}{2} \times 0.0298 \times 1.44 = +\$0.021
$$

$$
\text{Vega P\&L} = \mathcal{V} \times \Delta v = 17.8 \times (-0.0015) = -\$0.027
$$

$$
\text{Vanna P\&L} = \mathcal{A} \times \rho \xi v S \times \Delta t \approx -0.48 \times (-0.7)(0.5)(0.04)(100) \times (1/252) \approx +\$0.003
$$

$$
\text{Volga P\&L} = \frac{1}{2} \mathcal{G} \xi^2 v \times \Delta t = \frac{1}{2} \times 62.5 \times 0.25 \times 0.04 \times (1/252) \approx +\$0.001
$$

### P&L Attribution Summary

| Component | Value | Fraction |
|-----------|-------|----------|
| Delta | +\$0.680 | 100.4% |
| Gamma | +\$0.021 | 3.1% |
| Vega | $-$\$0.027 | $-$4.0% |
| Theta | $-$\$0.0001 | $\approx 0$% |
| Vanna | +\$0.003 | 0.4% |
| Volga | +\$0.001 | 0.1% |
| **Total explained** | **+\$0.677** | |

The **delta-hedged P&L** (removing the delta component) is approximately $+\$0.021 - \$0.027 + \$0.003 + \$0.001 \approx -\$0.002$. The vega term (from variance declining) nearly offsets the gamma gain, illustrating how stochastic volatility fundamentally changes the P&L profile relative to Black--Scholes.

!!! example "Observation"
    In this example, the stock rose 1.2% while variance fell by 3.75%. The negative $\rho = -0.7$ makes these moves consistent: rising stock prices are associated with falling variance (the leverage effect). The vega P&L from the variance decline partially offsets the gamma P&L from the stock move --- a signature feature of stochastic volatility that is invisible under Black--Scholes.

---

## Summary

| Concept | Formula / Description |
|---------|-----------------------|
| Heston Ito expansion | $dV = \Theta \, dt + \Delta \, dS + \mathcal{V} \, dv + \frac{1}{2}\Gamma v S^2 \, dt + \mathcal{A} \rho \xi v S \, dt + \frac{1}{2}\mathcal{G} \xi^2 v \, dt$ |
| Delta-hedged residual | $d\Pi = \mathcal{V} \xi \sqrt{v} \, dW^{(2)}$ (under continuous hedging) |
| Black--Scholes gamma P&L | $\frac{1}{2}\Gamma S^2[(\Delta S/S)^2 - \sigma^2 \Delta t]$ |
| Unexplained P&L sources | Discrete rehedging, higher-order terms, model misspecification, $\rho$ instability, vol-of-vol |

!!! abstract "Key Takeaways"
    1. **Two-factor Ito expansion**: Under Heston, the P&L decomposes into six terms --- theta, delta, gamma, vega, vanna, and volga --- compared to three under Black--Scholes.

    2. **Vega dominates for long-dated options**: The $\mathcal{V} \, dv_t$ term can be the largest contributor to delta-hedged P&L when variance moves are large relative to gamma gains.

    3. **Theta-gamma-vega identity**: The Heston PDE links all deterministic terms; under continuous hedging with the correct model, the residual P&L is purely driven by variance Brownian motion.

    4. **Unexplained P&L**: Discrete rehedging, higher-order Greeks, model misspecification, and parameter instability all generate unexplained P&L that practitioners must monitor and attribute.

    5. **Hedging implications**: To fully hedge under Heston, a trader needs instruments sensitive to variance (variance swaps, VIX options) in addition to delta hedging with the underlying.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Greeks via Characteristic Function Differentiation](greeks_via_cf_differentiation.md) | Analytic computation of Heston Greeks |
| [Greeks via Finite Differences](greeks_via_finite_differences.md) | Numerical Greek computation by bumping |
| [Vega Surface and Vol-of-Vol](vega_surface_and_vol_of_vol.md) | The term structure of variance sensitivity |
| [Variance Swaps (Closed-Form)](../exotic_pricing/variance_swaps_closed_form.md) | Hedging the vega P&L component |

---

## Exercises

**Exercise 1.**
In Black-Scholes, the delta-hedged P&L over an interval $[t, t+dt]$ is $dP\&L = \frac{1}{2}\Gamma S^2(\sigma_{\text{real}}^2 - \sigma_{\text{imp}}^2)dt + \Theta\,dt$. Under Heston, an additional vega term appears: $\mathcal{V}\,dv_t$. Explain the financial meaning of this term. If $\mathcal{V} > 0$ (long vega) and variance increases ($dv > 0$), is the P&L contribution positive or negative?

??? success "Solution to Exercise 1"
    The vega P&L term $\mathcal{V}\,dv_t$ captures the change in the option's value due to changes in the instantaneous variance $v_t$, holding all other variables fixed. This term arises because variance is a second stochastic factor in the Heston model: unlike Black-Scholes where $\sigma$ is constant, the Heston variance $v_t$ fluctuates randomly according to the CIR process $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}$.

    **Financial meaning.** If $\mathcal{V} > 0$ (the trader is long vega, i.e., the option price increases when variance rises), then:

    - When variance increases ($dv > 0$): the vega P&L contribution is $\mathcal{V} \times dv > 0$, which is **positive**. The option becomes more valuable because higher variance implies larger expected future moves in $S$, increasing the option's time value.
    - When variance decreases ($dv < 0$): the contribution is negative. The option loses value because the expected future volatility has declined.

    For a long call position, $\mathcal{V} > 0$ always (call prices are increasing in variance). So a variance increase ($dv > 0$) produces a **positive** P&L contribution.

    This term is absent from Black-Scholes because $v$ is constant, so $dv = 0$ identically. Under Heston, the vega P&L can be the dominant component of delta-hedged P&L for long-dated options, since variance moves $dv_t$ can be large (especially when $\xi$ is high) while the gamma P&L depends on realized stock moves which are of order $\sqrt{v\,dt}$.

---

**Exercise 2.**
The Heston P&L decomposition includes a vanna term $\partial^2 V / \partial S \partial v \cdot S\sqrt{v}\rho\xi v\,dt$. Explain why this term arises from the correlation between $dS$ and $dv$. For $\rho < 0$, does a simultaneous drop in $S$ and rise in $v$ produce a positive or negative vanna P&L for a long call position?

??? success "Solution to Exercise 2"
    The vanna term in the P&L decomposition is:

    $$
    \text{Vanna P\&L} = \mathcal{A}\,\rho\,\xi\,v_t\,S_t\,dt
    $$

    where $\mathcal{A} = \partial^2 V / \partial S \,\partial v$.

    **Why it arises from correlation.** In the two-dimensional Ito expansion of $dV(t, S_t, v_t)$, the cross-term is:

    $$
    \frac{\partial^2 V}{\partial S\,\partial v}\,dS_t\,dv_t
    $$

    Computing the quadratic covariation:

    $$
    dS_t\,dv_t = \bigl(\sqrt{v_t}\,S_t\,dW_t^{(1)}\bigr)\bigl(\xi\sqrt{v_t}\,dW_t^{(2)}\bigr) = \xi\,v_t\,S_t\,dW_t^{(1)}\,dW_t^{(2)} = \rho\,\xi\,v_t\,S_t\,dt
    $$

    This is nonzero precisely because $\rho \neq 0$: the stock and variance Brownian motions are correlated. If $\rho = 0$, the vanna P&L vanishes entirely.

    **Sign analysis for $\rho < 0$ and a long call.** Consider a simultaneous drop in $S$ and rise in $v$ (the leverage effect, which is the typical scenario when $\rho < 0$):

    - $\Delta S < 0$ and $\Delta v > 0$

    For a long call position, the vanna $\mathcal{A} = \partial^2 V / \partial S\,\partial v$ is typically **negative** for ATM and ITM options. Intuitively: when $S$ increases, the option moves deeper ITM and its sensitivity to variance (vega) decreases (because deep ITM options are less sensitive to volatility). So $\partial\mathcal{V}/\partial S < 0$, i.e., $\mathcal{A} < 0$.

    The vanna P&L over a discrete interval is approximately:

    $$
    \mathcal{A}\,\Delta S\,\Delta v \approx \mathcal{A} \times (\text{negative}) \times (\text{positive}) < 0 \quad \text{if } \mathcal{A} < 0
    $$

    Wait -- we must be more careful. The continuous-time vanna P&L from the Ito expansion is the *deterministic* cross-variation term $\mathcal{A}\,\rho\,\xi\,v\,S\,dt$, not $\mathcal{A}\,\Delta S\,\Delta v$. For $\rho < 0$, $\mathcal{A} < 0$, $\xi > 0$, $v > 0$, $S > 0$:

    $$
    \mathcal{A}\,\rho\,\xi\,v\,S\,dt = (\text{negative})(\text{negative})(\text{positive})(\text{positive})(\text{positive})(\text{positive}) > 0
    $$

    The vanna P&L is **positive** for a long call with $\rho < 0$. This makes financial sense: the leverage effect (negative correlation) means that when stocks drop, volatility rises, providing a partial natural hedge. The vanna term captures this beneficial correlation effect --- the option "benefits" from the systematic relationship between spot and variance.

---

**Exercise 3.**
A trader sells an ATM call and delta-hedges daily. Over one month, the unexplained P&L (residual after delta, gamma, theta, and vega terms) has a standard deviation of \$0.50 per option. Identify three sources of this unexplained P&L: (a) discrete hedging error, (b) unhedged volga ($\partial^2 V/\partial v^2$) exposure, (c) model mis-specification. Which is likely the dominant source?

??? success "Solution to Exercise 3"
    The three sources of unexplained P&L are:

    **(a) Discrete hedging error.** The P&L decomposition assumes continuous delta hedging ($dt \to 0$), but in practice the trader rebalances at discrete intervals $\Delta t$ (e.g., daily). The discretization error over each rebalancing interval is approximately:

    $$
    \text{Discrete error} \approx \frac{1}{2}\Gamma\,S^2\left[\left(\frac{\Delta S}{S}\right)^2 - v\,\Delta t\right] + \text{higher-order terms}
    $$

    This is the gamma slippage: the realized squared return $(\Delta S/S)^2$ deviates from its expected value $v\,\Delta t$ over finite intervals. The standard deviation of this term scales as $\mathcal{O}(\sqrt{\Delta t})$ per step and $\mathcal{O}((\Delta t)^{0})$ cumulatively over $T/\Delta t$ steps (since errors are partially diversified but not independent due to serial correlation in $v_t$). For daily hedging ($\Delta t = 1/252$), this can produce P&L noise of order \$0.10--\$0.50 per option over a month.

    **(b) Unhedged volga exposure.** The volga term $\frac{1}{2}\mathcal{G}\,\xi^2\,v\,dt$ is a deterministic contribution to the P&L decomposition, but it is often omitted from simplified attribution models. More importantly, the trader does not hedge the **stochastic** part of the volga exposure: changes in $\mathcal{G}$ itself as $(S, v)$ evolve, and the fact that $\xi$ may not be constant. For an ATM call, $\mathcal{G}$ is moderate, but for OTM options or variance-sensitive instruments, this can be significant. Over one month, the cumulative unhedged volga P&L is approximately:

    $$
    \sum_{i=1}^{N} \frac{1}{2}\mathcal{G}_i\,\xi^2\,v_i\,\Delta t \approx \frac{1}{2}\bar{\mathcal{G}}\,\xi^2\,\bar{v}\,T_{\text{month}}
    $$

    For $\bar{\mathcal{G}} \approx 60$, $\xi = 0.5$, $\bar{v} = 0.04$, $T_{\text{month}} = 1/12$: approximately $\frac{1}{2} \times 60 \times 0.25 \times 0.04 / 12 \approx \$0.025$.

    **(c) Model misspecification.** The Heston model assumes specific functional forms for the dynamics (CIR variance, constant parameters, no jumps). If the true process has:

    - Jumps in $S$ or $v$: the Ito expansion misses the jump terms entirely
    - Time-varying $\kappa$, $\theta$, $\xi$, or $\rho$: the Greeks computed with static parameters are systematically wrong
    - Rougher volatility dynamics ($H < 0.5$): the CIR process is too smooth, and the Heston Greeks understate the true sensitivities at short horizons

    **Dominant source.** For a standard ATM call hedged daily over one month, the **discrete hedging error** is likely the dominant source, producing the largest contribution to the \$0.50 standard deviation. The gamma slippage from daily rebalancing is inherently noisy and scales with $\Gamma\,S^2\,v$ (which is large for ATM options). The volga and model misspecification terms are smaller for vanilla ATM options but become more important for exotic or long-dated positions.

---

**Exercise 4.**
The gamma P&L is $\frac{1}{2}\Gamma S^2 (dS/S)^2 \approx \frac{1}{2}\Gamma S^2 v\,dt$. The vega P&L is $\mathcal{V}\,dv$. For typical equity Heston parameters ($v_0 = 0.04$, $\xi = 0.5$), estimate the order of magnitude of each term for an ATM call with $T = 0.5$, $S_0 = 100$. Which contributes more to daily P&L variance?

??? success "Solution to Exercise 4"
    **Gamma P&L (per day).** The expected magnitude of the gamma P&L per day is:

    $$
    \left|\frac{1}{2}\Gamma\,S_0^2\,v_0\,\Delta t\right| = \frac{1}{2} \times \Gamma \times 100^2 \times 0.04 \times \frac{1}{252}
    $$

    For an ATM call with $T = 0.5$, using the worked example values, $\Gamma \approx 0.0298$:

    $$
    \frac{1}{2} \times 0.0298 \times 10{,}000 \times 0.04 \times \frac{1}{252} \approx \frac{1}{2} \times 0.0298 \times 400 \times 0.00397 \approx \$0.024
    $$

    The **variance** of the daily gamma P&L (driven by the randomness of $(\Delta S/S)^2$) scales as $\Gamma^2 S^4 v^2 \Delta t / 2$, giving a daily standard deviation of approximately:

    $$
    \sigma_{\text{gamma}} \approx \Gamma\,S_0^2\,v_0\,\sqrt{\Delta t / 2} \approx 0.0298 \times 10{,}000 \times 0.04 \times \sqrt{1/504} \approx 11.92 \times 0.0445 \approx \$0.53
    $$

    **Vega P&L (per day).** The vega P&L is $\mathcal{V}\,\Delta v$. The daily change in variance under the Heston model has standard deviation:

    $$
    \sigma_{\Delta v} = \xi\sqrt{v_0\,\Delta t} = 0.5 \times \sqrt{0.04 / 252} = 0.5 \times 0.0126 \approx 0.0063
    $$

    With $\mathcal{V} \approx 17.8$:

    $$
    \sigma_{\text{vega}} = |\mathcal{V}| \times \sigma_{\Delta v} \approx 17.8 \times 0.0063 \approx \$0.112
    $$

    **Comparison.** The daily **expected** gamma P&L ($\approx \$0.024$) is larger than the daily expected vega P&L (which is approximately $\mathcal{V}\,\kappa(\theta - v_0)\,\Delta t = 0$ since $v_0 = \theta$). However, in terms of P&L **variance** (which drives hedging risk):

    $$
    \sigma_{\text{gamma}} \approx \$0.53, \qquad \sigma_{\text{vega}} \approx \$0.11
    $$

    The gamma P&L contributes more to daily P&L variance in this example, roughly 5 times more in standard deviation. However, the vega contribution is not negligible and would dominate for longer-dated options (where $\mathcal{V}$ is larger and $\Gamma$ is smaller) or during periods of high vol-of-vol ($\xi > 0.5$).

    Over longer horizons, the vega P&L can accumulate because variance changes are autocorrelated (mean-reverting but persistent), while gamma P&L noise is more diversified across independent daily stock moves. This means the vega contribution to cumulative P&L variance grows faster than $\sqrt{N}$ (where $N$ is the number of days), potentially becoming dominant over monthly or quarterly horizons.

---

**Exercise 5.**
To hedge the vega P&L, a trader can add a variance swap to the portfolio. Explain how: if the delta-hedged call has vega $\mathcal{V}$ and the variance swap has vega $\mathcal{V}_{\text{VS}} = \partial(\text{VS price})/\partial v_0$, what notional of the variance swap neutralizes the vega exposure?

??? success "Solution to Exercise 5"
    A variance swap pays the difference between realized and fixed (strike) variance. Its price under Heston is a function of $v_0$, and its vega is:

    $$
    \mathcal{V}_{\text{VS}} = \frac{\partial V_{\text{VS}}}{\partial v_0}
    $$

    For a variance swap with maturity $T_{\text{VS}}$, the fair strike is:

    $$
    K_{\text{var}} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{T}\int_0^T v_t\,dt\right] = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    The sensitivity to $v_0$ is:

    $$
    \mathcal{V}_{\text{VS}} = \frac{\partial K_{\text{var}}}{\partial v_0} \times \text{notional} = \frac{1 - e^{-\kappa T}}{\kappa T} \times \text{notional}
    $$

    **Hedging the vega exposure.** The delta-hedged call has unhedged vega P&L $\mathcal{V}_{\text{call}}\,dv_t$. To neutralize this, the trader adds $N$ units of variance swap notional such that the total vega is zero:

    $$
    \mathcal{V}_{\text{call}} + N \times \mathcal{V}_{\text{VS}} = 0
    $$

    Solving:

    $$
    N = -\frac{\mathcal{V}_{\text{call}}}{\mathcal{V}_{\text{VS}}}
    $$

    For example, with $\mathcal{V}_{\text{call}} = 17.8$ and a variance swap with $T = 0.5$, $\kappa = 2.0$:

    $$
    \frac{1 - e^{-\kappa T}}{\kappa T} = \frac{1 - e^{-1}}{1} = 1 - 0.368 = 0.632
    $$

    If the variance swap notional is quoted per unit of variance, $\mathcal{V}_{\text{VS}} = 0.632$ per unit notional. The required notional is:

    $$
    N = -\frac{17.8}{0.632} \approx -28.2
    $$

    The trader should **sell** approximately 28.2 units of variance swap notional (since $\mathcal{V}_{\text{call}} > 0$, the long call is long vega, and selling variance swaps provides short vega exposure).

    **Important caveat.** This hedge neutralizes only the first-order vega exposure $\mathcal{V}\,dv$. The residual P&L still contains the volga term $\frac{1}{2}\mathcal{G}\,\xi^2\,v\,dt$ and any mismatch in the vega term structure (the call's vega decays differently with $T$ than the variance swap's vega). A more precise hedge would match the vega at multiple maturities or use vega-weighted positions in variance swaps of different tenors.

---

**Exercise 6.**
Simulate a delta-hedging experiment under Heston: sell a 6-month ATM call, delta-hedge daily using the Heston delta, and record the total P&L across 10,000 paths. Decompose the P&L into gamma, theta, and vega components. Verify that the mean P&L is approximately zero (the hedge is unbiased) and that the standard deviation reflects the unhedged variance risk.

??? success "Solution to Exercise 6"
    **Simulation setup.**

    1. **Model parameters**: $S_0 = 100$, $K = 100$, $T = 0.5$, $r = 0.03$, $q = 0$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$.
    2. **Discretization**: Daily steps, $N = 126$ steps ($T = 0.5$ years $\times$ 252 days/year).
    3. **Paths**: $M = 10{,}000$ independent paths.
    4. **Simulation scheme**: Use the QE (quadratic exponential) scheme for the variance process to ensure $v_t \geq 0$, and log-Euler for the stock price.

    **Delta-hedging algorithm.** On each path $m$ and at each time step $t_i$:

    1. Compute the Heston delta $\Delta_i^m = \Delta(t_i, S_i^m, v_i^m)$ using Fourier inversion (or a fast approximation).
    2. The hedged portfolio P&L over $[t_i, t_{i+1}]$ is:

        $$
        \Delta\Pi_i^m = V(t_{i+1}, S_{i+1}^m, v_{i+1}^m) - V(t_i, S_i^m, v_i^m) - \Delta_i^m(S_{i+1}^m - S_i^m) - r\bigl(V(t_i, S_i^m, v_i^m) - \Delta_i^m S_i^m\bigr)\Delta t
        $$

    3. The total hedged P&L is $\Pi^m = \sum_{i=0}^{N-1} \Delta\Pi_i^m$.

    **P&L decomposition.** At each step, decompose $\Delta\Pi_i^m$ into:

    - **Gamma component**: $\frac{1}{2}\Gamma_i^m (S_i^m)^2 \left[(\Delta S_i^m / S_i^m)^2 - v_i^m \Delta t\right]$
    - **Theta component**: $\Theta_i^m \Delta t + \frac{1}{2}\Gamma_i^m (S_i^m)^2 v_i^m \Delta t - r(V_i^m - \Delta_i^m S_i^m)\Delta t$ (the deterministic part)
    - **Vega component**: $\mathcal{V}_i^m \Delta v_i^m$
    - **Residual**: everything not captured by the above (vanna, volga, higher-order, discretization)

    **Expected results.**

    - **Mean P&L $\approx 0$.** Under the risk-neutral measure with correct model pricing, the expected delta-hedged P&L is zero: $\mathbb{E}[\Pi] = 0$. Across 10,000 paths, the sample mean should be close to zero (within $\pm 2\sigma/\sqrt{M}$).
    - **Standard deviation.** The residual P&L after delta hedging is driven by the unhedged variance risk. From the continuous-time result $d\Pi = \mathcal{V}\,\xi\sqrt{v}\,dW^{(2)}$, the variance of the cumulative P&L is:

        $$
        \operatorname{Var}(\Pi) = \mathbb{E}\!\left[\int_0^T \mathcal{V}^2(t)\,\xi^2\,v_t\,dt\right]
        $$

        With $\mathcal{V} \approx 17.8$ (at inception, decreasing over time), $\xi^2 = 0.25$, $\bar{v} \approx 0.04$:

        $$
        \operatorname{Var}(\Pi) \approx \bar{\mathcal{V}}^2\,\xi^2\,\bar{v}\,T \approx (12)^2 \times 0.25 \times 0.04 \times 0.5 \approx 0.72
        $$

        So $\operatorname{Std}(\Pi) \approx \$0.85$. (Here $\bar{\mathcal{V}} \approx 12$ is the time-averaged vega.)

    - **Decomposition verification.** Summing the gamma, theta, and vega components across all time steps should approximately equal the total P&L for each path. The unexplained residual (from discretization, vanna, volga, higher-order terms) should have a standard deviation of approximately \$0.10--\$0.20 per option, much smaller than the \$0.85 total P&L standard deviation.

    - **Gamma P&L statistics.** The cumulative gamma P&L should have mean $\approx 0$ (since realized variance equals implied on average under the risk-neutral measure) and standard deviation of approximately \$0.30--\$0.50.

    - **Vega P&L statistics.** The cumulative vega P&L should also have mean $\approx 0$ (variance innovations have zero mean) but with a standard deviation of approximately \$0.60--\$0.80, confirming that variance risk is the dominant source of hedging uncertainty.
