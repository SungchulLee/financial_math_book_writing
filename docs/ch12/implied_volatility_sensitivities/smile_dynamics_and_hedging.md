# Smile Dynamics and Hedging


## Introduction


Smile dynamics describe how the implied volatility surface evolves as market conditions change. Understanding these dynamics is essential for **hedging volatility risk** beyond simple vega neutralization. A static view of the smile—treating implied volatility as a fixed input—leads to systematic hedging errors and unexpected P&L. This section develops the theory and practice of dynamic smile hedging.

## Static vs. Dynamic Smiles


### 1. The Static Smile Assumption


A **static smile** assumes the implied volatility surface is fixed in time except for deterministic decay:

$$
\sigma_{\text{IV}}(K, T; t) = \sigma_{\text{IV}}(K, T-t; 0)
$$


Under this assumption:

- The smile shape remains constant
- Only maturity decreases as time passes
- No dependence on spot movements or volatility shocks

**Implications:**

- Delta hedging uses Black-Scholes delta
- Vega hedging is straightforward
- P&L attribution is simple

**Limitation:** Real smiles move in complex ways, violating this assumption.

### 2. The Dynamic Smile Reality


A **dynamic smile** evolves with:

- **Spot movements:** Smile shifts, steepens, or flattens when spot moves
- **Volatility regime shifts:** Overall level changes with market conditions
- **Term structure evolution:** Different maturities respond differently
- **Skew dynamics:** The slope of the smile changes over time

**Consequence:** Delta-hedged options exhibit volatility-driven P&L even when the hedger is delta-neutral.

### 3. Sources of Dynamic Smile Effects


| Source | Description | Impact on Hedging |
|--------|-------------|-------------------|
| Spot-vol correlation | Negative correlation in equities | Vanna effects |
| Volatility mean reversion | Vol converges to long-run level | Term structure changes |
| Jumps | Discrete large moves | Skew steepening |
| Stochastic vol-of-vol | Uncertainty in vol process | Volga effects |
| Event risk | Known future events | Humps in term structure |

## Mathematical Framework for Smile Dynamics


### 1. The Smile as a Function of State Variables


Model the implied volatility surface as a function of state variables:

$$
\sigma_{\text{IV}}(K, T; S_t, v_t, \ldots) = f(K, T, S_t, v_t, \ldots)
$$


where $v_t$ may represent instantaneous variance, a volatility factor, or other state variables.

**Taylor expansion:**

$$
d\sigma_{\text{IV}} = \frac{\partial \sigma}{\partial S} dS + \frac{\partial \sigma}{\partial v} dv + \frac{\partial \sigma}{\partial t} dt + \frac{1}{2}\frac{\partial^2 \sigma}{\partial S^2}(dS)^2 + \ldots
$$


### 2. Smile Sensitivities


Define the following smile sensitivities:

**Spot sensitivity (at fixed strike):**

$$
\Sigma_S := \frac{\partial \sigma_{\text{IV}}(K)}{\partial S}
$$


**Variance sensitivity:**

$$
\Sigma_v := \frac{\partial \sigma_{\text{IV}}(K)}{\partial v}
$$


**Time decay of smile:**

$$
\Sigma_t := \frac{\partial \sigma_{\text{IV}}(K)}{\partial t}
$$


### 3. Stochastic Volatility Perspective


In a stochastic volatility model:

$$
\begin{align}
dS_t &= (r-q) S_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v \\
d\langle W^S, W^v \rangle_t &= \rho dt
\end{align}
$$


The implied volatility depends on both $S_t$ and $v_t$:

$$
\sigma_{\text{IV}}(K, T; S_t, v_t)
$$


The dynamics are:

$$
d\sigma_{\text{IV}} = \Sigma_S dS + \Sigma_v dv + \Sigma_t dt + \text{higher order}
$$


## Smile Dynamics and P&L Attribution


### 1. Option P&L Decomposition


The total P&L of a delta-hedged option position can be decomposed:

$$
\text{P\&L} = \underbrace{\Theta \cdot dt}_{\text{time decay}} + \underbrace{\frac{1}{2}\Gamma (dS)^2}_{\text{gamma P\&L}} + \underbrace{\mathcal{V} \cdot d\sigma_{\text{ATM}}}_{\text{parallel vol}} + \underbrace{\text{Smile effects}}_{\text{residual}}
$$


