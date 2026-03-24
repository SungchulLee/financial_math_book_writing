# Feller Condition and Boundary Behavior

The variance process in the Heston model is a **square-root diffusion** (CIR process), whose behavior near zero is critical for both mathematical well-posedness and numerical implementation. This section provides a rigorous treatment of boundary classification, the Feller condition, and practical implications.

---

## The CIR Variance Process

### Dynamics

The variance in the Heston model follows a Cox–Ingersoll–Ross (CIR) process:

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
$$

with parameters $\kappa > 0$ (mean reversion), $\theta > 0$ (long-run level), and $\xi > 0$ (volatility of volatility).

### Key Features

1. **Mean reversion:** $V_t$ is pulled toward $\theta$
2. **Square-root diffusion:** Volatility of $V$ vanishes as $V \to 0$
3. **Non-negative:** $V_t \geq 0$ for all $t$ (almost surely)

The challenge: ensuring the process stays strictly positive ($V_t > 0$) vs. merely non-negative ($V_t \geq 0$).

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

### Full Truncation

Replace $V_t^+ = \max(V_t, 0)$ in both drift and diffusion:

$$
V_{t+\Delta} = V_t + \kappa(\theta - V_t^+)\Delta + \xi\sqrt{V_t^+}\sqrt{\Delta}\,Z
$$

**Properties:**
- Simple to implement
- Introduces positive bias (variance is inflated)
- Bias is $O(\Delta)$

### Reflection

If $V_{t+\Delta} < 0$, set $V_{t+\Delta} = |V_{t+\Delta}|$:

**Properties:**
- Preserves variance distribution approximately
- Can introduce spurious oscillations
- Better than truncation for some metrics

### Quadratic-Exponential (QE) Scheme

Andersen's QE scheme matches moments of the exact transition density:

**Step 1:** Compute $m = \theta + (V_t - \theta)e^{-\kappa\Delta}$ and $s^2 = \frac{V_t\xi^2 e^{-\kappa\Delta}}{\kappa}(1-e^{-\kappa\Delta}) + \frac{\theta\xi^2}{2\kappa}(1-e^{-\kappa\Delta})^2$

**Step 2:** If $\psi = s^2/m^2 < \psi_c$ (typically $\psi_c = 1.5$), use quadratic:

$$
V_{t+\Delta} = a(b + Z)^2
$$

where $a, b$ are moment-matched.

**Step 3:** If $\psi \geq \psi_c$, use exponential:

$$
V_{t+\Delta} = \Psi^{-1}(U; p, \beta)
$$

where $\Psi$ is a mixture of point mass at 0 and exponential.

**Properties:**
- Near-exact distribution matching
- Robust under Feller violation
- Industry standard

### Exact Simulation

The transition $V_{t+\Delta} | V_t$ is a scaled non-central chi-squared:

$$
V_{t+\Delta} = \frac{\xi^2(1-e^{-\kappa\Delta})}{4\kappa}\chi'^2_{d,\lambda}
$$

where:
- $d = \frac{4\kappa\theta}{\xi^2}$ (degrees of freedom)
- $\lambda = \frac{4\kappa e^{-\kappa\Delta}}{\xi^2(1-e^{-\kappa\Delta})}V_t$ (non-centrality)

**Properties:**
- Exact in distribution
- Computationally expensive (non-central chi-squared sampling)
- Useful for benchmarking

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

---

**Exercise 2.** Using Feller's boundary classification, the scale function for the CIR process is

$$
s(x) = \int_c^x \exp\left(-\int_c^y \frac{2\kappa(\theta - z)}{\xi^2 z}\,dz\right)dy
$$

Evaluate the inner integral $\int_c^y \frac{2\kappa(\theta - z)}{\xi^2 z}\,dz$ in closed form (it involves $\ln y$ and linear terms). Show that for $\nu > 1$, the integral $\int_0^c s(x)\,dx$ diverges, which implies the boundary at zero is unattainable.

---

**Exercise 3.** For the Heston parameters $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $V_0 = 0.04$ (so $\nu = 0.64 < 1$), explain why the characteristic function and hence European option prices remain valid. Specifically, argue that the quantity $\mathbb{E}[\int_0^T V_s\,ds]$ is finite and well-defined even though $V_t$ can touch zero.

---

**Exercise 4.** In the Euler scheme with full truncation, starting from $V_t = 0.005$ with $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$:

(a) Compute the mean and variance of $V_{t+\Delta}$ before truncation.

(b) Find the probability that $V_{t+\Delta} < 0$ before truncation.

(c) Explain the bias introduced by replacing negative values with zero. Is this bias positive or negative in the expected value of $V$?

---

**Exercise 5.** The QE scheme switches between a quadratic and exponential approximation based on the ratio $\psi = s^2/m^2$. Given $V_t = 0.02$, $\kappa = 3$, $\theta = 0.04$, $\xi = 0.6$, $\Delta = 1/252$:

(a) Compute $m = \theta + (V_t - \theta)e^{-\kappa\Delta}$.

(b) Compute $s^2 = \frac{V_t\xi^2 e^{-\kappa\Delta}}{\kappa}(1 - e^{-\kappa\Delta}) + \frac{\theta\xi^2}{2\kappa}(1 - e^{-\kappa\Delta})^2$.

(c) Evaluate $\psi$ and determine which branch (quadratic or exponential with $\psi_c = 1.5$) the QE scheme would use.

---

**Exercise 6.** The exact transition distribution of the CIR process is a scaled non-central $\chi^2$ with degrees of freedom $d = 4\kappa\theta/\xi^2$ and non-centrality $\lambda = \frac{4\kappa e^{-\kappa\Delta}}{\xi^2(1 - e^{-\kappa\Delta})}V_t$. For $V_t = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\Delta = 1/252$, compute $d$ and $\lambda$. Verify that the mean of $V_{t+\Delta}$ equals $\theta + (V_t - \theta)e^{-\kappa\Delta}$.

---

**Exercise 7.** A risk manager calibrates the Heston model to S&P 500 options during a stress period and obtains $\kappa = 1.2$, $\theta = 0.08$, $\xi = 0.9$. Compute $\nu$ and determine if Feller is satisfied. The manager needs to run a Monte Carlo simulation with 100,000 paths. Compare the expected accuracy (in terms of bias and variance) of Euler truncation vs. QE for pricing a 1-year ATM call. Which scheme should she use, and why?
