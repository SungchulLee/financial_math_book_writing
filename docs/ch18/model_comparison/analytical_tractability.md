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

---

**Exercise 2.** In the Hull-White model, the time-dependent drift $\theta(t)$ is chosen to fit the initial yield curve exactly. Explain why this does not break the affine structure. Specifically, show that $\theta(t) - ar$ is still affine in $r$ even though $\theta(t)$ is time-dependent.

---

**Exercise 3.** A risk management desk needs to compute delta, gamma, and vega for 5,000 swaptions. Under Hull-White, each Greek is an analytical derivative costing $< 0.01$ ms. Under Black-Karasinski, each Greek requires a tree revaluation costing $\sim$50 ms. Compute the total time for all Greeks under each model. If the risk report must be produced within 30 minutes, which model is feasible?

---

**Exercise 4.** The CIR model is listed as having "partial" closed-form swaption pricing. Explain what this means: Jamshidian's decomposition applies, yielding a portfolio of bond puts, each of which has a closed-form CIR price via the non-central chi-squared CDF. Why is this considered "approximate" rather than fully closed-form?

---

**Exercise 5.** For Monte Carlo simulation, both Vasicek and Hull-White allow exact Gaussian sampling of $r_{t+\Delta t} | r_t$, while CIR requires non-central chi-squared sampling and BK requires Gaussian sampling of $\ln r_{t+\Delta t}$. Rank these four models by per-step simulation cost and explain the ranking.

---

**Exercise 6.** A structured product desk prices callable range accrual notes, which are path-dependent with early exercise features. Based on the tractability table, which models can price this product? What numerical method would each use? Why might the desk choose BK over Hull-White despite the computational cost?

---

**Exercise 7.** Consider a scenario where the market exhibits negative rates. Which models from the table can naturally handle negative rates? For those that cannot, what modifications are needed? Discuss the impact of these modifications on analytical tractability.