The "smile effects" capture:

- Changes in skew
- Changes in curvature
- Non-parallel volatility moves

### 2. Detailed P&L Attribution


Expanding the vega term:

$$
\mathcal{V} \cdot d\sigma = \mathcal{V} \cdot \left(\Sigma_S dS + \Sigma_v dv + \Sigma_t dt\right)
$$


**Cross-gamma (Vanna P&L):**

$$
\text{P\&L}_{\text{vanna}} = \mathcal{V} \cdot \Sigma_S \cdot dS
$$


This captures the interaction between spot moves and volatility changes.

**Pure volatility P&L:**

$$
\text{P\&L}_{\text{vol}} = \mathcal{V} \cdot \Sigma_v \cdot dv
$$


This captures changes in the underlying volatility state.

### 3. Second-Order Attribution


Including second-order terms:

$$
\text{P\&L} = \Delta \cdot dS + \Theta \cdot dt + \frac{1}{2}\Gamma (dS)^2 + \mathcal{V} \cdot d\sigma + \text{Vanna} \cdot dS \cdot d\sigma + \frac{1}{2}\text{Volga} \cdot (d\sigma)^2
$$


| Term | Greek | Source |
|------|-------|--------|
| $\Delta \cdot dS$ | Delta | Spot move |
| $\Theta \cdot dt$ | Theta | Time decay |
| $\frac{1}{2}\Gamma (dS)^2$ | Gamma | Spot convexity |
| $\mathcal{V} \cdot d\sigma$ | Vega | Vol level change |
| $\text{Vanna} \cdot dS \cdot d\sigma$ | Vanna | Spot-vol cross |
| $\frac{1}{2}\text{Volga} \cdot (d\sigma)^2$ | Volga | Vol convexity |

## Model-Based Smile Dynamics


Recall (see [§ Dynamic Consistency](../smile_dynamics/dynamic_consistency.md) and [§ Forward Smile](../smile_dynamics/forward_smile.md)): each model class produces a characteristic smile-dynamics signature:

- **Local volatility:** sticky-strike behavior; forward smile flattens over time, inconsistent with persistent empirical skew.
- **Heston / stochastic vol:** ATM level co-moves with $v_t$; spot-vol correlation $\rho < 0$ generates skew, vol-of-vol $\xi$ controls magnitude.
- **SABR ($\beta$):** backbone parameter interpolates between sticky strike ($\beta = 1$) and sticky delta ($\beta = 0$).
- **Bergomi:** forward variance curve $\xi_t^T = \mathbb{E}_t[\sigma_T^2]$ is the primary state, giving direct control over forward-smile dynamics.

For the hedging perspective below, what matters is the implied spot-vol sensitivity $\Sigma_S = \partial \sigma_{\text{IV}}/\partial S$ that each model induces; see [§ Sticky Strike vs Sticky Delta](sticky_strike_vs_sticky_delta.md) for the local-vol $\Rightarrow$ sticky-strike correspondence.

## Hedging Implications


### 1. Delta Hedging Under Smile Dynamics


The "true" delta depends on smile dynamics:

$$
\Delta_{\text{true}} = \Delta_{\text{BS}} + \mathcal{V} \cdot \Sigma_S
$$


where $\Sigma_S = \frac{\partial \sigma_{\text{IV}}(K)}{\partial S}$ is the smile sensitivity to spot.

**Sticky strike:** $\Sigma_S = 0$, so $\Delta_{\text{true}} = \Delta_{\text{BS}}$

**Sticky delta:** $\Sigma_S \neq 0$, requiring adjustment

**Model-implied:** Use the specific model's prediction for $\Sigma_S$

### 2. Vega Hedging Across Strikes


A single ATM option hedge provides **parallel vega** protection but not **skew protection**.

**Skew risk:** If the portfolio has different vega exposures at different strikes, a change in skew creates P&L:

$$
\text{P\&L}_{\text{skew}} = \sum_i \mathcal{V}_i \cdot \Delta\sigma(K_i) - \mathcal{V}_{\text{hedge}} \cdot \Delta\sigma_{\text{ATM}}
$$


**Skew hedge:** Use risk reversals (long OTM put, short OTM call) to hedge skew exposure.

### 3. Vega Hedging Across Maturities


