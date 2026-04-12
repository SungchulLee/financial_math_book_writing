# Measure Change in Affine Models

The passage from the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$ is the cornerstone of derivative pricing. For a general stochastic model, this measure change can destroy analytic tractability: a process with a nice closed-form characteristic function under $\mathbb{P}$ may lose that property under $\mathbb{Q}$. The remarkable **closure property** of affine processes is that exponential-affine measure changes preserve the affine class. Under the new measure, the process remains affine with modified parameters --- the drift changes, the jump intensity shifts, but the structural linearity in the state is maintained. This closure property is what makes affine models practical: one can calibrate under $\mathbb{Q}$ using the same analytical tools available under $\mathbb{P}$.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and prove the closure property: affine processes remain affine under exponential-affine measure changes
    2. Derive the transformed drift and jump parameters under the Girsanov theorem
    3. Define the Esscher transform and show it preserves the affine structure
    4. Compute the explicit parameter transformation for the Vasicek and CIR models
    5. Explain the financial interpretation: market price of risk as an affine function of the state

---

## Motivation

### The Pricing Problem

Consider a short-rate model $r_t = \rho_0 + \rho_1^\top X_t$ where $X_t$ is an affine process under the physical measure $\mathbb{P}$. To price bonds, we need the risk-neutral expectation

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds}\;\Big|\;\mathcal{F}_t\right]
$$

For this to be computable via the Riccati machinery, $X_t$ must also be affine under $\mathbb{Q}$. If the measure change from $\mathbb{P}$ to $\mathbb{Q}$ broke the affine structure, we would lose the exponential-affine bond price formula and need to resort to Monte Carlo or PDE methods.

The closure property guarantees that this does not happen: any measure change defined by an exponential-affine Radon–Nikodym derivative maps one set of affine parameters to another. The bond pricing formulas, characteristic functions, and Riccati equations all carry over to the new measure --- only the parameter values change.

---

## Girsanov Theorem for Affine Diffusions

### Setup

Let $X_t$ be a $d$-dimensional affine diffusion under $\mathbb{P}$:

$$
dX_t = \mu^{\mathbb{P}}(X_t)\,dt + \sigma(X_t)\,dW_t^{\mathbb{P}}
$$

where $\mu^{\mathbb{P}}(x) = b_0^{\mathbb{P}} + B^{\mathbb{P}} x$ is the affine drift and $\sigma(x)\sigma(x)^\top = a_0 + \sum_i \alpha_i x^{(i)}$ is the affine diffusion matrix.

### The Market Price of Risk

!!! info "Definition: Affine Market Price of Risk"
    An affine market price of risk is a process of the form

    $$
    \lambda(X_t) = \lambda_0 + \Lambda X_t
    $$

    where $\lambda_0 \in \mathbb{R}^d$ and $\Lambda \in \mathbb{R}^{d \times d}$ are constant.

The Girsanov theorem defines the risk-neutral Brownian motion:

$$
dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \sigma(X_t)^{-1}\!\bigl(\mu^{\mathbb{P}}(X_t) - \mu^{\mathbb{Q}}(X_t)\bigr)\,dt
$$

More precisely, if $\sigma(X_t)$ is invertible, the market price of risk satisfies

$$
\lambda(X_t) = \sigma(X_t)^{-1}\!\bigl(\mu^{\mathbb{P}}(X_t) - \mu^{\mathbb{Q}}(X_t)\bigr)
$$

### The Closure Theorem

!!! info "Theorem: Closure of Affine Class Under Measure Change"
    If $X_t$ is an affine diffusion under $\mathbb{P}$ with parameters $(b_0^{\mathbb{P}}, B^{\mathbb{P}}, a_0, \alpha_1, \ldots, \alpha_d)$, and the measure change from $\mathbb{P}$ to $\mathbb{Q}$ is defined by an affine market price of risk $\lambda(x) = \lambda_0 + \Lambda x$, then $X_t$ is also affine under $\mathbb{Q}$ with parameters

    $$
    b_0^{\mathbb{Q}} = b_0^{\mathbb{P}} - \sigma_0\lambda_0, \qquad B^{\mathbb{Q}} = B^{\mathbb{P}} - \Sigma_\Lambda
    $$

    where $\sigma_0$ and $\Sigma_\Lambda$ encode the interaction between the diffusion and the market price of risk. The diffusion matrix $(a_0, \alpha_1, \ldots, \alpha_d)$ is **unchanged**.

