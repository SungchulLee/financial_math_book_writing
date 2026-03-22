# Vasicek and CIR as Affine

The Vasicek and Cox-Ingersoll-Ross (CIR) models are the two canonical one-factor short-rate models, and both are affine processes. They illustrate the two fundamental cases of the affine framework: constant diffusion (Gaussian dynamics, Vasicek) and state-dependent diffusion (square-root dynamics, CIR). This section embeds both models in the affine framework, identifies the functions $F$ and $R$, derives the bond pricing Riccati solutions, and contrasts the two models systematically.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write the Vasicek and CIR models in affine parameter form
    2. Identify $F$, $R$, and the extended Riccati system for each model
    3. Derive closed-form bond prices for both models
    4. Compare Gaussian vs square-root dynamics and their financial implications

---

## Intuition

Both the Vasicek and CIR models describe a short rate $r_t$ that mean-reverts toward a long-term level $\theta$ with speed $\kappa$. They differ in how volatility depends on the level:

- **Vasicek**: $\sigma(r) = \sigma$ (constant). The rate can go negative. The transition density is Gaussian.
- **CIR**: $\sigma(r) = \xi\sqrt{r}$ (proportional to $\sqrt{r}$). The rate stays non-negative (under the Feller condition). The transition density is non-central chi-squared.

In the affine classification, Vasicek is the $A_0(1)$ model (zero CIR-type components among one total) and CIR is the $A_1(1)$ model (one CIR-type component among one total). Despite their different volatility structures, both produce exponential-affine bond prices---the hallmark of affine term structure models.

---

## Vasicek Model

### Dynamics and Affine Parameters

The Vasicek model under the risk-neutral measure:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
$$

State space: $D = \mathbb{R}$ (the rate is unconstrained), so $m = 0$, $d = 1$.

Affine parameters:

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| $b_0$ | $\kappa\theta$ | Constant drift |
| $b_1$ | $-\kappa$ | Mean-reversion speed |
| $a_0$ | $\sigma^2$ | Constant diffusion |
| $a_1$ | $0$ | No state-dependent volatility |
| $\rho_0$ | $0$ | Short rate offset |
| $\rho_1$ | $1$ | Short rate loading |

### Functions F and R

$$
F(w) = \kappa\theta\,w + \frac{1}{2}\sigma^2 w^2
$$

$$
R(w) = -\kappa\,w
$$

Since $a_1 = 0$, the function $R$ is linear---the Riccati equation degenerates to a first-order linear ODE.

### Bond Pricing Riccati System

With $\rho_0 = 0$ and $\rho_1 = 1$, the extended Riccati for bond pricing is:

$$
B'(\tau) = R(B(\tau)) - 1 = -\kappa B(\tau) - 1, \qquad B(0) = 0
$$

$$
A'(\tau) = F(B(\tau)) = \kappa\theta\,B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2, \qquad A(0) = 0
$$

### Solution

The $B$-equation is a linear ODE with constant coefficients. The solution is:

$$
B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}
$$

**Verification**: $B'(\tau) = -e^{-\kappa\tau}$ and $-\kappa B(\tau) - 1 = (1 - e^{-\kappa\tau}) - 1 = -e^{-\kappa\tau}$. $\square$

For the $A$-equation, substituting $B(\tau)$:

$$
A(\tau) = \left(\frac{\sigma^2}{2\kappa^2} - \theta\right)\!\left(B(\tau) + \tau\right) - \frac{\sigma^2}{4\kappa}B(\tau)^2
$$

### Bond Price and Yield

$$
P(t, T) = \exp\!\left(A(\tau) + B(\tau)\,r_t\right)
$$

The yield $y(\tau) = -[A(\tau) + B(\tau)\,r_t]/\tau$ is linear in $r_t$:

$$
y(\tau) = -\frac{A(\tau)}{\tau} + \frac{1 - e^{-\kappa\tau}}{\kappa\tau}\,r_t
$$

As $\tau \to \infty$, the yield converges to $y(\infty) = \theta - \frac{\sigma^2}{2\kappa^2}$, the long rate.

---

## CIR Model

### Dynamics and Affine Parameters

The CIR model under the risk-neutral measure:

$$
dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t
$$

State space: $D = \mathbb{R}_+$ (the rate is non-negative), so $m = 1$, $d = 1$.

Affine parameters:

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| $b_0$ | $\kappa\theta$ | Constant drift |
| $b_1$ | $-\kappa$ | Mean-reversion speed |
| $a_0$ | $0$ | No constant diffusion |
| $a_1$ | $\xi^2$ | State-dependent volatility |
| $\rho_0$ | $0$ | Short rate offset |
| $\rho_1$ | $1$ | Short rate loading |

### Functions F and R

$$
F(w) = \kappa\theta\,w
$$

$$
R(w) = -\kappa\,w + \frac{1}{2}\xi^2 w^2
$$

