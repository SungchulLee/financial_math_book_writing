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

Recall (see [§ Chapter 14](../../ch14/index.md)): a stochastic volatility model introduces an independent volatility factor with dynamics $dS_t = (r-q)S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}$, $dv_t = \alpha(v_t,t)\,dt + \beta(v_t,t)\,dW_t^{(2)}$, with $\text{Corr}(dW^{(1)}, dW^{(2)}) = \rho\,dt$. The key new elements -- vol-of-vol $\beta$, spot-vol correlation $\rho$, mean reversion $\alpha$, and a second Brownian motion (making the market incomplete) -- are absent in local volatility.

## The Gyongy Connection

### From Stochastic to Local Volatility

Recall (see [§ Gyongy Theorem and Markovian Projection](../properties/gyongy_theorem_markovian_projection.md)): the local volatility function that matches all marginals of any SV model is $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]$, the conditional average of instantaneous variance over paths reaching $K$ at $t$. Different SV models (Heston, SABR, Bergomi) produce different conditional expectations and hence different local volatility surfaces -- but all are consistent with the same vanilla option prices.

### Implications for Model Choice

The Gyongy projection clarifies the model selection problem:

1. **Vanilla pricing**: All models calibrated to the same vanilla surface have the same Gyongy projection. Local volatility is the unique one-factor summary of any model's vanilla-pricing content.
2. **Exotic pricing**: The choice between models matters only for path-dependent and forward smile-dependent products, where the conditional distributions $\text{Law}(S_T \mid S_t = K)$ differ.
3. **Dupire = Gyongy**: Applying Dupire's formula (see [§ Dupire Formula](../local_volatility_framework/dupire_formula_and_local_volatility_surface.md)) to market prices computes the Gyongy projection of whatever process generated those prices. The formula does not know or care about the underlying model.

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

Recall (see [§ Chapter 14](../../ch14/index.md)): the stochastic volatility framework is developed in full generality there (Heston, SABR, Bergomi, rough volatility). The Gyongy connection ensures that all of these models have a local volatility shadow, and the leverage function formalism provides a unified calibration framework.

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

---

## Exercises

**Exercise 1.** Explain the root cause of local volatility's limitations in one sentence. Why does the absence of an independent volatility Brownian motion $dW_t^v$ restrict the model's ability to capture realistic smile dynamics?

??? success "Solution to Exercise 1"
    The root cause is that in local volatility the instantaneous volatility $\sigma_{\text{loc}}(S_t, t)$ is a deterministic function of the spot price and time, so there is no independent Brownian motion driving volatility separately from the asset price. Without $dW_t^v$, the volatility path is completely determined by the spot path, which forces a perfect negative spot-vol correlation ($\rho = -1$), produces zero residual vol-of-vol, generates sticky-strike dynamics, and flattens forward smiles -- all because the model has only one source of randomness.

---

**Exercise 2.** In the stochastic local volatility (SLV) model, the asset dynamics are $dS_t = (r-q)S_t \, dt + L(S_t, t)\sqrt{v_t} S_t \, dW_t^S$ where $L(S, t)$ is the leverage function. Explain the role of $L$ in reconciling the stochastic volatility component with the observed vanilla surface. What happens if $L \equiv 1$?

??? success "Solution to Exercise 2"
    The leverage function $L(S, t)$ adjusts the diffusion coefficient of the SLV model so that the model's marginal distributions of $S_t$ match those implied by the market's vanilla option surface. Specifically, $L$ absorbs the discrepancy between the Dupire local volatility (which encodes the market vanilla prices) and the conditional expected variance from the stochastic volatility component, via

    $$
    L^2(K, t) = \frac{\sigma_{\text{loc}}^2(K, t)}{\mathbb{E}^{\mathbb{Q}}[v_t \mid S_t = K]}
    $$

    If $L \equiv 1$, the SLV model reduces to a pure stochastic volatility model. In this case, the model generally cannot match the full vanilla surface exactly, because the SV component alone typically lacks enough flexibility to reproduce every market-quoted call and put price. The calibration residuals in vanilla options would be nonzero, meaning the model would approximate, but not perfectly fit, the observed implied volatility surface.

