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
    The **$T$-survival measure** $\mathbb{Q}^S$ (or $\mathbb{Q}^{T,S}$) is defined on $\mathcal{F}_T$ by the Radon–Nikodym derivative:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T (r_s + \lambda_s)ds}}{\bar{P}(0,T)}
    $$

    Equivalently, for $t \le T$:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \frac{\bar{P}(t,T) \cdot e^{-\int_0^t (r_s + \lambda_s)ds}}{\bar{P}(0,T)}
    $$

### Well-Definedness

The Radon–Nikodym density is:

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

    Substituting the Radon–Nikodym derivative:

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

??? success "Solution to Exercise 1"
    **Step 1: Compute $\gamma$ for the CIR affine formula.**

    With $\kappa = 0.3$, $\sigma = 0.06$:

    $$
    \gamma = \sqrt{\kappa^2 + 2\sigma^2} = \sqrt{0.09 + 2(0.0036)} = \sqrt{0.09 + 0.0072} = \sqrt{0.0972} \approx 0.3118
    $$

    **Step 2: Compute $B(0,5)$.**

    $$
    B(\tau) = \frac{2(e^{\gamma \tau} - 1)}{(\gamma + \kappa)(e^{\gamma \tau} - 1) + 2\gamma}, \quad \tau = T = 5
    $$

    Compute $\gamma \tau = 0.3118 \times 5 = 1.559$, so $e^{1.559} \approx 4.754$:

    $$
    B(5) = \frac{2(4.754 - 1)}{(0.3118 + 0.3)(4.754 - 1) + 2(0.3118)} = \frac{2(3.754)}{0.6118(3.754) + 0.6236}
    $$

    $$
    = \frac{7.508}{2.296 + 0.624} = \frac{7.508}{2.920} \approx 2.572
    $$

    **Step 3: Compute $A(\tau)$.**

    $$
    \ln A(\tau) = \frac{2\kappa\theta}{\sigma^2}\ln\left(\frac{2\gamma e^{(\gamma+\kappa)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\right)
    $$

    $$
    \frac{2\kappa\theta}{\sigma^2} = \frac{2(0.3)(0.03)}{0.0036} = \frac{0.018}{0.0036} = 5.0
    $$

    The denominator is $2.920$ (from above). The numerator:

    $$
    2\gamma e^{(\gamma+\kappa)\tau/2} = 2(0.3118)e^{(0.6118)(2.5)} = 0.6236 \cdot e^{1.530} = 0.6236 \times 4.618 = 2.880
    $$

    $$
    \ln A(5) = 5.0 \times \ln\left(\frac{2.880}{2.920}\right) = 5.0 \times \ln(0.9863) = 5.0 \times (-0.01380) = -0.0690
    $$

    $$
    A(5) = e^{-0.0690} \approx 0.9333
    $$

    **Step 4: Survival probability.**

    $$
    S(0,5) = A(5) \cdot e^{-B(5)\lambda_0} = 0.9333 \times e^{-2.572 \times 0.02} = 0.9333 \times e^{-0.05144}
    $$

    $$
    = 0.9333 \times 0.9499 \approx 0.8866
    $$

    **Step 5: Defaultable zero-coupon bond price.**

    With constant $r = 4\%$:

    $$
    \bar{P}(0,5) = e^{-0.04 \times 5} \times S(0,5) = e^{-0.20} \times 0.8866 = 0.8187 \times 0.8866 \approx 0.7258
    $$

    **Step 6: Survival measure parameters.**

    $$
    \kappa^S = \kappa + \sigma^2 B(0,5) = 0.3 + (0.0036)(2.572) = 0.3 + 0.00926 = 0.3093
    $$

    $$
    \theta^S = \frac{\kappa\theta}{\kappa^S} = \frac{0.3 \times 0.03}{0.3093} = \frac{0.009}{0.3093} = 0.02910 = 2.91\%
    $$

    **Verification:**

    - $\kappa^S = 0.3093 > 0.3 = \kappa$ $\checkmark$ (faster mean reversion under survival measure)
    - $\theta^S = 2.91\% < 3.0\% = \theta$ $\checkmark$ (lower long-run mean under survival measure)

    Both results are consistent with the intuition: conditioning on survival biases the intensity downward (lower long-run level) and makes it mean-revert faster toward that lower level.

---

**Exercise 2.** Starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T (r_s + \lambda_s) ds}}{\bar{P}(0,T)}
$$

