# Bridge to Stochastic Volatility

The preceding sections have identified two fundamental limitations of local volatility: its sticky strike smile dynamics and its systematic flattening of the forward smile. Both failures stem from the same root cause -- the volatility process has no independent source of randomness. Resolving these limitations requires introducing a stochastic volatility factor, making the instantaneous volatility a random process with its own Brownian driver. This section develops the bridge from local volatility to stochastic volatility, explains how Gyongy's theorem connects the two frameworks, introduces the stochastic local volatility (SLV) model that combines the strengths of both, and derives the leverage function that links them. The goal is not to abandon local volatility but to understand its precise role as the Markovian projection of richer dynamics.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Explain why the limitations of local volatility necessitate stochastic volatility
    - State the general stochastic volatility framework and identify its key parameters
    - Apply Gyongy's theorem to derive the local volatility function from any SV model
    - Define the stochastic local volatility model and derive the leverage function
    - Compare the exotic option pricing properties of LV, SV, and SLV models
    - Describe the calibration procedure for SLV models

## Why Stochastic Volatility is Needed

### Summary of Local Volatility Failures

The local volatility model produces:

1. **Smile dynamics**: Approximately sticky strike, while markets are between sticky strike and sticky delta
2. **Spot-vol correlation**: $\rho_{S,\sigma} = -1$ (perfect), while markets show $|\rho| \approx 0.5$-$0.8$
3. **Vol-of-vol**: Zero residual vol-of-vol, while markets exhibit significant independent vol randomness
4. **Forward smile**: Systematically too flat, underpricing forward-starting options and cliquets

All four failures trace to a single structural property: in the local volatility model, volatility $\sigma_{\text{loc}}(S_t, t)$ is a **deterministic** function of $(S_t, t)$. Knowing the spot path completely determines the volatility path.

### What Stochastic Volatility Adds

A stochastic volatility model introduces an independent volatility factor:

$$
dS_t = (r - q)S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \alpha(v_t, t) \, dt + \beta(v_t, t) \, dW_t^{(2)}
$$

with $\text{Corr}(dW_t^{(1)}, dW_t^{(2)}) = \rho \, dt$, where $\rho \in [-1, 1]$ is the spot-vol correlation.

The key new elements are:

- **Vol-of-vol** $\beta$: Controls the amplitude of volatility fluctuations independent of spot
- **Spot-vol correlation** $\rho$: Controls the asymmetry (skew) of the smile; $\rho < 0$ produces downward skew
- **Mean reversion** $\alpha$: Controls the persistence of volatility shocks and the term structure
- **Two Brownian motions**: The market is incomplete (two sources of risk, one traded asset), so there is a family of equivalent martingale measures

## The Gyongy Connection

### From Stochastic to Local Volatility

Gyongy's theorem (developed in detail in the Gyongy's Theorem and Markovian Projection section) establishes the precise link between any stochastic volatility model and its local volatility projection.

**Theorem 13.5.2** (Gyongy Projection, Recalled).
Given the stochastic volatility model above, the local volatility function that matches all marginal distributions of $S_t$ is:

$$
\sigma_{\text{loc}}^2(K, t) = \mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]
$$

This conditional expectation averages the instantaneous variance $v_t$ over all paths that reach level $K$ at time $t$. Different stochastic volatility models (Heston, SABR, Bergomi) produce different conditional expectations and hence different local volatility surfaces -- but all of these surfaces are consistent with the same vanilla option prices.

### Implications for Model Choice

The Gyongy projection clarifies the model selection problem:

1. **Vanilla pricing**: All models calibrated to the same vanilla surface have the same Gyongy projection. Local volatility is the unique one-factor summary of any model's vanilla-pricing content.
2. **Exotic pricing**: The choice between models matters only for path-dependent and forward smile-dependent products, where the conditional distributions $\text{Law}(S_T \mid S_t = K)$ differ.
3. **Dupire = Gyongy**: Applying Dupire's formula to market prices computes the Gyongy projection of whatever process generated those prices. The formula does not know or care about the underlying model.

## The Stochastic Local Volatility Framework

### Model Specification

The **stochastic local volatility (SLV)** model combines both approaches:

$$
dS_t = (r - q)S_t \, dt + L(S_t, t)\sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi\sqrt{v_t} \, dW_t^{(2)}
$$

with $\text{Corr}(dW_t^{(1)}, dW_t^{(2)}) = \rho \, dt$, where $L(S, t)$ is the **leverage function** -- a deterministic function that adjusts the SV model to match vanilla prices exactly.

The SLV model has two components:

- **Stochastic volatility** $\sqrt{v_t}$: Provides realistic smile dynamics, vol-of-vol, and spot-vol decorrelation
- **Leverage function** $L(S, t)$: Ensures exact calibration to the vanilla surface