Different maturities respond differently to volatility shocks:

**Term structure risk:** The term structure may steepen or flatten:

$$
\Delta\sigma(T_{\text{long}}) \neq \Delta\sigma(T_{\text{short}})
$$


**Calendar vega:** Use calendar spreads to hedge term structure exposure.

**Vega bucketing:** Decompose vega by maturity bucket and hedge each bucket separately.

### 4. Vanna Hedging


Vanna exposure creates P&L when spot and volatility move together:

$$
\text{P\&L}_{\text{vanna}} \approx \text{Vanna} \cdot \Delta S \cdot \Delta\sigma
$$


**Empirical correlation:** For equities, spot and volatility are negatively correlated:

$$
\mathbb{E}[\Delta S \cdot \Delta\sigma] < 0
$$


**Vanna hedge:** Position in options or variance swaps to neutralize vanna.

### 5. Volga Hedging


Volga exposure creates P&L from volatility convexity:

$$
\text{P\&L}_{\text{volga}} \approx \frac{1}{2} \text{Volga} \cdot (\Delta\sigma)^2
$$


**Large OTM options:** Have significant positive volga, benefiting from vol-of-vol.

**Volga hedge:** Trade options at different strikes to neutralize volga exposure.

## Multi-Factor Hedging


### 1. The Hedging Problem


A portfolio of exotic options has exposures to:

- Spot ($\Delta$)
- Gamma ($\Gamma$)
- ATM volatility ($\mathcal{V}_{\text{ATM}}$)
- Skew ($\mathcal{V}_{\text{skew}}$)
- Term structure ($\mathcal{V}_{T_1}, \mathcal{V}_{T_2}, \ldots$)
- Higher-order Greeks (Vanna, Volga)

**Objective:** Find hedge ratios $h_1, h_2, \ldots$ for available instruments such that total exposure is minimized.

### 2. Linear Hedging


For first-order exposures, solve:

$$
\begin{pmatrix} \Delta_{\text{port}} \\ \mathcal{V}_{\text{ATM,port}} \\ \mathcal{V}_{\text{skew,port}} \end{pmatrix} + \begin{pmatrix} \Delta_1 & \Delta_2 & \Delta_3 \\ \mathcal{V}_{\text{ATM},1} & \mathcal{V}_{\text{ATM},2} & \mathcal{V}_{\text{ATM},3} \\ \mathcal{V}_{\text{skew},1} & \mathcal{V}_{\text{skew},2} & \mathcal{V}_{\text{skew},3} \end{pmatrix} \begin{pmatrix} h_1 \\ h_2 \\ h_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}
$$


This requires at least as many hedging instruments as exposures.

### 3. Practical Instrument Selection


**Liquid instruments for hedging:**

| Exposure | Typical Hedge |
|----------|---------------|
| Delta | Underlying, futures |
| ATM vega | ATM options, variance swaps |
| Skew | Risk reversals (25D) |
| Term structure | Calendar spreads |
| Gamma | ATM options |
| Vanna | Risk reversals, OTM options |
| Volga | Strangles, butterflies |

### 4. Hedge Ratio Estimation


**Model-based:** Use a calibrated model to compute Greeks and solve for hedge ratios.

**Empirical:** Estimate sensitivities from historical data:

$$
\Delta\sigma_{\text{port}} = \beta_1 \Delta\sigma_{\text{ATM}} + \beta_2 \Delta\text{skew} + \epsilon
$$


**Hybrid:** Combine model guidance with empirical adjustments.

## Numerical Example: Smile Hedging


### 1. Setup


**Portfolio:** Long 1-year ATM call, short 6-month 25-delta put

**Market data:**

- $S_0 = 100$, $r = 5\%$, $q = 0$
- ATM vol (1Y): 22%
- ATM vol (6M): 20%
- 25D put vol (6M): 25%

**Greeks:**

| Position | Delta | Vega (ATM) | Vega (25D) |
|----------|-------|------------|------------|
| Long 1Y ATM call | 0.57 | +25.5 | 0 |
| Short 6M 25D put | +0.15 | 0 | -12.3 |
| **Total** | 0.72 | +25.5 | -12.3 |

### 2. Scenario Analysis


**Scenario A: Parallel vol up 2%**