verify that $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_T}] = 1$. Then show that the restricted density $d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_t}$ is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 2"
    **Part 1: Normalization $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_T}] = 1$.**

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T}\right] = \mathbb{E}^{\mathbb{Q}}\left[\frac{e^{-\int_0^T (r_s + \lambda_s) ds}}{\bar{P}(0,T)}\right]
    $$

    $$
    = \frac{1}{\bar{P}(0,T)} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r_s + \lambda_s) ds}\right]
    $$

    By definition of $\bar{P}(0,T)$:

    $$
    \bar{P}(0,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r_s + \lambda_s) ds}\right]
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T}\right] = \frac{\bar{P}(0,T)}{\bar{P}(0,T)} = 1 \quad \checkmark
    $$

    **Part 2: The restricted density is a $\mathbb{Q}$-martingale.**

    Define $Z_t := \mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} \,\bigg|\, \mathcal{F}_t\right]$. By the tower property of conditional expectation, for $s \le t$:

    $$
    \mathbb{E}^{\mathbb{Q}}[Z_t \mid \mathcal{F}_s] = \mathbb{E}^{\mathbb{Q}}\left[\mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} \,\bigg|\, \mathcal{F}_t\right] \,\bigg|\, \mathcal{F}_s\right] = \mathbb{E}^{\mathbb{Q}}\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} \,\bigg|\, \mathcal{F}_s\right] = Z_s
    $$

    So $Z_t$ is a $\mathbb{Q}$-martingale by the tower property.

    Now we verify the explicit formula. Compute:

    $$
    Z_t = \mathbb{E}^{\mathbb{Q}}\left[\frac{e^{-\int_0^T (r_s + \lambda_s)ds}}{\bar{P}(0,T)} \,\bigg|\, \mathcal{F}_t\right] = \frac{e^{-\int_0^t (r_s + \lambda_s)ds}}{\bar{P}(0,T)} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} \mid \mathcal{F}_t\right]
    $$

    $$
    = \frac{e^{-\int_0^t (r_s + \lambda_s)ds} \cdot \bar{P}(t,T)}{\bar{P}(0,T)}
    $$

    This matches the restricted density formula given in the definition. The martingale property of $Z_t$ is equivalent to the statement that $e^{-\int_0^t (r_s + \lambda_s)ds} \bar{P}(t,T)$ is a $\mathbb{Q}$-martingale, which is precisely the statement that $\bar{P}(t,T)$ grows at the rate $r_t + \lambda_t$ under $\mathbb{Q}$ (the discounted defaultable bond price is a martingale). $\square$

---

**Exercise 3.** Prove the main pricing formula: for an $\mathcal{F}_T$-measurable payoff $X$,

$$
\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} X \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t]
$$

by applying the abstract Bayes formula. Identify each step of the argument.

??? success "Solution to Exercise 3"
    We prove the pricing formula using the abstract Bayes formula.

    **Abstract Bayes formula:** For any $\mathcal{F}_T$-measurable $X$ and a measure change with density $Z_T = d\mathbb{Q}^S/d\mathbb{Q}|_{\mathcal{F}_T}$:

    $$
    \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t] = \frac{\mathbb{E}^{\mathbb{Q}}[Z_T \cdot X \mid \mathcal{F}_t]}{\mathbb{E}^{\mathbb{Q}}[Z_T \mid \mathcal{F}_t]}
    $$

    **Step 1: Identify $Z_T$.**

    $$
    Z_T = \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{e^{-\int_0^T (r_s + \lambda_s)ds}}{\bar{P}(0,T)}
    $$

    **Step 2: Compute the denominator.**

    $$
    \mathbb{E}^{\mathbb{Q}}[Z_T \mid \mathcal{F}_t] = Z_t = \frac{e^{-\int_0^t (r_s + \lambda_s)ds} \cdot \bar{P}(t,T)}{\bar{P}(0,T)}
    $$

    (This was established in Exercise 2.)

    **Step 3: Compute the numerator.**

    $$
    \mathbb{E}^{\mathbb{Q}}[Z_T \cdot X \mid \mathcal{F}_t] = \frac{1}{\bar{P}(0,T)} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T (r_s+\lambda_s)ds} X \mid \mathcal{F}_t\right]
    $$

    $$
    = \frac{e^{-\int_0^t (r_s+\lambda_s)ds}}{\bar{P}(0,T)} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s+\lambda_s)ds} X \mid \mathcal{F}_t\right]
    $$

    **Step 4: Form the ratio.**

    $$
    \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t] = \frac{\frac{e^{-\int_0^t (r_s+\lambda_s)ds}}{\bar{P}(0,T)} \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s+\lambda_s)ds} X \mid \mathcal{F}_t\right]}{\frac{e^{-\int_0^t (r_s+\lambda_s)ds} \cdot \bar{P}(t,T)}{\bar{P}(0,T)}}
    $$

    The factors $e^{-\int_0^t (r_s+\lambda_s)ds}$ and $\bar{P}(0,T)$ cancel:

    $$
    = \frac{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s+\lambda_s)ds} X \mid \mathcal{F}_t\right]}{\bar{P}(t,T)}
    $$

    **Step 5: Rearrange.**

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s+\lambda_s)ds} X \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t]
    $$

    This is the desired pricing formula. $\square$

    **Key insight:** The survival measure absorbs the stochastic discounting (both interest rate and survival components) into the measure change, leaving only the "pure" expectation of $X$ under $\mathbb{Q}^S$ multiplied by the deterministic-at-time-$t$ quantity $\bar{P}(t,T)$.