### The Leverage Function

**Theorem 13.5.3** (Leverage Function from Gyongy Projection).
The leverage function satisfies:

$$
L^2(K, t) = \frac{\sigma_{\text{loc}}^2(K, t)}{\mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]}
$$

where $\sigma_{\text{loc}}(K, t)$ is the Dupire local volatility computed from market prices.

*Proof.* By Gyongy's theorem, the local volatility of the SLV model is:

$$
\sigma_{\text{loc, SLV}}^2(K, t) = \mathbb{E}^{\mathbb{Q}}[L^2(S_t, t) v_t \mid S_t = K] = L^2(K, t) \mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]
$$

where we used the fact that $L(S_t, t) = L(K, t)$ is deterministic given $S_t = K$. For the SLV model to match market prices, we need $\sigma_{\text{loc, SLV}}^2 = \sigma_{\text{loc}}^2$ (the Dupire local volatility from market data). Solving:

$$
L^2(K, t) = \frac{\sigma_{\text{loc}}^2(K, t)}{\mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]}
$$

$\square$

### Interpretation

The leverage function is the **ratio** of:

- **Market target**: $\sigma_{\text{loc}}^2(K, t)$, the local volatility surface from Dupire's formula
- **SV baseline**: $\mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]$, the conditional average variance from the stochastic volatility component

Where the SV model produces too little conditional variance relative to the market target, $L > 1$ amplifies the volatility. Where the SV model produces too much, $L < 1$ dampens it.

**Limiting cases:**

- If $L(S, t) \equiv 1$: The SLV model reduces to pure stochastic volatility ($\sigma_{\text{loc}}^2 = \mathbb{E}[v_t \mid S_t]$)
- If $v_t \equiv 1$: The SLV model reduces to pure local volatility ($L(S, t) = \sigma_{\text{loc}}(S, t)$)
- In general: $L$ interpolates between these extremes, with the SV component controlling the dynamics and the leverage function absorbing the calibration residual

## Calibration of the SLV Model

### The Particle Method

The conditional expectation $\mathbb{E}[v_t \mid S_t = K]$ does not have a closed form in general. The standard calibration procedure uses a **particle method** (Monte Carlo forward simulation):

**Algorithm** (SLV Calibration):

