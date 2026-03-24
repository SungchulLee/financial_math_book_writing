# Forward Smile Problem

The forward smile is the implied volatility surface that will prevail at a future time $t$, as predicted by the model today. It determines the prices of forward-starting options, cliquets, and any derivative whose payoff depends on the future option market. The forward smile problem is arguably the most important practical limitation of local volatility: while the model perfectly reproduces today's smile (static calibration), it predicts forward smiles that are systematically **too flat** compared to market-implied forward smiles. This flattening produces large and consistent pricing errors for products with forward smile exposure, making local volatility unreliable for exotic option desks.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define the forward implied volatility surface and its relationship to conditional densities
    - Derive the forward smile under local volatility from the local volatility surface
    - Prove that local volatility forward smiles are flatter than spot smiles
    - Compare forward smiles under local volatility and stochastic volatility
    - Quantify the pricing impact on forward-starting options and cliquets

## Definition of the Forward Smile

### Forward-Starting Options

A **forward-starting European call** with reset date $t$ and expiry $T > t$ has payoff:

$$
(S_T - \alpha S_t)^+
$$

where $\alpha > 0$ is a fixed percentage strike (e.g., $\alpha = 1$ for ATM forward-starting). The strike is set at time $t$ as a fraction of the then-prevailing spot $S_t$, and the option is exercised at time $T$.

The price at time $0$ is:

$$
C_{\text{fwd}}(\alpha, t, T) = e^{-rT}\mathbb{E}^{\mathbb{Q}}\bigl[(S_T - \alpha S_t)^+\bigr]
$$

### The Forward Implied Volatility

The **forward implied volatility** $\sigma_{\text{fwd}}(\alpha, t, T)$ is defined as the constant volatility that, plugged into a Black-Scholes formula with "spot" $S_t$ and "strike" $\alpha S_t$, gives the forward-starting option price conditional on $S_t$:

$$
C_{\text{fwd}}(\alpha, t, T \mid S_t) = C_{\text{BS}}\bigl(S_t, \alpha S_t, T - t, r, q, \sigma_{\text{fwd}}(\alpha, t, T)\bigr)
$$

The forward smile $\alpha \mapsto \sigma_{\text{fwd}}(\alpha, t, T)$ is the implied volatility smile that will apply to options initiated at time $t$.

### Connection to Conditional Density

The forward smile encodes the conditional density $p(S_T \mid S_t)$:

$$
C_{\text{fwd}}(\alpha, t, T \mid S_t) = e^{-r(T-t)}\int_{\alpha S_t}^{\infty}(S - \alpha S_t) p(S, T \mid S_t) \, dS
$$

Two models calibrated to the same spot smile (same marginals of $S_T$) can have different conditional densities $p(S_T \mid S_t)$ and hence different forward smiles.

## Forward Smile Under Local Volatility

### Derivation

Under the local volatility model, the dynamics are:

$$
dS_u = (r - q)S_u \, du + \sigma_{\text{loc}}(S_u, u) S_u \, dW_u^{\mathbb{Q}}
$$

Given $S_t = K$, the evolution for $u \in [t, T]$ depends on $\sigma_{\text{loc}}(S_u, u)$ for $S_u$ near $K$. The forward smile at time $t$ is determined by the **local volatility surface restricted to $[t, T]$** and the distribution of paths starting from $S_t = K$.

**Proposition 13.5.3** (Forward Smile Under Local Volatility).
Under the local volatility model, the forward implied volatility at the ATM forward strike ($\alpha = 1$) satisfies:

$$
\sigma_{\text{fwd}}^2(1, t, T) \approx \frac{1}{T - t}\int_t^T \sigma_{\text{loc}}^2(K, u) \, du
$$

where $K = S_0 e^{(r-q)t}$ is the forward spot at time $t$. The forward ATM vol is the time-average of the local volatility along the forward path.

### Why the Forward Smile Flattens

The forward smile is flatter than the spot smile for a fundamental reason: **the local volatility surface is already calibrated to produce the spot smile**, and averaging over paths that start at $S_t = K$ effectively smooths out the variation across strikes.

