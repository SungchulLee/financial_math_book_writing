# Survival Measure

The **survival measure** (or **$T$-survival measure**) is a change-of-measure technique that conditions on the event of no default up to a given horizon. By restricting the probability space to survival scenarios, it eliminates the default indicator from pricing formulas and converts pre-default valuation problems into standard expectations under a modified measure. This technique is the credit-risk analogue of the forward measure used in interest rate modeling.

---

## Motivation

### The Pre-Default Pricing Problem

Consider a defaultable claim paying $X$ at maturity $T$ if no default occurs. Under the risk-neutral measure $\mathbb{Q}$, the pre-default price at time $t$ (on $\{\tau > t\}$) is:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} X \cdot \mathbf{1}_{\{\tau > T\}} \mid \mathcal{G}_t\right]
$$

Under immersion, this simplifies to:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} X \mid \mathcal{F}_t\right]
$$

The intensity $\lambda_s$ couples credit and market risk within the expectation. The survival measure decouples them by absorbing the survival weighting into the probability measure.

### Analogy with Forward Measure

In interest rate theory, the **$T$-forward measure** $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire, eliminating the stochastic discount factor from pricing. Similarly, the **$T$-survival measure** uses the survival-contingent zero-coupon bond as numeraire, eliminating the survival probability from the expectation.

---

## Construction of the Survival Measure

### The Survival-Contingent Numeraire

Define the **defaultable zero-coupon bond with zero recovery**:

$$
\bar{P}(t,T) := \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} \mid \mathcal{F}_t\right]
$$

This is the price of a claim that pays 1 at time $T$ if and only if no default occurs, with no recovery at default. It combines interest rate discounting with survival weighting.

### Definition of the Survival Measure

!!! abstract "Definition"
    The **$T$-survival measure** $\mathbb{Q}^S$ (or $\mathbb{Q}^{T,S}$) is defined on $\mathcal{F}_T$ by the Radon-Nikodym derivative:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T (r_s + \lambda_s)ds}}{\bar{P}(0,T)}
    $$

    Equivalently, for $t \le T$:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{\bar{P}(t,T) \cdot e^{-\int_0^t (r_s + \lambda_s)ds}}{\bar{P}(0,T)}
    $$

### Well-Definedness

The Radon-Nikodym density is:

- **Positive:** Since $e^{-\int_0^T (r_s + \lambda_s)ds} > 0$ a.s.
- **Normalized:** $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S / d\mathbb{Q}] = 1$ by construction

Therefore $\mathbb{Q}^S$ is a well-defined probability measure equivalent to $\mathbb{Q}$ on $\mathcal{F}_T$.

---

## Pricing Under the Survival Measure

### Main Pricing Formula

!!! abstract "Theorem"
    For an $\mathcal{F}_T$-measurable payoff $X$ received at time $T$ conditional on survival:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} X \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}\left[X \mid \mathcal{F}_t\right]
    $$

??? info "Proof"
    By the abstract Bayes formula for change of measure:

    $$
    \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t] = \frac{\mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} X \mid \mathcal{F}_t\right]}{\mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} \mid \mathcal{F}_t\right]}
    $$

    Substituting the Radon-Nikodym derivative:

    $$
    = \frac{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r_s + \lambda_s)ds} X \mid \mathcal{F}_t\right] / \bar{P}(0,T)}{e^{-\int_0^t (r_s+\lambda_s)ds} \bar{P}(t,T) / \bar{P}(0,T)}
    $$

    $$
    = \frac{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} X \mid \mathcal{F}_t\right]}{\bar{P}(t,T)}
    $$

    Rearranging gives the result. $\square$

### Interpretation

The formula separates:

- **$\bar{P}(t,T)$:** The "price of survival"---discounting for both time value and credit risk
- **$\mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t]$:** The expected payoff in a world where default cannot occur

Under $\mathbb{Q}^S$, the payoff $X$ is evaluated as if default were impossible, but the measure itself adjusts probabilities to account for the conditioning on survival.

---

## Effect on Dynamics

### Girsanov Theorem Application

Under $\mathbb{Q}$, suppose market state variables follow:

$$
dX_t = \mu^{\mathbb{Q}}(X_t) dt + \sigma(X_t) dW_t^{\mathbb{Q}}
$$

Under $\mathbb{Q}^S$, by the Girsanov theorem, the drift changes:

$$
dX_t = \mu^{\mathbb{Q}^S}(X_t) dt + \sigma(X_t) dW_t^{\mathbb{Q}^S}
$$

where:

$$
\mu^{\mathbb{Q}^S}(X_t) = \mu^{\mathbb{Q}}(X_t) + \sigma(X_t) \sigma(X_t)^\top \nabla_X \ln \bar{P}(t,T)
$$

The extra drift $\sigma \sigma^\top \nabla_X \ln \bar{P}$ reflects the bias introduced by conditioning on survival. State variables that increase survival probability are given higher weight under $\mathbb{Q}^S$.

