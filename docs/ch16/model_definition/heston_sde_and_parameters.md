# Heston SDE and Parameters

The Black-Scholes model assumes that the volatility of an asset is constant over time, yet empirical data overwhelmingly reject this assumption: implied volatility surfaces exhibit skew and term structure that a single constant cannot reproduce. The Heston (1993) model addresses this by making volatility itself a random process, driven by its own source of noise that is correlated with the asset price. This section defines the Heston stochastic differential equation system, introduces its five parameters, explains their financial interpretation, and derives the log-price dynamics via Ito's lemma.

Building on the general stochastic volatility framework, the Heston model is distinguished by its square-root variance diffusion (a CIR process) and the resulting **affine structure**, which we develop in the [next section](affine_structure_and_riccati.md). The [connection to the general SV framework](connection_to_sv_framework.md) clarifies how the Heston model specializes a broader class of models.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Write the Heston bivariate SDE system under the risk-neutral measure
    - Identify and interpret each of the five model parameters
    - State the parameter domain constraints and explain why each is required
    - Derive the log-price SDE from the asset price SDE using Ito's lemma
    - Decompose correlated Brownian motions via the Cholesky factorization

---

## Motivation: Why Stochastic Volatility

Practitioners observe that the implied volatility of an option depends on both strike and maturity. Short-dated out-of-the-money puts on equity indices trade at significantly higher implied volatilities than at-the-money options -- the well-known **volatility skew**. This pattern is incompatible with constant volatility: if $\sigma$ were fixed, the Black-Scholes formula would produce a flat implied volatility surface.

A natural remedy is to let the instantaneous variance $v_t$ evolve stochastically. If large drops in the asset price tend to coincide with increases in variance (negative correlation), the model generates heavier left tails in the return distribution, which the Black-Scholes formula interprets as higher implied volatility for low-strike puts. The Heston model accomplishes this with a parsimonious five-parameter specification that retains analytical tractability.

---

## The Heston SDE System

### Definition

!!! info "Definition: Heston Model"
    Under the risk-neutral measure $\mathbb{Q}$, the Heston model specifies the joint dynamics of the asset price $S_t$ and instantaneous variance $v_t$ as:

    $$
    dS_t = (r - q)\,S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}
    $$

    $$
    dv_t = \kappa\,(\theta - v_t)\,dt + \sigma_v\,\sqrt{v_t}\,dW_t^{(2)}
    $$

    where $W_t^{(1)}$ and $W_t^{(2)}$ are standard Brownian motions under $\mathbb{Q}$ with instantaneous correlation:

    $$
    d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
    $$

    The constants $r \geq 0$ and $q \geq 0$ denote the risk-free interest rate and continuous dividend yield, respectively.

The first equation is a geometric Brownian motion with a stochastic volatility coefficient $\sqrt{v_t}$. The second equation is a **Cox-Ingersoll-Ross (CIR) process** for the variance, featuring mean reversion toward a long-run level $\theta$ at speed $\kappa$, with its own diffusion coefficient proportional to $\sqrt{v_t}$.

### The Five Parameters

The Heston model is governed by five parameters, each with a distinct financial interpretation.

| Parameter | Symbol | Domain | Interpretation |
|:---|:---:|:---:|:---|
| Initial variance | $v_0$ | $v_0 > 0$ | Current level of instantaneous variance |
| Mean-reversion speed | $\kappa$ | $\kappa > 0$ | Rate at which variance reverts to its long-run mean |
| Long-run variance | $\theta$ | $\theta > 0$ | Stationary (long-run average) level of variance |
| Vol-of-vol | $\sigma_v$ | $\sigma_v > 0$ | Volatility of the variance process itself |
| Correlation | $\rho$ | $\rho \in [-1, 1]$ | Instantaneous correlation between asset returns and variance changes |

!!! tip "Parameter Interpretation at a Glance"
    - **$\kappa$ and $\theta$ together** control the term structure of variance. Large $\kappa$ means variance quickly returns to $\theta$; small $\kappa$ means persistent deviations.
    - **$\sigma_v$** determines the curvature (convexity) of the implied volatility smile. Higher $\sigma_v$ produces fatter tails and more pronounced smiles.
    - **$\rho$** determines the skew of the implied volatility surface. Negative $\rho$ (typical for equities, with $\rho \approx -0.7$) generates negative skew. Positive $\rho$ (sometimes seen in FX or commodities) generates positive skew.
    - **$v_0$** sets the current at-the-money volatility level. In calibration, $v_0$ is often close to the squared ATM implied volatility.