**Theorem 13.5.1** (Forward Smile Flattening Under Local Volatility).
Let $\mathcal{S}_{\text{spot}} = \partial_K \sigma_{\text{imp}}|_{K = S_0}$ be the spot smile skew and $\mathcal{S}_{\text{fwd}}(t)$ be the forward smile skew at reset date $t$. Under local volatility, for short remaining maturity $T - t$:

$$
|\mathcal{S}_{\text{fwd}}(t)| < |\mathcal{S}_{\text{spot}}| \quad \text{for all } t > 0
$$

and $\mathcal{S}_{\text{fwd}}(t) \to 0$ as $t \to T$ (the forward smile becomes flat for short forward periods far in the future).

*Proof sketch.* The forward smile at time $t$ depends on the local volatility surface $\sigma_{\text{loc}}(S, u)$ for $u \in [t, T]$. As $t$ increases:

1. The local volatility surface has already been "used up" to generate the spot smile for maturities $[0, t]$.
2. The remaining surface $\sigma_{\text{loc}}(S, u)$ for $u \in [t, T]$ is flatter than the initial surface because the smile's skew is a cumulative effect that builds over $[0, T]$.
3. The ATM time-average relation $\sigma_{\text{imp}}^2 T = \int_0^T \sigma_{\text{loc}}^2 \, du$ means that the marginal local variance at late times must compensate for the early-time contribution, producing a flatter profile.

More precisely, the implied total variance satisfies $w(K, T) = \sigma_{\text{imp}}^2(K, T) T$, and the forward total variance is:

$$
w_{\text{fwd}}(K, t, T) = w(K, T) - w(K, t)
$$

For a concave function $T \mapsto w(K, T)$ (which is typical when the smile term structure flattens), the forward variance $w_{\text{fwd}}$ decreases with $t$, and the forward smile flattens. $\square$

### Heuristic Explanation

Consider the forward smile at a reset date $t$ far in the future. At time $t$, the spot will be at some level $S_t$. Under local volatility, the volatility for $u \in [t, T]$ is $\sigma_{\text{loc}}(S_u, u)$, which is deterministic given the spot path. But conditional on $S_t = K$, the paths during $[t, T]$ stay near $K$ for short $T - t$, and the local volatility variation across these nearby paths is small. The forward smile therefore inherits only the **local** variation of $\sigma_{\text{loc}}$ near $(K, t)$, not the **global** skew of the surface.

In contrast, under stochastic volatility, the volatility at time $t$ is random even conditional on $S_t = K$. High-vol states produce more skewed forward smiles, and the average over all possible vol states preserves significant forward smile curvature.

## Forward Smile Under Stochastic Volatility

### Persistent Forward Skew

Under a stochastic volatility model (e.g., Heston), the forward smile is generated by the conditional distribution of $S_T$ given $S_t$ **and** $v_t$. Since $v_t$ is random, the forward smile averages over all possible variance states:

$$
C_{\text{fwd}}(\alpha, t, T) = e^{-rT}\mathbb{E}^{\mathbb{Q}}\bigl[\mathbb{E}^{\mathbb{Q}}[(S_T - \alpha S_t)^+ \mid S_t, v_t]\bigr]
$$

Each realization of $v_t$ produces a different forward smile (higher $v_t$ gives a wider smile), and the mixture of these smiles preserves curvature.

**Key result**: The forward smile under stochastic volatility is:

$$
|\mathcal{S}_{\text{fwd}}^{\text{SV}}(t)| > |\mathcal{S}_{\text{fwd}}^{\text{LV}}(t)| \quad \text{for all } t > 0
$$

The stochastic volatility forward skew decays more slowly with $t$ than the local volatility forward skew.

### The Fundamental Difference

| Feature | Local Volatility | Stochastic Volatility |
|---------|-----------------|---------------------|
| Forward smile skew | Decays with $t$, approaches zero | Decays slowly, remains substantial |
| Forward smile curvature | Flattens rapidly | Persists due to vol-of-vol |
| Conditional variance | Deterministic given $S_t$ | Random (depends on $v_t$) |
| Forward-starting ATM vol | $\approx \sigma_{\text{loc}}(K, t)$ | Higher, reflecting vol uncertainty |

