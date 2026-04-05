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

---

## Exercises

**Exercise 1.** For the CIR process $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t$ with $\kappa = 2$, $\theta = 0.04$, $\xi = 0.3$, check whether the Feller condition $2\kappa\theta \geq \xi^2$ is satisfied. Interpret the result: can the variance reach zero?

??? success "Solution to Exercise 1"
    We compute $2\kappa\theta$ and $\xi^2$ directly:

    $$
    2\kappa\theta = 2 \times 2 \times 0.04 = 0.16
    $$

    $$
    \xi^2 = 0.3^2 = 0.09
    $$

    Since $0.16 \geq 0.09$, the Feller condition $2\kappa\theta \geq \xi^2$ is satisfied. Equivalently, $\nu = 2\kappa\theta / \xi^2 = 0.16 / 0.09 \approx 1.78 > 1$.

    **Interpretation.** Because $\nu > 1$, the boundary $V = 0$ is an entrance boundary. The inward drift $\kappa\theta = 0.08$ at $V = 0$ dominates the diffusion intensity $\xi^2/2 = 0.045$, so the mean-reverting force is strong enough to prevent the variance from ever reaching zero. The process $V_t$ stays strictly positive for all $t > 0$ almost surely.

---

**Exercise 2.** Repeat Exercise 1 with $\xi = 0.5$. Now the Feller condition is violated. Explain qualitatively what happens when $V_t$ hits zero: is the process absorbed at zero or reflected? What is the implication for the transition density at $V = 0$?

??? success "Solution to Exercise 2"
    With $\xi = 0.5$, we have $\xi^2 = 0.25$, while $2\kappa\theta = 0.16$ remains unchanged. Now $0.16 < 0.25$, so the Feller condition is violated. The dimension parameter is $\nu = 0.16/0.25 = 0.64 < 1$.

    **What happens at zero.** Since $0 < \nu < 1$, the boundary $V = 0$ is classified as a regular boundary with instant reflection. The process reaches zero in finite time with positive probability, but it is **not absorbed**: the mean-reverting drift $\kappa\theta > 0$ immediately pushes the process away from zero. The process touches zero and is instantly reflected back into $(0, \infty)$.

    **Implication for the transition density.** When $\nu < 1$, the transition measure of $V_T$ (conditional on $V_t > 0$) is no longer a purely continuous density on $(0, \infty)$. Instead, it is a mixture:

    $$
    \mathbb{P}(V_T \in \cdot \mid V_t = v) = p_0(t, T, v)\,\delta_0(\cdot) + p(t, T, v, \cdot)\,dy
    $$

    where $p_0 > 0$ is a positive probability mass at $V_T = 0$ and $p(t, T, v, y)$ is a continuous density on $(0, \infty)$. The atom at zero complicates likelihood-based estimation because the density is no longer everywhere positive on the interior.

---

**Exercise 3.** The Feller condition can be written as $\nu := 2\kappa\theta/\xi^2 \geq 1$, where $\nu$ is the dimension parameter of the non-central chi-squared distribution of $V_T$ (conditional on $V_t$). For the CIR process, express the conditional distribution of $V_T$ in terms of $\nu$ and explain why $\nu < 1$ implies a probability mass at $V_T = 0$.