$$
\text{P\&L} \approx 25.5 \times 0.02 - 12.3 \times 0.02 = 0.51 - 0.25 = +\$0.26
$$


**Scenario B: Skew steepens (25D put vol up 3%, ATM unchanged)**

$$
\text{P\&L} \approx 0 - 12.3 \times 0.03 = -\$0.37
$$


**Scenario C: Spot down 5%, vol up 2%**

$$
\text{P\&L}_{\Delta} = 0.72 \times (-5) = -\$3.60
$$

$$
\text{P\&L}_{\text{vol}} \approx +\$0.26 \text{ (as in A)}
$$

$$
\text{Total} \approx -\$3.34
$$


### 3. Hedge Construction


**Objective:** Neutralize delta, ATM vega, and skew exposure.

**Instruments:**

- Underlying (hedge delta)
- 6M ATM straddle (hedge ATM vega)
- 6M 25D risk reversal (hedge skew)

**Solution:** (simplified)

- Short 72 shares of underlying
- Short some ATM straddles to reduce ATM vega
- Long 25D risk reversal to offset short 25D put exposure

## Dynamic Consistency Considerations


Recall (see [§ Dynamic Consistency](../smile_dynamics/dynamic_consistency.md) and [§ Forward Smile](../smile_dynamics/forward_smile.md)) for the definition of dynamic consistency, the model-by-model classification, and the forward-smile diagnostic. The **hedging consequence** is the focus here: when a model is dynamically inconsistent (e.g., local vol, whose forward smile flattens too quickly), today's hedge ratios will mis-price tomorrow's exposure, recalibration injects P&L noise, and hedging effectiveness decays over the rebalancing horizon. Mitigation: prefer models with realistic forward-smile behavior, hedge with model-robust instruments (variance swaps), and rebalance frequently.

## Empirical Smile Dynamics


Recall (see [§ Empirical Stylized Facts](../smile_dynamics/empirical_stylized_facts.md)) for the stylized facts (SPX $\rho\approx -0.7$, skew steepens after down moves, FX cross-pair variation, single-stock idiosyncrasies), the quantitative measures (vol-spot beta $\approx -2$, skew-spot beta $\approx -0.4$, ATM-IV realized vol $\approx 3$-$5\%$), and the relevant time scales (intraday spot-vol correlation, days-to-weeks vol mean reversion, weeks-to-months skew normalization). The hedging consequences are developed in this section.

## Summary


Smile dynamics are central to volatility hedging:

### 1. Static vs. Dynamic

- **Static smile:** Fixed in time, delta = BS delta
- **Dynamic smile:** Evolves with spot, vol, time
- **Reality:** Smiles are highly dynamic

### 2. Model Perspectives

| Model | Smile Dynamics | Forward Smile |
|-------|---------------|---------------|
| Local vol | Sticky strike | Flattens |
| Stochastic vol | Leverage-driven | Persists |
| SABR | Adjustable via $\beta$ | Model-dependent |
| Bergomi | Realistic | Calibrated |

### 3. Hedging Requirements

- **Delta:** Adjust for smile dynamics ($\Sigma_S$)
- **Vega:** Bucket by strike and maturity
- **Vanna:** Hedge spot-vol cross-effects
- **Volga:** Hedge vol convexity

### 4. P&L Attribution

$$
\text{P\&L} = \Delta \cdot dS + \Theta \cdot dt + \frac{1}{2}\Gamma (dS)^2 + \mathcal{V} \cdot d\sigma + \text{Vanna} \cdot dS \cdot d\sigma + \frac{1}{2}\text{Volga} \cdot (d\sigma)^2
$$

### 5. Dynamic Consistency

- Most models are dynamically inconsistent
- Causes hedging degradation over time
- Forward smile diagnostics help identify issues

### 6. Empirical Regularities

- Negative spot-vol correlation in equities
- Skew steepens after down moves
- Vol mean-reverts over days to weeks
- Term structure inverts during stress

Effective volatility hedging requires understanding and managing all these dimensions of smile dynamics.

---

## Further Reading


- Derman, E. and Kani, I. *The Volatility Smile and Its Implied Tree*. Local volatility and smile dynamics.
- Bergomi, L. *Stochastic Volatility Modeling*. Comprehensive treatment of smile dynamics and hedging.
- Gatheral, J. *The Volatility Surface*. Empirical smile behavior and model comparison.
- Rebonato, R. *Volatility and Correlation*. Practical hedging under uncertain dynamics.
- Cont, R. and Kokholm, T. *A Consistent Pricing Model for Index Options and Volatility Derivatives*. Joint modeling of smile and VIX.

