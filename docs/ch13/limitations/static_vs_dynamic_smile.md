# Static vs Dynamic Smile

A model may perfectly reproduce today's observed option prices -- this is **static calibration**. But option traders care about more than today's prices: they need to know how prices will change tomorrow, next week, and at future dates. The model's prediction for the evolution of the implied volatility surface over time constitutes its **dynamic properties**. The central limitation of local volatility is the divorce between its excellent static calibration (it matches any arbitrage-free smile exactly) and its poor dynamic predictions (it systematically mispredicts how the smile evolves). This section formalizes the static-dynamic distinction, quantifies the specific failures of local volatility dynamics, and explains the consequences for exotic option pricing and hedging.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Distinguish between static calibration and dynamic smile predictions
    - Explain why perfect static calibration does not imply correct dynamics
    - Quantify the vol-of-vol implied by local volatility and compare with market data
    - Describe how local volatility misprices options that depend on future smiles
    - Formalize the connection between smile dynamics and exotic option pricing

## Static Calibration

### What Local Volatility Gets Right

The Dupire formula guarantees that the local volatility model exactly reproduces the entire observed European call price surface $C(K, T)$:

$$
C^{\text{LV}}(K, T) = C^{\text{market}}(K, T) \quad \text{for all } K > 0, \; T > 0
$$

This is equivalent to matching all marginal distributions of $S_T$ under the risk-neutral measure. By the Breeden-Litzenberger formula:

$$
p^{\text{LV}}(S, T) = e^{rT}\frac{\partial^2 C^{\text{LV}}}{\partial K^2}\bigg|_{K=S} = e^{rT}\frac{\partial^2 C^{\text{market}}}{\partial K^2}\bigg|_{K=S} = p^{\text{market}}(S, T)
$$

The local volatility model matches the risk-neutral density at every maturity. This is a direct consequence of Gyongy's theorem: the local volatility function $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}[\sigma_t^2 \mid S_t = K]$ is precisely the Markovian projection that preserves marginal distributions.

### The Limits of Static Consistency

However, matching marginals is far weaker than matching the full stochastic process. Two processes can have identical one-dimensional marginals at every time $t$ while having completely different:

- Joint distributions $(S_{t_1}, S_{t_2})$ at multiple times
- Path-space distributions (the law of trajectories)
- Conditional distributions $\text{Law}(S_T \mid S_t = K)$ for $t < T$

**Proposition 13.5.1** (Static Consistency Does Not Imply Dynamic Consistency).
Let $(S_t^{\text{LV}})$ and $(S_t^{\text{SV}})$ be the asset price processes under a local volatility model and a stochastic volatility model, respectively, calibrated to the same implied volatility surface. Then:

$$
\text{Law}(S_T^{\text{LV}}) = \text{Law}(S_T^{\text{SV}}) \quad \text{for all } T
$$

but in general:

$$
\text{Law}(S_T^{\text{LV}} \mid S_t^{\text{LV}} = K) \neq \text{Law}(S_T^{\text{SV}} \mid S_t^{\text{SV}} = K) \quad \text{for } 0 < t < T
$$

*Proof.* The equality of marginals follows from Gyongy's theorem. For the inequality, consider the conditional variance. Under local volatility:

$$
\text{Var}(S_T^{\text{LV}} \mid S_t^{\text{LV}} = K) = \text{function of } \sigma_{\text{loc}}(S, u) \text{ for } u \in [t, T]
$$

which is deterministic given $S_t = K$. Under stochastic volatility, the conditional variance depends on the (random) future path of $\sigma_t$:

$$
\text{Var}(S_T^{\text{SV}} \mid S_t^{\text{SV}} = K) = \text{function of } \sigma_u \text{ for } u \in [t, T]
$$

Since $\sigma_u$ is stochastic, this conditional variance is itself random, and its distribution differs from the deterministic local volatility case. $\square$

## Dynamic Smile Properties

### Vol-of-Vol

