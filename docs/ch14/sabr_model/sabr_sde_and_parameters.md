# SABR SDE and Parameters

The SABR model (Stochastic Alpha, Beta, Rho) is the industry-standard framework for modeling the implied volatility smile in interest rate and equity options markets. Introduced by Hagan, Kumar, Lesniewski, and Woodward (2002), the model couples a CEV-type forward dynamics with a lognormal stochastic volatility process, producing a parsimonious yet flexible smile parameterization. This section defines the SABR SDE system, explains the role and interpretation of each parameter, and establishes the properties that underpin all subsequent developments in this chapter.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the SABR SDE system and identify each parameter
    2. Explain the financial interpretation of $\alpha$, $\beta$, $\rho$, and $\nu$
    3. Describe how each parameter shapes the implied volatility smile
    4. Construct correlated Brownian increments via the Cholesky decomposition
    5. State the parameter constraints required for a well-defined model

---

## Motivation

Before the SABR model, practitioners faced a fundamental tension. The Black–Scholes framework assumes constant volatility, yet the market quotes different implied volatilities for different strikes --- the **volatility smile**. Local volatility models (Dupire) can match the smile at a single expiry but produce unrealistic smile dynamics: as the forward moves, the local volatility model predicts that the smile shifts in the wrong direction. Traders need a model that not only fits today's smile but also generates sensible smile dynamics when the forward rate changes. The SABR model addresses this by introducing a stochastic volatility factor with a specific parametric structure chosen to match the observed behavior of interest rate smiles.

---

## The SABR SDE System

### Forward Price Dynamics

The SABR model describes the evolution of a forward price $F_t$ (e.g., a forward swap rate or a forward LIBOR rate) under its natural pricing measure. Unlike spot price models, the forward has zero drift under the appropriate forward measure, so the dynamics are purely diffusive.

!!! info "Definition: SABR Model"
    The SABR model is defined by the SDE system:

    $$
    dF_t = \sigma_t F_t^{\beta}\,dW_t^{(1)}
    $$

    $$
    d\sigma_t = \nu \sigma_t\,dW_t^{(2)}
    $$

    $$
    d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
    $$

    with initial conditions $F_0 > 0$ and $\sigma_0 = \alpha > 0$, where:

    - $F_t$ is the forward price at time $t$
    - $\sigma_t$ is the stochastic volatility process
    - $\beta \in [0, 1]$ is the CEV exponent
    - $\nu \geq 0$ is the volatility of volatility (vol-of-vol)
    - $\rho \in (-1, 1)$ is the correlation between the forward and volatility shocks
    - $\alpha > 0$ is the initial volatility level

The forward equation has **no drift term** because $F_t$ is a martingale under the forward measure. This is a key structural feature: the absence of drift means the model automatically satisfies the martingale condition for option pricing, regardless of the parameter values.

### Volatility Dynamics

The stochastic volatility $\sigma_t$ follows a **geometric Brownian motion** (also called lognormal dynamics):

$$
\sigma_t = \alpha \exp\!\left(-\frac{\nu^2}{2}t + \nu W_t^{(2)}\right)
$$

This has several important consequences:

- $\sigma_t > 0$ for all $t \geq 0$ almost surely, so the volatility process never reaches zero or becomes negative
- The volatility has **no mean reversion**, unlike the Heston model where variance reverts to a long-run level $\theta$
- The expected value $\mathbb{E}[\sigma_t] = \alpha$ is constant, but the distribution of $\sigma_t$ broadens over time
- The variance of $\sigma_t$ grows as $\text{Var}(\sigma_t) = \alpha^2(e^{\nu^2 t} - 1)$

!!! warning "No Mean Reversion"
    The absence of mean reversion is both a strength and a limitation of the SABR model. It simplifies the mathematics and produces tractable implied volatility formulas, but it means the model is best suited for **single-expiry** smile fitting rather than joint calibration across the entire term structure. For multi-expiry consistency, practitioners either calibrate independently per expiry or use extensions with time-dependent parameters.

