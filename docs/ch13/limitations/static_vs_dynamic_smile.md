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

Recall (see [§ Dupire Formula](../local_volatility_framework/dupire_formula_and_local_volatility_surface.md)): the Dupire formula guarantees that the local volatility model exactly reproduces the entire observed European call surface, $C^{\text{LV}}(K, T) = C^{\text{market}}(K, T)$ for all $K > 0,\;T > 0$. Equivalently, via Breeden-Litzenberger ($p = e^{rT}\partial_{KK} C$, see [§ Implied Volatility and Risk-Neutral Density](../local_volatility_framework/implied_volatility_and_risk_neutral_density.md)), the model matches every risk-neutral marginal $p^{\text{LV}}(\cdot, T) = p^{\text{market}}(\cdot, T)$. By Gyongy's theorem (see [§ Gyongy Theorem and Markovian Projection](../properties/gyongy_theorem_markovian_projection.md)), $\sigma_{\text{loc}}^2(K, t) = \mathbb{E}[\sigma_t^2 \mid S_t = K]$ is the Markovian projection that preserves marginals.

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

Recall (see [§ Chapter 14](../../ch14/index.md)): under stochastic volatility models (e.g., Heston), the variance process $v_t$ has its own Brownian driver, and the parameter $\xi$ (vol-of-vol) introduces genuine randomness in volatility beyond what is explained by spot moves. The vol-of-vol under stochastic volatility is:

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

Recall (see [§ Smile Dynamics](../../ch12/smile_dynamics/dynamic_consistency.md)): Bergomi (2004) introduced the **skew stickiness ratio** (SSR) to quantify smile dynamics:

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

??? success "Solution to Exercise 1"
    Static calibration means the model reproduces all currently observed European option prices -- it matches today's implied volatility surface exactly. Dynamic consistency means the model correctly predicts how the implied volatility surface will evolve over time as the spot moves and time passes.

    A model can achieve perfect static calibration yet fail dynamically. This distinction matters whenever the pricing depends on the future smile. For example, consider a forward-starting option that resets in 6 months at ATM and expires in 12 months. Its price depends on the implied volatility smile that will prevail in 6 months -- the forward smile. Local volatility perfectly matches today's option prices (static calibration) but predicts a forward smile that is systematically too flat (dynamic failure). A stochastic volatility model may not match today's prices exactly but predicts a more realistic forward smile. The pricing difference for the forward-starting option can be 15--30% of the premium, demonstrating that static calibration alone is insufficient for products with forward smile exposure.

---

**Exercise 2.** The skew stickiness ratio (SSR) measures how the ATM implied volatility changes relative to the prediction under sticky strike. Local volatility implies SSR = 2, while markets show SSR $\approx$ 1.0-1.5 for equity indices. (a) Define SSR precisely. (b) Explain why local volatility produces SSR = 2. (c) What does the empirical SSR of 1.3 imply about the true smile dynamics?

??? success "Solution to Exercise 2"
    **(a)** The skew stickiness ratio is defined as

    $$
    \text{SSR} = \frac{\text{Cov}(d\sigma_{\text{imp}}^{\text{ATM}}, \, dS/S)}{\text{Var}(dS/S) \cdot \partial_K \sigma_{\text{imp}}|_{K = S_0}}
    $$

    It measures how much of the ATM implied volatility change per unit spot return is explained by sliding along the fixed smile curve.

    **(b)** Local volatility produces SSR = 2 because the smile is approximately sticky strike: the implied volatility surface remains anchored at fixed strike levels as the spot moves. When the spot increases by $dS$, the new ATM strike shifts to $S_0 + dS$, and the ATM implied vol changes by $\partial_K \sigma_{\text{imp}} \cdot dS$. However, the local volatility model also shifts the smile slightly due to the time evolution of $\sigma_{\text{loc}}(S, t)$, producing an additional contribution that doubles the naive sticky-strike effect, yielding SSR = 2. More precisely, under sticky strike the regression coefficient of $d\sigma_{\text{imp}}^{\text{ATM}}$ on $dS/S$ equals $S_0 \cdot \partial_K \sigma_{\text{imp}}$, and the SSR formula gives 2 after accounting for the quadratic variation effects in the local volatility dynamics.

    **(c)** An empirical SSR of 1.3 implies that the true smile dynamics are between sticky strike (SSR = 2) and sticky delta (SSR = 0). The smile partially follows the spot (sticky strike component) but also has an independent vol component that offsets part of the spot-driven effect. This is consistent with stochastic volatility models where $\rho \neq -1$ and $\xi > 0$: the independent vol shocks reduce the correlation between ATM vol changes and spot returns, lowering the SSR below the local volatility prediction of 2.