---

## Parameter Domain Constraints

Each parameter constraint has a mathematical or financial reason.

!!! info "Definition: Parameter Domain"
    The Heston parameter space is:

    $$
    \Theta = \{(v_0, \kappa, \theta, \sigma_v, \rho) : v_0 > 0,\; \kappa > 0,\; \theta > 0,\; \sigma_v > 0,\; \rho \in [-1, 1]\}
    $$

**Why $\kappa > 0$**: If $\kappa \leq 0$, the variance process has no mean reversion (or is explosive), and $v_t \to \infty$ almost surely. Positive $\kappa$ ensures the variance is pulled back toward $\theta$.

**Why $\theta > 0$**: The long-run target must be positive because variance is non-negative by definition. If $\theta = 0$, the variance process would be absorbed at zero.

**Why $\sigma_v > 0$**: If $\sigma_v = 0$, the variance becomes deterministic and the model collapses to a time-varying (but non-stochastic) volatility model. The entire point of the Heston framework is that $v_t$ is random.

**Why $|\rho| \leq 1$**: The correlation coefficient between two Brownian motions must lie in $[-1, 1]$ for the covariance matrix to be positive semi-definite.

**Why $v_0 > 0$**: The initial condition must be strictly positive. If $v_0 = 0$ and the Feller condition holds, the CIR process immediately becomes positive. If $v_0 = 0$ and the Feller condition fails, the process may remain at zero.

!!! warning "The Feller Condition"
    An additional constraint $2\kappa\theta \geq \sigma_v^2$ (the **Feller condition**) ensures that the variance process $v_t$ remains strictly positive for all $t > 0$. When this condition is violated, $v_t$ can touch zero. This is analyzed in detail in the [Feller Condition and Boundary Behavior](feller_condition_and_boundary.md) section. In practice, many calibrated Heston parameters violate the Feller condition, which has implications for simulation and pricing.

---

## Correlated Brownian Motions and Cholesky Decomposition

The correlation $\rho$ between $W_t^{(1)}$ and $W_t^{(2)}$ can be made explicit through a Cholesky decomposition. This is essential for simulation and for understanding the joint dynamics.

!!! success "Proposition: Cholesky Decomposition"
    Let $Z_t^{(1)}$ and $Z_t^{(2)}$ be two independent standard Brownian motions under $\mathbb{Q}$. Then the correlated pair $(W_t^{(1)}, W_t^{(2)})$ can be constructed as:

    $$
    W_t^{(1)} = Z_t^{(1)}
    $$

    $$
    W_t^{(2)} = \rho\,Z_t^{(1)} + \sqrt{1 - \rho^2}\,Z_t^{(2)}
    $$

**Proof.** We verify the three required properties. First, $W_t^{(1)} = Z_t^{(1)}$ is a standard Brownian motion by assumption. Second, $W_t^{(2)}$ is a linear combination of independent Brownian motions with coefficients $\rho$ and $\sqrt{1 - \rho^2}$. Since $\rho^2 + (1 - \rho^2) = 1$, the resulting process is again a standard Brownian motion (unit variance per unit time). Third, the instantaneous covariance is:

$$
d\langle W^{(1)}, W^{(2)} \rangle_t = d\langle Z^{(1)}, \rho\,Z^{(1)} + \sqrt{1 - \rho^2}\,Z^{(2)} \rangle_t = \rho\,d\langle Z^{(1)}, Z^{(1)} \rangle_t + \sqrt{1 - \rho^2}\,d\langle Z^{(1)}, Z^{(2)} \rangle_t = \rho\,dt
$$

where the last step uses $d\langle Z^{(1)}, Z^{(1)} \rangle_t = dt$ and $d\langle Z^{(1)}, Z^{(2)} \rangle_t = 0$ (independence). $\square$

Substituting the Cholesky decomposition into the Heston SDE gives an equivalent representation in terms of independent Brownian motions:

$$
dS_t = (r - q)\,S_t\,dt + \sqrt{v_t}\,S_t\,dZ_t^{(1)}
$$

$$
dv_t = \kappa\,(\theta - v_t)\,dt + \sigma_v\,\sqrt{v_t}\left(\rho\,dZ_t^{(1)} + \sqrt{1 - \rho^2}\,dZ_t^{(2)}\right)
$$

This form is the starting point for Monte Carlo simulation of the Heston model.

---

## Log-Price Dynamics

For pricing and characteristic function derivations, it is more convenient to work with the log-price $x_t = \ln S_t$ rather than $S_t$ itself. Ito's lemma provides the transformation.

!!! success "Proposition: Log-Price SDE"
    Define $x_t = \ln S_t$. Under the Heston model, the log-price satisfies:

    $$
    dx_t = \left(r - q - \tfrac{1}{2}\,v_t\right)dt + \sqrt{v_t}\,dW_t^{(1)}
    $$

**Proof.** Apply Ito's lemma to $f(S) = \ln S$ with the Heston price dynamics $dS_t = (r - q)\,S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}$. We have $f'(S) = 1/S$ and $f''(S) = -1/S^2$, so:

$$
dx_t = f'(S_t)\,dS_t + \tfrac{1}{2}\,f''(S_t)\,(dS_t)^2
$$

$$
= \frac{1}{S_t}\left[(r - q)\,S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}\right] + \tfrac{1}{2}\left(-\frac{1}{S_t^2}\right)v_t\,S_t^2\,dt
$$

$$
= (r - q)\,dt + \sqrt{v_t}\,dW_t^{(1)} - \tfrac{1}{2}\,v_t\,dt = \left(r - q - \tfrac{1}{2}\,v_t\right)dt + \sqrt{v_t}\,dW_t^{(1)}
$$

$\square$

The log-price drift $r - q - \frac{1}{2}v_t$ contains the familiar convexity correction $-\frac{1}{2}v_t$ that also appears in the Black-Scholes model. The key difference is that here this correction is stochastic (it depends on the random variance $v_t$), leading to a random drift.

!!! note "The Bivariate State Vector"
    The pair $(x_t, v_t)$ forms a Markov process: its future evolution depends only on the current values of the log-price and variance. The joint system is:

    $$
    dx_t = \left(r - q - \tfrac{1}{2}\,v_t\right)dt + \sqrt{v_t}\,dW_t^{(1)}
    $$

    $$
    dv_t = \kappa\,(\theta - v_t)\,dt + \sigma_v\,\sqrt{v_t}\,dW_t^{(2)}
    $$

    This bivariate system is the starting point for the characteristic function derivation and for the PDE approach to option pricing under the Heston model.

---

## Worked Example: Typical Equity Parameters

Consider a typical set of Heston parameters calibrated to S&P 500 index options:

| Parameter | Value | Interpretation |
|:---|:---:|:---|
| $v_0$ | $0.04$ | Current implied volatility $\approx 20\%$ ($\sqrt{0.04} = 0.20$) |
| $\kappa$ | $2.0$ | Half-life of variance shocks: $\ln 2 / \kappa \approx 0.35$ years |
| $\theta$ | $0.04$ | Long-run volatility $\approx 20\%$ |
| $\sigma_v$ | $0.5$ | Moderate vol-of-vol |
| $\rho$ | $-0.7$ | Strong negative correlation (leverage effect) |

With these parameters:

- **Feller ratio**: $2\kappa\theta / \sigma_v^2 = 2(2)(0.04) / 0.25 = 0.64 < 1$, so the Feller condition is **violated**. The variance can touch zero.
- **Long-run volatility**: $\sqrt{\theta} = 20\%$.
- **Half-life of variance shocks**: $\ln 2 / \kappa \approx 0.35$ years $\approx 4.2$ months. If variance jumps to $0.09$ (30\% vol), the expected time for it to return halfway to $\theta = 0.04$ is about 4 months.