### Correlation Structure

The two Brownian motions $W^{(1)}$ and $W^{(2)}$ are correlated with instantaneous correlation $\rho$. To simulate the model or perform explicit calculations, we decompose them using independent Brownian motions $B^{(1)}$ and $B^{(2)}$ via the **Cholesky factorization**:

$$
W_t^{(1)} = B_t^{(1)}
$$

$$
W_t^{(2)} = \rho\,B_t^{(1)} + \sqrt{1 - \rho^2}\,B_t^{(2)}
$$

This ensures $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt$ and $d\langle B^{(1)}, B^{(2)} \rangle_t = 0$. In matrix form, the diffusion matrix is:

$$
\Sigma = \begin{pmatrix} 1 & 0 \\ \rho & \sqrt{1 - \rho^2} \end{pmatrix}
$$

so that $(W^{(1)}, W^{(2)})^{\top} = \Sigma\,(B^{(1)}, B^{(2)})^{\top}$.

---

## Parameter Interpretation

The SABR model has four parameters: $\alpha$, $\beta$, $\rho$, and $\nu$. Each controls a distinct aspect of the implied volatility smile.

### Initial Volatility (alpha)

The parameter $\alpha = \sigma_0 > 0$ sets the **overall level** of the implied volatility surface. It is the starting value of the stochastic volatility process.

- $\alpha$ primarily determines the **ATM implied volatility** level
- For a given $\beta$, the ATM implied volatility is approximately $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$
- In calibration, $\alpha$ is typically the first parameter determined (from the ATM quote)

| $\alpha$ | ATM Vol Level | Market Regime |
|-----------|---------------|---------------|
| Low | Low implied vol | Calm markets |
| Medium | Moderate implied vol | Normal conditions |
| High | High implied vol | Stressed markets |

### CEV Exponent (beta)

The parameter $\beta \in [0, 1]$ controls the **backbone** of the model --- how the ATM implied volatility changes when the forward rate moves. The term $F^{\beta}$ in the forward dynamics means that the local volatility scales as a power of the forward level.

**Special cases:**

- $\beta = 0$: **Normal SABR**. The forward dynamics become $dF_t = \sigma_t\,dW_t^{(1)}$, an arithmetic Brownian motion. The forward can go negative. Best suited for interest rate markets where negative rates are possible.
- $\beta = 1$: **Lognormal SABR**. The forward dynamics become $dF_t = \sigma_t F_t\,dW_t^{(1)}$, a geometric Brownian motion with stochastic volatility. The forward is strictly positive. The local volatility is proportional to $F$, so returns have constant percentage volatility.
- $\beta = 0.5$: **CIR-type backbone**. The local volatility scales as $\sqrt{F}$, and the forward obeys square-root dynamics. A common choice for interest rate models.

The backbone relationship can be expressed as:

$$
\sigma_{\text{ATM}} \approx \frac{\alpha}{F^{1-\beta}}
$$

When $\beta < 1$, a decrease in $F$ causes an increase in ATM implied volatility (and vice versa), producing a **negative backbone effect** that contributes to the observed skew even before accounting for correlation. When $\beta = 1$, the ATM implied volatility is independent of $F$.

!!! tip "Choosing Beta in Practice"
    In interest rate markets, $\beta$ is typically **fixed by convention** rather than calibrated:

    - $\beta = 0$: Common in EUR and JPY swaption markets (accommodates negative rates)
    - $\beta = 0.5$: A traditional choice that balances normal and lognormal behavior
    - $\beta = 1$: Sometimes used for equity or FX options

    Fixing $\beta$ avoids degeneracy between $\alpha$ and $\beta$ in calibration (they are not jointly well identified from smile data alone).

### Correlation (rho)