---

**Exercise 3.** Under local volatility, the implied vol-of-vol is perfectly determined by the local volatility surface and is typically too low compared to realized vol-of-vol. Explain the mechanism: why does the deterministic nature of $\sigma_{\text{loc}}(S, t)$ underestimate the actual randomness of volatility?

??? success "Solution to Exercise 3"
    Under local volatility, $\sigma_{\text{loc}}(S_t, t)$ is a fixed, deterministic function of $(S_t, t)$. Given the spot $S_t$, the volatility at that instant is known with certainty. The only way volatility changes is through a spot move: if $S_t$ moves to a different level, the model reads off a different value from the same surface. There is no mechanism for volatility to change independently of the spot.

    In reality, implied volatility exhibits significant randomness that is uncorrelated with spot moves. For example, on days when the S&P 500 is flat, the VIX can still move substantially. This residual vol-of-vol, measured as $\hat{\xi}^2 = \text{Var}(\Delta\sigma_{\text{imp}}^{\text{ATM}} - \hat{\beta}\Delta S/S) / \Delta t$, is empirically large ($\hat{\xi} \approx 0.5$--$1.5$ for equity indices).

    Local volatility forces $\hat{\xi}^{\text{LV}} = 0$ because conditioning on $S_{t+\Delta t} = S_t$ completely eliminates all volatility uncertainty. The model has only one Brownian motion driving both spot and volatility, so spot-orthogonal vol shocks are structurally impossible. This underestimates the true randomness of volatility, leading to underpricing of any product sensitive to vol-of-vol (variance swaps, cliquets, options on implied volatility).

---

**Exercise 4.** A barrier option (e.g., a down-and-out call with barrier at 80% of spot) is priced under local volatility and Heston. The local volatility price is systematically lower. Explain why the incorrect smile dynamics of local volatility (too much sticky strike, too little vol-of-vol) lead to underpricing of this specific product.

??? success "Solution to Exercise 4"
    For a down-and-out call with a barrier at 80% of spot, the option is extinguished if the spot touches the barrier. The price depends critically on the probability of the spot reaching the barrier and on the conditional dynamics near the barrier.

    Under local volatility, the sticky-strike dynamics mean that as the spot falls toward the barrier, the implied volatility rises predictably along the fixed smile (because the smile has negative skew). The volatility increase is entirely deterministic given the spot move. This produces a specific barrier-touching probability that turns out to be too high in many cases, because local volatility overstates the spot-vol coupling.

    More precisely, local volatility's excessive spot-vol correlation ($\rho = -1$) means that spot declines are always accompanied by maximum vol increases, which inflates the diffusion coefficient near the barrier and increases the probability of barrier hits. However, the zero vol-of-vol also means there are no scenarios where vol spikes independently to push the spot through the barrier. The net effect for down-and-out calls is typically underpricing: the model underestimates the survival probability (probability of not hitting the barrier) because it mischaracterizes the conditional dynamics. The stochastic volatility model, with $|\rho| < 1$ and $\xi > 0$, produces a more nuanced barrier-touching probability that better reflects the independent vol risk and typically gives a higher price for the down-and-out call.

---

**Exercise 5.** Perfect static calibration guarantees that all European option prices match the market. Why is this necessary but not sufficient for correct pricing of exotic options? Provide two examples of exotic products where static calibration alone fails to produce accurate prices.

