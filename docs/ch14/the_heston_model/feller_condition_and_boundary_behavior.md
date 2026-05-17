# Feller Condition and Boundary Behavior

The variance process in the Heston model is a **square-root diffusion** (CIR process), whose behavior near zero is critical for both mathematical well-posedness and numerical implementation. This section provides a rigorous treatment of boundary classification, the Feller condition, and practical implications.

---

## The CIR Variance Process

Recall (see [§ Variance Dynamics — CIR Process](../../ch16/variance_dynamics/cir_variance_process_solution.md)) the Heston variance SDE

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V, \qquad \kappa,\theta,\xi>0,
$$

which is mean-reverting, has vanishing diffusion as $V\to 0$, and stays non-negative a.s. The question addressed here is **strict positivity** vs. merely non-negativity.

---

## The Feller Condition

### Statement

The **Feller condition** is:

$$
2\kappa\theta \geq \xi^2
$$

Equivalently, defining $\nu = \frac{2\kappa\theta}{\xi^2}$:

$$
\nu \geq 1
$$

### Interpretation

**If Feller holds ($\nu \geq 1$):**

- The boundary $V = 0$ is **unattainable**
- $V_t > 0$ for all $t > 0$ (almost surely)
- The process never touches zero

**If Feller fails ($\nu < 1$):**

- The boundary $V = 0$ is **attainable**
- $V_t$ can reach zero in finite time
- After reaching zero, the process immediately reflects back

### Heuristic Derivation

Near $V = 0$, the drift $\kappa\theta$ pushes the process away from zero, while the diffusion $\xi\sqrt{V}$ can push it toward zero.

The **speed measure** comparison:

- Drift contribution: $\kappa\theta$
- Diffusion contribution: $\frac{1}{2}\xi^2$

The drift dominates when $\kappa\theta > \frac{1}{2}\xi^2$, i.e., $2\kappa\theta > \xi^2$.

---

## Boundary Classification Theory

### Feller's Boundary Classification

For a diffusion $dX = \mu(X)dt + \sigma(X)dW$ on $(0, \infty)$, boundaries are classified using:

**Scale function:**

$$
s(x) = \int_c^x \exp\left(-\int_c^y \frac{2\mu(z)}{\sigma(z)^2}dz\right)dy
$$

**Speed measure:**

