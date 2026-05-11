# The Cox-Ingersoll-Ross (CIR) Model

The Cox-Ingersoll-Ross model (1985) is a mean-reverting short-rate model with **square-root volatility**. Unlike Vasicek, the CIR model can ensure non-negative interest rates under appropriate parameter conditions, while retaining analytical tractability.

---

## Model Specification

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$, the short rate follows:

$$
dr_t = \kappa(\theta - r_t) \, dt + \sigma \sqrt{r_t} \, dW_t^{\mathbb{Q}}
$$

where:

- $\kappa > 0$: mean-reversion speed
- $\theta > 0$: long-run mean level
- $\sigma > 0$: volatility parameter
- $W_t^{\mathbb{Q}}$: standard Brownian motion under $\mathbb{Q}$

### Key Difference from Vasicek

| Feature | Vasicek | CIR |
|---------|---------|-----|
| Volatility | $\sigma$ (constant) | $\sigma\sqrt{r_t}$ (state-dependent) |
| Rate distribution | Gaussian | Non-central chi-squared |
| Negative rates | Possible | Prevented (under Feller condition) |

---

## The Feller Condition

### Statement

The **Feller condition** is:

$$
\boxed{2\kappa\theta \geq \sigma^2}
$$

### Boundary Behavior

The behavior at $r = 0$ depends on the Feller condition:

| Condition | Behavior at $r = 0$ |
|-----------|---------------------|
| $2\kappa\theta \geq \sigma^2$ | $r = 0$ is **inaccessible**; rates stay strictly positive |
| $2\kappa\theta < \sigma^2$ | $r = 0$ is **attainable** but instantaneously reflecting |

In both cases, $r_t \geq 0$ for all $t$.

### Intuition

- The drift $\kappa(\theta - r_t)$ pushes $r_t$ toward $\theta > 0$
- Near $r = 0$, volatility $\sigma\sqrt{r_t}$ becomes small
- The Feller condition ensures the drift dominates near zero

---

## Distribution of r_t

### Transition Density

Given $r_s$ at time $s < t$, the distribution of $r_t$ is:

$$
r_t \mid r_s \sim \frac{c}{2} \chi^2\left(\nu, \lambda\right)
$$

where:

- $c = \frac{4\kappa}{\sigma^2(1 - e^{-\kappa(t-s)})}$
- $\nu = \frac{4\kappa\theta}{\sigma^2}$ (degrees of freedom)
- $\lambda = c \cdot r_s e^{-\kappa(t-s)}$ (non-centrality parameter)
- $\chi^2(\nu, \lambda)$ is the **non-central chi-squared** distribution

### Moments

**Mean:**

$$
\mathbb{E}[r_t \mid r_s] = r_s e^{-\kappa(t-s)} + \theta(1 - e^{-\kappa(t-s)})
$$

This is identical to Vasicek!

**Variance:**

$$
\text{Var}(r_t \mid r_s) = r_s \frac{\sigma^2}{\kappa}(e^{-\kappa(t-s)} - e^{-2\kappa(t-s)}) + \frac{\theta\sigma^2}{2\kappa}(1 - e^{-\kappa(t-s)})^2
$$

Unlike Vasicek, variance depends on the current rate $r_s$.

### Stationary Distribution

As $t \to \infty$:

$$
r_\infty \sim \text{Gamma}\left(\frac{2\kappa\theta}{\sigma^2}, \frac{2\kappa}{\sigma^2}\right)
$$

with mean $\theta$ and variance $\frac{\theta\sigma^2}{2\kappa}$.

---

## Zero-Coupon Bond Pricing

### Affine Structure

Like Vasicek, CIR yields **exponential-affine** bond prices:

$$
\boxed{P(t, T) = A(\tau) \exp(-B(\tau) \cdot r_t)}
$$

where $\tau = T - t$.

### Key Parameter

Define:

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

### Solution for B(τ)

$$
\boxed{B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}}
$$

### Solution for A(τ)