---

## Exercises

**Exercise 1.** A delta-hedged option portfolio has $\Gamma = 0.05$, $\mathcal{V} = 15.0$, $\text{Vanna} = -0.12$, $\text{Volga} = 2.5$, and $\Theta = -0.08$. The spot moves $\Delta S = -3$ and implied volatility moves $\Delta\sigma = +0.015$ over one day ($\Delta t = 1/252$). Compute the full second-order P&L decomposition and identify which term contributes the most.

??? success "Solution to Exercise 1"
    We compute each term in the P&L decomposition using the given Greeks and market moves.

    **Given:** $\Gamma = 0.05$, $\mathcal{V} = 15.0$, $\text{Vanna} = -0.12$, $\text{Volga} = 2.5$, $\Theta = -0.08$, $\Delta S = -3$, $\Delta\sigma = +0.015$, $\Delta t = 1/252$.

    The full second-order P&L is:

    $$
    \text{P\&L} = \Theta\,\Delta t + \tfrac{1}{2}\Gamma(\Delta S)^2 + \mathcal{V}\,\Delta\sigma + \text{Vanna}\,\Delta S\,\Delta\sigma + \tfrac{1}{2}\text{Volga}\,(\Delta\sigma)^2
    $$

    Computing each term:

    - **Theta:** $\Theta\,\Delta t = -0.08 \times (1/252) = -0.000317$
    - **Gamma:** $\frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2}\times 0.05 \times 9 = +0.225$
    - **Vega:** $\mathcal{V}\,\Delta\sigma = 15.0 \times 0.015 = +0.225$
    - **Vanna:** $\text{Vanna}\,\Delta S\,\Delta\sigma = -0.12 \times (-3)\times 0.015 = +0.0054$
    - **Volga:** $\frac{1}{2}\text{Volga}\,(\Delta\sigma)^2 = \frac{1}{2}\times 2.5 \times 0.000225 = +0.000281$

    **Total P&L:**

    $$
    \text{P\&L} \approx -0.000317 + 0.225 + 0.225 + 0.0054 + 0.000281 \approx +0.4554
    $$

    The two dominant contributors are the **gamma P&L** ($+0.225$) and the **vega P&L** ($+0.225$), each contributing roughly equally and together accounting for nearly all of the total. Theta, vanna, and volga are comparatively negligible. In this scenario, the portfolio benefits from both the realized large spot move (gamma) and the concurrent rise in implied volatility (vega).

---

**Exercise 2.** Explain the difference between a static smile and a dynamic smile. In the context of the Heston model, describe how each of the parameters $\rho$, $\xi$, and $\kappa$ affects the dynamics of the smile when the spot price decreases by 5%.

??? success "Solution to Exercise 2"
    A **static smile** assumes the implied volatility surface is fixed except for deterministic time decay. It does not change in response to spot movements or volatility regime shifts. A **dynamic smile** evolves as a function of spot price, variance, and other state variables, capturing real-market behavior.

    In the **Heston model**, the dynamics are governed by:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^v, \quad d\langle W^S, W^v\rangle = \rho\,dt
    $$

    When the spot decreases by 5%:

    - **$\rho$ (spot-vol correlation):** With $\rho < 0$ (typical for equities), a spot decrease is associated with an increase in $v_t$. This shifts the entire smile upward and steepens the skew, because the negative correlation amplifies the leverage effect: falling prices coincide with rising volatility.
    - **$\xi$ (vol-of-vol):** A larger $\xi$ means $v_t$ responds more violently to the Brownian shock $dW_t^v$. When spot drops and vol rises (via $\rho < 0$), a high $\xi$ amplifies the variance increase, making the smile shift more dramatic and increasing the curvature (wings) of the smile.
    - **$\kappa$ (mean-reversion speed):** A larger $\kappa$ dampens the effect of spot-driven volatility changes because variance reverts more quickly to $\theta$. With high $\kappa$, the initial vol spike after a 5% spot drop is partially absorbed, and the smile shift is more transient. With low $\kappa$, the volatility increase persists longer and the dynamic smile effects are more pronounced.

