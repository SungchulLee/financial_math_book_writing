# Yield Curve Dynamics from Affine Structure

The yield curve --- the function mapping maturities to interest rates --- is the most fundamental object in fixed-income markets. In an affine term structure model, the yield curve is an **affine function** of the state vector at every point in time. This means that the entire term structure, from overnight rates to thirty-year yields, is determined by a finite-dimensional state vector $X_t$, and the sensitivity of each yield to each factor is captured by explicit **factor loadings** derived from the Riccati solutions. This section develops the yield curve representation, derives the dynamics of yields and forward rates, and connects the factor loading structure to the empirically observed level-slope-curvature decomposition.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Express the continuously compounded yield and instantaneous forward rate as affine functions of the state vector
    2. Compute factor loadings $b_i(\tau) = -B_i(\tau)/\tau$ and interpret their maturity dependence
    3. Derive the stochastic dynamics of yields using Ito's lemma
    4. Connect the affine factor structure to the level-slope-curvature decomposition of the yield curve
    5. Compute explicit yield curves for the Vasicek and CIR models

---

## Motivation

### Why Yield Curves Matter

Every fixed-income security --- from Treasury bills to interest rate swaps to mortgage-backed securities --- is priced relative to the yield curve. Traders use the yield curve to identify relative value; risk managers use it to compute duration and convexity exposures; central banks use it to gauge market expectations of future policy rates. A model that generates the yield curve as a tractable, analytically transparent function of a few state variables is therefore enormously valuable.

The affine term structure framework achieves exactly this. Because the [exponential-affine bond price formula](exponential_affine_bond_price.md) gives $\ln P(t,T) = A(\tau) + B(\tau)^\top X_t$, the yield at maturity $\tau$ is a linear function of $X_t$ with coefficients determined by the Riccati solutions. The yield curve is not a free object that must be interpolated from market data; instead, it is a **derived quantity** that inherits all its structure from the state dynamics.

---

## Yields as Affine Functions of the State

### Continuously Compounded Yield

!!! info "Definition: Continuously Compounded Yield"
    The continuously compounded yield $y(t, T)$ for a zero-coupon bond maturing at $T$ is defined by

    $$
    y(t, T) = -\frac{\ln P(t, T)}{T - t}
    $$

    so that $P(t, T) = e^{-y(t,T)(T-t)}$.

Substituting the exponential-affine bond price $P(t,T) = \exp(A(\tau) + B(\tau)^\top X_t)$ with $\tau = T - t$:

$$
y(t, T) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)^\top}{\tau}X_t = a(\tau) + b(\tau)^\top X_t
$$

where

$$
a(\tau) = -\frac{A(\tau)}{\tau}, \qquad b(\tau) = -\frac{B(\tau)}{\tau}
$$

The yield is therefore an **affine function** of the state vector $X_t$, with maturity-dependent coefficients $a(\tau)$ (the intercept) and $b(\tau)$ (the factor loadings).

### Instantaneous Forward Rate

!!! info "Definition: Instantaneous Forward Rate"
    The instantaneous forward rate at time $t$ for future date $T$ is

    $$
    f(t, T) = -\frac{\partial \ln P(t, T)}{\partial T}
    $$

Differentiating $\ln P(t,T) = A(\tau) + B(\tau)^\top X_t$ with respect to $T$ (noting $\partial \tau / \partial T = 1$):

$$
f(t, T) = -A'(\tau) - B'(\tau)^\top X_t
$$

where the primes denote derivatives with respect to $\tau$. Substituting the Riccati equations:

$$
f(t, T) = \rho_0 - K_0^\top B(\tau) - \frac{1}{2}B(\tau)^\top H_0\,B(\tau) + \left(\rho_1 - K_1^\top B(\tau) - \frac{1}{2}\sum_{i=1}^d (B^\top H_i B)\,e_i\right)^\top X_t
$$

The forward rate is also affine in $X_t$, with loadings that are the derivatives of the yield loadings (up to sign).

!!! tip "Short Rate as Limiting Case"
    Taking $T \to t$ (i.e., $\tau \to 0$) in the forward rate formula recovers the short rate $r_t = f(t, t) = \rho_0 + \rho_1^\top X_t$, consistent with the affine short-rate specification, since $B(0) = \mathbf{0}$.

---

## Factor Loadings

### Definition and Maturity Structure

The vector $b(\tau) = -B(\tau)/\tau \in \mathbb{R}^d$ gives the **factor loadings** of the yield at maturity $\tau$. The $i$-th component $b_i(\tau)$ measures the sensitivity of the $\tau$-maturity yield to a unit change in the $i$-th state variable:

$$
\frac{\partial y(t, T)}{\partial X_t^{(i)}} = b_i(\tau) = -\frac{B_i(\tau)}{\tau}
$$