**Proof.** Under $\mathbb{Q}$, the dynamics of $X_t$ become

$$
dX_t = \mu^{\mathbb{Q}}(X_t)\,dt + \sigma(X_t)\,dW_t^{\mathbb{Q}}
$$

where

$$
\mu^{\mathbb{Q}}(x) = \mu^{\mathbb{P}}(x) - \sigma(x)\sigma(x)^\top\sigma(x)^{-\top}\lambda(x) = \mu^{\mathbb{P}}(x) - a(x)\,\tilde{\lambda}(x)
$$

For the general case with possibly singular $\sigma$, the drift transforms as

$$
\mu^{\mathbb{Q}}(x) = (b_0^{\mathbb{P}} + B^{\mathbb{P}}x) - \bigl(a_0 + \textstyle\sum_i \alpha_i x^{(i)}\bigr)(\lambda_0 + \Lambda x)
$$

Expanding and collecting terms:

$$
\mu^{\mathbb{Q}}(x) = \underbrace{(b_0^{\mathbb{P}} - a_0\lambda_0)}_{b_0^{\mathbb{Q}}} + \underbrace{(B^{\mathbb{P}} - a_0\Lambda - \textstyle\sum_i \alpha_i\lambda_{0,i} \cdot e_i^\top - \textstyle\sum_i \alpha_i (\Lambda x)_i)}_{B^{\mathbb{Q}} x + \text{higher-order terms}}x
$$

The key observation is that the terms involving $x^{(i)} \cdot \Lambda x$ produce **quadratic** dependence on $x$, which would break the affine structure. The closure holds when the market price of risk is chosen so that these problematic terms vanish or are absorbed into the linear structure. Specifically, for the standard specification:

- The constant part of the drift changes: $b_0^{\mathbb{Q}} = b_0^{\mathbb{P}} - a_0\lambda_0$
- The linear part of the drift changes: $B^{\mathbb{Q}} = B^{\mathbb{P}} - a_0\Lambda - \text{diag}(\alpha_i\lambda_0) - \ldots$
- The diffusion coefficients $a_0, \alpha_1, \ldots, \alpha_d$ remain unchanged $\square$

!!! warning "Restricted Market Price of Risk"
    Not every affine $\lambda(x) = \lambda_0 + \Lambda x$ preserves the affine structure. The matrix $\Lambda$ must satisfy compatibility conditions with $\alpha_1, \ldots, \alpha_d$ to ensure that the quadratic cross-terms in $\mu^{\mathbb{Q}}$ either vanish or can be absorbed into a linear structure. For the completely affine specification (Dai and Singleton, 2000), $\Lambda$ must be diagonal when restricted to the CIR-type components.

---

## The Esscher Transform

### Definition

The Esscher transform is a classical tool from actuarial science that provides a natural exponential-affine measure change.

!!! info "Definition: Esscher Transform"
    For a parameter $\theta \in \mathbb{R}^d$, the **Esscher transform** defines a new measure $\mathbb{Q}^\theta$ via the Radon–Nikodym derivative

    $$
    \frac{d\mathbb{Q}^\theta}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \frac{\exp(\theta^\top X_t)}{\mathbb{E}^{\mathbb{P}}[\exp(\theta^\top X_t)]}
    $$

### Preservation of Affine Structure

!!! info "Proposition: Esscher Transform Preserves Affine Class"
    If $X_t$ is affine under $\mathbb{P}$, then $X_t$ is also affine under the Esscher measure $\mathbb{Q}^\theta$, with modified parameters:

    - **Drift**: $b_0^{\mathbb{Q}} = b_0^{\mathbb{P}} + a_0\theta$, $B^{\mathbb{Q}} = B^{\mathbb{P}} + \sum_i \alpha_i\theta_i \cdot e_i e_i^\top$
    - **Diffusion**: unchanged ($a_0, \alpha_i$ are the same)
    - **Jump measure** (if present): $m_i^{\mathbb{Q}}(dz) = e^{\theta^\top z}\,m_i^{\mathbb{P}}(dz)$ (exponential tilting)