---

**Exercise 3.** The "true" delta under smile dynamics is $\Delta_{\text{true}} = \Delta_{\text{BS}} + \mathcal{V} \cdot \Sigma_S$, where $\Sigma_S = \partial \sigma_{\text{IV}}(K)/\partial S$. For an ATM call with $\Delta_{\text{BS}} = 0.55$, $\mathcal{V} = 20$, and $\Sigma_S = -0.003$ (implied by leverage effect), compute $\Delta_{\text{true}}$. How many additional shares should the hedger hold compared to the Black-Scholes delta?

??? success "Solution to Exercise 3"
    The true delta under smile dynamics is:

    $$
    \Delta_{\text{true}} = \Delta_{\text{BS}} + \mathcal{V}\cdot\Sigma_S
    $$

    Substituting $\Delta_{\text{BS}} = 0.55$, $\mathcal{V} = 20$, and $\Sigma_S = -0.003$:

    $$
    \Delta_{\text{true}} = 0.55 + 20 \times (-0.003) = 0.55 - 0.06 = 0.49
    $$

    The true delta is 0.49, compared to the Black-Scholes delta of 0.55. The hedger should hold $0.49 - 0.55 = -0.06$ additional shares per option compared to the Black-Scholes delta, meaning 6 fewer shares per 100 options.

    The negative $\Sigma_S$ reflects the leverage effect: when spot rises, IV tends to fall, which partially offsets the price increase. The correct hedge therefore requires a smaller position in the underlying.

---

**Exercise 4.** Compare the forward smile behavior of local volatility models versus stochastic volatility models. (a) Why does the local volatility model produce a forward smile that flattens over time? (b) Why is this inconsistent with empirical observations? (c) How do stochastic volatility models improve upon this?

??? success "Solution to Exercise 4"
    **(a)** In the local volatility model, the local volatility surface $\sigma_{\text{loc}}(S,t)$ is calibrated to match today's implied volatility surface exactly. The forward smile (the smile of forward-starting options) is determined by the future local volatility values along paths. Since $\sigma_{\text{loc}}(S,t)$ is a fixed deterministic function, the dispersion of future paths narrows as time progresses. For a forward-start option beginning at $T_1$, the effective volatility variation across strikes is driven only by the local vol surface in $[T_1, T_2]$. As $T_1$ increases, the conditional distribution of $S_{T_1}$ concentrates (by the law of large numbers for the diffusion), so the relevant portion of the local vol surface is traversed in a narrower range, producing a flatter forward smile.

    **(b)** Empirically, the volatility smile is persistent: the skew observed in short-dated options reappears in forward-start options and in the realized smiles of future option chains. The local volatility prediction of a flattening forward smile contradicts this stylized fact. Market participants consistently observe that forward skew remains steep, especially in equity indices.

    **(c)** Stochastic volatility models (e.g., Heston) introduce an additional random factor $v_t$ that evolves independently of the diffusion. Even conditioned on future time $T_1$, the variance $v_{T_1}$ remains random, so the forward smile retains curvature and skew. The correlation $\rho$ between spot and variance ensures that skew persists in the forward smile. This matches empirical observations far better than local volatility.

---

**Exercise 5.** A portfolio is long a 1-year ATM call (vega = \$25.5 at ATM, zero at 25-delta) and short a 6-month 25-delta put (vega = \$0 at ATM, \$12.3 at 25-delta). Construct a hedge using a 6-month ATM straddle and a 6-month 25-delta risk reversal. Set up the linear system to solve for the hedge ratios that neutralize both ATM vega and 25-delta vega exposures.