### Effect on Interest Rate

If the short rate $r_t$ is one of the state variables, its drift under $\mathbb{Q}^S$ changes to:

$$
\mu_r^{\mathbb{Q}^S} = \mu_r^{\mathbb{Q}} + \sigma_r^2 \frac{\partial \ln \bar{P}(t,T)}{\partial r}
$$

Since $\partial \bar{P}/\partial r < 0$ (higher rates reduce bond price), the drift of $r$ under $\mathbb{Q}^S$ is **lower** than under $\mathbb{Q}$.

### Effect on Default Intensity

Similarly, the intensity drift under $\mathbb{Q}^S$ changes:

$$
\mu_\lambda^{\mathbb{Q}^S} = \mu_\lambda^{\mathbb{Q}} + \sigma_\lambda^2 \frac{\partial \ln \bar{P}(t,T)}{\partial \lambda}
$$

Since $\partial \bar{P}/\partial \lambda < 0$ (higher intensity reduces survival probability), the drift of $\lambda$ under $\mathbb{Q}^S$ is **lower**. Intuitively, conditioning on survival biases the intensity downward.

---

## Independent Rates and Intensity

### Simplification Under Independence

When $r_t$ and $\lambda_t$ are independent under $\mathbb{Q}$:

$$
\bar{P}(t,T) = P(t,T) \cdot S(t,T)
$$

where $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s ds} \mid \mathcal{F}_t]$ and $S(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t]$.

The survival measure factorizes into components affecting rates and intensity separately, and the Girsanov drift corrections simplify.

### CIR Intensity Example

Suppose $\lambda_t$ follows a CIR process:

$$
d\lambda_t = \kappa(\theta - \lambda_t) dt + \sigma\sqrt{\lambda_t} \, dW_t^{\mathbb{Q}}
$$

Under $\mathbb{Q}^S$ (with CIR intensity independent of rates):

$$
d\lambda_t = \kappa^S(\theta^S - \lambda_t) dt + \sigma\sqrt{\lambda_t} \, dW_t^{\mathbb{Q}^S}
$$

where the adjusted parameters are:

$$
\kappa^S = \kappa + \sigma^2 B(t,T), \quad \theta^S = \frac{\kappa\theta}{\kappa + \sigma^2 B(t,T)}
$$

and $B(t,T)$ is the coefficient from the affine survival probability $S(t,T) = A(T-t)e^{-B(T-t)\lambda_t}$.

The intensity mean-reverts **faster** and toward a **lower** level under $\mathbb{Q}^S$, consistent with conditioning on survival.

---

## Applications

### Pricing Defaultable Bonds

For a zero-coupon defaultable bond with zero recovery:

$$
\bar{P}(t,T) = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}\left[\frac{S(t,T)}{1}\right]
$$

With recovery $R$ under RMV:

$$
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + (1-R)\lambda_s) ds} \mid \mathcal{F}_t\right]
$$

This can be evaluated under an appropriately defined survival measure with modified intensity loading $(1-R)\lambda$.

### CDS Pricing

The par CDS spread involves the ratio:

$$
s_{\text{par}} = \frac{(1-R) \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s)ds} \lambda_u du\right]}{\sum_i \Delta_i \bar{P}(t, t_i)}
$$

The denominator is the risky annuity, directly computed from $\bar{P}(t, t_i)$. The numerator can be rewritten using the survival measure to simplify the computation.

### Quanto-Survival Expectations

Expectations of the form:

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} f(\lambda_T)\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[f(\lambda_T)]
$$

arise when pricing options on credit spreads or when the payoff depends on the level of the intensity at maturity. Under $\mathbb{Q}^S$, one computes a standard expectation of $f(\lambda_T)$, then multiplies by the survival-weighted discount factor.

### Defaultable Swaptions

For swaptions on defaultable interest rate swaps, the survival measure provides the natural pricing framework:

$$
V_t = \bar{P}(t,T_0) \cdot \mathbb{E}^{\mathbb{Q}^S}\left[\left(\text{Swap Rate} - K\right)^+\right]
$$

The swap rate under $\mathbb{Q}^S$ incorporates credit-adjusted forward rates.

---

## Comparison with Other Measures

| Measure | Numeraire | Eliminates | Primary Use |
|---------|-----------|------------|-------------|
| Risk-neutral $\mathbb{Q}$ | Money market $e^{\int r_s ds}$ | None | General pricing |
| $T$-forward $\mathbb{Q}^T$ | $P(t,T)$ | Stochastic discounting | Interest rate derivatives |
| $T$-survival $\mathbb{Q}^S$ | $\bar{P}(t,T)$ | Stochastic discounting + survival | Defaultable claims |

The survival measure is strictly more powerful than the forward measure for credit-risky instruments because it handles both the interest rate and the default components simultaneously.

---

## Numerical Example