The maturity dependence of $b_i(\tau)$ determines how the $i$-th factor affects yields across the term structure.

### Connection to Level, Slope, and Curvature

Empirical studies of yield curve movements (Litterman and Scheinkman, 1991) consistently find that three principal components explain over 95% of yield curve variation:

1. **Level**: a parallel shift affecting all maturities equally
2. **Slope**: a tilt that moves short and long rates in opposite directions
3. **Curvature**: a twist that moves medium-term rates relative to both short and long rates

In a $d$-factor affine model, the factor loadings $b_i(\tau)$ play the role of these principal components. For a three-factor model with one Gaussian factor (constant diffusion) and two CIR-type factors (state-dependent diffusion):

- A factor with $b_i(\tau) \approx \text{const}$ for all $\tau$ acts as a **level** factor
- A factor with $b_i(\tau)$ monotonically decreasing from a high short-end value to zero acts as a **slope** factor
- A factor with $b_i(\tau)$ humped (peaking at intermediate $\tau$) acts as a **curvature** factor

!!! note "Factor Loadings Are Model-Determined"
    Unlike statistical principal component analysis, which extracts loadings from data, the factor loadings in an affine model are derived from the model parameters through the Riccati equations. The challenge of calibration is to choose parameters so that the model-implied loadings match the empirically observed principal components.

---

## Dynamics of Yields

### Yield Dynamics via Ito's Lemma

Since $y(t, T) = a(\tau) + b(\tau)^\top X_t$ and $\tau = T - t$, the yield at a fixed maturity date $T$ evolves as

$$
dy(t, T) = \left(-a'(\tau) - b'(\tau)^\top X_t + b(\tau)^\top \mu(X_t)\right)dt + b(\tau)^\top \sigma(X_t)\,dW_t
$$

where $a'(\tau) = da/d\tau$ and $b'(\tau) = db/d\tau$, and we used $d\tau = -dt$.

Substituting the affine drift $\mu(X_t) = K_0 + K_1 X_t$:

$$
dy(t, T) = \left(-a'(\tau) + b(\tau)^\top K_0 + \bigl(b(\tau)^\top K_1 - b'(\tau)^\top\bigr)X_t\right)dt + b(\tau)^\top \sigma(X_t)\,dW_t
$$

The drift of the yield is affine in $X_t$, and the volatility is $b(\tau)^\top \sigma(X_t)$, which is state-dependent when the diffusion coefficient $\sigma$ depends on $X_t$ (as in CIR-type models).

### Yield Volatility Term Structure

The instantaneous variance of the yield at maturity $\tau$ is

$$
\operatorname{Var}_t\!\bigl[dy(t,T)\bigr] = b(\tau)^\top\!\left(H_0 + \sum_{i=1}^d H_i\,X_t^{(i)}\right)\!b(\tau)\,dt
$$

This expression shows that:

- In the Vasicek model ($H_1 = 0$), all yield volatilities are **constant** (homoskedastic)
- In the CIR model ($H_0 = 0$, $H_1 \neq 0$), yield volatilities are **proportional to $\sqrt{X_t}$**, generating stochastic volatility across the entire yield curve from a single state variable

---

## Explicit Yield Curves

### Vasicek Yield Curve

Using $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$ from the [bond price formula](exponential_affine_bond_price.md), the Vasicek yield is

$$
y(t, T) = \frac{1 - e^{-\kappa\tau}}{\kappa\tau}\,r_t + \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\left(1 - \frac{1 - e^{-\kappa\tau}}{\kappa\tau}\right) + \frac{\sigma^2}{4\kappa^3\tau}(1 - e^{-\kappa\tau})^2
$$

!!! example "Vasicek Yield Curve Properties"
    The factor loading $b(\tau) = (1 - e^{-\kappa\tau})/(\kappa\tau)$ satisfies:

    - $b(0^+) = 1$: the shortest yields have unit sensitivity to the short rate
    - $b(\tau) \to 0$ as $\tau \to \infty$: very long yields are insensitive to the current short rate
    - $b(\tau)$ is monotonically decreasing and convex

    The **long rate** $y_\infty = \lim_{\tau \to \infty} y(t, T) = \theta - \sigma^2/(2\kappa^2)$ is deterministic and depends only on the long-run mean $\theta$ and the volatility-mean-reversion ratio $\sigma^2/\kappa^2$. This is a well-known limitation of the Vasicek model: the long end of the yield curve does not fluctuate.

### CIR Yield Curve

With $\gamma = \sqrt{\kappa^2 + 2\xi^2}$ and the CIR bond coefficients, the yield is

$$
y(t, T) = \frac{2(e^{\gamma\tau} - 1)}{[(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma]\,\tau}\,r_t - \frac{2\kappa\theta}{\xi^2\tau}\ln\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\right)
$$