$$
\boxed{A(\tau) = \left[\frac{2\gamma \exp\left(\frac{(\kappa + \gamma)\tau}{2}\right)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2}}
$$

### Derivation Outline

The bond pricing PDE is:

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 r \frac{\partial^2 P}{\partial r^2} = rP
$$

Using ansatz $P = A(\tau) e^{-B(\tau)r}$ leads to:

- Riccati ODE for $B(\tau)$: $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$
- Linear ODE for $\log A$: $(\log A)' = \kappa\theta B$

---

## Yield Curve Analysis

### Zero Rate

$$
z(t, T) = -\frac{\log P(t, T)}{\tau} = \frac{B(\tau)}{\tau} r_t - \frac{\log A(\tau)}{\tau}
$$

### Long-Term Yield

As $\tau \to \infty$:

$$
z_\infty = \frac{2\kappa\theta}{\gamma + \kappa}
$$

---

## Option Pricing

### Bond Options

A European call on a $T_2$-bond with strike $K$, expiring at $T_1$, has price involving the non-central chi-squared distribution:

$$
C = P(0, T_2) \cdot \chi^2_{2r^*(\phi + \psi + B)}(\nu, \lambda_1) - K P(0, T_1) \cdot \chi^2_{2r^*(\phi + \psi)}(\nu, \lambda_2)
$$

where the parameters are functions of model inputs and $r^*$ solves $P(T_1, T_2, r^*) = K$.

---

## Comparison: CIR vs. Vasicek

| Aspect | Vasicek | CIR |
|--------|---------|-----|
| SDE | $dr = \kappa(\theta-r)dt + \sigma dW$ | $dr = \kappa(\theta-r)dt + \sigma\sqrt{r}dW$ |
| Distribution | Gaussian | Non-central $\chi^2$ |
| Negative rates | Possible | No (if Feller holds) |
| $B(\tau)$ | $\frac{1-e^{-\kappa\tau}}{\kappa}$ | $\frac{2(e^{\gamma\tau}-1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ |
| Option pricing | Gaussian formulas | Non-central $\chi^2$ |
| Tractability | Very high | High |

---

## Strengths and Limitations

### Strengths

- **Non-negativity:** Rates remain non-negative (under Feller)
- **Analytical tractability:** Closed-form bond prices
- **Realistic volatility:** State-dependent volatility
- **Affine structure:** Efficient computation

### Limitations

- **Single factor:** Limited yield curve dynamics
- **Cannot fit arbitrary curves:** Pure CIR needs extension
- **Feller condition:** May be binding in low-rate environments

---

## Key Takeaways

- CIR: $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}dW_t$
- Feller condition $2\kappa\theta \geq \sigma^2$ ensures $r_t > 0$
- Distribution is non-central chi-squared
- Bond prices: $P = A(\tau)e^{-B(\tau)r}$ with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$

---

## Further Reading

- Cox, Ingersoll & Ross (1985), "A Theory of the Term Structure of Interest Rates"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3

---

## Exercises

**Exercise 1.** State the Feller condition $2\kappa\theta \ge \sigma^2$ for the CIR model and explain its financial significance. For $\kappa = 0.5$, $\theta = 0.04$, determine the maximum $\sigma$ for which the Feller condition holds.

??? success "Solution to Exercise 1"
    The **Feller condition** for the CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ is

    $$
    2\kappa\theta \geq \sigma^2
    $$

    **Financial significance.** When this condition holds, the origin $r = 0$ is an inaccessible boundary: the short rate remains strictly positive for all time. Near $r = 0$, the drift $\kappa\theta > 0$ pushes the rate upward, while the diffusion $\sigma\sqrt{r}$ shrinks to zero. The Feller condition ensures the inward drift dominates the outward diffusion sufficiently to prevent the process from reaching zero. This is essential in practice because negative or zero nominal rates have different economic interpretations, and the CIR model is often chosen precisely for this non-negativity guarantee.

    **Numerical calculation.** For $\kappa = 0.5$ and $\theta = 0.04$:

    $$
    2\kappa\theta = 2(0.5)(0.04) = 0.04
    $$

    The Feller condition requires $\sigma^2 \leq 0.04$, so

    $$
    \sigma \leq \sqrt{0.04} = 0.2
    $$

    The maximum volatility parameter for which the Feller condition holds is $\sigma_{\max} = 0.2$ (i.e., 20%).

---

---

**Exercise 2.** Show that the CIR bond price has the affine form $P(t,T) = e^{A(\tau) - B(\tau)r_t}$ by substituting into the term-structure PDE and deriving the Riccati equations for $A$ and $B$. State the boundary conditions $A(0) = 0$, $B(0) = 0$.

??? success "Solution to Exercise 2"
    The bond pricing PDE for the CIR model is

    $$
    \frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 r\frac{\partial^2 P}{\partial r^2} = rP
    $$

    with terminal condition $P(T,T,r) = 1$. Substituting the ansatz $P(t,T) = e^{A(\tau) - B(\tau)r}$ where $\tau = T - t$, we compute:

    $$
    \frac{\partial P}{\partial t} = (-A' + B'r)P, \quad \frac{\partial P}{\partial r} = -BP, \quad \frac{\partial^2 P}{\partial r^2} = B^2 P
    $$

    where primes denote derivatives with respect to $\tau$. Substituting and dividing by $P$:

    $$
    -A' + B'r - \kappa(\theta - r)B + \frac{1}{2}\sigma^2 r B^2 = r
    $$

    Collecting terms:

    - **Coefficient of $r$:** $B'(\tau) + \kappa B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 = 1$, i.e., $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$.
    - **Constant term:** $-A'(\tau) - \kappa\theta B(\tau) = 0$, i.e., $A'(\tau) = -\kappa\theta B(\tau)$, or equivalently $(\ln e^A)' = -\kappa\theta B$.

    The boundary conditions from $P(T,T) = 1$ give $e^{A(0) - B(0)r} = 1$ for all $r$, so $A(0) = 0$ and $B(0) = 0$.

    The $B$-equation is a Riccati ODE (quadratic in $B$), and the $A$-equation is a simple integral once $B$ is known. This confirms the affine structure. The PDE separates cleanly because the drift $\kappa(\theta - r)$ is affine in $r$ and the squared diffusion $\sigma^2 r$ is affine in $r$.

---

---

**Exercise 3.** Compare the CIR and Vasicek models: both are mean-reverting with the same drift structure. The key difference is the diffusion coefficient $\sigma\sqrt{r_t}$ versus $\sigma$. Explain how the square-root diffusion prevents negative rates (when the Feller condition holds) and how it affects the yield curve shape.

??? success "Solution to Exercise 3"
    Both models share the mean-reverting drift $\kappa(\theta - r_t)$. The crucial difference is the diffusion coefficient:

    - **Vasicek:** $\sigma(r) = \sigma$ (constant). The volatility does not depend on the level of $r_t$.
    - **CIR:** $\sigma(r) = \sigma\sqrt{r_t}$ (square-root). The volatility vanishes as $r_t \to 0$.

    **How square-root diffusion prevents negative rates.** As $r_t$ approaches zero from above:

    1. The diffusion $\sigma\sqrt{r_t} \to 0$, so random shocks become negligible.
    2. The drift $\kappa(\theta - r_t) \to \kappa\theta > 0$, providing a positive push away from zero.
    3. Under the Feller condition $2\kappa\theta \geq \sigma^2$, the deterministic drift dominates the stochastic fluctuations near zero, making $r = 0$ an inaccessible boundary.

    In Vasicek, the constant volatility $\sigma$ remains active even as $r_t$ approaches zero, and the Gaussian noise can push the rate below zero with positive probability.

    **Effect on yield curve shape.** In Vasicek, the long rate is $z_\infty = \theta - \sigma^2/(2\kappa^2)$, always below $\theta$ due to the convexity adjustment. In CIR, the long rate is $z_\infty = 2\kappa\theta/(\gamma + \kappa)$ where $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. The state-dependent volatility in CIR means that the convexity effect varies with the level of rates: high rates produce more volatility and a larger convexity correction, while low rates produce less. This makes the CIR yield curve shape more sensitive to the current rate level than Vasicek.

---

---

**Exercise 4.** The CIR transition density is a noncentral chi-squared distribution. For parameters $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.1$, $r_0 = 0.03$, $\Delta t = 0.25$, compute the degrees of freedom and noncentrality parameter. What is $\mathbb{E}[r_{\Delta t}]$ and $\text{Var}(r_{\Delta t})$?

??? success "Solution to Exercise 4"
    Given $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.1$, $r_0 = 0.03$, $\Delta t = 0.25$.

    The transition distribution is $r_{\Delta t} \mid r_0 \sim \frac{c}{2}\chi^2(\nu, \lambda)$ where:

    $$
    c = \frac{4\kappa}{\sigma^2(1 - e^{-\kappa \Delta t})} = \frac{4(0.3)}{0.01(1 - e^{-0.075})}
    $$

    Computing $e^{-0.075} \approx 0.92774$, so $1 - e^{-0.075} \approx 0.07226$:

    $$
    c = \frac{1.2}{0.01 \times 0.07226} = \frac{1.2}{0.0007226} \approx 1660.6
    $$

    **Degrees of freedom:**

    $$
    \nu = \frac{4\kappa\theta}{\sigma^2} = \frac{4(0.3)(0.05)}{0.01} = \frac{0.06}{0.01} = 6
    $$

    **Noncentrality parameter:**

    $$
    \lambda = c \cdot r_0 e^{-\kappa \Delta t} = 1660.6 \times 0.03 \times 0.92774 \approx 46.22
    $$

    **Mean:** The conditional mean of $r_{\Delta t}$ is (same formula as Vasicek):

    $$
    \mathbb{E}[r_{\Delta t}] = r_0 e^{-\kappa \Delta t} + \theta(1 - e^{-\kappa \Delta t}) = 0.03 \times 0.92774 + 0.05 \times 0.07226 \approx 0.02783 + 0.00361 = 0.03144
    $$

    **Variance:**

    $$
    \text{Var}(r_{\Delta t}) = r_0 \frac{\sigma^2}{\kappa}(e^{-\kappa \Delta t} - e^{-2\kappa \Delta t}) + \frac{\theta\sigma^2}{2\kappa}(1 - e^{-\kappa \Delta t})^2
    $$

    Computing each term:

    - $e^{-2\kappa \Delta t} = e^{-0.15} \approx 0.86071$
    - First term: $0.03 \times \frac{0.01}{0.3}(0.92774 - 0.86071) = 0.001 \times 0.06703 \approx 6.703 \times 10^{-5}$
    - Second term: $\frac{0.05 \times 0.01}{0.6}(0.07226)^2 = \frac{0.0005}{0.6} \times 0.005222 \approx 4.351 \times 10^{-6}$
    - Total: $\text{Var}(r_{\Delta t}) \approx 7.14 \times 10^{-5}$

    So $\text{Std}(r_{\Delta t}) \approx 0.00845$, meaning the short rate has a standard deviation of about 85 basis points over the quarter.

---

---

**Exercise 5.** Compute the 5-year and 10-year zero-coupon bond prices under CIR with $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.08$, $r_0 = 0.03$. Compare to the Vasicek model with the same $\kappa$, $\theta$, $r_0$ and $\sigma = 0.01$ (chosen to give similar yield curve levels). Which model produces a steeper long-end?

??? success "Solution to Exercise 5"
    **CIR bond prices.** With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.08$, $r_0 = 0.03$:

    $$
    \gamma = \sqrt{\kappa^2 + 2\sigma^2} = \sqrt{0.25 + 0.0128} = \sqrt{0.2628} \approx 0.5126
    $$

    For $\tau = 5$: $e^{\gamma\tau} = e^{2.563} \approx 12.975$

    $$
    B(5) = \frac{2(12.975 - 1)}{(0.5126 + 0.5)(12.975 - 1) + 2(0.5126)} = \frac{23.95}{1.0126 \times 11.975 + 1.0252} = \frac{23.95}{13.151} \approx 1.821
    $$

    The exponent for $\ln A$:

    $$
    \frac{2\kappa\theta}{\sigma^2} = \frac{0.04}{0.0064} = 6.25
    $$

    $$
    A(5) = \left[\frac{2(0.5126)e^{(0.5 + 0.5126)(5)/2}}{(0.5126 + 0.5)(e^{2.563} - 1) + 2(0.5126)}\right]^{6.25}
    $$

    Computing numerator: $2(0.5126)e^{2.5315} \approx 1.0252 \times 12.567 \approx 12.886$. Denominator: $13.151$ (same as above).

    $$
    A(5) \approx \left(\frac{12.886}{13.151}\right)^{6.25} \approx (0.9798)^{6.25} \approx 0.8810
    $$

    $$
    P^{\text{CIR}}(0,5) = A(5)e^{-B(5)r_0} = 0.8810 \times e^{-1.821 \times 0.03} = 0.8810 \times e^{-0.05463} \approx 0.8810 \times 0.9469 \approx 0.8342
    $$

    For $\tau = 10$: similar calculations give $P^{\text{CIR}}(0,10) \approx 0.6886$.

    **Vasicek bond prices.** With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$:

    $$
    B(5) = \frac{1 - e^{-2.5}}{0.5} = \frac{1 - 0.08209}{0.5} = 1.8358
    $$

    $$
    \ln A(5) = \left(0.04 - \frac{0.0001}{0.5}\right)(1.8358 - 5) - \frac{0.0001 \times 1.8358^2}{2.0}
    $$

    $$
    = (0.04 - 0.0002)(-3.1642) - 0.0001685 = 0.0398 \times (-3.1642) - 0.0001685 \approx -0.12594 - 0.00017 = -0.12611
    $$

    $$
    P^{\text{Vas}}(0,5) = e^{-0.12611 - 1.8358 \times 0.03} = e^{-0.12611 - 0.05507} = e^{-0.18118} \approx 0.8343
    $$

    The 5-year prices are very similar. For $\tau = 10$, $B(10) = (1 - e^{-5})/0.5 \approx 1.9865$:

    $$
    P^{\text{Vas}}(0,10) \approx e^{-0.26133 - 0.05960} \approx e^{-0.3209} \approx 0.7254
    $$

    Comparing: $P^{\text{CIR}}(0,10) \approx 0.689$ vs. $P^{\text{Vas}}(0,10) \approx 0.725$, so $z^{\text{CIR}}_{10} \approx 3.73\%$ vs. $z^{\text{Vas}}_{10} \approx 3.21\%$. The CIR model produces a steeper long end because the state-dependent volatility $\sigma\sqrt{r}$ generates a larger effective volatility at typical rate levels, leading to a bigger convexity correction.

---

---

**Exercise 6.** Explain why the CIR model belongs to the affine term structure class but the Black-Karasinski model does not. What computational consequence does this have for bond pricing and derivative valuation?

??? success "Solution to Exercise 6"
    **CIR is affine.** In the CIR model, the risk-neutral drift is $\mu^{\mathbb{Q}}(r) = \kappa(\theta - r) = \kappa\theta - \kappa r$ (affine in $r$), and the squared diffusion is $\sigma(r)^2 = \sigma^2 r$ (affine in $r$ with zero constant term). The affine term structure theory requires that both drift and squared diffusion be affine in the state, which CIR satisfies. Consequently, substituting $P = e^{A - Br}$ into the bond pricing PDE yields Riccati ODEs in $A$ and $B$ that decouple from the state $r$, giving closed-form solutions.

    **Black-Karasinski is not affine.** The Black-Karasinski model specifies $d\ln r_t = [\theta(t) - a(t)\ln r_t]\,dt + \sigma(t)\,dW_t$. By Ito's lemma, the SDE for $r_t$ is

    $$
    dr_t = r_t\!\left[\theta(t) - a(t)\ln r_t + \tfrac{1}{2}\sigma(t)^2\right]dt + \sigma(t)r_t\,dW_t
    $$

    The drift $r_t[\theta(t) - a(t)\ln r_t + \frac{1}{2}\sigma^2]$ involves $r\ln r$, which is not affine in $r$. The squared diffusion $\sigma^2 r^2$ is quadratic in $r$, not affine. The exponential-affine ansatz fails because the PDE cannot be separated into terms that are at most linear in $r$.

    **Computational consequences:**

    - **CIR:** Bond prices are available in closed form via the $A(\tau), B(\tau)$ formulas. European bond options can be priced using the noncentral chi-squared distribution. Calibration is fast because each bond price evaluation is $O(1)$.
    - **Black-Karasinski:** Bond prices must be computed numerically, typically via trinomial trees or finite-difference PDE solvers. Each bond price evaluation is $O(N)$ where $N$ is the number of time steps. Option pricing requires nesting (tree within a tree for Bermudan products) or Monte Carlo. Calibration is significantly slower due to the iterative numerical methods required at each parameter evaluation.