---

**Exercise 3.** Gyongy's theorem states that for any stochastic volatility model, there exists a local volatility model with the same marginal distributions. The local volatility is $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}[v_t \mid S_t = K]$. If $v_t$ and $S_t$ are negatively correlated ($\rho < 0$), is $\sigma_{\text{loc}}(K, t)$ increasing or decreasing in $K$? Explain the connection to the implied volatility skew.

??? success "Solution to Exercise 3"
    When $\rho < 0$, spot $S_t$ and variance $v_t$ are negatively correlated: paths that reach a high level $S_t = K$ tend to have lower variance $v_t$, while paths reaching a low level $S_t = K$ tend to have higher variance. Since the Gyongy projection is

    $$
    \sigma_{\text{loc}}^2(K, t) = \mathbb{E}[v_t \mid S_t = K]
    $$

    this negative correlation implies that $\sigma_{\text{loc}}(K, t)$ is **decreasing** in $K$: lower strikes correspond to higher conditional expected variance and vice versa. This produces a downward-sloping local volatility surface as a function of strike, which in turn generates a negatively skewed implied volatility smile -- matching the empirically observed equity skew where OTM puts (low strikes) have higher implied volatility than OTM calls (high strikes).

---

**Exercise 4.** The leverage function in SLV models is $L^2(K, t) = \sigma_{\text{loc}}^2(K, t) / \mathbb{E}[v_t \mid S_t = K]$. If $\sigma_{\text{loc}}(100, 0) = 0.20$ and $\mathbb{E}[v_0 \mid S_0 = 100] = 0.05$, compute $L(100, 0)$. If the stochastic vol component has higher vol-of-vol than implied by the local vol surface, will $L$ be greater or less than 1 at typical strikes?

??? success "Solution to Exercise 4"
    We have $\sigma_{\text{loc}}(100, 0) = 0.20$, so $\sigma_{\text{loc}}^2(100, 0) = 0.04$. Given $\mathbb{E}[v_0 \mid S_0 = 100] = 0.05$:

    $$
    L^2(100, 0) = \frac{0.04}{0.05} = 0.80
    $$

    $$
    L(100, 0) = \sqrt{0.80} \approx 0.894
    $$

    Since $L < 1$, the stochastic volatility component already generates more conditional variance at-the-money than the market requires, so the leverage function dampens it.

    If the SV component has higher vol-of-vol than implied by the local vol surface, then $\mathbb{E}[v_t \mid S_t = K]$ will generally be larger (higher vol-of-vol spreads the distribution of $v_t$ more widely, often raising the conditional mean at typical strikes). This makes the denominator of $L^2$ larger relative to the numerator, so $L < 1$ at typical strikes. The leverage function must attenuate the SV component to prevent the model from over-generating volatility relative to what the market vanilla surface implies.

---

**Exercise 5.** Compare the prices of a 1-year cliquet option (sum of capped monthly returns) under three models: pure local volatility, Heston stochastic volatility, and SLV. Which model do you expect to give the highest price, and why? Relate your answer to the forward smile behavior of each model.

??? success "Solution to Exercise 5"
    The **Heston stochastic volatility model** is expected to give the highest cliquet price, followed by SLV, with pure local volatility giving the lowest price.

    The reasoning is as follows. Each monthly return in the cliquet is effectively a forward-starting option, priced using the forward smile at each reset date. Local volatility produces systematically flat forward smiles (the skew and curvature decay rapidly with the reset date), so the capped monthly returns are priced as if the tails are thin -- undervaluing tail risk and underpricing the cliquet. Stochastic volatility (Heston) preserves forward smile curvature through the vol-of-vol parameter $\xi$, producing persistent skew and convexity at each reset. The wider forward smiles assign higher probabilities to extreme monthly returns, increasing the value of the caps and floors and raising the cliquet price. The SLV model sits between the two: its stochastic component preserves some forward smile curvature while its leverage function constrains the calibration, so the forward smiles are more curved than LV but potentially slightly less so than pure SV (depending on the mixing parameter $\eta$).

    Typical price differences are 15--30% of the premium between LV and SV, driven entirely by the forward smile behavior.