---

**Exercise 4.** Suppose $r_t$ and $\lambda_t$ are independent under $\mathbb{Q}$, with $r_t$ following a Vasicek model and $\lambda_t$ following a CIR model. Show that the defaultable bond price factorizes as $\bar{P}(t,T) = P(t,T) \cdot S(t,T)$. Under the survival measure, do the Girsanov drift corrections for $r_t$ and $\lambda_t$ interact, or are they independent? Justify your answer.

??? success "Solution to Exercise 4"
    **Factorization under independence.**

    When $r_t$ and $\lambda_t$ are independent under $\mathbb{Q}$:

    $$
    \bar{P}(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s)ds} \mid \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} \mid \mathcal{F}_t^r\right] \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T \lambda_s ds} \mid \mathcal{F}_t^\lambda\right]
    $$

    $$
    = P(t,T) \cdot S(t,T)
    $$

    The factorization holds because for independent random variables $X, Y$: $\mathbb{E}[e^{-(X+Y)}] = \mathbb{E}[e^{-X}]\mathbb{E}[e^{-Y}]$.

    Here $r_t$ follows a Vasicek model: $dr_t = a(b - r_t)dt + \sigma_r dW_t^{r,\mathbb{Q}}$ and $\lambda_t$ follows a CIR model: $d\lambda_t = \kappa(\theta - \lambda_t)dt + \sigma_\lambda \sqrt{\lambda_t} \, dW_t^{\lambda,\mathbb{Q}}$ with $W^r$ and $W^\lambda$ independent.

    **Girsanov drift corrections.**

    The Radon--Nikodym density factorizes:

    $$
    Z_T = \frac{e^{-\int_0^T r_s ds} \cdot e^{-\int_0^T \lambda_s ds}}{\bar{P}(0,T)} = \frac{e^{-\int_0^T r_s ds}}{P(0,T)} \cdot \frac{e^{-\int_0^T \lambda_s ds}}{S(0,T)}
    $$

    **For $r_t$ (Vasicek):** The Girsanov drift correction depends only on $\nabla_r \ln P(t,T)$:

    $$
    \mu_r^{\mathbb{Q}^S} = a(b - r_t) + \sigma_r^2 \frac{\partial \ln P(t,T)}{\partial r}
    $$

    For Vasicek, $P(t,T) = A_r(T-t) e^{-B_r(T-t) r_t}$ where $B_r(\tau) = \frac{1-e^{-a\tau}}{a}$, so $\frac{\partial \ln P}{\partial r} = -B_r(T-t)$ and:

    $$
    \mu_r^{\mathbb{Q}^S} = a(b - r_t) - \sigma_r^2 B_r(T-t)
    $$

    This depends only on $r_t$ and time, not on $\lambda_t$.

    **For $\lambda_t$ (CIR):** The drift correction depends only on $\nabla_\lambda \ln S(t,T)$:

    $$
    \mu_\lambda^{\mathbb{Q}^S} = \kappa(\theta - \lambda_t) + \sigma_\lambda^2 \lambda_t \frac{\partial \ln S(t,T)}{\partial \lambda}
    $$

    For CIR, $S(t,T) = A_\lambda(T-t) e^{-B_\lambda(T-t)\lambda_t}$, so $\frac{\partial \ln S}{\partial \lambda} = -B_\lambda(T-t)$ and:

    $$
    \mu_\lambda^{\mathbb{Q}^S} = \kappa(\theta - \lambda_t) - \sigma_\lambda^2 B_\lambda(T-t) \lambda_t = (\kappa + \sigma_\lambda^2 B_\lambda)(\theta^S - \lambda_t)
    $$

    This depends only on $\lambda_t$ and time, not on $r_t$.

    **Conclusion:** The Girsanov drift corrections for $r_t$ and $\lambda_t$ are **independent**---each correction involves only the respective state variable and the corresponding component of $\bar{P}(t,T)$. This is a direct consequence of the independence assumption and the factorization $\bar{P} = P \cdot S$. If $r_t$ and $\lambda_t$ were correlated, cross-derivative terms would appear in the Girsanov corrections, coupling the two dynamics under $\mathbb{Q}^S$.