??? example "Instantaneous Variance of the Log-Return"
    Over a small time interval $\Delta t$, the log-return $\Delta x \approx (r - q - \frac{1}{2}v_t)\Delta t + \sqrt{v_t}\sqrt{\Delta t}\,\epsilon$ has conditional variance approximately $v_t \Delta t$. With $v_0 = 0.04$ and $\Delta t = 1/252$ (one trading day):

    $$
    \text{Std}(\Delta x) \approx \sqrt{v_0 \cdot \Delta t} = \sqrt{0.04 / 252} \approx 1.26\%
    $$

    This is the daily standard deviation of the log-return, consistent with the annualized volatility of $\sqrt{0.04} = 20\%$ via the $\sqrt{252}$ scaling.

---

## Notation Conventions

Throughout this chapter, we adopt the following notation for the Heston model:

| Symbol | Meaning |
|:---|:---|
| $S_t$ | Asset price at time $t$ |
| $v_t$ | Instantaneous variance at time $t$ |
| $x_t = \ln S_t$ | Log-price |
| $r$ | Risk-free interest rate |
| $q$ | Continuous dividend yield |
| $\kappa$ | Mean-reversion speed of variance |
| $\theta$ | Long-run (stationary) variance level |
| $\sigma_v$ (or $\xi$) | Vol-of-vol (volatility of variance) |
| $\rho$ | Correlation between price and variance Brownian motions |
| $\tau = T - t$ | Time to maturity |
| $W_t^{(1)}, W_t^{(2)}$ | Correlated Brownian motions under $\mathbb{Q}$ |
| $Z_t^{(1)}, Z_t^{(2)}$ | Independent Brownian motions under $\mathbb{Q}$ |

!!! note "Vol-of-Vol Notation"
    Different sources use different symbols for the vol-of-vol parameter: $\sigma_v$, $\xi$, $\gamma$, or $\eta$. In this chapter we primarily use $\sigma_v$, but the chapter overview and some subsequent sections use $\xi$. Both refer to the same parameter.

---

## Summary

The Heston model is a bivariate SDE system in which the asset price follows a geometric Brownian motion with stochastic variance, and the variance follows a CIR process. The five parameters -- $v_0$, $\kappa$, $\theta$, $\sigma_v$, $\rho$ -- control the initial volatility level, the speed and target of mean reversion, the randomness of variance, and the correlation between asset returns and variance changes, respectively. The Cholesky decomposition expresses the correlated Brownian motions in terms of independent ones, and Ito's lemma provides the log-price dynamics that serve as the foundation for the characteristic function derivation in subsequent sections.

The next section examines the [connection to the general stochastic volatility framework](connection_to_sv_framework.md), showing how the Heston model specializes a broader class of SV models.

---

## Exercises

**Exercise 1.** Starting from $dS_t = rS_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S$, apply Ito's lemma to derive the SDE for $x_t = \log S_t$. Identify the drift and diffusion of $x_t$ and explain why the drift contains the term $-\frac{1}{2}V_t$.