The parameter $\rho \in (-1, 1)$ controls the **skew** of the implied volatility smile --- the asymmetry between low-strike and high-strike implied volatilities.

When $\rho < 0$ (the typical case for equities and rates), a downward shock to the forward is correlated with an upward shock to volatility. This means:

- When $F$ decreases, $\sigma$ tends to increase, making OTM puts more expensive
- When $F$ increases, $\sigma$ tends to decrease, making OTM calls cheaper
- The result is a **negatively skewed** implied volatility smile

The first-order effect of $\rho$ on the ATM skew is:

$$
\frac{\partial \sigma_{\text{impl}}}{\partial K}\bigg|_{K=F} \propto \rho\,\nu
$$

| $\rho$ | Smile Shape | Typical Market |
|--------|-------------|----------------|
| $\rho < 0$ | Negative skew (downside vol higher) | Equities, rates |
| $\rho = 0$ | Symmetric smile | Rare in practice |
| $\rho > 0$ | Positive skew (upside vol higher) | Some commodities |

### Vol-of-Vol (nu)

The parameter $\nu \geq 0$ controls the **curvature** (convexity) of the implied volatility smile --- how much the wings are lifted relative to the ATM level.

- $\nu = 0$ reduces the SABR model to a deterministic CEV model (no stochastic volatility)
- Larger $\nu$ produces more pronounced smile curvature in both wings
- $\nu$ affects the **kurtosis** of the forward distribution: higher $\nu$ means heavier tails

The second-order effect of $\nu$ on smile curvature is:

$$
\frac{\partial^2 \sigma_{\text{impl}}}{\partial K^2}\bigg|_{K=F} \propto \nu^2
$$

!!! example "Parameter Effects on the Smile"
    Consider a 1-year ATM forward at $F = 0.03$ (3% swap rate) with $\beta = 0.5$:

    - **Base case:** $\alpha = 0.03$, $\rho = -0.3$, $\nu = 0.4$ produces a moderately skewed smile with mild curvature
    - **Increase** $\alpha$ **to 0.05:** the entire smile shifts upward (higher ATM level)
    - **Decrease** $\rho$ **to** $-0.6$: the smile tilts further, with OTM puts becoming more expensive relative to OTM calls
    - **Increase** $\nu$ **to 0.8:** both wings lift, creating a more pronounced "smile" shape
    - **Change** $\beta$ **from 0.5 to 0:** the backbone flattens, and the model can accommodate negative forwards

---

## Parameter Summary Table

| Parameter | Symbol | Domain | Primary Effect | Calibration Role |
|-----------|--------|--------|----------------|------------------|
| Initial vol | $\alpha$ | $(0, \infty)$ | ATM volatility level | Determined from ATM quote |
| CEV exponent | $\beta$ | $[0, 1]$ | Backbone (vol vs. forward) | Fixed by convention |
| Correlation | $\rho$ | $(-1, 1)$ | Smile skew | Fitted to OTM skew |
| Vol-of-vol | $\nu$ | $[0, \infty)$ | Smile curvature | Fitted to OTM wings |

---

## Properties of the SABR Process

### Martingale Property

Since $F_t$ has no drift, it is a local martingale under the forward measure. For $\beta \in (0, 1]$, the process is a true martingale provided the initial conditions are well-behaved. For $\beta < 1$, the forward can reach zero, and whether $F_t$ remains a true martingale depends on the boundary condition imposed at $F = 0$. With an absorbing boundary at zero, the expected value $\mathbb{E}[F_T]$ may be strictly less than $F_0$, a phenomenon called **probability mass leakage** that has important implications for arbitrage-free pricing (discussed in the section on arbitrage-free SABR).

### Scaling Behavior

The SABR model exhibits a useful scaling property. If $(F_t, \sigma_t)$ is a solution with parameters $(\alpha, \beta, \rho, \nu)$ and initial forward $F_0$, then for any $\lambda > 0$:

$$
(\lambda F_t, \lambda^{1-\beta}\sigma_t) \text{ is a solution with initial forward } \lambda F_0 \text{ and initial vol } \lambda^{1-\beta}\alpha
$$

This scaling property implies that the implied volatility smile, when expressed in terms of log-moneyness $\ln(K/F)$, is invariant under rescaling of the forward level (for fixed $\beta$).

### Moment Explosion

Because the volatility follows geometric Brownian motion, the moments of $\sigma_t$ grow exponentially:

$$
\mathbb{E}[\sigma_t^n] = \alpha^n \exp\!\left(\frac{n(n-1)}{2}\nu^2 t\right)
$$

For large $n$ or large $t$, this growth can cause the moments of $F_T$ to explode. Specifically, the $n$-th moment $\mathbb{E}[F_T^n]$ may be infinite for sufficiently large $n$, depending on $\beta$, $\nu$, and $T$. This moment explosion does not affect option pricing directly (option payoffs have at most linear growth), but it does impact Monte Carlo simulation convergence and certain exotic pricing applications.

---

## Comparison with Other Stochastic Volatility Models

The SABR model differs from other stochastic volatility models in several important respects.

| Feature | SABR | Heston | Hull–White SV |
|---------|------|--------|---------------|
| Forward dynamics | CEV ($F^{\beta}$) | GBM ($S$) | GBM ($S$) |
| Vol dynamics | Lognormal ($\sigma$) | CIR ($V$) | Lognormal ($\sigma$) |
| Mean reversion | No | Yes ($\kappa$) | Optional |
| Closed-form IV | Yes (Hagan approx.) | No (CF via Fourier) | No |
| Primary use | Per-expiry smile | Full surface | Full surface |
| Handles negative $F$ | Yes (if $\beta = 0$) | No | No |
| # Free parameters | 3 ($\alpha, \rho, \nu$; $\beta$ fixed) | 5 ($\kappa, \theta, \xi, \rho, V_0$) | 4+ |

The key advantage of SABR is its **closed-form implied volatility approximation** (the Hagan formula), which allows traders to quickly convert between SABR parameters and implied volatilities. This makes the model especially popular in interest rate markets, where thousands of swaption prices must be interpolated and risk-managed in real time.

---

## Summary

The SABR model is defined by a driftless CEV forward process coupled with a lognormal stochastic volatility. Its four parameters --- $\alpha$ (ATM level), $\beta$ (backbone), $\rho$ (skew), and $\nu$ (curvature) --- each control a distinct feature of the implied volatility smile. The absence of mean reversion makes the model best suited for per-expiry calibration, while the CEV exponent $\beta$ provides flexibility to handle different asset classes including negative interest rates (when $\beta = 0$). The correlation structure is implemented via Cholesky decomposition of the driving Brownian motions. These dynamics form the foundation for the Hagan implied volatility approximation, boundary analysis, and calibration methods developed in the subsequent sections.

---

## Further Reading

- Hagan, P., Kumar, D., Lesniewski, A., & Woodward, D. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Rebonato, R., McKay, K., & White, R. (2009). *The SABR/LIBOR Market Model*. Wiley.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley, Chapter 7.

---

## Exercises

**Exercise 1.** Write down the SABR SDE system for the special case $\beta = 0$ (normal SABR). Show that the forward $F_t$ can become negative. Compute the expected value $\mathbb{E}[F_T]$ and explain why it equals $F_0$ (the martingale property).