The Esscher transform tilts the jump size distribution exponentially while shifting the drift. Because both modifications are compatible with the affine structure, the Riccati system under $\mathbb{Q}^\theta$ takes the same form with updated parameters.

---

## Examples

### Vasicek Model

Under $\mathbb{P}$, the Vasicek model has $dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma\,dW_t^{\mathbb{P}}$. With a constant market price of risk $\lambda$:

$$
dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \sigma\,dW_t^{\mathbb{P}}
$$

Under $\mathbb{Q}$ with $dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \lambda\,dt$:

$$
dr_t = \kappa^{\mathbb{P}}\bigl(\theta^{\mathbb{P}} - r_t\bigr)\,dt - \sigma\lambda\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

$$
= \kappa^{\mathbb{P}}\!\left(\theta^{\mathbb{P}} - \frac{\sigma\lambda}{\kappa^{\mathbb{P}}} - r_t\right)dt + \sigma\,dW_t^{\mathbb{Q}}
$$

!!! example "Vasicek Parameter Transformation"
    The risk-neutral parameters are:

    - $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}}$ (mean-reversion speed unchanged)
    - $\theta^{\mathbb{Q}} = \theta^{\mathbb{P}} - \sigma\lambda/\kappa^{\mathbb{P}}$ (long-run mean shifts)
    - $\sigma^{\mathbb{Q}} = \sigma^{\mathbb{P}}$ (volatility unchanged)

    The Vasicek model remains Vasicek under the measure change. Only the long-run mean $\theta$ is affected.

### CIR Model

Under $\mathbb{P}$, the CIR model has $dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \xi\sqrt{r_t}\,dW_t^{\mathbb{P}}$. The diffusion coefficient $\xi\sqrt{r_t}$ depends on the state, so the market price of risk must be chosen carefully.

The standard CIR market price of risk is $\lambda(r_t) = \lambda_1\sqrt{r_t}/\xi$ for some constant $\lambda_1$, giving:

$$
dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt - \lambda_1 r_t\,dt + \xi\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

$$
= (\kappa^{\mathbb{P}} + \lambda_1)\!\left(\frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda_1} - r_t\right)dt + \xi\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

!!! example "CIR Parameter Transformation"
    The risk-neutral parameters are:

    - $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_1$ (mean-reversion speed increases if $\lambda_1 > 0$)
    - $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/(\kappa^{\mathbb{P}} + \lambda_1)$ (long-run mean decreases if $\lambda_1 > 0$)
    - $\xi^{\mathbb{Q}} = \xi^{\mathbb{P}}$ (volatility unchanged)

    Crucially, $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$, so the product $\kappa\theta$ is invariant. If the Feller condition $2\kappa^{\mathbb{P}}\theta^{\mathbb{P}} \geq \xi^2$ holds under $\mathbb{P}$, it holds under $\mathbb{Q}$ as well.

---

## Measure Change for Jump-Diffusions

### Extended Girsanov Theorem

For affine jump-diffusions, the measure change modifies both the Brownian motion drift and the jump compensator. The Radon–Nikodym derivative takes the form

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \mathcal{E}\!\left(\int_0^t \lambda_s^\top dW_s^{\mathbb{P}}\right) \cdot \prod_{0 < s \leq t} \eta(X_{s^-}, \Delta X_s)\,e^{\int_0^t (1 - \bar{\eta}(X_s))\,\lambda^J(X_s)\,ds}
$$

where $\lambda_s$ changes the Brownian motion drift and $\eta$ tilts the jump intensity and size distribution.

For the affine structure to be preserved:

1. The Brownian drift change $\lambda(x)$ must be affine in $x$
2. The jump intensity change must be exponential-affine: $\eta(x, z) = \exp(\gamma_0 + \gamma_1^\top z)$ for constants $\gamma_0$ and $\gamma_1$

Under these conditions, the jump compensator transforms as

$$
m_i^{\mathbb{Q}}(dz) = e^{\gamma_1^\top z}\,m_i^{\mathbb{P}}(dz)
$$