1. Fix the SV parameters $(\kappa, \theta, \xi, \rho, v_0)$ and compute $\sigma_{\text{loc}}(K, t)$ from market data via Dupire's formula
2. Simulate $N$ paths of $(S_t^{(i)}, v_t^{(i)})$ on a time grid $\{t_0, t_1, \ldots, t_M\}$ using the SV dynamics with $L \equiv 1$ initially
3. At each time step $t_k$, estimate $\mathbb{E}[v_{t_k} \mid S_{t_k} = K_j]$ by binning paths:

    $$
    \hat{\mathbb{E}}[v_{t_k} \mid S_{t_k} \approx K_j] = \frac{\sum_{i: S_{t_k}^{(i)} \in \text{bin}(K_j)} v_{t_k}^{(i)}}{\#\{i: S_{t_k}^{(i)} \in \text{bin}(K_j)\}}
    $$

4. Compute $L^2(K_j, t_k) = \sigma_{\text{loc}}^2(K_j, t_k) / \hat{\mathbb{E}}[v_{t_k} \mid S_{t_k} \approx K_j]$
5. Re-simulate with the updated $L$ and iterate until convergence

This iterative procedure converges because the leverage function adjusts the marginal distributions of $S_t$ to match the Dupire target.

### The Mixing Parameter

In practice, the SLV model is controlled by a **mixing parameter** $\eta \in [0, 1]$:

$$
dS_t = (r-q)S_t \, dt + L(S_t, t) v_t^{\eta/2} S_t \, dW_t^{(1)}
$$

- $\eta = 0$: Pure local volatility ($v_t^0 = 1$, all dynamics from $L$)
- $\eta = 1$: Full stochastic volatility component, leverage function adjusts for calibration
- Intermediate $\eta$: Blends the two, controlling the balance between static fit and dynamic realism

Practitioners typically set $\eta$ based on the desired vol-of-vol and forward smile properties, with $\eta \in [0.5, 1.0]$ being common.

## Comparison of Model Families

### Pricing Properties

| Property | Local Vol | Stochastic Vol | SLV |
|----------|----------|----------------|-----|
| Vanilla calibration | Perfect | Approximate | Perfect |
| Smile dynamics | Sticky strike | Realistic | Realistic |
| Vol-of-vol | Zero | $\xi$ (parameter) | $\eta \xi$ (tunable) |
| Forward smile | Too flat | Persistent | Persistent |
| Barrier options | Biased | Better | Best |
| Cliquets | Underpriced | Overpriced (if miscalibrated) | Accurate |
| Complexity | Low | Medium | High |

### Hedging Properties

The delta hedging performance differs across models:

**Proposition 13.5.4** (Delta Decomposition Under SLV).
The SLV delta can be decomposed as:

$$
\Delta_{\text{SLV}} = \Delta_{\text{BS}} + \text{Vega}_{\text{BS}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{\text{SLV}}
$$

where the implied vol sensitivity $\partial_{S_0}\sigma_{\text{imp}}|_{\text{SLV}}$ lies between the local volatility and pure stochastic volatility predictions:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{\text{SV}} < \frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{\text{SLV}} < \frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{\text{LV}}
$$

The SLV delta is a blend of the LV delta and the SV delta, with the mixing controlled by $\eta$.

## From Chapter 13 to Chapter 14

### The Modeling Hierarchy

The progression through volatility models follows a natural hierarchy:

1. **Black-Scholes** (Chapter 6): Constant volatility, flat smile, complete market, tractable
2. **Local Volatility** (Chapter 13): State-dependent volatility, perfect vanilla fit, complete market, wrong dynamics
3. **Stochastic Volatility** (Chapter 14): Random volatility, realistic dynamics, incomplete market, imperfect vanilla fit
4. **Stochastic Local Volatility**: Combined approach, perfect fit with realistic dynamics, highest complexity

Each step adds modeling power but also complexity. The key insight from local volatility is that **fitting vanilla prices is a necessary but not sufficient condition for a good model**. The additional requirements -- realistic smile dynamics, correct forward smiles, accurate exotic pricing -- necessitate the stochastic volatility framework developed in the next chapter.

### What to Expect in Chapter 14

Chapter 14 develops the stochastic volatility framework in full generality:

- **Heston model**: The canonical two-factor model with CIR variance dynamics, semi-analytical pricing via Fourier transforms
- **SABR model**: The standard model for interest rate derivatives, with an explicit implied volatility approximation
- **Bergomi models**: Forward variance models that directly parameterize the forward smile
- **Rough volatility**: Models with non-Markovian, fractional Brownian motion driving the variance

The Gyongy connection ensures that all of these models have a local volatility shadow, and the leverage function formalism provides a unified calibration framework.

??? example "When to Use Which Model"

    **European options only (vanilla book):**
    Use local volatility. It is the simplest model that perfectly calibrates to the vanilla surface, and the smile dynamics are irrelevant for a book of Europeans.

    **Barrier options (single barrier, standard terms):**
    Use stochastic local volatility with moderate mixing ($\eta \approx 0.5$-$0.7$). The barrier prices are sensitive to smile dynamics, and the SLV model provides a good balance of calibration accuracy and dynamic realism.

    **Cliquets and forward-starting options:**
    Use stochastic volatility (Heston or Bergomi) calibrated as closely as possible to the vanilla surface, or SLV with high mixing ($\eta \approx 0.8$-$1.0$). The forward smile is the dominant pricing driver, and local volatility severely underprices these products.

    **Variance swaps and vol derivatives:**
    Use stochastic volatility with calibrated vol-of-vol. The payoff depends directly on the distribution of realized variance, which is determined by the vol-of-vol parameter $\xi$.

    **Hedging exotic positions:**
    Use SLV for computing hedge ratios (deltas, vegas). The SLV delta incorporates both the static smile effect (via $L$) and the dynamic smile effect (via $\eta$), providing more robust hedges than either pure LV or pure SV.

## Summary

The bridge from local volatility to stochastic volatility is built on three pillars:

1. **Gyongy's theorem**: Every stochastic volatility model has a local volatility projection $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}[v_t \mid S_t = K]$ that matches all vanilla prices. Local volatility is the Markovian shadow of any diffusion model.
2. **The leverage function**: The SLV model $dS = (r-q)S\,dt + L(S,t)\sqrt{v_t}S\,dW^{(1)}$ combines exact calibration (through $L$) with realistic dynamics (through $v_t$), with $L^2 = \sigma_{\text{loc}}^2 / \mathbb{E}[v_t \mid S_t]$.
3. **The mixing parameter**: The parameter $\eta$ controls the blend between local and stochastic volatility, interpolating from pure LV ($\eta = 0$) to full SV with leverage ($\eta = 1$).

The central message is that local volatility is not wrong -- it is **incomplete**. It captures the correct marginal distributions but misses the conditional distributions that drive exotic option prices and hedging performance. Stochastic volatility adds the missing degrees of freedom, and the SLV framework provides the practical synthesis.