## Pricing Impact

### Forward-Starting Options

For a forward-starting call with $\alpha = 1$ (ATM), both models give similar prices (since both are calibrated to ATM vol). But for $\alpha \neq 1$ (OTM forward-starting options), the local volatility model underprices because its forward smile is too flat:

$$
C_{\text{fwd}}^{\text{LV}}(\alpha, t, T) < C_{\text{fwd}}^{\text{SV}}(\alpha, t, T) \quad \text{for } \alpha \neq 1
$$

The underpicing is more severe for:

- Longer reset dates $t$ (more forward smile flattening)
- More OTM strikes ($|\alpha - 1|$ large, where smile curvature matters most)
- Higher vol-of-vol $\xi$ in the true model

### Cliquets and Accumulators

Cliquet options sum capped/floored forward returns over multiple periods:

$$
\text{Payoff} = \sum_{i=1}^{n} \max\bigl(\min(R_i, C), F\bigr)
$$

where $R_i = S_{t_i}/S_{t_{i-1}} - 1$, $C$ is the cap, and $F$ is the floor.

Each period $[t_{i-1}, t_i]$ is a forward-starting option. The total cliquet price depends on $n$ forward smiles, each of which local volatility predicts to be too flat. The cumulative pricing error can be very large:

$$
\Pi^{\text{LV}}_{\text{cliquet}} \ll \Pi^{\text{SV}}_{\text{cliquet}}
$$

with typical differences of 10-30% of the premium, concentrated in products with tight caps and floors that are sensitive to the wings of the forward smile.

??? example "Forward Smile Comparison: Numerical Illustration"

    **Setup.** An equity index with $S_0 = 100$, $r = 0.03$, $q = 0.01$, spot implied vol skew $\partial_K \sigma_{\text{imp}} = -0.001$.

    The spot ATM implied volatility for 1-year maturity is $\sigma_{\text{imp}}(100, 1) = 0.20$.

    **Forward smile at $t = 0.5$, maturity $T = 1$ (6-month forward option):**

    Under local volatility, the forward ATM vol is:

    $$
    \sigma_{\text{fwd}}^{\text{LV}} \approx \sqrt{\frac{w(K, 1) - w(K, 0.5)}{0.5}} = \sqrt{\frac{0.04 - 0.018}{0.5}} = \sqrt{0.044} \approx 0.210
    $$

    The forward skew under LV: using the flattening result, the forward skew is approximately:

    $$
    \mathcal{S}_{\text{fwd}}^{\text{LV}} \approx 0.5 \times \mathcal{S}_{\text{spot}} = -0.0005
    $$

    Under stochastic volatility (Heston with $\xi = 0.5$, $\rho = -0.7$):

    $$
    \mathcal{S}_{\text{fwd}}^{\text{SV}} \approx 0.8 \times \mathcal{S}_{\text{spot}} = -0.0008
    $$

    The stochastic volatility forward skew is 60% stronger than the local volatility forward skew. For a 10% OTM forward-starting put ($\alpha = 0.9$), this translates to an implied vol difference of approximately:

    $$
    \Delta\sigma_{\text{imp}} \approx (0.0008 - 0.0005) \times 10 = 0.003 = 0.3\%
    $$

    in implied volatility terms, which corresponds to a price difference of roughly 1-2% of the option premium -- significant for a structured product desk.

## Diagnosing the Problem in Practice

### Market-Implied Forward Smile

The market-implied forward smile can be extracted from:

1. **Calendar spreads**: The difference $C(K, T_2) - C(K, T_1)$ for $T_2 > T_1$ gives information about the forward density
2. **Forward-starting option quotes**: Direct quotes for forward-starting options (available in equity structured products markets)
3. **Variance swap term structure**: The forward variance $\sigma_{\text{fwd}}^2 = (w(T_2) - w(T_1))/(T_2 - T_1)$ from variance swap quotes

Comparing market-implied forward smiles with local volatility predictions reveals the systematic flattening problem.

### Variance Swap Forward Skew

The variance swap strike $K_{\text{var}}(T)$ is related to the integral of the implied volatility smile:

$$
K_{\text{var}}(T) = \frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K, T)}{K^2}\,dK + \int_F^{\infty}\frac{C(K, T)}{K^2}\,dK\right)
$$

The forward variance swap strike is:

$$
K_{\text{var}}^{\text{fwd}}(t, T) = \frac{T \cdot K_{\text{var}}(T) - t \cdot K_{\text{var}}(t)}{T - t}
$$

Under local volatility, the forward variance swap strike is deterministic. Under stochastic volatility, it is random, and the expected value can differ from the local volatility prediction.

## Connection to the Chapter

The forward smile problem is the bridge between the limitations of local volatility and the motivation for stochastic volatility:

- **Static vs Dynamic Smile**: The forward smile is the most concrete manifestation of the dynamic failure -- it is a directly observable prediction that can be tested against market data.
- **Bridge to Stochastic Volatility**: Resolving the forward smile problem requires introducing independent volatility randomness ($\xi > 0$), which is the defining feature of stochastic volatility models.
- **Gyongy's Theorem**: The theorem explains why local volatility matches the spot smile (marginals) but not the forward smile (conditionals).

## Summary

The forward smile problem is the most important practical limitation of local volatility:

1. **Definition**: The forward smile $\sigma_{\text{fwd}}(\alpha, t, T)$ is the implied volatility surface that will prevail at a future reset date $t$, as predicted by the model.
2. **Flattening**: Local volatility produces forward smiles that are systematically flatter than market-implied forward smiles, with the skew decaying as the reset date $t$ increases.
3. **Root cause**: Under local volatility, the forward variance is deterministic given the spot path. There is no independent vol randomness to sustain forward smile curvature.
4. **Pricing impact**: Forward-starting options, cliquets, and accumulators are systematically underpriced by local volatility, with errors of 10-30% of premium for structured products.
5. **Stochastic volatility resolution**: Stochastic volatility models produce more persistent forward smiles due to the vol-of-vol parameter $\xi$, better matching market data.
6. **Observable test**: Forward smiles can be extracted from calendar spreads, forward-starting option quotes, and variance swap term structures, providing a direct empirical test of the model.

---

## Exercises

**Exercise 1.** Define the forward implied volatility surface $\sigma_{\text{fwd}}(K, T_1, T_2)$ and explain how it relates to the conditional distribution of $S_{T_2}$ given information at $T_1$. Why do forward-starting options depend on this surface?

---

**Exercise 2.** Under local volatility, explain intuitively why the forward smile becomes flatter as $T_1$ increases. Relate this to the diffusion of the probability density over the local volatility surface.

---

**Exercise 3.** A 1-year forward-starting ATM call (resetting at 6 months, expiring at 12 months) is priced using local volatility at \$4.20 and using Heston at \$5.10. (a) Which model produces a flatter forward smile? (b) Compute the percentage pricing difference. (c) If the market price is \$5.00, which model is closer?

---

**Exercise 4.** The forward variance between $T_1$ and $T_2$ under local volatility is

$$
\sigma_{\text{fwd}}^2(K, T_1, T_2) = \frac{w(K, T_2) - w(K, T_1)}{T_2 - T_1}
$$

Given a negatively-skewed spot smile, show that the forward smile computed from this formula has reduced skew compared to the spot smile. What property of the total variance $w(K, T)$ causes this?

---

**Exercise 5.** A cliquet option with 12 monthly resets and caps/floors depends on 12 successive forward smiles. If local volatility underestimates each forward smile skew by 30%, estimate the cumulative pricing error direction for a cliquet that has downside floors. Is the cliquet overpriced or underpriced by local volatility?

---

**Exercise 6.** Describe how to extract market-implied forward smiles from (a) variance swap term structures and (b) calendar spreads of vanilla options. Which approach is more model-dependent, and why?

---

**Exercise 7.** The forward smile problem is often cited as the main motivation for stochastic volatility models. However, stochastic volatility models have their own forward smile predictions. Design a test comparing the forward smile predictions of local volatility, Heston, and SABR to market data from forward-starting options. What data would you need, and what metric would you use to assess accuracy?