??? success "Solution to Exercise 5"
    Perfect static calibration guarantees that all European (single-maturity, single-strike) option prices match the market. This means the model correctly captures the marginal distribution of $S_T$ at each maturity $T$. However, exotic options depend on more than marginals:

    **Example 1: Forward-starting options.** A forward-starting call depends on the conditional distribution $p(S_{T_2} \mid S_{T_1})$. Two models with the same marginals at $T_1$ and $T_2$ can have different conditional distributions. Local volatility, which has the same marginals as a stochastic volatility model, produces a flatter forward smile (thinner tails in the conditional distribution), underpricing OTM forward-starting options by 10--30%.

    **Example 2: Variance swaps.** The variance swap payoff $\sum_i (\log S_{t_i}/S_{t_{i-1}})^2$ depends on the distribution of realized variance along the path, not just the terminal distribution. The convexity of the variance swap (how its value depends on the strike) is determined by the vol-of-vol, which differs between local volatility ($\hat{\xi} = 0$) and stochastic volatility ($\hat{\xi} = \xi\sqrt{1-\rho^2} > 0$). Both models match the same vanilla prices but disagree on variance swap convexity.

    In both cases, the exotic payoff depends on joint distributions across time or on path properties, which are not pinned down by marginal distributions alone.

---

**Exercise 6.** The local volatility model implies a perfect negative correlation between spot and volatility ($\rho_{S,\sigma} = -1$). Empirically, equity indices exhibit $\rho \approx -0.7$. How does this discrepancy affect the hedging of a delta-neutral, vega-neutral portfolio? Which Greek is most affected?

??? success "Solution to Exercise 6"
    Local volatility implies $\rho_{S,\sigma} = -1$ (perfect negative correlation between spot and volatility), while the market has $\rho \approx -0.7$. The correlation discrepancy affects hedging because it determines how much vega exposure accompanies a delta-neutral position.

    In a delta-neutral, vega-neutral portfolio, the primary remaining exposure is to the **cross-gamma** (or vanna) -- the sensitivity of delta to volatility, equivalently the sensitivity of vega to spot. The vanna is

    $$
    \frac{\partial^2 \Pi}{\partial S \, \partial \sigma}
    $$

    Under local volatility with $\rho = -1$, every spot move produces a perfectly predictable vol move, so the vanna exposure is hedged as part of the delta hedge. Under the true dynamics with $\rho = -0.7$, the vol move accompanying a spot move is smaller and noisier, so the vanna hedge ratios computed from local volatility are wrong.

    The Greek most affected is **vanna** (and relatedly, the volga -- second derivative of price with respect to implied vol). The LV model overestimates the correlation-driven component of vanna hedging and ignores the independent vol risk, leading to hedging errors when volatility moves independently of the spot.

---

**Exercise 7.** Stochastic local volatility (SLV) models aim to combine the static calibration of local volatility with the dynamic realism of stochastic volatility. Describe the tradeoff: what is gained and what is lost in terms of (a) model complexity, (b) calibration effort, (c) pricing accuracy for vanillas, and (d) pricing accuracy for exotics?

??? success "Solution to Exercise 7"
    **(a) Model complexity.** Local volatility requires one function $\sigma_{\text{loc}}(S, t)$ on a 2D grid. Stochastic volatility adds parameters ($\kappa, \theta, \xi, \rho, v_0$) and a second state variable. SLV requires both the SV parameters and the leverage function $L(S, t)$, making it the most complex with two state variables plus a calibrated surface. Complexity increases from LV to SV to SLV.

    **(b) Calibration effort.** LV calibration is straightforward via Dupire's formula (essentially differentiating the option price surface). SV requires nonlinear optimization over a small parameter space but may not achieve exact fit. SLV calibration is the most demanding: it requires iterative Monte Carlo (particle method) to estimate the conditional expectation $\mathbb{E}[v_t \mid S_t = K]$ and compute the leverage function, often requiring multiple simulation passes to converge.

    **(c) Pricing accuracy for vanillas.** LV matches all vanilla prices exactly by construction. SV typically achieves a good but imperfect fit, with residual errors at extreme strikes or maturities. SLV matches all vanilla prices exactly (the leverage function absorbs the calibration residual). So LV and SLV are perfect, while SV is approximate.

    **(d) Pricing accuracy for exotics.** LV systematically misprices exotics that depend on forward smiles or smile dynamics (cliquets, barriers, forward-starting options). SV produces more realistic exotic prices due to genuine vol-of-vol and proper forward smiles, but calibration imperfections in the vanilla surface can propagate to exotic prices. SLV combines exact vanilla calibration with realistic dynamics, producing the most accurate exotic prices. The gain is significant for forward-smile-dependent products (10--30% pricing improvement over LV), at the cost of the additional calibration and computational complexity.