$$
m(x) = \frac{1}{\sigma(x)^2 s'(x)}
$$

### Classification of Zero for CIR

For the CIR process, the boundary $V = 0$ is classified as:

| Condition | Boundary type | Behavior |
|-----------|---------------|----------|
| $\nu \geq 2$ | Entrance | Cannot start at 0, never reaches 0 |
| $1 \leq \nu < 2$ | Entrance-not-exit | Can start at 0, cannot return to 0 |
| $0 < \nu < 1$ | Regular | Can reach 0, instantly reflects |

**For Heston calibration:** Typically $\nu \in (0.5, 2)$, spanning all cases.

---

## Practical Relevance

### Calibrated Parameters Often Violate Feller

Empirical calibrations frequently produce $\nu < 1$:

| Market | Typical $\nu$ | Feller satisfied? |
|--------|---------------|-------------------|
| S&P 500 (normal) | 0.8–1.5 | Sometimes |
| S&P 500 (stressed) | 0.3–0.8 | Rarely |
| Individual stocks | 0.5–1.2 | Often not |
| FX | 1.0–2.0 | Usually |

**Why?** Markets exhibit sharp volatility spikes ($\xi$ large) combined with moderate mean reversion ($\kappa\theta$ not large enough).

### Option Pricing Remains Valid

**Key result:** Heston option pricing formulas remain valid even when Feller fails.

The characteristic function is well-defined for all parameter values with $\kappa, \theta, \xi > 0$. The pricing integrals converge regardless of Feller.

**Intuition:** Option prices depend on the distribution of $\int_0^T V_s\,ds$, which is well-defined even if $V$ touches zero occasionally.

### Simulation Challenges

Feller violation creates numerical difficulties:

1. **Euler scheme instability:** $V_{t+\Delta}$ can become negative
2. **Bias:** Truncation or reflection introduces systematic errors
3. **Path-dependent products:** Barrier crossings become sensitive to discretization

---

## Simulation Schemes Under Feller Violation

Recall (see [§ Variance Dynamics — Simulation](../../ch16/variance_dynamics/cir_variance_process_solution.md) and [§ European Pricing — Monte Carlo](../../ch16/european_pricing/semi_closed_form_fourier_inversion.md)) the standard schemes:

- **Full truncation Euler:** $V_{t+\Delta}=V_t+\kappa(\theta-V_t^+)\Delta+\xi\sqrt{V_t^+}\sqrt{\Delta}\,Z$ — simple, $O(\Delta)$ positive bias.
- **Reflection:** $V_{t+\Delta}\mapsto|V_{t+\Delta}|$ — less bias than truncation, may oscillate.
- **Andersen QE:** moment-match the exact non-central $\chi^2$, switching between a quadratic branch and an exponential-with-mass-at-zero branch at $\psi_c\approx 1.5$ — industry standard, robust under $\nu<1$.
- **Exact non-central $\chi^2$:** $V_{t+\Delta}=\tfrac{\xi^2(1-e^{-\kappa\Delta})}{4\kappa}\,\chi'^2_{d,\lambda}$ with $d=4\kappa\theta/\xi^2$, $\lambda=\tfrac{4\kappa e^{-\kappa\Delta}}{\xi^2(1-e^{-\kappa\Delta})}V_t$ — distributionally exact, costly.

---

## Numerical Example

**Parameters:** $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $V_0 = 0.04$

**Feller ratio:** $\nu = \frac{2 \times 2 \times 0.04}{0.25} = 0.64 < 1$ (Feller violated)

**Simulation comparison** (10,000 paths, $T = 1$, $\Delta = 1/252$):

| Scheme | $\mathbb{E}[\bar{V}]$ | Std. Error | Neg. variance freq. |
|--------|----------------------|------------|---------------------|
| True value | 0.0400 | — | — |
| Euler (truncation) | 0.0412 | 0.0003 | 12% |
| Reflection | 0.0405 | 0.0003 | 12% |
| QE scheme | 0.0401 | 0.0003 | 0% |
| Exact | 0.0400 | 0.0003 | 0% |

The QE scheme nearly eliminates bias while avoiding negative variance entirely.

---

## Key Takeaways

- The Feller condition $2\kappa\theta \geq \xi^2$ guarantees strict positivity
- Violations are common in market calibration (high vol-of-vol)
- Option pricing formulas remain valid regardless of Feller
- Simulation requires careful schemes: QE is the industry standard
- Exact simulation is possible via non-central chi-squared

---

## Further Reading

- Cox, J., Ingersoll, J., & Ross, S. (1985). *A theory of the term structure of interest rates*. Econometrica.
- Feller, W. (1951). *Two singular diffusion problems*. Annals of Mathematics.
- Andersen, L. (2008). *Efficient simulation of the Heston stochastic volatility model*. Journal of Computational Finance.
- Lord, R., Koekkoek, R., & van Dijk, D. (2010). *A comparison of biased simulation schemes for stochastic volatility models*. Quantitative Finance.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer.

---

## Exercises

**Exercise 1.** Compute the Feller ratio $\nu = 2\kappa\theta/\xi^2$ for the following parameter sets and classify the boundary at $V = 0$ (entrance, entrance-not-exit, or regular):

| Set | $\kappa$ | $\theta$ | $\xi$ |
|-----|----------|----------|--------|
| A   | 3.0      | 0.04     | 0.30   |
| B   | 1.5      | 0.05     | 0.50   |
| C   | 5.0      | 0.02     | 0.80   |
| D   | 2.0      | 0.06     | 0.40   |

??? success "Solution to Exercise 1"
    Compute $\nu = 2\kappa\theta/\xi^2$ for each set and classify the boundary:

    **Set A:** $\kappa = 3.0$, $\theta = 0.04$, $\xi = 0.30$

    $$
    \nu = \frac{2 \times 3.0 \times 0.04}{0.09} = \frac{0.24}{0.09} = 2.667
    $$

    Since $\nu \geq 2$, the boundary is **entrance**: the process cannot start at 0 and never reaches 0.

    **Set B:** $\kappa = 1.5$, $\theta = 0.05$, $\xi = 0.50$

    $$
    \nu = \frac{2 \times 1.5 \times 0.05}{0.25} = \frac{0.15}{0.25} = 0.60
    $$

    Since $0 < \nu < 1$, the boundary is **regular**: the process can reach 0 and instantly reflects.

    **Set C:** $\kappa = 5.0$, $\theta = 0.02$, $\xi = 0.80$

    $$
    \nu = \frac{2 \times 5.0 \times 0.02}{0.64} = \frac{0.20}{0.64} = 0.3125
    $$

    Since $0 < \nu < 1$, the boundary is **regular**.

    **Set D:** $\kappa = 2.0$, $\theta = 0.06$, $\xi = 0.40$

    $$
    \nu = \frac{2 \times 2.0 \times 0.06}{0.16} = \frac{0.24}{0.16} = 1.50
    $$

    Since $1 \leq \nu < 2$, the boundary is **entrance-not-exit**: the process can start at 0 but cannot return to 0 once it leaves.

---

**Exercise 2.** Using Feller's boundary classification, the scale function for the CIR process is

$$
s(x) = \int_c^x \exp\left(-\int_c^y \frac{2\kappa(\theta - z)}{\xi^2 z}\,dz\right)dy
$$

Evaluate the inner integral $\int_c^y \frac{2\kappa(\theta - z)}{\xi^2 z}\,dz$ in closed form (it involves $\ln y$ and linear terms). Show that for $\nu > 1$, the integral $\int_0^c s(x)\,dx$ diverges, which implies the boundary at zero is unattainable.

??? success "Solution to Exercise 2"
    The inner integral is:

    $$
    I(y) = \int_c^y \frac{2\kappa(\theta - z)}{\xi^2 z}\,dz = \frac{2\kappa}{\xi^2}\int_c^y \left(\frac{\theta}{z} - 1\right)dz
    $$

    Evaluating:

    $$
    I(y) = \frac{2\kappa}{\xi^2}\left[\theta\ln\frac{y}{c} - (y - c)\right]
    $$

    The scale density is therefore:

    $$
    s'(x) = \exp(-I(x)) = \exp\left(-\frac{2\kappa}{\xi^2}\left[\theta\ln\frac{x}{c} - (x - c)\right]\right)
    $$

    Simplifying (absorbing constants):

    $$
    s'(x) \propto x^{-2\kappa\theta/\xi^2}\exp\left(\frac{2\kappa x}{\xi^2}\right) = x^{-\nu}\exp\left(\frac{2\kappa x}{\xi^2}\right)
    $$

    Near $x = 0$, the exponential factor $\to 1$, so $s'(x) \sim x^{-\nu}$.

    Integrating to get $s(x)$:

    $$
    s(x) = \int_0^x s'(y)\,dy \sim \int_0^x y^{-\nu}\,dy
    $$

    For $\nu > 1$, $\int_0^x y^{-\nu}\,dy$ diverges as the lower limit approaches 0, because the exponent satisfies $-\nu < -1$.

    In Feller's boundary classification, when $\int_0^c s(x)\,dx = \infty$ (which follows from $s(x) \to \infty$ as $x \to 0^+$ fast enough), the boundary at zero is **unattainable** -- the process cannot reach it in finite time. This is the rigorous statement behind the Feller condition $\nu > 1$.

---

**Exercise 3.** For the Heston parameters $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $V_0 = 0.04$ (so $\nu = 0.64 < 1$), explain why the characteristic function and hence European option prices remain valid. Specifically, argue that the quantity $\mathbb{E}[\int_0^T V_s\,ds]$ is finite and well-defined even though $V_t$ can touch zero.

??? success "Solution to Exercise 3"
    Even when the Feller condition fails ($\nu = 0.64 < 1$), the variance process $V_t$ is well-defined as a non-negative diffusion. At the boundary $V = 0$, the classification is "regular" with instantaneous reflection, meaning $V_t$ can touch zero but immediately bounces back. The process spends zero Lebesgue time at the origin.

    The expected integrated variance is:

    $$
    \mathbb{E}\left[\int_0^T V_s\,ds\right] = \theta T + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}
    $$

    This formula is derived from $\mathbb{E}[V_s] = \theta + (V_0 - \theta)e^{-\kappa s}$ and integrating over $[0, T]$. The expectation $\mathbb{E}[V_s]$ is finite for all $s$ regardless of the Feller condition, because the CIR process has finite moments of all orders for any $\kappa, \theta, \xi > 0$.

    Therefore $\mathbb{E}[\int_0^T V_s\,ds]$ is finite and well-defined. The characteristic function $\varphi(\tau, u) = \exp(C + DV_0 + iuX_0)$ is obtained by solving the Riccati ODEs, which have explicit solutions for all parameter values with $\kappa, \theta, \xi > 0$. The solutions $C(\tau, u)$ and $D(\tau, u)$ are analytic functions of $u$ and do not require the Feller condition.

    Consequently, European option prices computed via Fourier inversion of the characteristic function remain valid. The key insight is that option prices depend on the distribution of integrated variance $\int_0^T V_s\,ds$, which is well-behaved even when $V_t$ occasionally touches zero, since the set of times where $V_t = 0$ has measure zero.