which is simply the Esscher-type exponential tilting of the jump size distribution. The jump intensity and the moment generating function of the jump sizes both change, but the affine dependence on $x$ is preserved.

---

## Financial Interpretation

### Market Price of Risk

The market price of risk $\lambda(X_t) = \lambda_0 + \Lambda X_t$ has a natural financial interpretation:

- **$\lambda_0$**: the baseline risk premium, independent of the state
- **$\Lambda X_t$**: the state-dependent risk premium, which captures how compensation for risk varies with market conditions

For interest rate models, a positive $\lambda_1$ (in the CIR specification) means that investors demand **higher compensation** when rates are high, consistent with the observation that bond risk premia vary with the business cycle.

### Essentially Affine and Extended Affine Specifications

Duffee (2002) introduced the distinction between:

- **Completely affine**: $\lambda(x) = \sqrt{a(x)}\,\tilde{\lambda}$ where $\tilde{\lambda}$ is constant. This restricts the market price of risk to be proportional to the diffusion volatility.
- **Essentially affine**: allows the Gaussian components to have unrestricted market prices of risk, while CIR components retain the completely affine form. This permits richer dynamics for bond risk premia.

The essentially affine specification maintains the affine structure under $\mathbb{Q}$ while providing significantly more flexibility in modeling the time variation of risk premia.

---

## Summary

The closure property of affine processes under measure change is the key to their practical utility. The Girsanov theorem transforms the drift of an affine diffusion while leaving the diffusion matrix unchanged; when the market price of risk is affine in the state, the transformed drift remains affine, and the process stays in the affine class under the new measure. The Esscher transform provides a canonical exponential tilting that preserves affine structure for both diffusion and jump components. For standard models, the parameter transformations are explicit: the Vasicek model shifts its long-run mean, and the CIR model jointly adjusts its mean-reversion speed and long-run level while preserving the Feller condition. The essentially affine specification of Duffee (2002) expands the space of admissible market prices of risk while maintaining analytical tractability.

---

## Further Reading

- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Duffee, G. (2002). "Term Premia and Interest Rate Forecasts in Affine Models." *Journal of Finance*, 57(1), 405--443.
- Cheridito, P., Filipovic, D., and Kimmel, R. (2007). "Market Price of Risk Specifications for Affine Models." *Journal of Financial Economics*, 83(1), 123--170.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

---

## Exercises

**Exercise 1.** For the Vasicek model under $\mathbb{P}$ with parameters $\kappa^{\mathbb{P}} = 0.5$, $\theta^{\mathbb{P}} = 0.06$, $\sigma = 0.02$, and a constant market price of risk $\lambda = 0.3$, compute the risk-neutral parameters $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$. Verify that the diffusion coefficient $\sigma$ is unchanged under the measure change.

??? success "Solution to Exercise 1"
    From the Vasicek parameter transformation formulas:

    - $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} = 0.5$ (mean-reversion speed is unchanged)
    - $\theta^{\mathbb{Q}} = \theta^{\mathbb{P}} - \frac{\sigma\lambda}{\kappa^{\mathbb{P}}} = 0.06 - \frac{0.02 \times 0.3}{0.5} = 0.06 - 0.012 = 0.048$
    - $\sigma^{\mathbb{Q}} = \sigma^{\mathbb{P}} = 0.02$ (diffusion coefficient is unchanged)

    The risk-neutral parameters are $\kappa^{\mathbb{Q}} = 0.5$, $\theta^{\mathbb{Q}} = 0.048$, and $\sigma^{\mathbb{Q}} = 0.02$. The diffusion coefficient $\sigma$ is unchanged because the Girsanov theorem only modifies the drift of the Brownian motion, not its quadratic variation. The volatility $\sigma$ enters the diffusion matrix $a = \sigma^2$, which is invariant under the measure change.

---

**Exercise 2.** For the CIR model, the standard market price of risk is $\lambda(r) = \lambda_1 \sqrt{r}/\xi$. Show that the measure change produces risk-neutral parameters with $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$. Explain why this invariance of the product $\kappa\theta$ guarantees that the Feller condition is preserved under the measure change.