---

**Exercise 5.** Consider a defaultable coupon bond paying $c$ at times $t_1, \ldots, t_n = T$ conditional on survival, with recovery $R$ paid at default. Express the price of this bond using the survival measure $\mathbb{Q}^S$ and the defaultable zero-coupon bonds $\bar{P}(t, t_i)$. Compare this expression with the standard risk-neutral pricing formula.

??? success "Solution to Exercise 5"
    **Defaultable coupon bond price under $\mathbb{Q}$:**

    The bond pays coupon $c$ at times $t_1, \ldots, t_n = T$ conditional on survival, plus principal 1 at $T$ conditional on survival, and recovery $R$ at default.

    Under the risk-neutral measure:

    $$
    V_t = \underbrace{\sum_{i=1}^{n} c \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{t_i}(r_s + \lambda_s)ds} \mid \mathcal{F}_t\right]}_{\text{coupon payments}} + \underbrace{\mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^{T}(r_s + \lambda_s)ds} \mid \mathcal{F}_t\right]}_{\text{principal}} + \underbrace{R \cdot \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u r_s ds} \lambda_u e^{-\int_t^u \lambda_s ds} du \mid \mathcal{F}_t\right]}_{\text{recovery at default}}
    $$

    **Rewriting using the survival measure:**

    Apply the pricing formula $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^{t_i}(r_s+\lambda_s)ds} X \mid \mathcal{F}_t] = \bar{P}(t,t_i) \cdot \mathbb{E}^{\mathbb{Q}^{S_i}}[X \mid \mathcal{F}_t]$ for each maturity $t_i$:

    **Coupon and principal terms:**

    $$
    \sum_{i=1}^{n} c \cdot \bar{P}(t, t_i) + \bar{P}(t, T)
    $$

    Here the payoff $X = c$ (or $X = 1$) is deterministic, so $\mathbb{E}^{\mathbb{Q}^{S_i}}[c] = c$.

    **Recovery term:** The recovery payment involves a more complex expectation. Using the identity:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\int_t^T e^{-\int_t^u (r_s + \lambda_s)ds} \lambda_u \, du \mid \mathcal{F}_t\right] = -\int_t^T \frac{\partial}{\partial u}\bar{P}(t,u) \, du = \bar{P}(t,t) - \bar{P}(t,T) = 1 - \bar{P}(t,T)
    $$

    (when $r$ and $\lambda$ are deterministic, or using stochastic Fubini more generally with appropriate integrability).

    More generally, the recovery term can be written as:

    $$
    R \int_t^T \bar{P}(t, u) \cdot \mathbb{E}^{\mathbb{Q}^{S_u}}[\lambda_u \mid \mathcal{F}_t] \, du
    $$

    **Complete expression using survival measure:**

    $$
    V_t = \sum_{i=1}^{n} c \cdot \bar{P}(t, t_i) + \bar{P}(t, T) + R \int_t^T \bar{P}(t, u) \cdot \mathbb{E}^{\mathbb{Q}^{S_u}}[\lambda_u \mid \mathcal{F}_t] \, du
    $$

    **Comparison with standard risk-neutral pricing:**

    - The standard formula requires computing expectations involving the joint distribution of $(r, \lambda)$ inside the exponential
    - The survival measure formula separates the "price of survival" ($\bar{P}$) from the "payoff evaluation" (expectations under $\mathbb{Q}^S$)
    - For deterministic or affine models, $\bar{P}(t, t_i)$ has closed-form expressions, making the survival measure approach computationally efficient
    - The coupon and principal components are expressed as simple sums of defaultable zero-coupon bond prices, directly analogous to how default-free coupon bonds are sums of zero-coupon bonds