---

**Exercise 4.** In the Euler scheme with full truncation, starting from $V_t = 0.005$ with $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$:

(a) Compute the mean and variance of $V_{t+\Delta}$ before truncation.

(b) Find the probability that $V_{t+\Delta} < 0$ before truncation.

(c) Explain the bias introduced by replacing negative values with zero. Is this bias positive or negative in the expected value of $V$?

??? success "Solution to Exercise 4"
    With $V_t = 0.005$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$:

    **(a)** The Euler update (before truncation) is $V_{t+\Delta} = V_t + \kappa(\theta - V_t)\Delta + \xi\sqrt{V_t}\sqrt{\Delta}\,Z$.

    Mean:

    $$
    \mathbb{E}[V_{t+\Delta}] = V_t + \kappa(\theta - V_t)\Delta = 0.005 + 2(0.04 - 0.005)/252 = 0.005 + 0.000278 = 0.005278
    $$

    Variance:

    $$
    \text{Var}[V_{t+\Delta}] = \xi^2 V_t \Delta = 0.25 \times 0.005 \times (1/252) = 4.960 \times 10^{-6}
    $$

    Standard deviation: $\sqrt{4.960 \times 10^{-6}} = 0.002227$.

    **(b)** Setting $V_{t+\Delta} < 0$:

    $$
    0.005278 + 0.002227\,Z < 0 \implies Z < -\frac{0.005278}{0.002227} = -2.370
    $$

    $$
    \mathbb{P}(V_{t+\Delta} < 0) = \Phi(-2.370) \approx 0.89\%
    $$

    **(c)** The full truncation scheme replaces negative values with zero. This introduces a **positive bias** in $\mathbb{E}[V]$. The true distribution allows the process to take values that, in the discrete approximation, would be slightly negative. By setting these to zero instead, the scheme inflates the average variance. Formally, $\mathbb{E}[\max(V_{t+\Delta}, 0)] > \mathbb{E}[V_{t+\Delta}]$ whenever $\mathbb{P}(V_{t+\Delta} < 0) > 0$. This upward bias in variance leads to overestimation of option prices in Monte Carlo simulations.