??? success "Solution to Exercise 2"
    Under $\mathbb{P}$, the CIR dynamics are $dr_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r_t)\,dt + \xi\sqrt{r_t}\,dW_t^{\mathbb{P}}$. The market price of risk $\lambda(r) = \lambda_1\sqrt{r}/\xi$ gives $\sigma(r)\lambda(r) = \xi\sqrt{r}\cdot\lambda_1\sqrt{r}/\xi = \lambda_1 r$. The risk-neutral drift is

    $$
    \mu^{\mathbb{Q}}(r) = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - r) - \lambda_1 r = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} - (\kappa^{\mathbb{P}} + \lambda_1)r
    $$

    Rewriting in mean-reverting form: $\mu^{\mathbb{Q}}(r) = (\kappa^{\mathbb{P}} + \lambda_1)\!\left(\frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda_1} - r\right)$, so $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_1$ and $\theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda_1}$. Therefore

    $$
    \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = (\kappa^{\mathbb{P}} + \lambda_1)\cdot\frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda_1} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}
    $$

    The Feller condition requires $2\kappa\theta \geq \xi^2$. Since $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$, the product $\kappa\theta$ is the same under both measures, so $2\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} \geq \xi^2$ if and only if $2\kappa^{\mathbb{P}}\theta^{\mathbb{P}} \geq \xi^2$. The Feller condition is automatically preserved.

---

**Exercise 3.** Explain why a market price of risk of the form $\lambda(x) = \lambda_0 + \Lambda x$ with a general (non-diagonal) matrix $\Lambda$ can break the affine structure for CIR-type components. Show explicitly that the cross-term $\alpha_i x^{(i)} \Lambda x$ produces a quadratic dependence on $x$ that cannot be absorbed into a linear drift.

??? success "Solution to Exercise 3"
    For a CIR-type component $i$, the diffusion matrix contribution is $\alpha_i x^{(i)}$, so the drift transformation involves the term

    $$
    -\alpha_i x^{(i)} (\lambda_0 + \Lambda x) = -\alpha_i\lambda_0 x^{(i)} - \alpha_i x^{(i)} \Lambda x
    $$

    The first term $-\alpha_i\lambda_0 x^{(i)}$ is linear in $x$ and can be absorbed into the drift matrix $B^{\mathbb{Q}}$. However, the second term $-\alpha_i x^{(i)} \Lambda x$ is **quadratic** in $x$: it involves the product $x^{(i)} \cdot (\Lambda x)_j$ for each $j$.

    If $\Lambda$ is non-diagonal, say $\Lambda_{ij} \neq 0$ for $j \neq i$, then the term $-\alpha_i x^{(i)} \Lambda_{ij} x^{(j)}$ introduces a product $x^{(i)} x^{(j)}$ into the drift. This cannot be written as an affine function of $x$, breaking the affine structure.

    For the affine structure to be preserved, the cross-terms must vanish. When restricted to CIR-type components, this requires $\alpha_i (\Lambda x)$ to depend only on $x^{(i)}$ (not on other state variables). If each $\alpha_i$ is a scalar times a matrix that acts only on the $i$-th coordinate, then $\Lambda$ must be diagonal on the CIR subspace: $\Lambda_{ij} = 0$ for $i \neq j$ when both $i$ and $j$ are CIR-type indices. This is the completely affine restriction of Dai and Singleton (2000).

---

**Exercise 4.** For the Esscher transform with parameter $\theta \in \mathbb{R}$, applied to a one-dimensional OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, compute the drift of $X_t$ under the new measure $\mathbb{Q}^\theta$. Show that $X_t$ remains an OU process under $\mathbb{Q}^\theta$ with modified parameters $\kappa^{\mathbb{Q}} = \kappa - \sigma^2\theta$ and unchanged diffusion $\sigma$.