??? success "Solution to Exercise 1"
    For $\beta = 0$, the SABR SDE system becomes:

    $$
    dF_t = \sigma_t\,dW_t^{(1)}
    $$

    $$
    d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
    $$

    $$
    d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt
    $$

    The forward follows arithmetic Brownian motion with stochastic volatility. Since the diffusion coefficient $\sigma_t$ does not depend on $F_t$, there is no mechanism preventing $F_t$ from becoming negative. Specifically, conditional on the volatility path, $F_T - F_0 = \int_0^T \sigma_s\,dW_s^{(1)}$ is a Gaussian random variable (a stochastic integral of a predictable process against Brownian motion), which takes negative values with positive probability whenever $\int_0^T \sigma_s^2\,ds > 0$.

    For the expected value, since $F_t$ has **no drift**, $F_t$ is a local martingale. The stochastic integral $\int_0^t \sigma_s\,dW_s^{(1)}$ has zero expectation (it is a true martingale for integrable $\sigma$), so:

    $$
    \mathbb{E}[F_T] = F_0 + \mathbb{E}\!\left[\int_0^T \sigma_s\,dW_s^{(1)}\right] = F_0 + 0 = F_0
    $$

    This is the martingale property: the expected forward at any future time equals the current forward. It holds because the forward measure eliminates drift from the forward dynamics, and the stochastic integral has zero expectation.

---

**Exercise 2.** Using the Cholesky decomposition $W_t^{(2)} = \rho\,B_t^{(1)} + \sqrt{1-\rho^2}\,B_t^{(2)}$, verify that $\text{Var}[W_t^{(2)}] = t$ and $\text{Cov}[W_t^{(1)}, W_t^{(2)}] = \rho t$. For $\rho = -0.65$, compute the fraction of the volatility shock $dW^{(2)}$ that is correlated with the forward shock $dW^{(1)}$ versus the orthogonal component.

??? success "Solution to Exercise 2"
    Using $W_t^{(2)} = \rho\,B_t^{(1)} + \sqrt{1-\rho^2}\,B_t^{(2)}$ where $B^{(1)}$ and $B^{(2)}$ are independent standard Brownian motions:

    **Variance of $W_t^{(2)}$:**

    $$
    \text{Var}[W_t^{(2)}] = \text{Var}[\rho\,B_t^{(1)} + \sqrt{1-\rho^2}\,B_t^{(2)}]
    $$

    $$
    = \rho^2\,\text{Var}[B_t^{(1)}] + (1-\rho^2)\,\text{Var}[B_t^{(2)}] + 2\rho\sqrt{1-\rho^2}\,\text{Cov}[B_t^{(1)}, B_t^{(2)}]
    $$

    Since $B^{(1)}$ and $B^{(2)}$ are independent, the covariance term vanishes, and $\text{Var}[B_t^{(i)}] = t$, giving:

    $$
    \text{Var}[W_t^{(2)}] = \rho^2 t + (1-\rho^2)t = t
    $$

    **Covariance of $W_t^{(1)}$ and $W_t^{(2)}$:**

    $$
    \text{Cov}[W_t^{(1)}, W_t^{(2)}] = \text{Cov}[B_t^{(1)}, \rho\,B_t^{(1)} + \sqrt{1-\rho^2}\,B_t^{(2)}]
    $$

    $$
    = \rho\,\text{Var}[B_t^{(1)}] + \sqrt{1-\rho^2}\,\text{Cov}[B_t^{(1)}, B_t^{(2)}] = \rho\,t
    $$

    For $\rho = -0.65$, the volatility shock decomposes as:

    $$
    dW^{(2)} = -0.65\,dB^{(1)} + \sqrt{1 - 0.4225}\,dB^{(2)} = -0.65\,dB^{(1)} + 0.7599\,dB^{(2)}
    $$

    The fraction correlated with $dW^{(1)} = dB^{(1)}$ is $|\rho| = 0.65$, or 65% of the volatility shock variance comes from the same source as the forward shock. The orthogonal component has coefficient $\sqrt{1 - \rho^2} = 0.7599$, contributing $1 - \rho^2 = 57.75\%$ of the variance. In other words, 42.25% of the variance of $dW^{(2)}$ is explained by $dW^{(1)}$, and the remaining 57.75% is independent.

---