Since $a_1 = \xi^2 \neq 0$, the function $R$ is quadratic---a genuine Riccati equation.

### Feller Condition

The CIR process stays strictly positive if and only if the **Feller condition** holds:

$$
2\kappa\theta \geq \xi^2
$$

When violated, the process can reach zero but is instantaneously reflected. This condition translates to the admissibility requirement $(b_0)_1 = \kappa\theta > 0$ being strong enough relative to the diffusion.

### Bond Pricing Riccati System

$$
B'(\tau) = -\kappa B(\tau) + \frac{1}{2}\xi^2 B(\tau)^2 - 1, \qquad B(0) = 0
$$

$$
A'(\tau) = \kappa\theta\,B(\tau), \qquad A(0) = 0
$$

### Solution

Define the discriminant $\gamma = \sqrt{\kappa^2 + 2\xi^2}$.

The $B$-equation is a scalar Riccati with constant term $-1$, linear term $-\kappa$, and quadratic coefficient $\frac{1}{2}\xi^2$. By the substitution $B = -\frac{2}{\xi^2}\frac{h'}{h}$ or by direct integration:

$$
B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

**Verification**: Computing $B'(\tau)$ by the quotient rule and checking that $B' = -\kappa B + \frac{1}{2}\xi^2 B^2 - 1$ is algebraically tedious but routine. $\square$

For the $A$-equation:

$$
A(\tau) = \frac{2\kappa\theta}{\xi^2}\log\!\left(\frac{2\gamma\,e^{(\gamma + \kappa)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)
$$

### Bond Price and Yield

$$
P(t, T) = \exp\!\left(A(\tau) + B(\tau)\,r_t\right)
$$

Since $B(\tau) < 0$, the bond price is decreasing in $r_t$. The yield is:

$$
y(\tau) = -\frac{A(\tau)}{\tau} + \frac{2(e^{\gamma\tau} - 1)}{[(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma]\tau}\,r_t
$$

As $\tau \to \infty$:

$$
y(\infty) = \frac{2\kappa\theta}{\gamma + \kappa}
$$

---

## Side-by-Side Comparison

| Feature | Vasicek | CIR |
|---------|---------|-----|
| **State space** | $\mathbb{R}$ | $\mathbb{R}_+$ |
| **Classification** | $A_0(1)$ | $A_1(1)$ |
| **Diffusion** | $\sigma$ (constant) | $\xi\sqrt{r}$ (state-dependent) |
| **$R(w)$** | $-\kappa w$ (linear) | $-\kappa w + \frac{1}{2}\xi^2 w^2$ (quadratic) |
| **$B(\tau)$ ODE** | Linear | Riccati |
| **$B(\tau)$ solution** | $-(1-e^{-\kappa\tau})/\kappa$ | Ratio of exponentials |
| **Transition density** | Gaussian | Non-central $\chi^2$ |
| **Negative rates** | Possible | Impossible (Feller) |
| **Long rate** | $\theta - \sigma^2/(2\kappa^2)$ | $2\kappa\theta/(\gamma + \kappa)$ |

??? example "Numerical Comparison"
    With $\kappa = 0.5$, $\theta = 0.05$, $\sigma = \xi = 0.1$, $r_0 = 0.03$:

    **Vasicek**: $B(5) = -(1 - e^{-2.5})/0.5 = -1.836$. Bond price $P(0, 5) = e^{A(5) + B(5) \cdot 0.03}$.

    **CIR**: $\gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} = 0.5196$. $B(5) = -2(e^{2.598} - 1)/[(1.0196)(e^{2.598} - 1) + 1.0392]$.

    The CIR bond price is slightly higher because the square-root volatility reduces uncertainty when rates are low, effectively lowering the convexity adjustment. $\square$

---

## Summary

The Vasicek and CIR models are the simplest non-trivial affine term structure models. Vasicek, with constant diffusion ($A_0(1)$), produces a linear Riccati equation and Gaussian dynamics that permit negative rates. CIR, with square-root diffusion ($A_1(1)$), produces a genuine quadratic Riccati equation and non-central chi-squared dynamics that guarantee non-negative rates under the Feller condition. Both yield exponential-affine bond prices $P(t, T) = e^{A(\tau) + B(\tau)r_t}$ with explicit solutions for $A$ and $B$, making them the building blocks of multi-factor affine term structure models.

---

## Further Reading

- Vasicek, O. (1977). "An Equilibrium Characterization of the Term Structure." *Journal of Financial Economics*, 5(2), 177-188.
- Cox, J. C., Ingersoll, J. E., & Ross, S. A. (1985). "A Theory of the Term Structure of Interest Rates." *Econometrica*, 53(2), 385-407.
- Brigo, D. & Mercurio, F. *Interest Rate Models - Theory and Practice*. Springer, 2007, Chapters 3-4.