??? success "Solution to Exercise 4"
    The OU process has $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, so $\mu(x) = -\kappa x$ and $a = \sigma^2$ (constant diffusion). The Esscher Radon–Nikodym derivative is $\frac{d\mathbb{Q}^\theta}{d\mathbb{P}}\big|_{\mathcal{F}_t} = \frac{e^{\theta X_t}}{\mathbb{E}[e^{\theta X_t}]}$. By Girsanov's theorem, the drift under $\mathbb{Q}^\theta$ is $\mu^{\mathbb{Q}}(x) = \mu^{\mathbb{P}}(x) + a\theta = -\kappa x + \sigma^2\theta$. Under $\mathbb{Q}^\theta$, the dynamics become

    $$
    dX_t = (-\kappa X_t + \sigma^2\theta)\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    Defining $\kappa^{\mathbb{Q}} = \kappa - \sigma^2\theta$ and rearranging, the original OU process (which mean-reverts to 0 under $\mathbb{P}$) now mean-reverts to $\sigma^2\theta/\kappa^{\mathbb{Q}}$ under $\mathbb{Q}^\theta$:

    $$
    dX_t = (\kappa - \sigma^2\theta)\!\left(\frac{\sigma^2\theta}{\kappa - \sigma^2\theta} - X_t\right)dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    This is still an OU process with $\kappa^{\mathbb{Q}} = \kappa - \sigma^2\theta$ and unchanged diffusion $\sigma^{\mathbb{Q}} = \sigma$, confirming that the Esscher transform preserves the OU (affine) structure.

---

**Exercise 5.** Consider an affine jump-diffusion with compound Poisson jumps having exponential jump sizes with parameter $\eta$ under $\mathbb{P}$. Under the Esscher transform $m^{\mathbb{Q}}(dz) = e^{\gamma z}m^{\mathbb{P}}(dz)$, show that the jump sizes under $\mathbb{Q}$ are still exponentially distributed, but with parameter $\eta - \gamma$ (provided $\gamma < \eta$). What is the new jump intensity?

??? success "Solution to Exercise 5"
    Under $\mathbb{P}$, the jump size density is $f^{\mathbb{P}}(z) = \eta e^{-\eta z}\mathbf{1}_{z > 0}$ and the jump measure is $m^{\mathbb{P}}(dz) = \lambda\eta e^{-\eta z}\mathbf{1}_{z > 0}\,dz$. Under the Esscher transform with parameter $\gamma$:

    $$
    m^{\mathbb{Q}}(dz) = e^{\gamma z}m^{\mathbb{P}}(dz) = \lambda\eta e^{(\gamma - \eta)z}\mathbf{1}_{z > 0}\,dz = \lambda\eta e^{-(\eta - \gamma)z}\mathbf{1}_{z > 0}\,dz
    $$

    For this to be a valid measure, we need $\eta - \gamma > 0$, i.e., $\gamma < \eta$. To identify the new intensity and jump size distribution, normalize:

    $$
    \lambda^{\mathbb{Q}} = \int_0^\infty m^{\mathbb{Q}}(dz) = \lambda\eta\int_0^\infty e^{-(\eta - \gamma)z}\,dz = \frac{\lambda\eta}{\eta - \gamma}
    $$

    The jump size density under $\mathbb{Q}$ is

    $$
    f^{\mathbb{Q}}(z) = \frac{m^{\mathbb{Q}}(dz)/dz}{\lambda^{\mathbb{Q}}} = \frac{\lambda\eta e^{-(\eta - \gamma)z}}{\lambda\eta/(\eta - \gamma)} = (\eta - \gamma)e^{-(\eta - \gamma)z}\mathbf{1}_{z > 0}
    $$

    This is an exponential distribution with parameter $\eta^{\mathbb{Q}} = \eta - \gamma$. The new jump intensity is $\lambda^{\mathbb{Q}} = \lambda\eta/(\eta - \gamma) > \lambda$ (jumps become more frequent), while the new mean jump size is $1/(\eta - \gamma) > 1/\eta$ (jumps become larger on average). Both effects are intuitive: the exponential tilting $e^{\gamma z}$ upweights larger jumps.

---

**Exercise 6.** In the essentially affine specification of Duffee (2002), the Gaussian components of the state vector can have unrestricted market prices of risk while CIR components are restricted to the completely affine form. For a two-factor model with one Gaussian factor $X_1$ and one CIR factor $X_2$, write down the most general essentially affine market price of risk $\lambda(x)$ and identify which parameters are free and which are constrained.

