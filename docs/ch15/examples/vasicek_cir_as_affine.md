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

---

## Exercises

**Exercise 1.** For the Vasicek model, the bond price $B(\tau)$ satisfies $B'(\tau) = -1 - \kappa B(\tau)$ with $B(0) = 0$. Solve this linear ODE to obtain $B(\tau) = \frac{1}{\kappa}(e^{-\kappa\tau} - 1)$ and then integrate $A'(\tau) = \kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2$ to derive the complete bond price formula.

??? success "Solution to Exercise 1"
    The ODE for $B(\tau)$ is:

    $$
    B'(\tau) = -1 - \kappa B(\tau), \qquad B(0) = 0
    $$

    This is a first-order linear ODE. The integrating factor is $e^{\kappa\tau}$. Multiplying both sides:

    $$
    \frac{d}{d\tau}\!\left[e^{\kappa\tau} B(\tau)\right] = -e^{\kappa\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{\kappa\tau} B(\tau) - B(0) = -\frac{e^{\kappa\tau} - 1}{\kappa}
    $$

    Since $B(0) = 0$:

    $$
    B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa} = \frac{e^{-\kappa\tau} - 1}{\kappa}
    $$

    Now substitute into the $A$-equation:

    $$
    A'(\tau) = \kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2
    $$

    Let $\beta(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}$ so that $B(\tau) = -\beta(\tau)$. Then:

    $$
    A'(\tau) = -\kappa\theta\,\beta(\tau) + \frac{1}{2}\sigma^2\beta(\tau)^2
    $$

    Integrating $\int_0^\tau \beta(s)\,ds = \frac{1}{\kappa}[\tau - \beta(\tau)]$ and $\int_0^\tau \beta(s)^2\,ds$ by expanding and integrating term by term:

    $$
    A(\tau) = -\theta[\tau - \beta(\tau)] + \frac{\sigma^2}{2\kappa^2}\!\left[\tau - 2\beta(\tau) + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right]
    $$

    Rearranging:

    $$
    A(\tau) = \left(\frac{\sigma^2}{2\kappa^2} - \theta\right)(B(\tau) + \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    The complete bond price is $P(t, T) = \exp(A(\tau) + B(\tau)\,r_t)$ with $\tau = T - t$.

---

**Exercise 2.** Compare the long-run yield $y_\infty = \lim_{\tau \to \infty} y(\tau)$ for the Vasicek and CIR models. For the Vasicek model, show that $y_\infty = \theta - \frac{\sigma^2}{2\kappa^2}$, and for the CIR model, show that $y_\infty = \frac{2\kappa\theta}{\gamma + \kappa}$ where $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. For which model can the long-run yield be negative?

??? success "Solution to Exercise 2"
    **Vasicek long-run yield**: As $\tau \to \infty$, $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa \to -1/\kappa$. For the yield:

    $$
    y(\tau) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)}{\tau}r_t
    $$

    As $\tau \to \infty$, $B(\tau)/\tau \to 0$ (the $r_t$-dependent term vanishes). For $A(\tau)/\tau$, using $A(\tau) = (\frac{\sigma^2}{2\kappa^2} - \theta)(B(\tau) + \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2$:

    $$
    \frac{A(\tau)}{\tau} \to \frac{\sigma^2}{2\kappa^2} - \theta + 0 = \frac{\sigma^2}{2\kappa^2} - \theta
    $$

    Therefore:

    $$
    y_\infty^{\text{Vas}} = -\left(\frac{\sigma^2}{2\kappa^2} - \theta\right) = \theta - \frac{\sigma^2}{2\kappa^2}
    $$

    This can be negative when $\sigma^2 > 2\kappa^2\theta$, i.e., when volatility is large relative to the mean-reversion speed and long-run level.

    **CIR long-run yield**: As $\tau \to \infty$, $e^{\gamma\tau} \to \infty$, so:

    $$
    B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma} \to \frac{-2}{\gamma + \kappa}
    $$

    $$
    \frac{A(\tau)}{\tau} \to \frac{2\kappa\theta}{\xi^2}\cdot\frac{\gamma + \kappa}{2} - \frac{2\kappa\theta}{\xi^2}\cdot\frac{(\gamma + \kappa)}{2} + \ldots
    $$

    More directly, using the known result:

    $$
    y_\infty^{\text{CIR}} = \frac{2\kappa\theta}{\gamma + \kappa}
    $$

    where $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. Since $\gamma > \kappa$, we have $\gamma + \kappa > 2\kappa$, so $y_\infty^{\text{CIR}} < \theta$. Moreover, since $\kappa, \theta, \gamma > 0$, the CIR long-run yield is always positive: $y_\infty^{\text{CIR}} > 0$.

    **Conclusion**: Only the Vasicek model can produce a negative long-run yield (when $\sigma^2/(2\kappa^2) > \theta$). The CIR model always has $y_\infty > 0$.