??? success "Solution to Exercise 3"
    The conditional distribution of $V_T$ given $V_t = v$ is a scaled non-central chi-squared distribution. Specifically, define $c_\tau = 2\kappa / (\xi^2(1 - e^{-\kappa\tau}))$ where $\tau = T - t$. Then

    $$
    2c_\tau V_T \mid V_t = v \;\sim\; \chi^2(2\nu,\; 2c_\tau v\,e^{-\kappa\tau})
    $$

    where $\chi^2(2\nu, \lambda)$ denotes the non-central chi-squared distribution with $2\nu$ degrees of freedom and non-centrality parameter $\lambda = 2c_\tau v\,e^{-\kappa\tau}$.

    When $\nu \geq 1$ (equivalently $2\nu \geq 2$), the $\chi^2(2\nu, \lambda)$ distribution has a continuous density on $(0, \infty)$ that vanishes at zero, so $V_T > 0$ almost surely.

    When $\nu < 1$ (equivalently $2\nu < 2$), the density of $\chi^2(2\nu, \lambda)$ diverges as $y \to 0^+$ and has a **probability mass at zero**:

    $$
    \mathbb{P}(\chi^2(2\nu, \lambda) = 0) = e^{-\lambda/2} > 0
    $$

    This mass at zero corresponds to the event $V_T = 0$. Intuitively, with fewer than two effective degrees of freedom, the chi-squared random variable can equal zero, reflecting the fact that the diffusion is strong enough relative to the drift to push the process all the way to the boundary.

---

**Exercise 4.** For the Euler discretization of the CIR process, $\hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t + \xi\sqrt{\hat{V}_n}\sqrt{\Delta t}\,Z_{n+1}$, explain why negative values of $\hat{V}_{n+1}$ can occur even when the Feller condition holds. Describe two common remedies: absorption ($\hat{V}_{n+1} = \max(\hat{V}_{n+1}, 0)$) and reflection ($\hat{V}_{n+1} = |\hat{V}_{n+1}|$).

??? success "Solution to Exercise 4"
    Starting from the Euler scheme $\hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t + \xi\sqrt{\hat{V}_n}\sqrt{\Delta t}\,Z_{n+1}$ with $Z_{n+1} \sim N(0,1)$, note that even when $\hat{V}_n > 0$, the Gaussian increment $Z_{n+1}$ is unbounded below. We get $\hat{V}_{n+1} < 0$ whenever

    $$
    Z_{n+1} < -\frac{\hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t}{\xi\sqrt{\hat{V}_n \Delta t}}
    $$

    Since the right-hand side is finite for any $\hat{V}_n > 0$ and $\Delta t > 0$, and the Gaussian distribution has support on all of $\mathbb{R}$, there is always a positive probability of a negative outcome. This happens even when the Feller condition holds because the Euler scheme approximates the continuous dynamics with a discrete step of finite size --- the continuous process never goes negative, but the discrete approximation can "overshoot" the boundary in a single step.

    **Absorption (full truncation).** Replace $\hat{V}_{n+1}$ by $\max(\hat{V}_{n+1}, 0)$. Any negative realization is set to zero. This is simple to implement but introduces a systematic positive bias: the truncated process has a higher mean than the true process near the boundary. The scheme converges as $\Delta t \to 0$ but with a slower convergence rate than the standard Euler scheme.

    **Reflection.** Replace $\hat{V}_{n+1}$ by $|\hat{V}_{n+1}|$. When the scheme produces a negative value $-\epsilon$, it is reflected to $+\epsilon$. This preserves the magnitude of the overshoot and is motivated by the reflecting boundary behavior of the true CIR process when the Feller condition is violated. Reflection also converges as $\Delta t \to 0$ and tends to produce less bias than absorption, but it can be less stable for very large step sizes.

---

**Exercise 5.** The scale function $s(x)$ and speed measure $m(x)$ of a one-dimensional diffusion classify the boundary behavior. For the CIR process, compute $s(x) = \exp(-\int^x \frac{2\kappa(\theta - y)}{\xi^2 y}\,dy)$ and determine the integrability of $s(x)$ near $x = 0$. How does this relate to the Feller condition?