**Setup:** CIR intensity with $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1.5\%$, $r = 3\%$ (constant), $T = 3$ years.

**Step 1: Survival probability (CIR affine formula)**

$$
\gamma = \sqrt{0.25 + 0.0128} = 0.5128
$$

$$
B(3) = \frac{2(e^{1.538} - 1)}{(1.013)(e^{1.538} - 1) + 1.026} = \frac{2(3.655)}{1.013(3.655) + 1.026} = \frac{7.310}{4.728} = 1.546
$$

$$
S(0,3) \approx A(3) \cdot e^{-1.546 \times 0.015}
$$

After computing $A(3) \approx 0.968$:

$$
S(0,3) \approx 0.968 \times 0.977 = 0.946
$$

**Step 2: Survival-weighted discount factor**

$$
\bar{P}(0,3) = e^{-0.03 \times 3} \times 0.946 = 0.914 \times 0.946 = 0.865
$$

**Step 3: CIR drift under survival measure**

$$
\kappa^S = 0.5 + 0.0064 \times 1.546 = 0.5 + 0.0099 = 0.510
$$

$$
\theta^S = \frac{0.5 \times 0.02}{0.510} = 0.0196 = 1.96\%
$$

Under $\mathbb{Q}^S$, the intensity mean-reverts faster ($\kappa^S = 0.510$ vs $\kappa = 0.500$) toward a lower level ($\theta^S = 1.96\%$ vs $\theta = 2\%$). The effects are modest here because $\sigma$ is small, but they become pronounced for volatile, high-intensity names.

---

## Key Takeaways

- The survival measure $\mathbb{Q}^S$ is defined by using the zero-recovery defaultable bond as numeraire
- It eliminates the survival indicator from pricing formulas: $V_t = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[X]$
- Under $\mathbb{Q}^S$, drift changes push interest rates lower and default intensity lower, reflecting conditioning on survival
- For CIR intensity, the adjusted parameters have closed-form expressions
- The survival measure is the credit-risk analogue of the forward measure in interest rate theory
- Applications include defaultable bond pricing, CDS valuation, and credit spread options

---

## Further Reading

- Schonbucher, P. J. (2003). *Credit Derivatives Pricing Models*. Wiley, Chapter 5.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 10.
- Collin-Dufresne, P., Goldstein, R., & Hugonnier, J. (2004). A general formula for valuing defaultable securities. *Econometrica*, 72(5), 1377--1407.
- Jeanblanc, M., Yor, M., & Chesney, M. (2009). *Mathematical Methods for Financial Markets*. Springer.

---

## Exercises

**Exercise 1.** Let $r = 4\%$ (constant) and suppose default intensity follows a CIR process with $\kappa = 0.3$, $\theta = 3\%$, $\sigma = 6\%$, and $\lambda_0 = 2\%$. Using the affine formula for the survival probability, compute the defaultable zero-coupon bond price $\bar{P}(0, 5)$ and the survival measure parameters $\kappa^S$ and $\theta^S$. Verify that $\kappa^S > \kappa$ and $\theta^S < \theta$.

---

**Exercise 2.** Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T (r_s + \lambda_s) ds}}{\bar{P}(0,T)}
$$

verify that $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_T}] = 1$. Then show that the restricted density $d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_t}$ is a $\mathbb{Q}$-martingale.

---

**Exercise 3.** Prove the main pricing formula: for an $\mathcal{F}_T$-measurable payoff $X$,

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} X \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t]
$$

by applying the abstract Bayes formula. Identify each step of the argument.

---

**Exercise 4.** Suppose $r_t$ and $\lambda_t$ are independent under $\mathbb{Q}$, with $r_t$ following a Vasicek model and $\lambda_t$ following a CIR model. Show that the defaultable bond price factorizes as $\bar{P}(t,T) = P(t,T) \cdot S(t,T)$. Under the survival measure, do the Girsanov drift corrections for $r_t$ and $\lambda_t$ interact, or are they independent? Justify your answer.

---

**Exercise 5.** Consider a defaultable coupon bond paying $c$ at times $t_1, \ldots, t_n = T$ conditional on survival, with recovery $R$ paid at default. Express the price of this bond using the survival measure $\mathbb{Q}^S$ and the defaultable zero-coupon bonds $\bar{P}(t, t_i)$. Compare this expression with the standard risk-neutral pricing formula.

---

**Exercise 6.** Using the numerical example parameters ($\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1.5\%$, $r = 3\%$), compute the par CDS spread for a 3-year CDS with quarterly premium payments and 40% recovery. Use the survival measure to simplify the computation of the risky annuity in the denominator.

---

**Exercise 7.** Compare the $T$-forward measure and the $T$-survival measure by answering the following: (a) What numeraire defines each measure? (b) What quantity is eliminated from pricing formulas by each measure change? (c) Under what condition does the survival measure reduce to the forward measure? (d) Give an example of a derivative for which the survival measure is essential but the forward measure is insufficient.
