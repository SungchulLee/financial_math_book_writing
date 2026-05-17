# Analytical Tractability Comparison

The choice of short-rate model in practice often hinges not on which model best fits the data, but on which model allows the fastest and most reliable computation of prices and risk sensitivities. Vasicek and CIR are affine models with closed-form bond prices, option prices, and known transition densities. Hull-White extends Vasicek with time-dependent drift while preserving the affine structure, retaining all closed-form results. Black-Karasinski sacrifices this tractability for log-normal rates and guaranteed positivity, requiring numerical methods for every calculation. This section catalogues exactly what each model can and cannot compute in closed form, providing a systematic basis for model selection.

!!! info "Prerequisites"

    - [Vasicek Model](../short_rate_models/vasicek_model.md)
    - [CIR Model](../short_rate_models/cir_model.md)
    - [Hull-White Model](../short_rate_models/hull_white_model.md)
    - [Non-Affine Structure](../black_karasinski/non_affine_structure.md) (why BK has no closed forms)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define what makes a short-rate model affine and state the consequences for bond pricing
    2. List the closed-form results available for Vasicek, CIR, and Hull-White
    3. Explain why Black-Karasinski requires numerical methods for all pricing
    4. Compare computational costs across models for common pricing tasks
    5. Recommend model choice based on tractability requirements

---

## Affine vs Non-Affine Models

Recall (see [§ Affine bond pricing (general theory)](../../ch15/affine_term_structure/bond_pricing_affine_framework.md)).

### Affine term structure

A model is affine if the zero-coupon bond price has the form

$$
P(t, T) = \exp\bigl(A(t, T) + B(t, T)\,r_t\bigr)
$$

where $A$ and $B$ are deterministic functions satisfying Riccati ODEs. This structure implies:

- Bond prices are exponential-linear in $r_t$ (fast evaluation)
- Yields and forward rates are linear in $r_t$
- Bond option prices reduce to expectations of known distributions
- Greeks are analytical derivatives of $A$ and $B$

### Non-affine models

When the short-rate dynamics produce a bond pricing PDE with non-linear coefficients in $r$, the exponential-affine form fails. The bond price $P(t, T)$ is still a conditional expectation $\mathbb{E}^{\mathbb{Q}}[\exp(-\int_t^T r_s\,ds)\,|\,\mathcal{F}_t]$, but it cannot be expressed in closed form.

---

## Model-by-Model Tractability

### Vasicek

Recall (see [§ Vasicek SDE and bond pricing](../vasicek_model/vasicek_sde_and_ou_process.md)).

SDE: $dr_t = a(b - r_t)\,dt + \sigma\,dW_t$

| Quantity | Closed form | Formula |
|----------|:-----------:|---------|
| Bond price | Yes | $P(t,T) = e^{A(\tau) + B(\tau)r_t}$ with $B(\tau) = \frac{1-e^{-a\tau}}{a}$ |
| Transition density | Yes | $r_t\,|\,r_s \sim \mathcal{N}(\mu, \nu^2)$ |
| Bond option | Yes | Jamshidian formula |
| Cap/floor | Yes | Sum of bond options |
| Swaption | Yes | Jamshidian decomposition |
| Greeks | Yes | Analytical |

### CIR

Recall (see [§ CIR, Feller, and non-central chi-squared](../cir_model/cir_sde_and_square_root_process.md)).

SDE: $dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$

| Quantity | Closed form | Formula |
|----------|:-----------:|---------|
| Bond price | Yes | $P(t,T) = e^{A(\tau) + B(\tau)r_t}$ with different $A$, $B$ |
| Transition density | Yes | Non-central $\chi^2$ |
| Bond option | Yes | Via non-central $\chi^2$ CDF |
| Cap/floor | Yes | Sum of bond options |
| Swaption | Approximate | Requires numerical integration |
| Greeks | Yes (bonds) | Analytical for bonds; numerical for options |

### Hull-White (extended Vasicek)

Recall (see [§ Hull-White (full treatment)](../../ch20/index.md)).

SDE: $dr_t = [\theta(t) - a\,r_t]\,dt + \sigma\,dW_t$

| Quantity | Closed form | Formula |
|----------|:-----------:|---------|
| Bond price | Yes | $P(t,T) = e^{A(t,T) + B(\tau)r_t}$ with time-dependent $A$ |
| Transition density | Yes | Normal, same form as Vasicek |
| Bond option | Yes | Modified Jamshidian formula |
| Cap/floor | Yes | Sum of bond options |
| Swaption | Yes | Jamshidian trick with coupon bond decomposition |
| Greeks | Yes | Analytical |
| Yield curve fit | Exact | $\theta(t)$ calibrated to market curve |

