# Boundary Behavior and Feller Classification

The CIR-type components of an affine process live on $\mathbb{R}_+$ and have square-root diffusion that vanishes at zero. The boundary $x = 0$ is therefore a distinguished point where the diffusion degenerates, and the qualitative behavior of the process near this boundary depends critically on the balance between the mean-reverting drift and the diffusion intensity. The **Feller condition** $2\kappa\theta \geq \xi^2$ determines whether the boundary is ever reached: when satisfied, the process stays strictly positive for all time; when violated, the process touches zero with positive probability but is immediately reflected back. This classification, based on Feller's (1951) theory of boundary behavior for one-dimensional diffusions, has profound consequences for the well-posedness of the SDE, the existence of transition densities, and the numerical simulation of affine processes.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and interpret the Feller condition $2\kappa\theta \geq \xi^2$ for the CIR process
    2. Classify the boundary $x = 0$ using Feller's scale function and speed measure
    3. Determine whether a CIR-type process reaches zero in finite time
    4. Explain the implications of boundary behavior for transition densities and simulation
    5. Extend the Feller classification to multidimensional affine processes

---

## Motivation

### Why Boundary Behavior Matters

Consider the CIR variance process in the Heston model:

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t, \qquad V_0 > 0
$$

If $V_t$ hits zero, the diffusion coefficient vanishes and the process degenerates. Three questions arise:

1. **Does $V_t$ ever reach zero?** If yes, the square-root diffusion creates a singular point.
2. **What happens at zero?** Is the process absorbed (stuck at zero forever) or reflected (immediately pushed back)?
3. **Does the process have a smooth transition density?** This matters for likelihood-based estimation and pricing.

The answers depend on the relationship between $\kappa\theta$ (the strength of the inward drift at the boundary) and $\xi^2/2$ (the intensity of the diffusion that could push the process to the boundary).

---

## Feller's Boundary Classification

### The Scale Function and Speed Measure

For a one-dimensional diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ on $(0, \infty)$, Feller's classification uses two fundamental objects.

!!! info "Definition: Scale Function"
    The **scale function** $s(x)$ satisfies $\mathcal{A}s = 0$ where $\mathcal{A}$ is the generator. For the CIR process:

    $$
    s'(x) = \exp\!\left(-\int^x \frac{2\mu(y)}{\sigma^2(y)}\,dy\right) = \exp\!\left(-\int^x \frac{2\kappa(\theta - y)}{\xi^2 y}\,dy\right)
    $$

    Computing the integral:

    $$
    s'(x) = x^{-2\kappa\theta/\xi^2}\,e^{2\kappa x/\xi^2}
    $$