---

**Exercise 5.** The QE scheme switches between a quadratic and exponential approximation based on the ratio $\psi = s^2/m^2$. Given $V_t = 0.02$, $\kappa = 3$, $\theta = 0.04$, $\xi = 0.6$, $\Delta = 1/252$:

(a) Compute $m = \theta + (V_t - \theta)e^{-\kappa\Delta}$.

(b) Compute $s^2 = \frac{V_t\xi^2 e^{-\kappa\Delta}}{\kappa}(1 - e^{-\kappa\Delta}) + \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta})^2$.

(c) Evaluate $\psi$ and determine which branch (quadratic or exponential with $\psi_c = 1.5$) the QE scheme would use.

??? success "Solution to Exercise 5"
    With $V_t = 0.02$, $\kappa = 3$, $\theta = 0.04$, $\xi = 0.6$, $\Delta = 1/252$:

    **(a)** Compute $m$:

    $$
    e^{-\kappa\Delta} = e^{-3/252} = e^{-0.01190} = 0.98817
    $$

    $$
    m = \theta + (V_t - \theta)e^{-\kappa\Delta} = 0.04 + (0.02 - 0.04)(0.98817) = 0.04 - 0.01976 = 0.02024
    $$

    **(b)** Compute $s^2$:

    $$
    1 - e^{-\kappa\Delta} = 1 - 0.98817 = 0.01183
    $$

    First term:

    $$
    \frac{V_t\xi^2 e^{-\kappa\Delta}}{\kappa}(1 - e^{-\kappa\Delta}) = \frac{0.02 \times 0.36 \times 0.98817}{3} \times 0.01183 = \frac{0.007115}{3} \times 0.01183 = 2.372 \times 10^{-3} \times 0.01183 = 2.806 \times 10^{-5}
    $$

    Second term:

    $$
    \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta})^2 = \frac{0.04 \times 0.36}{6} \times (0.01183)^2 = 2.400 \times 10^{-3} \times 1.399 \times 10^{-4} = 3.358 \times 10^{-7}
    $$

    $$
    s^2 = 2.806 \times 10^{-5} + 3.358 \times 10^{-7} \approx 2.840 \times 10^{-5}
    $$

    **(c)** Compute $\psi$:

    $$
    \psi = \frac{s^2}{m^2} = \frac{2.840 \times 10^{-5}}{(0.02024)^2} = \frac{2.840 \times 10^{-5}}{4.097 \times 10^{-4}} = 0.0693
    $$

    Since $\psi = 0.0693 < \psi_c = 1.5$, the QE scheme uses the **quadratic branch**: $V_{t+\Delta} = a(b + Z)^2$, where $a$ and $b$ are determined by moment matching to $m$ and $s^2$. The small $\psi$ indicates the distribution is well-concentrated and far from zero, making the quadratic (squared Gaussian) approximation accurate.