**Exercise 3.** The volatility process $\sigma_t = \alpha\exp(-\nu^2 t/2 + \nu W_t^{(2)})$ is a geometric Brownian motion. For $\alpha = 0.03$, $\nu = 0.5$, compute the expected value, variance, and 95th percentile of $\sigma_T$ at $T = 1$ and $T = 5$. Explain why the absence of mean reversion makes the SABR model less suitable for multi-expiry calibration.

??? success "Solution to Exercise 3"
    The volatility $\sigma_t = \alpha\exp(-\nu^2 t/2 + \nu W_t^{(2)})$ is lognormally distributed since $-\nu^2 t/2 + \nu W_t^{(2)} \sim \mathcal{N}(-\nu^2 t/2, \nu^2 t)$.

    With $\alpha = 0.03$ and $\nu = 0.5$:

    **Expected value** (independent of $t$):

    $$
    \mathbb{E}[\sigma_t] = \alpha\,\exp\!\left(-\frac{\nu^2 t}{2} + \frac{\nu^2 t}{2}\right) = \alpha = 0.03
    $$

    **Variance:**

    $$
    \text{Var}(\sigma_t) = \alpha^2(e^{\nu^2 t} - 1)
    $$

    At $T = 1$: $\text{Var}(\sigma_1) = (0.03)^2(e^{0.25} - 1) = 9 \times 10^{-4} \times 0.2840 = 2.556 \times 10^{-4}$, so $\text{Std}(\sigma_1) = 0.01599$.

    At $T = 5$: $\text{Var}(\sigma_5) = (0.03)^2(e^{1.25} - 1) = 9 \times 10^{-4} \times 2.4903 = 2.241 \times 10^{-3}$, so $\text{Std}(\sigma_5) = 0.04734$.

    **95th percentile:** Since $\ln(\sigma_t/\alpha) \sim \mathcal{N}(-\nu^2 t/2, \nu^2 t)$, the 95th percentile is:

    $$
    \sigma_t^{95\%} = \alpha\exp(-\nu^2 t/2 + 1.645\nu\sqrt{t})
    $$

    At $T = 1$: $\sigma_1^{95\%} = 0.03\exp(-0.125 + 1.645 \times 0.5) = 0.03\exp(0.6975) = 0.03 \times 2.009 = 0.06026$.

    At $T = 5$: $\sigma_5^{95\%} = 0.03\exp(-0.625 + 1.645 \times 1.118) = 0.03\exp(1.214) = 0.03 \times 3.367 = 0.1010$.

    The 95th percentile at $T = 5$ is more than triple the initial value, illustrating how the lognormal volatility distribution spreads dramatically over time. Without mean reversion, the distribution becomes extremely diffuse at long horizons, meaning SABR parameters calibrated at one expiry will not produce realistic volatility distributions at much longer expiries. This is why per-expiry calibration is necessary and multi-expiry consistency is poor.

---

**Exercise 4.** The backbone relationship is $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$. For $\alpha = 0.04$ and $F = 3\%$, compute $\sigma_{\text{ATM}}$ for $\beta = 0, 0.5, 1.0$. If the forward drops from 3% to 2%, recompute $\sigma_{\text{ATM}}$ for each $\beta$. Which value of $\beta$ produces the largest change in ATM vol for a given forward move?