??? success "Solution to Exercise 5"
    The scale function derivative is obtained from

    $$
    s'(x) = \exp\!\left(-\int^x \frac{2\mu(y)}{\sigma^2(y)}\,dy\right) = \exp\!\left(-\int^x \frac{2\kappa(\theta - y)}{\xi^2 y}\,dy\right)
    $$

    Computing the integral inside the exponential:

    $$
    \int \frac{2\kappa(\theta - y)}{\xi^2 y}\,dy = \frac{2\kappa\theta}{\xi^2}\ln y - \frac{2\kappa}{\xi^2}y
    $$

    Therefore

    $$
    s'(x) = x^{-2\kappa\theta/\xi^2}\,e^{2\kappa x/\xi^2} = x^{-\nu}\,e^{2\kappa x/\xi^2}
    $$

    where $\nu = 2\kappa\theta/\xi^2$.

    **Integrability near $x = 0$.** Near $x = 0$, the exponential factor $e^{2\kappa x/\xi^2} \to 1$, so $s'(x) \sim x^{-\nu}$. Integrating from $0$ to some $c > 0$:

    $$
    \int_0^c s'(x)\,dx \sim \int_0^c x^{-\nu}\,dx
    $$

    This integral converges if and only if $-\nu > -1$, i.e., $\nu < 1$, which means $2\kappa\theta < \xi^2$ (Feller condition violated).

    - When **$\nu \geq 1$** (Feller condition holds): $\int_0^c s'(x)\,dx = \infty$, meaning $s(0^+) = -\infty$. The boundary $x = 0$ is not reachable in natural scale --- it is an entrance boundary.
    - When **$\nu < 1$** (Feller condition violated): $\int_0^c s'(x)\,dx < \infty$, meaning $s(0^+)$ is finite. The boundary is reachable in finite time --- it is a regular boundary.

    Thus the integrability of the scale function near the origin is directly equivalent to the Feller condition.

---

**Exercise 6.** In the multidimensional setting (e.g., the Heston model), the Feller condition applies to each CIR-type component independently. For a two-factor model on $\mathbb{R}_+^2$ where $V_t^{(1)}$ satisfies the Feller condition but $V_t^{(2)}$ does not, describe the behavior of the process near the boundary $V_t^{(2)} = 0$ while $V_t^{(1)} > 0$. Does the overall model remain well-defined?

??? success "Solution to Exercise 6"
    In the two-factor model on $\mathbb{R}_+^2$, each component $V_t^{(i)}$ satisfies its own CIR-type dynamics with parameters $(\kappa_i, \theta_i, \xi_i)$ and its own Feller condition $2\kappa_i\theta_i \geq \xi_i^2$.

    **Behavior near $V_t^{(2)} = 0$ while $V_t^{(1)} > 0$.** Since $V_t^{(1)}$ satisfies the Feller condition, it remains strictly positive for all time, so the process never approaches the corner $(0, 0)$. Meanwhile, $V_t^{(2)}$ violates the Feller condition, so it reaches the boundary $V^{(2)} = 0$ in finite time with positive probability. At this boundary, the diffusion of the second component vanishes but the drift $\kappa_2\theta_2 > 0$ immediately pushes $V_t^{(2)}$ back into the interior. The process touches the face $\{V^{(2)} = 0, V^{(1)} > 0\}$ and is instantly reflected.

    **Well-posedness.** The overall model remains well-defined. Each CIR-type component is individually well-posed:

    - If the Feller condition holds, the component stays strictly positive and has a smooth transition density on $(0, \infty)$.
    - If the Feller condition is violated but $\kappa_i\theta_i > 0$, the component has a reflecting boundary at zero and is still a well-defined strong solution to the SDE. The transition measure has an atom at zero but the process is not absorbed.

    The fact that one component touches zero does not affect the well-posedness of the other components (assuming the cross-component coupling preserves the affine structure, e.g., the drift of $V^{(1)}$ at $V^{(2)} = 0$ remains nonnegative). The overall process lives on $\mathbb{R}_+^2$ and is a valid affine process, with a transition measure that is smooth in the $V^{(1)}$ direction but has a possible atom at zero in the $V^{(2)}$ direction. The Riccati ODE system and Fourier pricing machinery remain fully valid regardless of whether individual components satisfy the Feller condition.