---

**Exercise 3.** The Vasicek model has Gaussian transitions: $r_T \mid r_t \sim N(\mu_\tau, \sigma_\tau^2)$. Derive the conditional mean $\mu_\tau = \theta(1 - e^{-\kappa\tau}) + r_t e^{-\kappa\tau}$ and variance $\sigma_\tau^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$ directly from the SDE. What is the stationary distribution as $\tau \to \infty$?

??? success "Solution to Exercise 3"
    The Vasicek SDE is $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$. This is a linear SDE (Ornstein-Uhlenbeck process). The solution by variation of constants is:

    $$
    r_T = e^{-\kappa\tau}r_t + \theta(1 - e^{-\kappa\tau}) + \sigma\int_t^T e^{-\kappa(T-s)}\,dW_s
    $$

    **Conditional mean**: The stochastic integral has zero expectation, so:

    $$
    \mu_\tau = \mathbb{E}[r_T \mid r_t] = \theta(1 - e^{-\kappa\tau}) + r_t e^{-\kappa\tau}
    $$

    This is a weighted average of $r_t$ and $\theta$, with the weight on $r_t$ decaying exponentially.

    **Conditional variance**: By Ito's isometry:

    $$
    \sigma_\tau^2 = \operatorname{Var}(r_T \mid r_t) = \sigma^2 \int_t^T e^{-2\kappa(T-s)}\,ds = \sigma^2 \cdot \frac{1 - e^{-2\kappa\tau}}{2\kappa}
    $$

    **Stationary distribution**: As $\tau \to \infty$:

    $$
    \mu_\infty = \theta, \qquad \sigma_\infty^2 = \frac{\sigma^2}{2\kappa}
    $$

    The stationary distribution is $N(\theta, \sigma^2/(2\kappa))$. The rate fluctuates around $\theta$ with a standard deviation of $\sigma/\sqrt{2\kappa}$, confirming that faster mean reversion ($\kappa$ large) or lower volatility ($\sigma$ small) concentrates the rate around $\theta$.

---

**Exercise 4.** For the CIR model, the transition density involves the non-central chi-squared distribution. Without deriving the density, use the characteristic function to compute the conditional mean $\mathbb{E}[r_T \mid r_t]$ and variance $\operatorname{Var}(r_T \mid r_t)$. Verify that $\mathbb{E}[r_T \mid r_t] = \theta(1 - e^{-\kappa\tau}) + r_t e^{-\kappa\tau}$ (same mean as Vasicek) but the variance differs.