The CIR yield curve guarantees $y(t, T) \geq 0$ whenever $r_t \geq 0$, reflecting the non-negativity of CIR rates. The long rate is $y_\infty = 2\kappa\theta/(\gamma + \kappa)$, which is also deterministic but always positive.

---

## Yield Curve Shapes

The affine framework can generate the four canonical yield curve shapes observed in practice:

| Shape | Condition (Vasicek) |
|---|---|
| **Normal** (upward sloping) | $r_t < \theta - \sigma^2/(2\kappa^2)$ |
| **Inverted** (downward sloping) | $r_t > \theta$ |
| **Humped** | $r_t$ moderately above $\theta - \sigma^2/(2\kappa^2)$ |
| **Flat** | $r_t \approx \theta - \sigma^2/(2\kappa^2)$ |

The convexity correction $\sigma^2/(2\kappa^2)$ plays a crucial role: even when $r_t = \theta$ (the rate is at its long-run mean), the yield curve slopes downward at the long end because the convexity effect depresses long yields below $\theta$.

!!! warning "One-Factor Limitations"
    A single-factor affine model cannot simultaneously fit the level and slope of the yield curve independently. The slope is determined by $r_t - y_\infty$, which is controlled by the same state variable $r_t$ that determines the level. Multi-factor models are needed to match the empirical observation that level, slope, and curvature move somewhat independently.

---

## Summary

In an affine term structure model, the continuously compounded yield is $y(t,T) = a(\tau) + b(\tau)^\top X_t$, where the factor loadings $b(\tau) = -B(\tau)/\tau$ are derived from the Riccati solutions for the bond price. The instantaneous forward rate is also affine in the state. The maturity dependence of the factor loadings determines how each state variable influences the term structure --- acting as level, slope, or curvature factors --- providing a structural counterpart to the empirical principal component decomposition. The Vasicek model produces a yield curve with a deterministic long rate and constant yield volatilities, while the CIR model generates non-negative yields with stochastic volatility across all maturities. Multi-factor extensions are required to capture the independent movements of level, slope, and curvature observed in data.

---

## Further Reading

- Litterman, R. and Scheinkman, J. (1991). "Common Factors Affecting Bond Returns." *Journal of Fixed Income*, 1(1), 54--61.
- Duffie, D. and Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379--406.
- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Piazzesi, M. (2010). "Affine Term Structure Models." In *Handbook of Financial Econometrics*, Vol. 1, 691--766.

---

## Exercises

**Exercise 1.** For the Vasicek model with $B(\tau) = \frac{1}{\kappa}(e^{-\kappa\tau} - 1)$, compute the factor loading $b(\tau) = -B(\tau)/\tau$ and plot it as a function of $\tau$ for $\kappa = 0.5$. Show that $b(\tau) \to 1$ as $\tau \to 0$ and $b(\tau) \to 0$ as $\tau \to \infty$. Interpret these limits.

---

**Exercise 2.** Derive the instantaneous forward rate $f(t, T) = -\frac{\partial}{\partial T}\log P(t, T) = -A'(\tau) - B'(\tau)^\top X_t$ for the Vasicek model. Verify that $f(t, t) = r_t$ (the short rate) by evaluating at $\tau = 0$.

---

**Exercise 3.** Using the affine yield formula $y(t, \tau) = a(\tau) + b(\tau)^\top X_t$ with $a(\tau) = -A(\tau)/\tau$ and $b(\tau) = -B(\tau)/\tau$, apply Ito's lemma to derive $dy(t, \tau)$ for a one-factor model. Express the drift and volatility of the yield in terms of $b(\tau)$, the state dynamics, and the Riccati solution $B(\tau)$.

---

**Exercise 4.** For a two-factor model with $X_t = (X_t^{(1)}, X_t^{(2)})^\top$ and factor loadings $b_1(\tau)$ and $b_2(\tau)$, explain the level-slope-curvature interpretation: if $b_1(\tau) \approx 1$ for all $\tau$ (flat loading) and $b_2(\tau)$ is monotonically decreasing from 1 to 0, which factor controls the level and which controls the slope of the yield curve?

---

**Exercise 5.** Compute the convexity of a zero-coupon bond in the Vasicek model: $\frac{\partial^2}{\partial r^2}\log P(t,T) = B(\tau)^2$. How does convexity depend on maturity $\tau$? Why is convexity always non-negative in one-factor affine models?

---

**Exercise 6.** The Nelson-Siegel yield curve model parametrizes yields as $y(\tau) = \beta_0 + \beta_1\frac{1 - e^{-\lambda\tau}}{\lambda\tau} + \beta_2(\frac{1 - e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau})$. Show that the Vasicek factor loading $b(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa\tau}$ matches the Nelson-Siegel slope factor. Does any affine model generate the curvature factor as well?