??? success "Solution to Exercise 5"
    The portfolio exposures are:

    | | ATM vega | 25-delta vega |
    |---|---------|---------------|
    | Long 1Y ATM call | $+25.5$ | $0$ |
    | Short 6M 25D put | $0$ | $-12.3$ |
    | **Portfolio** | $+25.5$ | $-12.3$ |

    Let the hedge instruments have the following vega profiles. Denote the 6M ATM straddle vega at ATM as $\mathcal{V}_{\text{str}}^{\text{ATM}}$ and at 25-delta as $\mathcal{V}_{\text{str}}^{25}$, and the 6M 25D risk reversal vega at ATM as $\mathcal{V}_{\text{RR}}^{\text{ATM}}$ and at 25-delta as $\mathcal{V}_{\text{RR}}^{25}$.

    Let $h_1$ = number of straddles and $h_2$ = number of risk reversals. The linear system to neutralize both exposures is:

    $$
    \begin{pmatrix} \mathcal{V}_{\text{str}}^{\text{ATM}} & \mathcal{V}_{\text{RR}}^{\text{ATM}} \\ \mathcal{V}_{\text{str}}^{25} & \mathcal{V}_{\text{RR}}^{25} \end{pmatrix} \begin{pmatrix} h_1 \\ h_2 \end{pmatrix} = \begin{pmatrix} -25.5 \\ +12.3 \end{pmatrix}
    $$

    The right-hand side is the negative of the portfolio exposures. In a typical setup, the ATM straddle has large ATM vega and small 25-delta vega, while the risk reversal has small ATM vega but significant 25-delta vega. This makes the matrix well-conditioned, and the system has a unique solution $h_1, h_2$ that simultaneously neutralizes both vega buckets.

---

**Exercise 6.** Define dynamic consistency for a volatility model. Explain why local volatility models fail the dynamic consistency test in practice. What diagnostic tool (involving the forward smile) can be used to detect dynamic inconsistency?

??? success "Solution to Exercise 6"
    A volatility model is **dynamically consistent** if, after calibrating to today's implied volatility surface and evolving the model forward in time, the resulting implied volatility surface at a future date matches what the market would produce upon recalibration. Formally, the model's predicted future smile should be consistent with the smile that would be calibrated from future option prices.

    **Local volatility models fail** dynamic consistency because:

    - The local vol surface $\sigma_{\text{loc}}(S,t)$ is fixed at calibration. When the market evolves and the model is recalibrated, a different $\sigma_{\text{loc}}$ surface is obtained.
    - The model predicts that forward smiles flatten over time (as discussed in Exercise 4), but empirical recalibration produces persistent skew.
    - Daily recalibration produces a sequence of different local vol surfaces, each inconsistent with the previous day's model evolution.

    **Diagnostic tool:** The **forward smile** serves as a key diagnostic. One computes the model-implied forward smile (the implied volatility surface of forward-starting options) and compares it to:

    1. Historically realized future smiles, and
    2. The market-implied forward smile extracted from calendar spread prices.

    If the model's forward smile flattens significantly faster than observed in the market, the model is dynamically inconsistent. Stochastic volatility models generally produce forward smiles that are closer to market observations, though they are not perfectly consistent either.

---

**Exercise 7.** Using the empirical data for SPX (vol-spot beta $\approx -2.0$ and skew-spot beta $\approx -0.4$), estimate the change in ATM implied volatility and skew when the SPX drops by 3%. If a trader holds a portfolio that is vega-neutral but has positive skew exposure, will the portfolio gain or lose money? Explain.

??? success "Solution to Exercise 7"
    The vol-spot beta relates ATM IV changes to log-spot changes:

    $$
    \Delta\sigma_{\text{ATM}} \approx \text{(vol-spot beta)} \times \frac{\Delta S}{S}
    $$

    For a 3% drop ($\Delta S/S = -0.03$):

    $$
    \Delta\sigma_{\text{ATM}} \approx (-2.0)\times(-0.03) = +0.06 = +6\%
    $$

    ATM implied volatility rises by approximately 6 percentage points.

    The skew-spot beta relates skew changes to log-spot changes:

    $$
    \Delta(\text{skew}) \approx (-0.4)\times(-0.03) = +0.012
    $$

    The skew steepens by approximately 1.2 percentage points (becomes more negative in the conventional sense that OTM put IVs rise more than ATM).

    For the trader who is vega-neutral but has positive skew exposure:

    - **Vega-neutral:** The parallel rise of 6% in ATM vol does not directly affect the portfolio (net vega is zero).
    - **Positive skew exposure:** The portfolio benefits when skew steepens. Since the 3% spot drop causes the skew to steepen (OTM put IVs rise more than ATM IVs), the positive skew position **gains money**.

    The P&L from the skew move is approximately proportional to the skew exposure times $\Delta(\text{skew}) = +0.012$. The portfolio profits because the skew steepening is in the direction that benefits a long skew position.