??? success "Solution to Exercise 4"
    Using $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$ with $\alpha = 0.04$:

    **At $F = 3\% = 0.03$:**

    - $\beta = 0$: $\sigma_{\text{ATM}} = 0.04 / 0.03^1 = 1.333$ (133.3%)
    - $\beta = 0.5$: $\sigma_{\text{ATM}} = 0.04 / 0.03^{0.5} = 0.04 / 0.1732 = 0.2309$ (23.09%)
    - $\beta = 1.0$: $\sigma_{\text{ATM}} = 0.04 / 0.03^{0} = 0.04$ (4.0%)

    **At $F = 2\% = 0.02$:**

    - $\beta = 0$: $\sigma_{\text{ATM}} = 0.04 / 0.02 = 2.000$ (200.0%), change = +66.7%
    - $\beta = 0.5$: $\sigma_{\text{ATM}} = 0.04 / 0.02^{0.5} = 0.04 / 0.1414 = 0.2828$ (28.28%), change = +5.19%
    - $\beta = 1.0$: $\sigma_{\text{ATM}} = 0.04$ (4.0%), change = 0%

    **$\beta = 0$ produces the largest change** in ATM vol for a given forward move. The backbone slope is $-(1-\beta)\alpha / F^{2-\beta}$, which is steepest when $\beta = 0$: the Black implied volatility scales as $1/F$, so any decrease in $F$ causes a dramatic increase in implied volatility. For $\beta = 1$, the backbone is flat and ATM vol does not change at all with the forward. This is why $\beta = 0$ is used for negative-rate environments: it produces the strongest negative correlation between rates and Black vol, which matches market observations.

---

**Exercise 5.** Explain the moment explosion property: $\mathbb{E}[\sigma_t^n] = \alpha^n\exp(n(n-1)\nu^2 t/2)$. For $\alpha = 0.03$, $\nu = 0.5$, compute $\mathbb{E}[\sigma_1^2]$ and $\mathbb{E}[\sigma_1^4]$. At what maturity $T^*$ does the fourth moment exceed $10^6 \cdot \alpha^4$? What are the implications for Monte Carlo simulation convergence?

??? success "Solution to Exercise 5"
    The moment formula is:

    $$
    \mathbb{E}[\sigma_t^n] = \alpha^n \exp\!\left(\frac{n(n-1)}{2}\nu^2 t\right)
    $$

    This follows because $\sigma_t = \alpha\exp(-\nu^2 t/2 + \nu W_t)$ and $\sigma_t^n = \alpha^n \exp(-n\nu^2 t/2 + n\nu W_t)$. Taking the expectation and using $\mathbb{E}[\exp(\theta W_t)] = \exp(\theta^2 t/2)$:

    $$
    \mathbb{E}[\sigma_t^n] = \alpha^n \exp\!\left(-\frac{n\nu^2 t}{2} + \frac{n^2\nu^2 t}{2}\right) = \alpha^n \exp\!\left(\frac{n(n-1)}{2}\nu^2 t\right)
    $$

    With $\alpha = 0.03$, $\nu = 0.5$:

    $$
    \mathbb{E}[\sigma_1^2] = (0.03)^2 \exp\!\left(\frac{2 \times 1}{2} \times 0.25 \times 1\right) = 9 \times 10^{-4} \times e^{0.25} = 9 \times 10^{-4} \times 1.284 = 1.156 \times 10^{-3}
    $$

    $$
    \mathbb{E}[\sigma_1^4] = (0.03)^4 \exp\!\left(\frac{4 \times 3}{2} \times 0.25 \times 1\right) = 8.1 \times 10^{-7} \times e^{1.5} = 8.1 \times 10^{-7} \times 4.482 = 3.630 \times 10^{-6}
    $$

    For the fourth moment to exceed $10^6 \cdot \alpha^4 = 10^6 \times 8.1 \times 10^{-7} = 0.81$:

    $$
    \alpha^4 \exp(6 \times 0.25 \times T^*) = 0.81
    $$

    $$
    8.1 \times 10^{-7} \exp(1.5\,T^*) = 0.81
    $$

    $$
    \exp(1.5\,T^*) = 10^6
    $$

    $$
    T^* = \frac{6\ln 10}{1.5} = \frac{13.816}{1.5} = 9.21 \text{ years}
    $$

    For Monte Carlo simulation, moment explosion means that a small number of paths with very high volatility realizations dominate the sample average, causing extremely high variance in estimators and slow convergence. Variance reduction techniques (such as control variates) are essential for long-dated simulations.

