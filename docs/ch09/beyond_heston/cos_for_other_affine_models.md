# COS Method for Other Affine Models

The COS method requires only one model-specific input: the characteristic function $\phi(u)$. Everything else---the cosine expansion, payoff coefficients, truncation rule, and summation---is model-independent. This universality means the COS method applies immediately to any model with a known characteristic function. This section develops the characteristic functions for four important model families beyond Heston---Bates (SVJ), Variance Gamma, CGMY/tempered stable, and NIG---and explains the model-specific considerations for applying the COS method to each.

!!! info "Prerequisites"
    - [COS Pricing Formula](../cos_method/cos_pricing_formula.md) (the model-independent pricing formula)
    - [Truncation to Finite Domain](../cos_method/truncation_to_finite_domain.md) (cumulant-based truncation)
    - [Error Analysis and Convergence](../cos_method/error_analysis_and_convergence.md) (convergence rates)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the characteristic function for Bates, VG, CGMY, and NIG models
    2. Compute cumulants for each model to determine the truncation interval
    3. Assess the convergence rate of the COS method for each model
    4. Identify model-specific implementation considerations
    5. Select appropriate $N$ and $[a, b]$ for each model

---

## The COS Method Is Model-Agnostic

Recall the COS pricing formula:

$$
V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k\, V_k
$$

The payoff coefficients $V_k$ depend only on the payoff function and the truncation interval $[a, b]$. The density coefficients $F_k$ depend only on the characteristic function:

$$
F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
$$

To apply COS to a new model, we need only:

1. The characteristic function $\phi(u)$ (plug into $F_k$)
2. The first four cumulants $c_1, c_2, c_3, c_4$ (for the truncation interval)

---

## Bates Model (Stochastic Volatility with Jumps)

The Bates (1996) model combines the Heston stochastic volatility with Merton-style log-normal jumps.

!!! note "Definition: Bates Model"
    Under the risk-neutral measure:

    $$
    \frac{dS_t}{S_t} = (r - q - \lambda\bar{\mu})\,dt + \sqrt{v_t}\,dW_t^S + (e^J - 1)\,dN_t
    $$

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^v
    $$

    where $\text{Corr}(dW^S, dW^v) = \rho$, $N_t$ is a Poisson process with intensity $\lambda$, and $J \sim N(\mu_J, \sigma_J^2)$. The compensator is $\bar{\mu} = e^{\mu_J + \sigma_J^2/2} - 1$.

The characteristic function of the log-price is the product of the Heston CF and the Merton jump CF:

$$
\phi_{\text{Bates}}(u) = \phi_{\text{Heston}}(u)\cdot\exp\!\left(\lambda T\left[e^{i\mu_J u - \sigma_J^2 u^2/2} - 1 - i\bar{\mu} u\right]\right)
$$

The jump component adds a multiplicative factor to the Heston CF, making the implementation straightforward: compute the Heston CF as before, then multiply by the jump factor.

**COS considerations:**

- **Cumulants:** Add the jump cumulants to the Heston cumulants. The jump contribution to the variance is $\lambda T(\sigma_J^2 + \mu_J^2)$, and to the fourth cumulant is $\lambda T(\mu_J^4 + 6\mu_J^2\sigma_J^2 + 3\sigma_J^4)$.
- **Convergence:** Exponential, same as Heston. The jump component adds kurtosis but does not affect the analyticity strip.
- **Typical $N$:** 64--128, same as Heston.

---

## Variance Gamma Model

The Variance Gamma (VG) model (Madan, Carr, and Chang, 1998) is a pure-jump Levy process obtained by time-changing a Brownian motion with drift by a gamma subordinator.

!!! note "Definition: Variance Gamma Process"
    The log-price under VG is:

    $$
    X_T = (r - q + \omega)T + \theta G_T + \sigma W_{G_T}
    $$

    where $G_T$ is a gamma process with mean rate 1 and variance rate $\nu$, $\theta$ controls the drift (skewness), $\sigma$ controls the diffusion (volatility), and $\omega = \frac{1}{\nu}\ln(1 - \theta\nu - \sigma^2\nu/2)$ is the convexity correction.

The characteristic function is:

$$
\phi_{\text{VG}}(u) = \exp\!\left(iu(r-q+\omega)T\right)\left(\frac{1}{1 - iu\theta\nu + \sigma^2\nu u^2/2}\right)^{T/\nu}
$$

**COS considerations:**