### Black-Karasinski

Recall (see [§ Black-Karasinski](../black_karasinski/log_normal_short_rate_sde.md)).

SDE: $d(\ln r_t) = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$

| Quantity | Closed form | Formula |
|----------|:-----------:|---------|
| Bond price | No | Tree or PDE required |
| Transition density | Partial | Log-normal for $r_t$, but $\int r_s\,ds$ has no known distribution |
| Bond option | No | Tree |
| Cap/floor | No | Tree |
| Swaption | No | Tree |
| Greeks | No | Finite differences on tree |
| Yield curve fit | Exact | $\theta(t)$ calibrated numerically on tree |

---

## Computational Cost Comparison

The table below estimates the cost of pricing a single European swaption:

| Model | Method | Operations | Typical time |
|-------|--------|------------|-------------|
| Vasicek | Jamshidian | $O(n)$ bond option evaluations | $< 1$ ms |
| CIR | Semi-analytical | $O(n)$ $\chi^2$ CDF evaluations | $< 5$ ms |
| Hull-White | Jamshidian | $O(n)$ bond option evaluations | $< 1$ ms |
| Black-Karasinski | Trinomial tree | $O(N_t \times N_x)$ | 10--100 ms |

where $n$ is the number of coupon dates and $N_t$, $N_x$ are tree dimensions.

!!! warning "Greeks Amplify the Gap"
    For a single price, the cost difference is manageable. For Greeks computation, affine models evaluate analytical derivatives at near-zero marginal cost, while BK requires rerunning the tree with perturbed inputs. Computing delta, gamma, vega, and theta for a swaption book under BK can be 100--1000$\times$ slower than under Hull-White.

---

## When Tractability Matters Most

| Use case | Recommended model | Reason |
|----------|------------------|--------|
| Real-time risk (XVA, CVA) | Hull-White | Closed-form Greeks, fast recalibration |
| Monte Carlo simulation | Vasicek / Hull-White | Exact simulation of $r_t$ |
| Positive rates required | CIR or Black-Karasinski | CIR if speed matters; BK if log-normal tails matter |
| Exotic path-dependent | Hull-White tree or BK tree | Tree-based pricing; HW faster per node |
| Regulatory capital (stressed scenarios) | Hull-White | Speed for large portfolio revaluation |

---

## Summary

| Model | Affine | Bond CF | Option CF | Speed rank |
|-------|:------:|:-------:|:---------:|:----------:|
| Vasicek | Yes | Yes | Yes | 1 |
| Hull-White | Yes | Yes | Yes | 1 |
| CIR | Yes | Yes | Partial | 2 |
| Black-Karasinski | No | No | No | 3 |

The tractability hierarchy is clear: Vasicek $\approx$ Hull-White $>$ CIR $\gg$ Black-Karasinski. The question is whether the log-normal rate distribution and guaranteed positivity of BK justify the computational cost. For calibration quality comparisons, see [Calibration Fit Comparison](calibration_fit_comparison.md). For a detailed structural comparison of Hull-White and BK, see [Vasicek vs CIR vs Hull-White](vasicek_vs_cir_vs_hull_white.md).

---

## Exercises

**Exercise 1.** State the affine condition for a one-factor short-rate model: the drift $\mu(t,r)$ and squared diffusion $\sigma^2(t,r)$ must be affine in $r$. For each of the four models (Vasicek, CIR, Hull-White, Black-Karasinski), write $\mu(t,r)$ and $\sigma^2(t,r)$ and verify whether the affine conditions are satisfied.