---

**Exercise 6.** The SABR model has four parameters but only three are typically calibrated ($\alpha, \rho, \nu$) while $\beta$ is fixed. Explain the identifiability issue: why can't $\beta$ and $\alpha$ be simultaneously determined from smile data alone? (Hint: consider how $\alpha$ and $\beta$ jointly affect the ATM implied volatility through $\sigma_{\text{ATM}} \approx \alpha/F^{1-\beta}$.)

??? success "Solution to Exercise 6"
    The ATM implied volatility is approximately $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$. If we change $\beta$ while simultaneously adjusting $\alpha$ to keep $\alpha / F^{1-\beta}$ fixed, the ATM implied volatility remains unchanged. Concretely, two parameter pairs $(\alpha_1, \beta_1)$ and $(\alpha_2, \beta_2)$ produce the same ATM vol whenever:

    $$
    \frac{\alpha_1}{F^{1-\beta_1}} = \frac{\alpha_2}{F^{1-\beta_2}} \quad \Longleftrightarrow \quad \alpha_2 = \alpha_1 \cdot F^{\beta_2 - \beta_1}
    $$

    The smile data alone (especially near ATM) cannot distinguish between these parameter combinations because they produce nearly identical implied volatilities near the money. The off-the-money behavior differs slightly through the correction terms in the Hagan formula, but these differences are typically within bid-ask spreads for reasonable ranges of $\beta$.

    This is a classic **identifiability problem**: the likelihood surface in the $(\alpha, \beta)$ plane has a ridge along the curve $\alpha \propto F^{1-\beta}$, making the joint determination of $\alpha$ and $\beta$ ill-conditioned. The standard solution is to **fix $\beta$ by convention** (e.g., $\beta = 0.5$ for USD swaptions), which collapses the ridge to a single point and allows $\alpha$ to be uniquely determined from the ATM quote.

---

**Exercise 7.** Compare the SABR and Heston models by identifying which feature of the implied volatility surface each model is better equipped to capture. Specifically, for each of the following, state which model performs better and why: (a) single-expiry smile fitting; (b) term structure of ATM volatility; (c) calibration speed; (d) handling negative rates; (e) consistency across expiries.

??? success "Solution to Exercise 7"
    **(a) Single-expiry smile fitting:** **SABR performs better.** The Hagan closed-form formula allows instant evaluation, and 3 free parameters ($\alpha, \rho, \nu$) provide sufficient flexibility to fit the smile at a single expiry. Heston requires numerical Fourier inversion (slower) and has 5 parameters that are harder to calibrate to a single expiry without overfitting or instability.

    **(b) Term structure of ATM volatility:** **Heston performs better.** The mean-reversion parameter $\kappa$ in Heston drives the ATM vol toward the long-run level $\theta$, naturally producing a term structure. SABR has no mean reversion, so the ATM vol is approximately $\alpha / F^{1-\beta}$ at all maturities, requiring independent calibration per expiry.

    **(c) Calibration speed:** **SABR performs better.** The Hagan formula is algebraic (microseconds per evaluation), while Heston requires numerical integration of the characteristic function (milliseconds per evaluation). For a swaption cube with thousands of smiles, SABR calibration is orders of magnitude faster.

    **(d) Handling negative rates:** **SABR performs better.** With $\beta = 0$ (normal SABR), the forward follows arithmetic Brownian motion and can go negative naturally. Heston is formulated for positive asset prices (geometric Brownian motion with CIR variance) and cannot handle negative forwards without modification.

    **(e) Consistency across expiries:** **Heston performs better.** Heston is a global model with a single set of parameters that applies across all expiries simultaneously. The mean reversion, long-run variance, and vol-of-vol jointly determine the smile at every maturity. SABR requires independent calibration at each expiry, creating dynamic inconsistency between expiries.