!!! info "Definition: Speed Measure"
    The **speed measure** has density

    $$
    m(x) = \frac{1}{\sigma^2(x)\,s'(x)} = \frac{1}{\xi^2 x}\,x^{2\kappa\theta/\xi^2}\,e^{-2\kappa x/\xi^2} = \frac{1}{\xi^2}\,x^{2\kappa\theta/\xi^2 - 1}\,e^{-2\kappa x/\xi^2}
    $$

### Feller's Boundary Test

The boundary $x = 0$ is classified by evaluating two integrals near zero. Define $\nu = 2\kappa\theta/\xi^2$.

**Test 1: Is the boundary reachable?** Compute

$$
\int_0^c s'(x)\int_x^c m(y)\,dy\,dx
$$

for some $c > 0$. If this integral is **finite**, the boundary is reached in finite time with positive probability. If it is **infinite**, the boundary is never reached.

**Test 2: Can the process leave the boundary?** Compute

$$
\int_0^c m(x)\int_x^c s'(y)\,dy\,dx
$$

If finite, the process can leave zero; if infinite, it cannot.

### Result for CIR

!!! info "Theorem: Feller Classification for CIR"
    For the CIR process with parameter $\nu = 2\kappa\theta/\xi^2$:

    | Condition | Classification | Behavior |
    |---|---|---|
    | $\nu \geq 1$ (i.e., $2\kappa\theta \geq \xi^2$) | **Entrance** boundary | Zero is never reached; process stays strictly positive |
    | $0 < \nu < 1$ (i.e., $0 < 2\kappa\theta < \xi^2$) | **Regular** boundary with reflection | Zero is reached in finite time; process is instantly reflected |
    | $\nu = 0$ (i.e., $\kappa\theta = 0$) | **Exit** boundary | Zero is reached and the process is absorbed |

**Proof sketch for the entrance case ($\nu \geq 1$).** Near $x = 0$, the scale function derivative behaves as $s'(x) \sim x^{-\nu}$ and the speed measure as $m(x) \sim x^{\nu - 1}$. The reachability integral involves

$$
\int_0^c x^{-\nu}\int_x^c y^{\nu-1}\,dy\,dx \sim \int_0^c x^{-\nu}\left(\frac{c^\nu - x^\nu}{\nu}\right)dx
$$

The leading term near $x = 0$ is $\int_0^c x^{-\nu} \cdot c^\nu/\nu\,dx$, which diverges for $\nu \geq 1$. Therefore the boundary is not reachable. $\square$

---

## The Feller Condition

### Statement

!!! info "Definition: Feller Condition"
    The CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ satisfies the **Feller condition** if

    $$
    2\kappa\theta \geq \xi^2
    $$

    Equivalently, $\nu = 2\kappa\theta/\xi^2 \geq 1$.

### Geometric Interpretation

At $x = 0$, the drift is $\kappa\theta > 0$ (pushing the process away from zero) and the diffusion is $\xi\sqrt{x} \to 0$ (vanishing). The Feller condition says that the inward drift is strong enough relative to the diffusion that the process cannot reach zero despite the random fluctuations.

!!! example "Numerical Intuition"
    Consider $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$. Then $2\kappa\theta = 0.16$ and $\xi^2 = 0.09$, so $\nu = 0.16/0.09 \approx 1.78 > 1$. The Feller condition is satisfied and the variance process stays strictly positive.

    Now increase volatility-of-volatility to $\xi = 0.6$. Then $\xi^2 = 0.36$ and $\nu = 0.16/0.36 \approx 0.44 < 1$. The Feller condition is violated and the process can touch zero.

### Consequences for the Transition Density

When the Feller condition holds ($\nu \geq 1$), the CIR process has a smooth transition density on $(0, \infty)$ given by the non-central chi-squared distribution:

$$
p(t, x, y) = c_t\,e^{-c_t(x\,e^{-\kappa t} + y)}\left(\frac{y}{x\,e^{-\kappa t}}\right)^{(\nu-1)/2} I_{\nu-1}\!\left(2c_t\sqrt{xy\,e^{-\kappa t}}\right)
$$

where $c_t = 2\kappa/(\xi^2(1 - e^{-\kappa t}))$ and $I_{\nu-1}$ is the modified Bessel function of the first kind. When the Feller condition is violated ($0 < \nu < 1$), the transition density has an atom at zero:

$$
\mathbb{P}(X_t = 0 \mid X_0 = x) > 0
$$

In this case, the transition measure is a mixture of a point mass at zero and a continuous density on $(0, \infty)$.

---

## Implications for Numerical Simulation

### The Euler Scheme Problem

The standard Euler-Maruyama scheme for the CIR process:

$$
X_{t+\Delta t} = X_t + \kappa(\theta - X_t)\Delta t + \xi\sqrt{X_t}\,\sqrt{\Delta t}\,Z, \qquad Z \sim N(0,1)
$$

can produce **negative values** even when the Feller condition is satisfied. The probability of negativity decreases with $\Delta t$ but is nonzero for any finite step size.

!!! warning "Common Fixes and Their Pitfalls"
    Several schemes address this issue:

    1. **Full truncation**: Replace $X_t$ by $\max(X_t, 0)$ in the square root and drift. Introduces bias.
    2. **Reflection**: Replace $X_{t+\Delta t}$ by $|X_{t+\Delta t}|$ when negative. Converges but with slow rate.
    3. **Implicit Milstein**: Uses the implicit form to avoid negativity. More complex to implement.
    4. **Exact simulation** (Broadie and Kaya, 2006): Samples from the true non-central chi-squared distribution. Exact but computationally expensive.

    When the Feller condition is violated, even exact simulation produces zeros, which the numerical scheme must handle correctly.

---

## Multidimensional Extension

### Component-Wise Feller Condition

For a $d$-dimensional affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$, each CIR-type component $i \in \{1, \ldots, m\}$ has its own Feller condition:

$$
2(b_0)_i \geq (\alpha_i)_{ii}
$$

where $(b_0)_i$ is the constant drift of the $i$-th component (evaluated at $x^{(i)} = 0$ with other CIR components at zero) and $(\alpha_i)_{ii}$ is the diffusion coefficient.

!!! info "Proposition: Feller Condition for Heston Variance"
    In the Heston model, the variance process has $b_0^{(1)} = \kappa\theta$ and $(\alpha_1)_{11} = \xi^2$. The Feller condition is $2\kappa\theta \geq \xi^2$, identical to the scalar CIR condition.

### Cross-Component Effects

In multidimensional models, the drift of the $i$-th CIR component at $x^{(i)} = 0$ may depend on other state variables:

$$
\mu_i(x)\big|_{x^{(i)}=0} = (b_0)_i + \sum_{j \neq i} B_{ij} x^{(j)}
$$

The Feller condition $(b_0)_i \geq (\alpha_i)_{ii}/2$ ensures that the boundary $x^{(i)} = 0$ is not reached even in the worst case (all other state variables at their minimum values). For Gaussian components ($j \in J$), $x^{(j)}$ is unbounded below, so the drift $\mu_i(x)$ can become negative for large negative $x^{(j)}$ if $B_{ij} > 0$. In such cases, a more careful analysis involving the joint distribution of all components is needed.

---

## Feller Condition in Practice

### Calibrated Models Often Violate Feller

Empirical calibrations of the Heston model to equity option surfaces frequently find $2\kappa\theta < \xi^2$. Typical calibrated values for equity indices:

| Parameter | Typical range |
|---|---|
| $\kappa$ | 1.0 -- 5.0 |
| $\theta$ | 0.02 -- 0.08 |
| $\xi$ | 0.3 -- 1.0 |
| $2\kappa\theta$ | 0.04 -- 0.80 |
| $\xi^2$ | 0.09 -- 1.00 |

The Feller condition is often violated when $\xi$ is large (high vol-of-vol) and $\kappa\theta$ is small (low long-run variance times slow mean reversion).

!!! tip "Practical Consequence"
    Violation of the Feller condition does not invalidate the model --- the affine process remains well-defined with reflecting boundary. However, it changes the nature of the transition density (adding an atom at zero) and requires more careful numerical treatment. For option pricing via Fourier inversion, the characteristic function is valid regardless of whether the Feller condition holds; the Riccati ODE has the same solution in both cases.

---

## Summary

The Feller classification determines the boundary behavior of CIR-type components in affine processes. The Feller condition $2\kappa\theta \geq \xi^2$ ensures that the boundary $x = 0$ is an entrance boundary (never reached), so the process stays strictly positive and has a smooth non-central chi-squared transition density. When violated ($2\kappa\theta < \xi^2$), the boundary is regular with instant reflection: the process touches zero with positive probability but is immediately pushed back, and the transition measure has an atom at zero. The Feller condition has important implications for numerical simulation (Euler schemes can produce negative values regardless of the condition) and for estimation (the likelihood function changes structure). In multidimensional models, each CIR component has its own Feller condition, and cross-component effects can complicate the analysis. Empirical calibrations frequently violate the Feller condition, but the affine pricing machinery (Riccati ODEs, Fourier inversion) remains valid in both cases.

---

## Further Reading

- Feller, W. (1951). "Two Singular Diffusion Problems." *Annals of Mathematics*, 54(1), 173--182.
- Cox, J., Ingersoll, J., and Ross, S. (1985). "A Theory of the Term Structure of Interest Rates." *Econometrica*, 53(2), 385--407.
- Broadie, M. and Kaya, O. (2006). "Exact Simulation of Stochastic Volatility and Other Affine Jump Diffusion Processes." *Operations Research*, 54(2), 217--231.
- Andersen, L. (2008). "Simple and Efficient Simulation of the Heston Stochastic Volatility Model." *Journal of Computational Finance*, 11(3), 1--42.