- **Cumulants:**
    - $c_1 = (r - q + \omega)T$
    - $c_2 = (\sigma^2 + \nu\theta^2)T$
    - $c_3 = (2\theta^3\nu^2 + 3\sigma^2\theta\nu)T$
    - $c_4 = (3\sigma^4\nu + 12\sigma^2\theta^2\nu^2 + 6\theta^4\nu^3)T$
- **Convergence:** Exponential. The VG density is smooth (no atoms, no discontinuities) with exponential tails.
- **Typical $N$:** 128--256. The VG density is more peaked and heavier-tailed than the log-normal, requiring more terms.
- **Truncation:** Use the full cumulant formula with $L = 12$ due to heavier tails.

---

## CGMY Model

The CGMY model (Carr, Geman, Madan, and Yor, 2002) generalizes the Variance Gamma by allowing infinite activity and infinite variation through the parameter $Y$.

!!! note "Definition: CGMY Process"
    The CGMY process is a tempered stable process with Levy measure:

    $$
    \nu(dx) = \begin{cases} C\frac{e^{-G|x|}}{|x|^{1+Y}}\,dx & \text{if } x < 0 \\ C\frac{e^{-Mx}}{x^{1+Y}}\,dx & \text{if } x > 0 \end{cases}
    $$

    where $C > 0$ (activity), $G > 0$ (left exponential decay), $M > 0$ (right exponential decay), and $Y < 2$ (fine structure).

The characteristic function is:

$$
\phi_{\text{CGMY}}(u) = \exp\!\left(iu(r-q+\omega)T + CT\Gamma(-Y)\left[(M-iu)^Y - M^Y + (G+iu)^Y - G^Y\right]\right)
$$

where $\omega = -C\Gamma(-Y)[(M-1)^Y - M^Y + (G+1)^Y - G^Y]$ and $\Gamma$ is the gamma function.

**COS considerations:**

- **Convergence depends on $Y$:**
    - $Y < 0$: compound Poisson (finite activity), exponential convergence
    - $0 \leq Y < 1$: infinite activity, finite variation, exponential convergence
    - $1 \leq Y < 2$: infinite activity, infinite variation, convergence may slow

- **Typical $N$:** 128 for $Y < 1$; may need 256--512 for $Y$ near 2.

!!! warning "Branch Cuts in CGMY CF"
    The complex powers $(M - iu)^Y$ and $(G + iu)^Y$ require careful branch selection when $Y$ is non-integer. Use the principal branch of the complex logarithm: $(z)^Y = \exp(Y\ln z)$ with $\ln z = \ln|z| + i\arg(z)$, $\arg(z) \in (-\pi, \pi]$.

---

## Normal Inverse Gaussian Model

The Normal Inverse Gaussian (NIG) model (Barndorff-Nielsen, 1998) is a special case of the generalized hyperbolic distribution and produces a flexible density with semi-heavy tails.

!!! note "Definition: NIG Process"
    The NIG process has characteristic function:

    $$
    \phi_{\text{NIG}}(u) = \exp\!\left(iu(r - q + \omega)T + \delta T\left(\sqrt{\alpha^2 - \beta^2} - \sqrt{\alpha^2 - (\beta + iu)^2}\right)\right)
    $$

    where $\alpha > 0$ (tail heaviness), $\beta \in (-\alpha, \alpha)$ (asymmetry), $\delta > 0$ (scale), and $\omega = \delta(\sqrt{\alpha^2 - (\beta+1)^2} - \sqrt{\alpha^2 - \beta^2})$.

**COS considerations:**

- **Cumulants:**
    - $c_2 = \delta T \alpha^2 / (\alpha^2 - \beta^2)^{3/2}$
    - $c_3 = 3\delta T \alpha^2 \beta / (\alpha^2 - \beta^2)^{5/2}$
    - $c_4 = 3\delta T \alpha^2(4\beta^2 + \alpha^2) / (\alpha^2 - \beta^2)^{7/2}$
- **Convergence:** Exponential. The NIG density is $C^\infty$ with exponential tails.
- **Typical $N$:** 128.

---

## Comparative Summary

| Model | CF complexity | Convergence rate | Typical $N$ | Special considerations |
|---|---|---|---|---|
| Heston | Riccati ODE solution | Exponential | 64--128 | Branch cut in $d$ |
| Bates | Heston + jump factor | Exponential | 64--128 | Same as Heston |
| Variance Gamma | Closed-form | Exponential | 128--256 | Peaked density, wider $[a,b]$ |
| CGMY ($Y < 1$) | Closed-form with $\Gamma(-Y)$ | Exponential | 128--256 | Branch cut in complex powers |
| CGMY ($Y \geq 1$) | Same | Slower than exponential | 256--512 | May need filtering |
| NIG | Closed-form | Exponential | 128 | Complex square root |