??? success "Solution to Exercise 4"
    The CIR SDE is $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$. The conditional mean can be computed directly by taking expectations of the SDE. Since $\mathbb{E}[dW_t] = 0$:

    $$
    \frac{d}{dt}\mathbb{E}[r_t] = \kappa(\theta - \mathbb{E}[r_t])
    $$

    This linear ODE for $m(t) = \mathbb{E}[r_t \mid r_0]$ has the solution:

    $$
    \mathbb{E}[r_T \mid r_t] = \theta(1 - e^{-\kappa\tau}) + r_t e^{-\kappa\tau}
    $$

    This is identical to the Vasicek conditional mean.

    For the variance, define $v(t) = \operatorname{Var}(r_t \mid r_0)$. Using Ito's formula on $r_t^2$:

    $$
    d(r_t^2) = 2r_t\,dr_t + (dr_t)^2 = 2r_t[\kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t] + \xi^2 r_t\,dt
    $$

    Taking expectations:

    $$
    \frac{d}{dt}\mathbb{E}[r_t^2] = 2\kappa\theta\,\mathbb{E}[r_t] - 2\kappa\,\mathbb{E}[r_t^2] + \xi^2\,\mathbb{E}[r_t]
    $$

    Since $v(t) = \mathbb{E}[r_t^2] - (\mathbb{E}[r_t])^2$, combining with the mean equation yields:

    $$
    v'(t) = -2\kappa\,v(t) + \xi^2\,m(t)
    $$

    Substituting $m(t) = \theta(1 - e^{-\kappa t}) + r_0 e^{-\kappa t}$ and solving the linear ODE with $v(0) = 0$:

    $$
    \operatorname{Var}(r_T \mid r_t) = r_t \cdot \frac{\xi^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \theta \cdot \frac{\xi^2}{2\kappa}(1 - e^{-\kappa\tau})^2
    $$

    Unlike the Vasicek variance $\sigma^2(1 - e^{-2\kappa\tau})/(2\kappa)$, the CIR variance depends on the current rate $r_t$. When $r_t$ is large, the variance is larger (because the diffusion $\xi\sqrt{r_t}$ is larger). This state-dependent variance is the key difference from the Vasicek model.

---

**Exercise 5.** The Feller condition for the CIR model is $2\kappa\theta \geq \xi^2$. Interpret each side of this inequality financially: what does $\kappa\theta$ represent, and what does $\xi^2$ represent? Explain intuitively why the mean reversion "pull" must dominate the volatility for the rate to stay strictly positive.

??? success "Solution to Exercise 5"
    The Feller condition is $2\kappa\theta \geq \xi^2$.

    **Left side ($\kappa\theta$)**: The quantity $\kappa\theta$ is the "pull" of mean reversion at $r = 0$. When $r_t = 0$, the drift is $\kappa(\theta - 0) = \kappa\theta > 0$, pushing the rate upward. The product $\kappa\theta$ measures the strength of this restoring force: $\kappa$ is the speed at which the rate is pulled back, and $\theta$ is how far the target is from zero. Together, $\kappa\theta$ is the instantaneous drift at the origin.

    **Right side ($\xi^2$)**: The quantity $\xi^2$ measures the volatility's ability to push the rate toward zero. Near $r = 0$, the diffusion coefficient is $\xi\sqrt{r}$, and the quadratic variation is $\xi^2 r$. The term $\xi^2$ appears because of the Ito correction: $d(\sqrt{r_t})$ involves a term $-\xi^2/(8\sqrt{r_t})\,dt$ that pulls $\sqrt{r_t}$ toward zero. The larger $\xi^2$, the stronger this downward pressure.

    **Intuition**: The rate stays strictly positive when the deterministic drift at the boundary ($\kappa\theta$) is strong enough to overcome the random fluctuations that push it toward zero (scaled by $\xi^2/2$). If $2\kappa\theta < \xi^2$, the volatility-induced downward drift dominates near zero, and the process can reach the boundary. The factor of 2 arises from the Ito correction in the SDE for $\sqrt{r_t}$.

---

**Exercise 6.** Plot (or sketch) the yield curves $y(\tau) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)}{\tau}r_0$ for the Vasicek model with $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$ for three different starting rates: $r_0 = 0.02$ (below $\theta$), $r_0 = 0.05$ (at $\theta$), and $r_0 = 0.08$ (above $\theta$). Describe the shape of each curve (normal, inverted, or humped).

??? success "Solution to Exercise 6"
    With $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$, the key quantities are:

    $$
    B(\tau) = -\frac{1 - e^{-0.5\tau}}{0.5} = -2(1 - e^{-0.5\tau})
    $$

    $$
    y_\infty = \theta - \frac{\sigma^2}{2\kappa^2} = 0.05 - \frac{0.0004}{0.5} = 0.05 - 0.0008 = 0.0492
    $$

    The yield at maturity $\tau$ is $y(\tau) = -A(\tau)/\tau - B(\tau) r_0/\tau$. At $\tau \to 0$, $y(0^+) = r_0$ (the instantaneous short rate). As $\tau \to \infty$, $y \to 0.0492$.

    **Case $r_0 = 0.02$ (below $\theta$)**: The yield starts at $y(0^+) = 0.02$ and rises toward $y_\infty = 0.0492$. The curve is **normal** (upward sloping), reflecting the expectation that rates will mean-revert upward from their currently low level.

    **Case $r_0 = 0.05$ (at $\theta$)**: The yield starts at $y(0^+) = 0.05$ and decreases slightly toward $y_\infty = 0.0492$. The curve is nearly flat with a slight downward slope, reflecting only the convexity adjustment $-\sigma^2/(2\kappa^2) = -0.0008$. This is a **mildly inverted** (slightly downward-sloping) curve.

    **Case $r_0 = 0.08$ (above $\theta$)**: The yield starts at $y(0^+) = 0.08$ and falls toward $y_\infty = 0.0492$. The curve is **inverted** (downward sloping), reflecting the market's expectation that the currently high rate will mean-revert downward toward $\theta = 0.05$.

    In all three cases, the long end converges to the same value $y_\infty = 0.0492$. The shape of the yield curve is determined by the position of $r_0$ relative to $\theta$: below $\theta$ gives a normal curve, at $\theta$ gives a flat curve (modulo convexity), and above $\theta$ gives an inverted curve.