??? success "Solution to Exercise 1"
    The affine condition requires that the drift $\mu(t,r)$ and squared diffusion $\sigma^2(t,r)$ of the short rate SDE $dr_t = \mu(t,r_t)\,dt + \sigma(t,r_t)\,dW_t$ are both affine functions of $r$, i.e., of the form $\alpha_0(t) + \alpha_1(t)\,r$ for deterministic functions $\alpha_0$, $\alpha_1$.

    **Vasicek:** $\mu(t,r) = a(b - r) = ab - ar$ and $\sigma^2(t,r) = \sigma^2$. Both are affine in $r$ (with $\alpha_1^{\mu} = -a$ and $\alpha_1^{\sigma^2} = 0$). Affine: **Yes**.

    **CIR:** $\mu(t,r) = a(b - r) = ab - ar$ and $\sigma^2(t,r) = \sigma^2 r$. Both are affine in $r$ (with $\alpha_1^{\mu} = -a$ and $\alpha_1^{\sigma^2} = \sigma^2$). Affine: **Yes**.

    **Hull-White:** $\mu(t,r) = \theta(t) - ar$ and $\sigma^2(t,r) = \sigma^2$. Both are affine in $r$ (the time dependence in $\theta(t)$ enters through $\alpha_0(t) = \theta(t)$, which is permissible since the affine condition allows time-dependent coefficients). Affine: **Yes**.

    **Black-Karasinski:** The SDE is $d(\ln r_t) = [\theta(t) - a\ln r_t]\,dt + \sigma\,dW_t$. Applying Ito's lemma to $r_t = e^{x_t}$ where $x_t = \ln r_t$, we get

    $$
    dr_t = r_t\!\left[\theta(t) - a\ln r_t + \tfrac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t
    $$

    The drift $\mu(t,r) = r[\theta(t) - a\ln r + \frac{1}{2}\sigma^2]$ contains $r\ln r$, which is not affine in $r$. The squared diffusion $\sigma^2(t,r) = \sigma^2 r^2$ is quadratic in $r$, also not affine. Affine: **No**.

---

**Exercise 2.** In the Hull-White model, the time-dependent drift $\theta(t)$ is chosen to fit the initial yield curve exactly. Explain why this does not break the affine structure. Specifically, show that $\theta(t) - ar$ is still affine in $r$ even though $\theta(t)$ is time-dependent.

??? success "Solution to Exercise 2"
    The affine structure requires $\mu(t,r)$ and $\sigma^2(t,r)$ to be affine in $r$ with possibly time-dependent coefficients. For Hull-White:

    $$
    \mu(t,r) = \theta(t) - ar
    $$

    This is affine in $r$ with intercept $\alpha_0(t) = \theta(t)$ and slope $\alpha_1 = -a$. The fact that $\theta(t)$ depends on calendar time $t$ does not violate the affine condition, because the condition is about linearity in the state variable $r$, not about time homogeneity.

    Substituting $P(t,T) = \exp(A(t,T) + B(t,T)\,r_t)$ into the bond pricing PDE still yields a Riccati ODE for $B(\tau)$ (which is identical to Vasicek's) and an ODE for $A(t,T)$ that now involves $\theta(t)$. The $B$-equation remains $\dot{B} = -1 + aB$, producing $B(\tau) = (1 - e^{-a\tau})/a$, independent of $\theta(t)$. The $A$-equation becomes

    $$
    \frac{\partial A}{\partial t} = -\theta(t)\,B(\tau) + \tfrac{1}{2}\sigma^2 B(\tau)^2
    $$

    which is an ordinary integral over the known function $\theta(t)$. The solution links $A(t,T)$ to the market discount curve $P^M(0,\cdot)$. The key point is that time dependence in drift coefficients preserves the affine structure; it is non-linearity in $r$ (as in Black-Karasinski) that breaks it.

---

**Exercise 3.** A risk management desk needs to compute delta, gamma, and vega for 5,000 swaptions. Under Hull-White, each Greek is an analytical derivative costing $< 0.01$ ms. Under Black-Karasinski, each Greek requires a tree revaluation costing $\sim$50 ms. Compute the total time for all Greeks under each model. If the risk report must be produced within 30 minutes, which model is feasible?

??? success "Solution to Exercise 3"
    Each swaption requires delta, gamma, and vega: 3 Greeks per swaption, for 5,000 swaptions, giving 15,000 Greek evaluations.

    **Hull-White (analytical):**

    $$
    15{,}000 \times 0.01\;\text{ms} = 150\;\text{ms} = 0.15\;\text{seconds}
    $$

    **Black-Karasinski (tree-based):**

    $$
    15{,}000 \times 50\;\text{ms} = 750{,}000\;\text{ms} = 750\;\text{seconds} \approx 12.5\;\text{minutes}
    $$

    Under the 30-minute constraint, both models are technically feasible in terms of total time. However, Hull-White completes in under 1 second, leaving ample time for report generation, data aggregation, and reruns. Black-Karasinski uses 12.5 minutes of the 30-minute window, and this estimate is optimistic: it assumes serial computation with no overhead. In practice, with data I/O, aggregation across desks, and potential reruns for scenario analysis, the 12.5 minutes would likely push the total process close to or beyond 30 minutes.

    Moreover, if the portfolio grows or if additional Greeks (cross-gamma, theta) are required, the BK approach becomes infeasible while HW remains comfortably within budget. **Hull-White is the clearly feasible and recommended model.**

---

**Exercise 4.** The CIR model is listed as having "partial" closed-form swaption pricing. Explain what this means: Jamshidian's decomposition applies, yielding a portfolio of bond puts, each of which has a closed-form CIR price via the non-central chi-squared CDF. Why is this considered "approximate" rather than fully closed-form?

??? success "Solution to Exercise 4"
    Jamshidian's decomposition converts a coupon bond option into a portfolio of zero-coupon bond options. Each zero-coupon bond option requires a closed-form price. In the CIR model, the zero-coupon bond option price is expressed as

    $$
    \text{Call}(P(T_1, T_2), K) = P(0, T_2)\,\chi^2(d_2;\,\nu,\,\lambda_2) - K\,P(0, T_1)\,\chi^2(d_1;\,\nu,\,\lambda_1)
    $$

    where $\chi^2(\cdot;\,\nu,\,\lambda)$ denotes the CDF of the non-central chi-squared distribution with $\nu$ degrees of freedom and non-centrality parameter $\lambda$, and $d_1$, $d_2$, $\lambda_1$, $\lambda_2$ are known functions of the model parameters.

    This is "partial" or "semi-analytical" rather than "fully closed-form" for several reasons:

    1. The non-central chi-squared CDF has no elementary closed-form expression; it is evaluated as an infinite series $\chi^2(x;\,\nu,\,\lambda) = \sum_{k=0}^{\infty} e^{-\lambda/2}\frac{(\lambda/2)^k}{k!}\,F_{\chi^2}(x;\,\nu+2k)$, which must be truncated.
    2. The evaluation requires numerical computation (typically via continued fractions, series expansion, or special function libraries), unlike the Vasicek/Hull-White case where only the standard normal CDF $\Phi(\cdot)$ is needed.
    3. Accuracy depends on implementation details (series truncation, numerical precision) and can degrade for extreme parameter values (small $\nu$ or large $\lambda$).

    Thus, while the CIR bond option price avoids Monte Carlo or PDE methods and is expressed through known special functions, it is not "closed-form" in the same elementary sense as the Black-Scholes or Vasicek formulas.

---

**Exercise 5.** For Monte Carlo simulation, both Vasicek and Hull-White allow exact Gaussian sampling of $r_{t+\Delta t} | r_t$, while CIR requires non-central chi-squared sampling and BK requires Gaussian sampling of $\ln r_{t+\Delta t}$. Rank these four models by per-step simulation cost and explain the ranking.

??? success "Solution to Exercise 5"
    **Ranking from fastest to slowest per simulation step:**

    1. **Vasicek** (fastest): Sample $r_{t+\Delta t} \mid r_t \sim \mathcal{N}(\mu, \nu^2)$ using a single standard normal draw plus two multiplications and one addition. Cost: one uniform random number, one inverse normal CDF evaluation (or Box-Muller), and $O(1)$ arithmetic.

    2. **Hull-White** (essentially tied with Vasicek): Same Gaussian sampling as Vasicek, but the conditional mean $\mu(t, t+\Delta t)$ depends on $\theta(t)$, requiring a lookup or interpolation of the market curve. The marginal cost over Vasicek is one interpolation per step. Cost: one normal draw plus $O(1)$ arithmetic plus one curve lookup.

    3. **Black-Karasinski**: The log-rate $x_t = \ln r_t$ is Gaussian, so $x_{t+\Delta t} \mid x_t$ can be sampled exactly as a normal variate. The cost is similar to Hull-White (one normal draw, one curve lookup for $\theta(t)$), but one must then exponentiate to recover $r_{t+\Delta t} = e^{x_{t+\Delta t}}$. More importantly, computing derived quantities (bond prices, discount factors) from the simulated $r$-paths requires numerical methods (no closed-form bond price), which adds substantial per-step overhead. Cost per rate sample: similar to HW; cost per usable price: significantly higher.

    4. **CIR** (slowest): Exact simulation requires sampling from the non-central chi-squared distribution. This is typically done by: (i) sampling a Poisson random variable $N \sim \text{Pois}(\lambda/2)$, then (ii) sampling a chi-squared with $\nu + 2N$ degrees of freedom. This requires at least two random number generations and more complex distribution sampling. Alternative methods (rejection sampling, quadratic Gaussian approximation) trade accuracy for speed. Cost: 2+ random draws, more complex special-function evaluations.

    The ranking reflects the distributional complexity: Gaussian (one draw, elementary functions) $<$ log-normal (one draw plus exponentiation, but no closed-form bonds) $<$ non-central chi-squared (multiple draws, special functions).

---

**Exercise 6.** A structured product desk prices callable range accrual notes, which are path-dependent with early exercise features. Based on the tractability table, which models can price this product? What numerical method would each use? Why might the desk choose BK over Hull-White despite the computational cost?

??? success "Solution to Exercise 6"
    A callable range accrual note has the following features: the coupon accrues only on days when a reference rate falls within a specified range (path-dependent), and the issuer can call (redeem early) on specified dates (early exercise). This combination requires:

    - **Path dependence**: The accrual condition must be evaluated at each time step along each path.
    - **Early exercise**: Backward induction is needed to determine optimal call strategy.

    **Models that can price this product:**

    - **Hull-White (trinomial tree)**: Build a recombining trinomial tree, compute the range accrual coupon at each node based on whether $r$ falls in the range, and apply backward induction for the call feature. Bond prices at each node are available in closed form.
    - **Black-Karasinski (trinomial tree)**: Same tree-based approach, but bond prices at each node require sub-tree backward induction (no closed-form bond price).
    - **CIR (tree)**: Possible but tree construction is more complex due to the $\sqrt{r}$ diffusion.
    - **Vasicek**: Not suitable for production pricing (cannot fit the yield curve), but could price the product on a tree in principle.

    **Why the desk might choose BK over Hull-White despite computational cost:**

    1. **Rate positivity**: If the range accrual references rates near zero (e.g., JPY LIBOR), the Hull-White model may generate negative rates that fall outside any reasonable accrual range, distorting the accrual probability. BK guarantees positive rates.
    2. **Log-normal smile**: The accrual probability depends on the distribution of rates around the range boundaries. The log-normal distribution of BK may better match the market-implied distribution (inferred from cap smile data) than the normal distribution of HW.
    3. **Skewness**: BK produces positively skewed rate distributions, which can materially affect the probability of rates falling in asymmetric ranges.

    The desk accepts the higher computational cost (roughly 10--100$\times$ slower per tree evaluation) because the pricing accuracy for this specific product outweighs the speed advantage of Hull-White.

---

**Exercise 7.** Consider a scenario where the market exhibits negative rates. Which models from the table can naturally handle negative rates? For those that cannot, what modifications are needed? Discuss the impact of these modifications on analytical tractability.

??? success "Solution to Exercise 7"
    **Models that naturally handle negative rates:**

    - **Vasicek**: The short rate follows a Gaussian (Ornstein-Uhlenbeck) process, so $r_t$ can take any real value, including negative. Negative rates are a natural feature, not a bug, of the model.
    - **Hull-White**: Same Gaussian structure as Vasicek with time-dependent drift. Negative rates occur with positive probability, and the model requires no modification.

    **Models that cannot naturally handle negative rates:**

    - **CIR**: Under the Feller condition $2\kappa\theta \ge \sigma^2$, the rate stays strictly positive. The $\sqrt{r_t}$ diffusion vanishes at zero, creating a natural boundary.
        - *Modification for negative rates*: Use a **shifted CIR** model: let $r_t = x_t + \delta$ where $x_t$ follows a CIR process and $\delta < 0$ is a shift parameter. The shifted rate $r_t$ can be negative (down to $\delta$) while $x_t$ remains positive. This preserves the affine structure: $P(t,T) = e^{A(\tau) + B(\tau)(r_t - \delta)}$ can still be computed in closed form with modified $A$ coefficients. Tractability is **largely preserved**.
    - **Black-Karasinski**: The short rate is $r_t = e^{x_t}$ where $x_t$ is Gaussian, so $r_t > 0$ always.
        - *Modification for negative rates*: Use a **shifted BK** model: $r_t = e^{x_t} + \delta$ with $\delta < 0$. This allows rates down to $\delta$ but introduces additional complexity into the already numerical pricing framework. Since BK already requires tree-based pricing, the shift adds a layer of complexity to tree construction (the shift must be incorporated at every node) but does not fundamentally change the computational method. Tractability impact: **moderate** (BK was already non-analytical, so the marginal loss is smaller).

    **Summary of tractability impact:**

    | Model | Modification | Closed-form bonds | Closed-form options | Speed impact |
    |-------|-------------|:-----------------:|:-------------------:|:------------:|
    | Vasicek | None needed | Yes | Yes | None |
    | Hull-White | None needed | Yes | Yes | None |
    | CIR $\to$ Shifted CIR | Shift $\delta < 0$ | Yes (modified $A$) | Yes (modified) | Minimal |
    | BK $\to$ Shifted BK | Shift $\delta < 0$ | No | No | Moderate |

    The Gaussian models are naturally suited to negative-rate environments, which is one reason Hull-White became even more dominant after European and Japanese rates turned negative. The shifted CIR preserves most tractability, while shifted BK adds complexity to an already numerical framework.