??? success "Solution to Exercise 1"
    Starting from $dS_t = rS_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S$, apply Ito's lemma to $f(S) = \ln S$. The first and second derivatives are $f'(S) = 1/S$ and $f''(S) = -1/S^2$. By Ito's formula:

    $$
    dx_t = f'(S_t)\,dS_t + \tfrac{1}{2}f''(S_t)\,(dS_t)^2
    $$

    Substituting the dynamics:

    $$
    dx_t = \frac{1}{S_t}\bigl[rS_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S\bigr] + \tfrac{1}{2}\left(-\frac{1}{S_t^2}\right)V_t S_t^2\,dt
    $$

    $$
    = r\,dt + \sqrt{V_t}\,dW_t^S - \tfrac{1}{2}V_t\,dt = \left(r - \tfrac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^S
    $$

    The drift of the log-price is $r - \frac{1}{2}V_t$ and the diffusion coefficient is $\sqrt{V_t}$. The term $-\frac{1}{2}V_t$ is the **Ito correction** (or convexity adjustment): it arises because $\ln S$ is a concave function of $S$, and the second-order Ito term subtracts $\frac{1}{2}\sigma^2$ from the drift when converting from the price SDE to the log-price SDE. Under stochastic volatility, this correction is itself random, depending on the current variance level $V_t$.

---

**Exercise 2.** The Heston model has five parameters: $\kappa$, $\theta$, $\sigma_v$, $\rho$, and $V_0$. Describe the financial role of each parameter. Which parameter controls the overall level of implied volatility? Which controls the skew? Which controls the smile's convexity?

??? success "Solution to Exercise 2"
    The five Heston parameters and their financial roles:

    - **$V_0$ (initial variance):** Sets the current level of instantaneous variance. The at-the-money implied volatility is approximately $\sqrt{V_0}$, so $V_0$ controls the **overall level** of the implied volatility surface.

    - **$\kappa$ (mean-reversion speed):** Determines how quickly the variance reverts to its long-run level $\theta$. Large $\kappa$ means variance shocks are short-lived, which affects the **term structure** of the implied volatility surface (faster flattening at longer maturities).

    - **$\theta$ (long-run variance):** The stationary mean of the variance process. Together with $\kappa$, it determines the long-maturity implied volatility level.

    - **$\rho$ (correlation):** Controls the **skew** of the implied volatility surface. Negative $\rho$ (typical for equities, $\rho \approx -0.7$) generates negative skew: when the stock price falls, variance tends to rise, making downside puts more expensive. Positive $\rho$ would generate positive skew.

    - **$\sigma_v$ (vol-of-vol):** Controls the **convexity** (curvature or smile) of the implied volatility surface. Higher $\sigma_v$ means the variance process is more volatile, producing fatter tails in the return distribution, which translates to more pronounced curvature in the smile.

    In summary: $V_0$ controls the level, $\rho$ controls the skew, and $\sigma_v$ controls the smile's convexity.

---

**Exercise 3.** Show that if $\sigma_v = 0$ (zero vol-of-vol), the Heston model collapses to the Black-Scholes model with deterministic (but time-varying) variance. What happens to the implied volatility surface in this limit?

??? success "Solution to Exercise 3"
    If $\sigma_v = 0$, the variance SDE becomes:

    $$
    dV_t = \kappa(\theta - V_t)\,dt
    $$

    This is an ordinary differential equation (no stochastic term). Solving:

    $$
    V_t = \theta + (V_0 - \theta)e^{-\kappa t}
    $$

    The variance is a deterministic function of time that decays exponentially from $V_0$ toward $\theta$. Substituting into the asset price equation:

    $$
    dS_t = rS_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S
    $$

    This is a geometric Brownian motion with deterministic but time-varying volatility $\sqrt{V_t}$. The log-return over $[0, T]$ is Gaussian with variance $\int_0^T V_t\,dt$, which is a deterministic quantity.

    Since the return distribution is still Gaussian (conditionally and unconditionally), the implied volatility surface is **flat across strikes** at each maturity. The implied volatility at maturity $T$ equals:

    $$
    \sigma_{\text{imp}}(T) = \sqrt{\frac{1}{T}\int_0^T V_t\,dt}
    $$

    There is no skew ($\rho$ is irrelevant when $\sigma_v = 0$) and no smile. Only the term structure of implied volatility is nontrivial, reflecting the deterministic path of $V_t$ from $V_0$ to $\theta$.

---

**Exercise 4.** Compute the instantaneous covariance $\operatorname{Cov}(dx_t, dV_t) = \rho\sigma_v V_t\,dt$ between the log-price and the variance. For $\rho = -0.7$, $\sigma_v = 0.3$, and $V_t = 0.04$, evaluate this covariance numerically and interpret its sign.

??? success "Solution to Exercise 4"
    Using the Cholesky decomposition $W_t^{(1)} = Z_t^{(1)}$ and $W_t^{(2)} = \rho Z_t^{(1)} + \sqrt{1 - \rho^2}Z_t^{(2)}$, the instantaneous covariance is:

    $$
    \operatorname{Cov}(dx_t, dV_t) = \mathbb{E}\bigl[\sqrt{V_t}\,dW_t^{(1)} \cdot \sigma_v\sqrt{V_t}\,dW_t^{(2)}\bigr]
    $$

    $$
    = \sigma_v V_t\,\mathbb{E}\bigl[dW_t^{(1)}\,dW_t^{(2)}\bigr] = \sigma_v V_t \cdot \rho\,dt = \rho\sigma_v V_t\,dt
    $$

    For $\rho = -0.7$, $\sigma_v = 0.3$, and $V_t = 0.04$:

    $$
    \operatorname{Cov}(dx_t, dV_t) = (-0.7)(0.3)(0.04)\,dt = -0.0084\,dt
    $$

    The negative sign means that when the log-price decreases ($dx_t < 0$), the variance tends to increase ($dV_t > 0$), and vice versa. This is the **leverage effect**: falling stock prices are associated with rising volatility. Economically, this reflects the observation that market sell-offs are accompanied by spikes in implied volatility (e.g., the VIX rises when the S&P 500 falls). This negative correlation is the primary mechanism by which the Heston model generates the negative implied volatility skew observed in equity markets.

---

**Exercise 5.** The variance process $dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t^V$ has mean-reverting drift. Compute $\mathbb{E}[V_t \mid V_0]$ by solving the ODE $\frac{d}{dt}\mathbb{E}[V_t] = \kappa(\theta - \mathbb{E}[V_t])$ and show that $\mathbb{E}[V_t] = \theta + (V_0 - \theta)e^{-\kappa t}$.

??? success "Solution to Exercise 5"
    Taking expectations of the variance SDE $dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t$, and using $\mathbb{E}[dW_t] = 0$:

    $$
    d\,\mathbb{E}[V_t] = \kappa\bigl(\theta - \mathbb{E}[V_t]\bigr)\,dt
    $$

    Let $m(t) = \mathbb{E}[V_t]$. This gives the ODE:

    $$
    m'(t) = \kappa(\theta - m(t)), \qquad m(0) = V_0
    $$

    This is a first-order linear ODE. Define $y(t) = m(t) - \theta$, so $y'(t) = m'(t) = -\kappa y(t)$, which gives $y(t) = y(0)e^{-\kappa t} = (V_0 - \theta)e^{-\kappa t}$. Therefore:

    $$
    \mathbb{E}[V_t] = \theta + (V_0 - \theta)e^{-\kappa t}
    $$

    As $t \to \infty$, $\mathbb{E}[V_t] \to \theta$, confirming that $\theta$ is the long-run mean. The decay is exponential with rate $\kappa$: if the current variance is above (below) $\theta$, it is pulled down (up) toward $\theta$ at an exponential rate.

---

**Exercise 6.** For a typical equity calibration ($\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.5$, $\rho = -0.75$, $V_0 = 0.04$), compute the half-life of mean reversion $t_{1/2} = \ln 2/\kappa$ and the stationary standard deviation of $V_t$. Is the Feller condition $2\kappa\theta \geq \sigma_v^2$ satisfied?

??? success "Solution to Exercise 6"
    Given $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.5$, $\rho = -0.75$, $V_0 = 0.04$:

    **Half-life of mean reversion:**

    $$
    t_{1/2} = \frac{\ln 2}{\kappa} = \frac{0.6931}{2} \approx 0.347 \text{ years} \approx 4.2 \text{ months}
    $$

    This means that if variance is perturbed from $\theta$, the expected time for the deviation to halve is about 4.2 months.

    **Stationary variance of $V_t$:** The CIR process has stationary distribution that is a Gamma distribution. The stationary variance is:

    $$
    \operatorname{Var}_\infty(V_t) = \frac{\sigma_v^2 \theta}{2\kappa} = \frac{(0.5)^2 (0.04)}{2(2)} = \frac{0.01}{4} = 0.0025
    $$

    The stationary standard deviation is:

    $$
    \operatorname{Std}_\infty(V_t) = \sqrt{0.0025} = 0.05
    $$

    Since $\theta = 0.04$, the coefficient of variation is $0.05/0.04 = 1.25$, indicating substantial variability in the variance process relative to its mean.

    **Feller condition check:**

    $$
    2\kappa\theta = 2(2)(0.04) = 0.16
    $$

    $$
    \sigma_v^2 = (0.5)^2 = 0.25
    $$

    Since $0.16 < 0.25$, the Feller condition $2\kappa\theta \geq \sigma_v^2$ is **violated**. The Feller ratio is $F = 0.16/0.25 = 0.64 < 1$. This means the variance process can reach zero with positive probability, which is typical for calibrated equity parameters.