---

## Implementation Pattern

The model-agnostic nature of COS allows a clean software architecture:

!!! tip "Software Design"
    A generic COS pricer takes a characteristic function as input (a callable), plus the truncation parameters. Model-specific code is isolated to:

    1. A function that evaluates $\phi(u)$ given model parameters
    2. A function that computes cumulants $c_1, \ldots, c_4$ given model parameters

    Everything else (payoff coefficients, summation, truncation interval) is shared across all models. This separation simplifies testing, validation, and the addition of new models.

---

## Example: VG Option Pricing via COS

!!! example "Variance Gamma Call Price"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.05$, $T = 1$, $\sigma = 0.12$, $\theta = -0.14$, $\nu = 0.2$.

    Cumulants: $c_1 \approx 0.0465$, $c_2 \approx 0.0183$, $c_3 \approx -0.0019$, $c_4 \approx 0.0004$.

    Truncation: $[a, b] \approx [-1.5, 1.6]$ with $L = 12$.

    COS price with $N = 128$: $V_{\text{COS}} = 6.2341$ (to 4 decimal places), agreeing with FFT-based VG pricing to $10^{-8}$.

    The negative $\theta$ produces a negatively skewed density, consistent with the implied volatility skew.

---

## Summary

The COS method extends to any model with a known characteristic function:

| Requirement | How it is satisfied |
|---|---|
| Characteristic function | Closed-form for affine and Levy models |
| Cumulants for truncation | Computed from derivatives of $\ln\phi$ at $u = 0$ |
| Smoothness for convergence | Most financial densities are $C^\infty$ or analytic |
| Implementation | Only $\phi(u)$ and cumulants are model-specific |

**The COS method's model-agnostic architecture---requiring only the characteristic function as input---makes it a universal pricing engine for the entire family of affine and Levy models, with exponential convergence guaranteed whenever the risk-neutral density is smooth.**

---

## Exercises

**Exercise 1.** The Bates characteristic function is $\phi_{\text{Bates}}(u) = \phi_{\text{Heston}}(u)\cdot\exp(\lambda T[e^{i\mu_J u - \sigma_J^2 u^2/2} - 1 - i\bar{\mu}u])$. For $\lambda = 0.5$, $\mu_J = -0.1$, $\sigma_J = 0.15$, and $T = 1$, compute the jump compensator $\bar{\mu} = e^{\mu_J + \sigma_J^2/2} - 1$ and evaluate the jump factor at $u = 0$, $u = 1$, and $u = 10$. Verify that $\phi_{\text{Bates}}(0) = 1$.

---

**Exercise 2.** For the Variance Gamma model, compute the four cumulants using the formulas given in the text with parameters $\sigma = 0.12$, $\theta = -0.14$, $\nu = 0.2$, $r = 0.05$, $T = 1$. Compare $c_2$ and $c_4$ to those of a Gaussian with the same variance. How much wider is the cumulant-based truncation interval for VG compared to Black-Scholes?

---

**Exercise 3.** The CGMY characteristic function involves the complex power $(M - iu)^Y$. For $M = 10$ and $Y = 0.5$, evaluate $(M - iu)^Y$ at $u = 0, 5, 20$ using the principal branch $z^Y = \exp(Y\ln|z| + iY\arg(z))$. Explain why careful branch selection is important and what error arises from using the wrong branch.

---

**Exercise 4.** The convergence rate of the COS method for CGMY depends on the parameter $Y$. Explain why $Y < 1$ (finite variation) gives exponential convergence while $Y \geq 1$ (infinite variation) can produce slower convergence. Relate this to the smoothness of the CGMY density and the decay rate of $|\phi_{\text{CGMY}}(u)|$ for large $|u|$.

---

**Exercise 5.** The NIG characteristic function involves $\sqrt{\alpha^2 - (\beta + iu)^2}$. For $\alpha = 15$, $\beta = -5$, compute this square root at $u = 0$ and $u = 10$. Verify that the Feller condition $\alpha > |\beta|$ ensures the square root is real at $u = 0$, and explain what happens when $u$ is large enough that $\alpha^2 - (\beta + iu)^2$ has negative real part.

---

**Exercise 6.** Design a software architecture for a generic COS pricer. The pricer should accept as input: (a) a callable $\phi(u)$ that evaluates the characteristic function, (b) a callable that returns cumulants $c_1, \ldots, c_4$, (c) the payoff type (call/put), (d) the option parameters ($K$, $r$, $T$). Describe the steps of the algorithm and explain which parts are model-specific and which are model-independent. How would you add a new model (e.g., NIG) to this framework?