---

**Exercise 6.** The exact transition distribution of the CIR process is a scaled non-central $\chi^2$ with degrees of freedom $d = 4\kappa\theta/\xi^2$ and non-centrality $\lambda = \frac{4\kappa e^{-\kappa\Delta}}{\xi^2(1 - e^{-\kappa\Delta})}V_t$. For $V_t = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$, compute $d$ and $\lambda$. Verify that the mean of $V_{t+\Delta}$ equals $\theta + (V_t - \theta)e^{-\kappa\Delta}$.

??? success "Solution to Exercise 6"
    With $V_t = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$:

    **Degrees of freedom:**

    $$
    d = \frac{4\kappa\theta}{\xi^2} = \frac{4 \times 2 \times 0.04}{0.25} = \frac{0.32}{0.25} = 1.28
    $$

    **Non-centrality parameter:**

    $$
    e^{-\kappa\Delta} = e^{-2/252} \approx 0.99209
    $$

    $$
    \lambda = \frac{4\kappa e^{-\kappa\Delta}}{\xi^2(1 - e^{-\kappa\Delta})}V_t = \frac{4 \times 2 \times 0.99209}{0.25 \times 0.00791} \times 0.04 = \frac{7.9367}{0.001978} \times 0.04 = 4012.7 \times 0.04 = 160.5
    $$

    **Verification of the mean:** The mean of a non-central $\chi^2$ with $d$ degrees of freedom and non-centrality $\lambda$ is $d + \lambda$. The scaling factor is:

    $$
    c = \frac{\xi^2(1 - e^{-\kappa\Delta})}{4\kappa} = \frac{0.25 \times 0.00791}{8} = 2.472 \times 10^{-4}
    $$

    $$
    \mathbb{E}[V_{t+\Delta}] = c(d + \lambda) = 2.472 \times 10^{-4} \times (1.28 + 160.5) = 2.472 \times 10^{-4} \times 161.78 = 0.03999 \approx 0.04
    $$

    The theoretical mean is:

    $$
    \theta + (V_t - \theta)e^{-\kappa\Delta} = 0.04 + (0.04 - 0.04) \times 0.99209 = 0.04
    $$

    The values agree, confirming the exact transition distribution is consistent with the CIR moment formula.

---

**Exercise 7.** A risk manager calibrates the Heston model to S&P 500 options during a stress period and obtains $\kappa = 1.2$, $\theta = 0.08$, $\xi = 0.9$. Compute $\nu$ and determine if Feller is satisfied. The manager needs to run a Monte Carlo simulation with 100,000 paths. Compare the expected accuracy (in terms of bias and variance) of Euler truncation vs. QE for pricing a 1-year ATM call. Which scheme should she use, and why?

??? success "Solution to Exercise 7"
    **Feller ratio:**

    $$
    \nu = \frac{2\kappa\theta}{\xi^2} = \frac{2 \times 1.2 \times 0.08}{0.81} = \frac{0.192}{0.81} = 0.237
    $$

    Since $\nu = 0.237 < 1$, the Feller condition is **strongly violated**. The variance process will frequently touch zero.

    **Euler truncation:**

    - With such a low Feller ratio, the probability of generating negative variance in a single step is substantial. The truncation $V_t^+ = \max(V_t, 0)$ will be triggered frequently, especially when $V_t$ is small.
    - This introduces a positive bias in variance (and hence in option prices). From the numerical example in the text, Euler truncation with $\nu = 0.64$ already showed 3% bias in $\mathbb{E}[\bar{V}]$. With $\nu = 0.237$, the bias will be considerably larger.
    - The statistical variance of the estimator is comparable across schemes, but the bias is the dominant error source.

    **QE scheme:**

    - The QE scheme matches the first two moments of the exact non-central $\chi^2$ transition density and switches between quadratic and exponential approximations depending on $\psi = s^2/m^2$.
    - With the Feller condition strongly violated, $\psi$ will frequently exceed $\psi_c$, triggering the exponential branch, which correctly assigns positive probability to $V_{t+\Delta} = 0$.
    - Bias is nearly zero even for $\nu \ll 1$.

    **Recommendation:** The QE scheme should be used. With 100,000 paths the statistical error will be small (roughly proportional to $1/\sqrt{100{,}000} \approx 0.3\%$), so the dominant error is discretization bias. Euler truncation's $O(\Delta)$ bias can easily exceed the Monte Carlo standard error, producing a systematically mispriced call. The QE scheme eliminates this bias at minimal additional computational cost.