---

**Exercise 6.** Using the numerical example parameters ($\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1.5\%$, $r = 3\%$), compute the par CDS spread for a 3-year CDS with quarterly premium payments and 40% recovery. Use the survival measure to simplify the computation of the risky annuity in the denominator.

??? success "Solution to Exercise 6"
    **Parameters:** $\kappa = 0.5$, $\theta = 2\%$, $\sigma = 8\%$, $\lambda_0 = 1.5\%$, $r = 3\%$, $T = 3$ years, quarterly premiums, $R = 40\%$.

    **Par CDS spread formula:**

    $$
    s_{\text{par}} = \frac{(1-R) \cdot \text{Protection Leg}}{\text{Risky Annuity}}
    $$

    **Step 1: Compute $\bar{P}(0, t_i)$ for quarterly dates.**

    Using the CIR affine formula with $\gamma = \sqrt{0.25 + 2(0.0064)} = \sqrt{0.2628} \approx 0.5126$ (from the numerical example in the text):

    For each quarterly date $t_i = 0.25, 0.5, \ldots, 3.0$, we compute $S(0, t_i)$ via the CIR formula and $\bar{P}(0, t_i) = e^{-r \cdot t_i} \cdot S(0, t_i)$.

    Using the numerical example values and interpolating (the text gives $S(0,3) \approx 0.946$), we approximate a few key values:

    | $t_i$ | $e^{-0.03 t_i}$ | $S(0, t_i)$ (approx.) | $\bar{P}(0, t_i)$ |
    |:------:|:----------------:|:----------------------:|:------------------:|
    | 0.25 | 0.9925 | 0.9963 | 0.9889 |
    | 0.50 | 0.9851 | 0.9925 | 0.9778 |
    | 1.00 | 0.9704 | 0.9847 | 0.9556 |
    | 2.00 | 0.9418 | 0.9675 | 0.9112 |
    | 3.00 | 0.9139 | 0.9460 | 0.8646 |

    **Step 2: Risky annuity (using survival measure).**

    $$
    A = \sum_{i=1}^{12} \Delta_i \cdot \bar{P}(0, t_i) \quad \text{where } \Delta_i = 0.25
    $$

    Approximating the sum by trapezoidal rule on the quarterly grid:

    $$
    A \approx 0.25 \times \left(\bar{P}(0, 0.25) + \bar{P}(0, 0.5) + \cdots + \bar{P}(0, 3.0)\right)
    $$

    Using a smooth interpolation of $\bar{P}$, the sum of the 12 quarterly values is approximately $11.39$:

    $$
    A \approx 0.25 \times 11.39 = 2.848
    $$

    **Step 3: Protection leg.**

    The protection leg pays $(1-R)$ at default:

    $$
    \text{Prot} = \int_0^3 \bar{P}(0, u) \cdot \mathbb{E}^{\mathbb{Q}^{S_u}}[\lambda_u] \, du
    $$

    For a rough estimate, use the approximation $\text{Prot} \approx 1 - \bar{P}(0, 3) - r \cdot A$:

    From the survival probability, the expected loss from default over 3 years is $1 - S(0,3) \approx 1 - 0.946 = 0.054$. The protection leg (discounted) is approximately:

    $$
    \text{Prot} \approx (1 - e^{-0.03 \times 3})(1) - (1 - \bar{P}(0,3) - (1 - e^{-0.03 \times 3}))
    $$

    A simpler approximation: with nearly constant intensity close to the long-run mean ($\lambda \approx 0.018$ average over 3 years for this mean-reverting CIR):

    $$
    \text{Prot} \approx \int_0^3 e^{-(r + \bar{\lambda})u} \bar{\lambda} \, du \approx \bar{\lambda} \cdot A_{\text{continuous}} \approx 0.018 \times 2.85 = 0.0513
    $$

    **Step 4: Par CDS spread.**

    $$
    s_{\text{par}} = \frac{(1-R) \times \text{Prot}}{A} = \frac{0.6 \times 0.0513}{2.848} \approx \frac{0.0308}{2.848} \approx 0.0108 = 108 \text{ bps}
    $$

    **Cross-check with the simple approximation $s \approx (1-R)\lambda^{\mathbb{Q}}$:**

    With average $\lambda^{\mathbb{Q}} \approx 1.8\%$: $s \approx 0.6 \times 0.018 = 0.0108 = 108$ bps, which is consistent.

    The survival measure simplifies the risky annuity computation because $\bar{P}(0, t_i)$ can be computed in closed form from the CIR affine formula, avoiding the need for Monte Carlo simulation of the joint $(r, \lambda)$ dynamics.

