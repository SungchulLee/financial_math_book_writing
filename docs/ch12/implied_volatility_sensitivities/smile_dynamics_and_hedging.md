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


### 1. Local Volatility Dynamics


In local volatility models, the smile dynamics are fully determined by the local volatility surface:

$$
\sigma_{\text{loc}}(S, t) = \sigma_{\text{loc}}(S, t) \quad \text{(fixed)}
$$


**Key property:** The local vol model produces **sticky strike** behavior:
- IV at each strike is fixed
- When spot moves, the option "visits" different parts of the local vol surface
- No smile-related P&L at fixed strike

**Forward smile:** The local vol model implies a specific forward smile that typically **flattens** over time:

$$
\sigma_{\text{fwd}}(K, T_1, T_2) \to \text{flat as } T_1 \to \infty
$$


This is inconsistent with persistent empirical skew, a major shortcoming of local vol.

### 2. Stochastic Volatility Dynamics (Heston)


The Heston model produces richer smile dynamics:

**ATM volatility:**

$$
\sigma_{\text{ATM}}^2 \approx v_t + \text{corrections}
$$


So ATM volatility moves with the variance process $v_t$.

**Skew:**

$$
\text{Skew} \propto \rho \cdot \xi
$$


The spot-vol correlation $\rho$ generates skew, and vol-of-vol $\xi$ affects its magnitude.

**Smile dynamics:**
- When $v_t$ increases, the entire smile shifts up
- When $S_t$ decreases (with $\rho < 0$), $v_t$ tends to increase, steepening the skew
- This creates **leverage-like dynamics**

### 3. SABR Dynamics


The SABR model:

$$
\begin{align}
dF_t &= \alpha_t F_t^\beta dW_t^F \\
d\alpha_t &= \nu \alpha_t dW_t^\alpha \\
d\langle W^F, W^\alpha \rangle &= \rho dt
\end{align}
$$


**Backbone parameter $\beta$:**
- $\beta = 1$: Lognormal dynamics, sticky strike behavior
- $\beta = 0$: Normal dynamics, sticky delta behavior
- $0 < \beta < 1$: Intermediate

**SABR smile dynamics:**
- The parameter $\alpha_t$ (ATM vol) evolves stochastically
- Skew is controlled by $\rho$ and $\nu$
- The model can match both smile shape and basic dynamics

### 4. Bergomi's Framework


Bergomi models the forward variance curve directly:

$$
\xi_t^T = \mathbb{E}_t[\sigma_T^2]
$$


The dynamics:

$$
d\xi_t^T = \xi_t^T \cdot \omega(T-t) \cdot dZ_t
$$


**Key insight:** By specifying how forward variances evolve, Bergomi's model can match:
- Realistic smile dynamics
- Forward smile behavior
- Term structure of skew

This framework provides a unified approach to smile dynamics and is widely used in equity derivatives.

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


### 1. The Dynamic Consistency Problem


A model is **dynamically consistent** if:
- Calibrated to today's surface
- Evolved forward under the model
- The resulting surface matches future recalibration

**Violation:** Most models exhibit dynamic inconsistency:
- Local vol: Forward smile flattens unrealistically
- Stochastic vol: Better but not perfect
- Market-implied: Not a model, just interpolation

### 2. Consequences for Hedging


**If the model is dynamically inconsistent:**
- Today's hedge ratios may be wrong for tomorrow's market
- Recalibration introduces P&L noise
- Hedging effectiveness degrades over time

**Mitigation:**
- Use models with better dynamic properties
- Hedge with robust instruments (variance swaps)
- Frequent recalibration and hedge adjustment

### 3. Forward Smile as a Diagnostic


The **forward smile** reveals model dynamics:

$$
\sigma_{\text{fwd}}(K, T_1, T_2) = \text{IV of forward-start option}
$$


**Local vol:** Forward smile flattens quickly
**Stochastic vol:** Forward smile persists but may steepen/flatten
**Empirical:** Forward smile should reflect expected future dynamics

Comparing model-implied forward smiles to historical smile behavior is a key model validation tool.

## Empirical Smile Dynamics


### 1. Stylized Facts


**Equity indices (SPX, EURO STOXX):**
- Negative spot-vol correlation: $\rho \approx -0.7$
- Skew steepens after down moves
- Vol spikes decay within days to weeks
- Term structure inverts during stress

**FX markets:**
- Spot-vol correlation varies by pair
- EUR/USD: near zero correlation
- EM pairs: often positive correlation

**Individual stocks:**
- More idiosyncratic behavior
- Earnings-driven dynamics
- Jump risk dominates

### 2. Quantitative Measures


**Skew-spot beta:**

$$
\frac{d(\text{skew})}{d(\text{log spot})} \approx -0.3 \text{ to } -0.5 \text{ for SPX}
$$


**Vol-spot beta:**

$$
\frac{d(\sigma_{\text{ATM}})}{d(\text{log spot})} \approx -1.5 \text{ to } -2.5 \text{ for SPX}
$$


**Vol-of-vol:**

$$
\text{Realized vol of ATM IV} \approx 3\% \text{ to } 5\% \text{ annualized}
$$


### 3. Time Scales


| Effect | Time Scale |
|--------|------------|
| Spot-vol correlation | Intraday to daily |
| Vol mean reversion | Days to weeks |
| Skew normalization | Weeks to months |
| Term structure normalization | Months |

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