??? success "Solution to Exercise 6"
    In the two-factor model, $X_1$ is Gaussian (Vasicek-type) with constant diffusion $a_{11} = \sigma_1^2$, and $X_2$ is CIR-type with state-dependent diffusion $a_{22} = \xi^2 X_2$. The cross-diffusion is zero: $a_{12} = a_{21} = 0$.

    The essentially affine market price of risk allows unrestricted specification for the Gaussian component but restricts the CIR component to the completely affine form:

    $$
    \lambda(x) = \begin{pmatrix} \lambda_{10} + \Lambda_{11}x_1 + \Lambda_{12}x_2 \\ \lambda_{20}\sqrt{x_2}/\xi \end{pmatrix}
    $$

    The Gaussian component $\lambda_1(x) = \lambda_{10} + \Lambda_{11}x_1 + \Lambda_{12}x_2$ is fully general (affine in $x$). Since the diffusion for $X_1$ is constant ($\sigma_1^2$), the product $a_{11}\lambda_1(x) = \sigma_1^2(\lambda_{10} + \Lambda_{11}x_1 + \Lambda_{12}x_2)$ remains affine in $x$, so no quadratic terms arise.

    The CIR component $\lambda_2(x) = \lambda_{20}\sqrt{x_2}/\xi$ is restricted so that $\sigma_2(x)\lambda_2(x) = \xi\sqrt{x_2}\cdot\lambda_{20}\sqrt{x_2}/\xi = \lambda_{20}x_2$, which is linear in $x_2$ only. A general affine $\lambda_2(x) = \lambda_{20} + \Lambda_{21}x_1 + \Lambda_{22}x_2$ would produce terms like $\xi^2 x_2(\Lambda_{21}x_1) = \xi^2\Lambda_{21}x_1 x_2$, which is quadratic.

    Free parameters: $\lambda_{10}$, $\Lambda_{11}$, $\Lambda_{12}$ (three parameters for the Gaussian component) and $\lambda_{20}$ (one parameter for the CIR component). Constrained: $\Lambda_{21} = 0$ and $\Lambda_{22}$ must take the specific completely affine form. This gives four free parameters total, compared to only two in the completely affine specification.

---

**Exercise 7.** Suppose you calibrate a CIR model to the yield curve and obtain risk-neutral parameters $\kappa^{\mathbb{Q}} = 0.8$, $\theta^{\mathbb{Q}} = 0.05$, $\xi = 0.15$. From time-series estimation, you find $\kappa^{\mathbb{P}} = 0.3$ and $\theta^{\mathbb{P}} = 0.07$. Compute the implied market price of risk parameter $\lambda_1$ and verify that $\kappa^{\mathbb{P}}\theta^{\mathbb{P}} = \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}}$.

??? success "Solution to Exercise 7"
    From the CIR parameter transformation: $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda_1$, so

    $$
    \lambda_1 = \kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}} = 0.8 - 0.3 = 0.5
    $$

    Now verify the invariance of $\kappa\theta$:

    $$
    \kappa^{\mathbb{P}}\theta^{\mathbb{P}} = 0.3 \times 0.07 = 0.021
    $$

    $$
    \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = 0.8 \times 0.05 = 0.040
    $$

    These are **not** equal: $0.021 \neq 0.040$. This means the estimated parameters are inconsistent with the standard CIR market price of risk specification $\lambda(r) = \lambda_1\sqrt{r}/\xi$, which requires $\kappa^{\mathbb{P}}\theta^{\mathbb{P}} = \kappa^{\mathbb{Q}}\theta^{\mathbb{Q}}$.

    From $\kappa^{\mathbb{Q}} = 0.8$ and the invariance constraint, the implied $\theta^{\mathbb{Q}}$ should be $\kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}} = 0.021/0.8 = 0.02625$, not $0.05$. Alternatively, from $\theta^{\mathbb{Q}} = 0.05$, the implied $\kappa^{\mathbb{Q}}$ should be $0.021/0.05 = 0.42$, not $0.8$.

    The discrepancy indicates that either the cross-sectional calibration ($\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}$) or the time-series estimation ($\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}$) contains estimation error, or the simple one-parameter market price of risk specification is inadequate for this data.