---

**Exercise 7.** Compare the $T$-forward measure and the $T$-survival measure by answering the following: (a) What numeraire defines each measure? (b) What quantity is eliminated from pricing formulas by each measure change? (c) Under what condition does the survival measure reduce to the forward measure? (d) Give an example of a derivative for which the survival measure is essential but the forward measure is insufficient.

??? success "Solution to Exercise 7"
    **(a) Numeraires:**

    - **$T$-forward measure $\mathbb{Q}^T$:** The numeraire is the default-free zero-coupon bond $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s ds} \mid \mathcal{F}_t]$.
    - **$T$-survival measure $\mathbb{Q}^S$:** The numeraire is the zero-recovery defaultable zero-coupon bond $\bar{P}(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T (r_s + \lambda_s) ds} \mid \mathcal{F}_t]$.

    **(b) What each measure eliminates:**

    - **$\mathbb{Q}^T$ eliminates:** The stochastic discount factor $e^{-\int_t^T r_s ds}$. Under $\mathbb{Q}^T$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s ds} X \mid \mathcal{F}_t\right] = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[X \mid \mathcal{F}_t]
    $$

    - **$\mathbb{Q}^S$ eliminates:** Both the stochastic discount factor and the survival probability. Under $\mathbb{Q}^S$:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} X \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}[X \mid \mathcal{F}_t]
    $$

    **(c) When the survival measure reduces to the forward measure:**

    The survival measure reduces to the forward measure when **there is no default risk**, i.e., when $\lambda_t = 0$ for all $t$. In this case:

    $$
    \bar{P}(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + 0) ds} \mid \mathcal{F}_t\right] = P(t,T)
    $$

    and the Radon--Nikodym densities coincide:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{e^{-\int_0^T r_s ds}}{\bar{P}(0,T)} = \frac{e^{-\int_0^T r_s ds}}{P(0,T)} = \frac{d\mathbb{Q}^T}{d\mathbb{Q}}
    $$

    More generally, if $\lambda_t$ is deterministic, then $S(t,T) = e^{-\int_t^T \lambda_s ds}$ is deterministic, and $\bar{P}(t,T) = P(t,T) \cdot S(t,T)$. In this case, $\mathbb{Q}^S = \mathbb{Q}^T$ on $\mathcal{F}_T$ because the deterministic survival factor cancels in the density ratio. The two measures differ only when $\lambda_t$ is stochastic.

    **(d) Example where survival measure is essential but forward measure is insufficient:**

    Consider a **credit spread option** with payoff $(\lambda_T - K)^+$ at time $T$, conditional on survival. The price is:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T (r_s + \lambda_s) ds} (\lambda_T - K)^+ \mid \mathcal{F}_t\right] = \bar{P}(t,T) \cdot \mathbb{E}^{\mathbb{Q}^S}\left[(\lambda_T - K)^+ \mid \mathcal{F}_t\right]
    $$

    Under $\mathbb{Q}^S$, we compute a standard option expectation, but the distribution of $\lambda_T$ is adjusted (e.g., lower mean for CIR intensity). The forward measure $\mathbb{Q}^T$ cannot handle this because:

    - $\mathbb{Q}^T$ only eliminates $e^{-\int r_s ds}$, leaving the survival weighting $e^{-\int \lambda_s ds}$ inside the expectation
    - The payoff $(\lambda_T - K)^+$ depends on $\lambda_T$, which is correlated with $e^{-\int \lambda_s ds}$, making the factorization impossible under $\mathbb{Q}^T$
    - Under $\mathbb{Q}^T$: $V_t = P(t,T) \cdot \mathbb{E}^{\mathbb{Q}^T}[e^{-\int_t^T \lambda_s ds}(\lambda_T - K)^+ \mid \mathcal{F}_t]$, which still has the intractable product of $e^{-\int \lambda_s ds}$ and a function of $\lambda_T$

    The survival measure resolves this by absorbing the survival weighting into the measure, yielding a clean expectation of $(\lambda_T - K)^+$ under $\mathbb{Q}^S$.