The **vol-of-vol** (volatility of volatility) measures the variability of implied volatility itself. Under local volatility, the instantaneous volatility $\sigma_{\text{loc}}(S_t, t)$ is a deterministic function of $(S_t, t)$. Therefore:

$$
\text{Vol-of-vol}^{\text{LV}} = \text{Var}\bigl(\sigma_{\text{loc}}(S_{t+\Delta t}, t + \Delta t) \mid S_t\bigr)
$$

This variance arises **solely** from the randomness of $S_{t+\Delta t}$. The volatility process has no independent source of randomness -- it is "slaved" to the spot.

Under stochastic volatility models (e.g., Heston), the variance process $v_t$ has its own Brownian driver:

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

The parameter $\xi$ (vol-of-vol) introduces genuine randomness in volatility beyond what is explained by spot moves. The vol-of-vol under stochastic volatility is:

$$
\text{Vol-of-vol}^{\text{SV}} = \xi^2 v_t \, \Delta t + O(\Delta t^2)
$$

which is strictly positive even when the spot is fixed.

**Key distinction**: Under local volatility, conditioning on $S_{t+\Delta t} = S_t$ eliminates all volatility randomness. Under stochastic volatility, volatility can change even when the spot is unchanged.

### The Smile After a Spot Move

Consider what happens to the implied volatility surface at time $t + \Delta t$ after the spot moves from $S_0$ to $S_0 + \Delta S$.

**Under local volatility**: The smile is approximately anchored at fixed strikes (sticky strike). The new ATM implied volatility at strike $K = S_0 + \Delta S$ is read off the original smile at the new strike:

$$
\sigma_{\text{imp}}^{\text{ATM, new}} \approx \sigma_{\text{imp}}(K = S_0 + \Delta S, T - \Delta t)
$$

For negative equity skew, a spot increase shifts ATM to a higher strike where implied vol is lower. The ATM vol drops predictably.

**Under stochastic volatility**: The spot move $\Delta S$ is partially correlated with a vol move $\Delta\sigma$ (through the correlation parameter $\rho$), but there is an additional independent vol shock. The new smile reflects both the spot move and the independent vol innovation, producing a wider range of possible future smiles.

### Realized Smile Variability

An observable test of smile dynamics is the time series of ATM implied volatility. Define:

$$
\hat{\xi}^2 = \frac{\text{Var}(\Delta\sigma_{\text{imp}}^{\text{ATM}} - \hat{\beta}\Delta S/S)}{\Delta t}
$$

where $\hat{\beta}$ is the regression coefficient of ATM vol changes on spot returns. This residual variance measures the vol-of-vol unexplained by spot moves.

- **Empirically**: $\hat{\xi}$ is significantly positive (typically 0.5-1.5 for equity indices), indicating substantial independent vol randomness.
- **Local volatility prediction**: $\hat{\xi}^{\text{LV}} = 0$ (all vol changes are explained by spot moves).
- **Stochastic volatility**: $\hat{\xi}^{\text{SV}} = \xi\sqrt{1 - \rho^2}$, which matches empirical data with appropriate parameter choices.

## Exotic Option Pricing Implications

### Path-Dependent Options

Options whose payoff depends on the path of $S_t$ (not just the terminal value $S_T$) are sensitive to the joint distribution of $(S_{t_1}, S_{t_2}, \ldots, S_{t_n})$, which local volatility and stochastic volatility models predict differently.

**Proposition 13.5.2** (Exotic Pricing Under Static-Equivalent Models).
Let $\Pi^{\text{LV}}$ and $\Pi^{\text{SV}}$ be the prices of a path-dependent exotic under local and stochastic volatility models calibrated to the same vanilla surface. Then:

$$
\Pi^{\text{LV}} = \Pi^{\text{SV}} \quad \Longleftrightarrow \quad \text{the exotic depends only on marginals of } S_T
$$

In general, for path-dependent exotics:

$$
\Pi^{\text{LV}} \neq \Pi^{\text{SV}}
$$

and the difference can be substantial.

### Specific Examples

| Product | Static/Dynamic | LV vs SV Difference |
|---------|---------------|-------------------|
| European call/put | Static (single marginal) | Zero (by construction) |
| Variance swap | Path-dependent | LV underprices (lower realized vol variability) |
| Barrier option | Path-dependent | Systematic bias (direction depends on barrier type) |
| Cliquet/accumulator | Forward smile-dependent | LV significantly underprices |
| Forward-starting option | Future smile-dependent | LV gives flatter smile, underprices OTM options |

### The Variance Swap Test

The variance swap payoff is $\sum_{i}(\log S_{t_i}/S_{t_{i-1}})^2$, which depends on the realized volatility path. Under local volatility, the distribution of realized variance has **thinner tails** than under stochastic volatility because the volatility path is deterministic given the spot path. In stochastic volatility models, the vol-of-vol parameter $\xi$ creates additional dispersion in realized variance.

**Consequence**: Local volatility underprices variance swap convexity (the curvature in the variance swap value as a function of strike). This is a directly observable market test: variance swap convexity quotes exceed local volatility predictions.

## Quantifying the Dynamic Failure

### The Skew Stickiness Ratio

Bergomi (2004) introduced the **skew stickiness ratio** (SSR) to quantify smile dynamics:

$$
\text{SSR} = \frac{\text{Cov}\bigl(d\sigma_{\text{imp}}^{\text{ATM}}, \, dS/S\bigr)}{\text{Var}(dS/S) \cdot \partial_K \sigma_{\text{imp}}|_{K = S_0}}
$$

The SSR measures how much of the observed ATM vol change per spot return is explained by the smile slope:

- **SSR = 2**: Sticky strike regime (local volatility prediction)
- **SSR = 0**: Sticky delta regime (smile moves rigidly with spot)
- **SSR = 1**: Intermediate (the smile "half-sticks" to strikes)

Empirically, the SSR for equity indices is typically between 1.0 and 1.5, between the local volatility prediction of 2 and the sticky delta prediction of 0.

### Formal Decomposition

The total implied volatility change can be decomposed as:

$$
d\sigma_{\text{imp}}^{\text{ATM}} = \underbrace{\text{SSR} \cdot \partial_K\sigma_{\text{imp}} \cdot \frac{dS}{S}}_{\text{spot-driven (deterministic)}} + \underbrace{d\epsilon}_{\text{vol-of-vol (stochastic)}}
$$

where $d\epsilon$ is the residual vol shock uncorrelated with spot returns. Local volatility sets $d\epsilon = 0$ and $\text{SSR} = 2$. The market has $d\epsilon \neq 0$ and $\text{SSR} < 2$.

## Worked Example

??? example "Cliquet Pricing: LV vs SV"

    **Setup.** A one-year cliquet option on an equity index pays the sum of monthly capped and floored returns:

    $$
    \text{Payoff} = \sum_{i=1}^{12} \min\bigl(\max(R_i, -3\%), +5\%\bigr)
    $$

    where $R_i = S_{t_i}/S_{t_{i-1}} - 1$ is the monthly return. The payoff depends on 12 forward-starting options, each of which is sensitive to the **forward smile** at the start of each period.

    **Under local volatility**: The forward smile at time $t_i$ for expiry $t_{i+1}$ is determined by the local volatility surface $\sigma_{\text{loc}}(S, t)$ for $t \in [t_i, t_{i+1}]$. Because LV produces flat forward smiles (see the Forward Smile Problem section), the floor at $-3\%$ and cap at $+5\%$ are priced using a nearly flat smile, undervaluing the tail risk.

    **Under stochastic volatility**: The forward smile retains significant curvature due to the vol-of-vol parameter $\xi$. The capped/floored returns are priced with a more convex smile, reflecting higher tail probabilities.

    **Typical price difference**: The cliquet price under stochastic volatility can be 15-30% higher than under local volatility, with the difference driven entirely by the forward smile (since both models are calibrated to the same spot smile).