---

**Exercise 6.** The mixing parameter $\eta$ in an SLV model controls the blend between local and stochastic volatility. At $\eta = 0$, the model reduces to pure local volatility; at $\eta = 1$, it becomes full stochastic volatility with leverage. Describe qualitatively how the forward smile changes as $\eta$ increases from 0 to 1. What value of $\eta$ best fits typical equity markets?

??? success "Solution to Exercise 6"
    At $\eta = 0$, the model is pure local volatility: $v_t^0 = 1$ and all dynamics come from the leverage function $L(S, t)$. The forward smile is flat because the volatility is deterministic given the spot path, with no independent vol randomness to sustain curvature.

    As $\eta$ increases from 0 toward 1, the stochastic volatility component $v_t^{\eta/2}$ contributes more to the diffusion. This introduces genuine vol-of-vol into the forward dynamics: conditional on $S_t = K$, the variance $v_t$ is still random, and this randomness generates persistent forward smile curvature. The forward skew strengthens, the forward smile wings widen, and the overall forward smile shape approaches that of a pure SV model.

    At $\eta = 1$, the model has the full SV component with leverage, and the forward smile is as persistent as the SV model allows.

    For typical equity markets, practitioners find that $\eta \in [0.5, 1.0]$ fits best, with $\eta \approx 0.6$--$0.8$ being the most common range. This balances the need for persistent forward smiles (higher $\eta$) against the calibration stability of the leverage function (lower $\eta$ means $L$ does more of the work, making it closer to 1 and more stable numerically).

---

**Exercise 7.** A practitioner must choose between Heston, local volatility, and SLV for pricing barrier options on the S&P 500. Discuss the tradeoffs: (a) calibration difficulty, (b) forward smile accuracy, (c) hedging performance, and (d) computational cost. Make a recommendation with justification.

??? success "Solution to Exercise 7"
    **(a) Calibration difficulty.** Local volatility is the easiest to calibrate: Dupire's formula gives a closed-form expression. Heston requires nonlinear optimization over 5 parameters with a Fourier-based pricing engine; this is moderately difficult and can suffer from local minima and parameter degeneracy ($\kappa$-$\theta$ and $\xi$-$\rho$ tradeoffs). SLV is the hardest: it requires calibrating the SV parameters, computing the Dupire surface, and then iteratively estimating the leverage function via Monte Carlo particle methods.

    **(b) Forward smile accuracy.** Local volatility produces systematically flat forward smiles, making it the worst for barrier options whose value depends on conditional densities at the barrier level. Heston produces more realistic forward smiles with persistent skew, but may not match the vanilla surface perfectly, introducing calibration error. SLV combines exact vanilla calibration with realistic forward smiles, making it the most accurate.

    **(c) Hedging performance.** Local volatility deltas are biased because the model assumes sticky-strike dynamics, overpredicting the sensitivity of implied vol to spot moves. Heston deltas incorporate vol-of-vol and partial correlation, producing more realistic hedges. SLV deltas blend both effects and are generally the most robust, with the mixing parameter $\eta$ controlling the balance.

    **(d) Computational cost.** Local volatility is cheapest (PDE or tree methods on a 2D grid). Heston is moderate (Fourier pricing for vanillas, PDE or Monte Carlo for barriers). SLV is the most expensive (particle method calibration plus full Monte Carlo pricing).

    **Recommendation.** For pricing barrier options on the S&P 500, use the SLV model with moderate mixing $\eta \approx 0.5$--$0.7$. Barrier option prices are highly sensitive to the conditional density at the barrier, which depends critically on the forward smile. Local volatility's flat forward smiles produce systematic bias, while Heston's imperfect vanilla calibration introduces its own errors. SLV eliminates both issues at the cost of higher computational effort, which is justified given the typical notional sizes of barrier option books.