## The Fundamental Tension

The static-dynamic dichotomy reveals a fundamental tension in option modeling:

1. **Local volatility** achieves perfect static calibration but has one factor, producing deterministic vol dynamics with zero vol-of-vol
2. **Stochastic volatility** introduces genuine vol dynamics with additional parameters ($\xi$, $\rho$) but typically cannot perfectly fit the vanilla surface without additional degrees of freedom
3. **Stochastic local volatility** combines both approaches: the local volatility component ensures perfect calibration while the stochastic volatility component provides realistic dynamics

This tension motivates the SLV framework discussed in the Bridge to Stochastic Volatility section.

## Summary

The static vs dynamic distinction is the most important conceptual framework for understanding the limitations of local volatility:

1. **Static calibration**: Local volatility perfectly matches all European option prices by construction (Dupire's formula). This is guaranteed by Gyongy's theorem and is model-free.
2. **Dynamic failure**: The model predicts sticky strike smile dynamics with zero vol-of-vol, while markets exhibit partial sticky delta behavior with significant independent vol randomness.
3. **Vol-of-vol deficit**: Local volatility has zero residual vol-of-vol ($\hat{\xi}^{\text{LV}} = 0$), while empirical data shows $\hat{\xi} > 0$.
4. **SSR mismatch**: The skew stickiness ratio is 2 under local volatility but typically 1.0-1.5 in markets.
5. **Exotic mispricing**: Path-dependent and forward smile-dependent options are systematically mispriced: local volatility underprices products with convexity in volatility (cliquets, variance swaps, forward-starting options).
6. **Resolution**: Stochastic local volatility models combine perfect static calibration with realistic dynamics, addressing the fundamental tension at the cost of increased complexity.

---

## Exercises

**Exercise 1.** Distinguish between static calibration and dynamic consistency. A model can perfectly match today's option prices (static) yet predict incorrect future smile behavior (dynamic). Give an example of a situation where this distinction matters for pricing.

---

**Exercise 2.** The skew stickiness ratio (SSR) measures how the ATM implied volatility changes relative to the prediction under sticky strike. Local volatility implies SSR = 2, while markets show SSR $\approx$ 1.0-1.5 for equity indices. (a) Define SSR precisely. (b) Explain why local volatility produces SSR = 2. (c) What does the empirical SSR of 1.3 imply about the true smile dynamics?

---

**Exercise 3.** Under local volatility, the implied vol-of-vol is perfectly determined by the local volatility surface and is typically too low compared to realized vol-of-vol. Explain the mechanism: why does the deterministic nature of $\sigma_{\text{loc}}(S, t)$ underestimate the actual randomness of volatility?

---

**Exercise 4.** A barrier option (e.g., a down-and-out call with barrier at 80% of spot) is priced under local volatility and Heston. The local volatility price is systematically lower. Explain why the incorrect smile dynamics of local volatility (too much sticky strike, too little vol-of-vol) lead to underpricing of this specific product.

---

**Exercise 5.** Perfect static calibration guarantees that all European option prices match the market. Why is this necessary but not sufficient for correct pricing of exotic options? Provide two examples of exotic products where static calibration alone fails to produce accurate prices.

---

**Exercise 6.** The local volatility model implies a perfect negative correlation between spot and volatility ($\rho_{S,\sigma} = -1$). Empirically, equity indices exhibit $\rho \approx -0.7$. How does this discrepancy affect the hedging of a delta-neutral, vega-neutral portfolio? Which Greek is most affected?

---

**Exercise 7.** Stochastic local volatility (SLV) models aim to combine the static calibration of local volatility with the dynamic realism of stochastic volatility. Describe the tradeoff: what is gained and what is lost in terms of (a) model complexity, (b) calibration effort, (c) pricing accuracy for vanillas, and (d) pricing accuracy for exotics?
