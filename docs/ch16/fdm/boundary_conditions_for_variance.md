# Boundary Conditions for Variance

The Heston PDE is solved on a bounded domain $[x_{\min}, x_{\max}] \times [0, v_{\max}]$, and each of the four edges requires a boundary condition. The stock-price boundaries ($x_{\min}$ and $x_{\max}$) are handled similarly to one-dimensional Black-Scholes, but the **variance boundaries** are qualitatively different. At $v = 0$, the PDE **degenerates**---the second-order variance diffusion term vanishes---and the appropriate boundary condition depends on the Feller condition. At $v = v_{\max}$, the solution must be insensitive to the artificial truncation of the variance domain. Getting these conditions right is essential for accuracy and stability of any finite difference scheme.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the reduced PDE at $v = 0$ when the Feller condition holds
    2. Choose appropriate boundary conditions at $v = v_{\max}$
    3. Apply standard Dirichlet/Neumann conditions at the stock-price boundaries
    4. Handle the corner points where two boundaries meet

!!! tip "Prerequisites"
    This section requires the [2D PDE formulation](two_dimensional_pde_formulation.md) and the [Feller condition](../model_definition/feller_condition_and_boundary.md).

---

## The Variance Boundary at v = 0

### PDE Degeneracy

Recall (see [§ Two-Dimensional PDE Formulation](two_dimensional_pde_formulation.md)) the Heston PDE in $(x, v)$. At $v = 0$, every term multiplied by $v$ vanishes, leaving the **reduced PDE**:

$$
\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

This is a **first-order** PDE in $v$---the diffusion in the variance direction disappears entirely. The drift term $\kappa\theta > 0$ pushes the variance away from zero (Feller-driven dynamics; see [§ Feller condition](../model_definition/feller_condition_and_boundary.md)), so information flows **into** the domain from the $v = 0$ boundary.

### Feller Condition Holds: No Boundary Condition Needed

When $2\kappa\theta \geq \xi^2$, the continuous-time CIR process never reaches zero (see [§ CIR variance solution](../variance_dynamics/cir_variance_process_solution.md)). The reduced PDE at $v = 0$ is a well-posed first-order equation with an outward-pointing drift ($\kappa\theta > 0$), meaning the characteristics flow from $v = 0$ into the interior. In this case:

- **No boundary condition is needed** at $v = 0$ in the PDE sense (the problem is well-posed without one)
- The reduced PDE itself serves as the "boundary condition" by providing the equation that $V$ must satisfy on this edge
- In the finite difference implementation, the reduced PDE replaces the full PDE at the $v = 0$ grid row

The discrete approximation at $j = 0$ uses **one-sided (upwind) differences** for $\partial V / \partial v$ since the drift is positive:

$$
\frac{\partial V}{\partial v}\bigg|_{v=0} \approx \frac{V_{i,1} - V_{i,0}}{v_1 - v_0}
$$

### Feller Condition Violated

When $2\kappa\theta < \xi^2$, the variance process can reach zero. The boundary at $v = 0$ becomes **attainable**, and additional care is required:

- The reduced PDE still applies at $v = 0$ (the diffusion terms still vanish)
- The drift $\kappa\theta$ remains positive, so the behavior is similar: the characteristic still points inward
- Some implementations use an **absorbing** condition ($V$ computed from the reduced PDE) or a **reflecting** condition (extrapolation from interior points)

In practice, the difference between the Feller-satisfied and Feller-violated cases at $v = 0$ is modest for European options, because the option value is a smooth function of $v$ even at $v = 0$.

!!! note "Why the PDE Degeneracy Matters"
    Standard second-order finite differences require two neighboring points in each direction. At $v = 0$, the absence of a second-order term in $v$ means there is no $V_{i,-1}$ to worry about, and the first-order upwind scheme is both natural and correctly captures the physics of the CIR process.

---

## The Variance Boundary at v = v_max

At $v = v_{\max}$, the truncation is artificial---the true domain extends to $v = \infty$. The boundary condition should make the numerical solution insensitive to the choice of $v_{\max}$ provided it is large enough.

### Neumann Condition

The simplest and most common choice is a **zero-Neumann** (zero second derivative) condition:

$$
\frac{\partial^2 V}{\partial v^2}\bigg|_{v = v_{\max}} = 0
$$

This is equivalent to linear extrapolation from the interior:

$$
V_{i, N_v} = 2 V_{i, N_v - 1} - V_{i, N_v - 2}
$$

### Asymptotic Condition

For large $v$, the option price approaches a limiting form. For a European call as $v \to \infty$:

$$
V(t, S, v) \to S e^{-q(T-t)}
$$

because when volatility is infinite, the call is almost surely in-the-money at expiry. This **Dirichlet** condition is more accurate than Neumann for very large $v_{\max}$ but less commonly used in practice because it requires $v_{\max}$ to be genuinely large.

### Practical Recommendation

Use $v_{\max} = 5\theta$ to $10\theta$ with the Neumann condition. For typical Heston parameters ($\theta = 0.04$), this gives $v_{\max} = 0.20$ to $0.40$, which is sufficient for the option value to be nearly linear in $v$ at the boundary.

---

## Stock Price Boundaries

### At x_min (S close to 0)

For a European call, as $S \to 0$ (equivalently $x \to -\infty$), the option value approaches zero:

$$
V(t, x, v) \to 0 \quad \text{as } x \to x_{\min}
$$

This is a **Dirichlet** condition. For a European put, the corresponding condition is:

$$
V(t, x, v) \to K e^{-r(T-t)} - S e^{-q(T-t)} \quad \text{as } x \to x_{\min}
$$

### At x_max (S large)

For a European call as $S \to \infty$:

$$
V(t, x, v) \to S e^{-q(T-t)} - K e^{-r(T-t)} \quad \text{as } x \to x_{\max}
$$

For a put, $V \to 0$.

Alternatively, a **Neumann condition** $\partial V / \partial x |_{x_{\max}} = e^{x_{\max}} e^{-q(T-t)}$ (for a call) can be used, which is less sensitive to the exact choice of $x_{\max}$.

---

## Corner Points

The four corners of the computational domain---$(x_{\min}, 0)$, $(x_{\max}, 0)$, $(x_{\min}, v_{\max})$, $(x_{\max}, v_{\max})$---require special treatment because two boundary conditions meet.

The standard approach is to **prioritize the stock-price boundary** over the variance boundary:

| Corner | Condition |
|--------|-----------|
| $(x_{\min}, 0)$ | $V = 0$ (call) or $V = Ke^{-r\tau} - Se^{-q\tau}$ (put) |
| $(x_{\max}, 0)$ | $V = Se^{-q\tau} - Ke^{-r\tau}$ (call) or $V = 0$ (put) |
| $(x_{\min}, v_{\max})$ | $V = 0$ (call) or $V = Ke^{-r\tau} - Se^{-q\tau}$ (put) |
| $(x_{\max}, v_{\max})$ | $V = Se^{-q\tau} - Ke^{-r\tau}$ (call) or $V = 0$ (put) |

These are determined by the dominant behavior of the payoff in the respective limit.

---

## Boundary Condition Summary

The following table collects all boundary conditions for a European call:

| Boundary | Type | Condition |
|----------|------|-----------|
| $v = 0$ | Reduced PDE | $V_t + (r-q)V_x + \kappa\theta V_v - rV = 0$ |
| $v = v_{\max}$ | Neumann | $V_{vv} = 0$ (linear extrapolation) |
| $x = x_{\min}$ | Dirichlet | $V = 0$ |
| $x = x_{\max}$ | Dirichlet | $V = e^{x-q\tau} - Ke^{-r\tau}$ |

For a put, replace the Dirichlet values accordingly.

---

## Worked Example

Consider an ATM European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$, $q = 0$, and Heston parameters $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

**Feller ratio**: $2\kappa\theta/\xi^2 = 0.12/0.09 \approx 1.33 > 1$ --- Feller holds.

**At $v = 0$, the reduced PDE becomes:**

$$
\frac{\partial V}{\partial t} + 0.05 \frac{\partial V}{\partial x} + 0.06 \frac{\partial V}{\partial v} - 0.05 V = 0
$$

The positive coefficient $\kappa\theta = 0.06$ on $V_v$ confirms the upwind direction: the drift pushes variance away from zero.

??? example "Sensitivity to v_max"
    Testing the HV ADI scheme with grid $100 \times 50$:

    | $v_{\max}$ | ATM call price | Error vs Fourier |
    |-----------|:--------------:|:----------------:|
    | $0.10$ | $\$10.29$ | $\$0.07$ |
    | $0.20$ | $\$10.35$ | $\$0.01$ |
    | $0.40$ | $\$10.36$ | $< \$0.01$ |
    | $0.80$ | $\$10.36$ | $< \$0.01$ |

    With $v_{\max} = 5\theta = 0.20$, the boundary truncation error is already within $\$0.01$. Increasing $v_{\max}$ beyond $10\theta$ wastes grid points without improving accuracy.

---

## Summary

Boundary conditions for the Heston PDE require careful treatment at all four edges. The most distinctive feature is the **degeneracy at $v = 0$**, where the PDE reduces to first order and the Feller condition determines the nature of the boundary. When Feller holds, the reduced PDE itself serves as the boundary condition with an upwind discretization. At $v = v_{\max}$, a Neumann condition with $v_{\max} = 5$--$10\theta$ is sufficient. Stock-price boundaries use standard Dirichlet conditions from the asymptotic behavior of the payoff. Corner points are determined by the dominant stock-price limit. These conditions are incorporated into the [ADI schemes](adi_schemes.md) at each implicit sweep.

---

## Exercises

**Exercise 1.**
At $v = 0$, the Heston PDE reduces to $\partial V / \partial t + (r - q)\partial V / \partial x + \kappa\theta \partial V / \partial v - rV = 0$. Explain why the second-derivative terms vanish. If $\kappa\theta > 0$ (Feller satisfied), the term $\kappa\theta \partial V / \partial v$ pushes information into the domain. Discretize this reduced PDE using forward differences in $v$ and central differences in $x$.

??? success "Solution to Exercise 1"
    **Why second-derivative terms vanish.** In the Heston PDE:

    $$
    \frac{\partial V}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV = 0
    $$

    every second-order diffusion term carries a factor of $v$: the $\partial^2 V / \partial x^2$ term has coefficient $v/2$, the $\partial^2 V / \partial v^2$ term has coefficient $\xi^2 v / 2$, and the mixed derivative has coefficient $\rho \xi v$. This is because all diffusion in the Heston model is driven by $\sqrt{v}$---the stock diffusion is $\sqrt{v} S \, dW^{(1)}$ and the variance diffusion is $\xi \sqrt{v} \, dW^{(2)}$. At $v = 0$, the noise vanishes identically, and the system becomes deterministic. Setting $v = 0$, the surviving terms are:

    $$
    \frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
    $$

    Note that the drift $\kappa(\theta - v)|_{v=0} = \kappa\theta > 0$ (assuming $\theta > 0$), so the variance drift pushes away from zero.

    **Discretization of the reduced PDE.** Using forward (upwind) differences in $v$ and central differences in $x$ on a non-uniform grid:

    $$
    \frac{\partial V}{\partial v}\bigg|_{i,0} \approx \frac{V_{i,1} - V_{i,0}}{v_1 - v_0} = \frac{V_{i,1} - V_{i,0}}{\Delta v_0^+}
    $$

    This is a first-order upwind approximation, appropriate because the drift $\kappa\theta > 0$ carries information from $v = 0$ into the interior. A backward difference would be inappropriate as there is no grid point at $v < 0$.

    For the $x$-derivative, central differences are used:

    $$
    \frac{\partial V}{\partial x}\bigg|_{i,0} \approx \frac{V_{i+1,0} - V_{i-1,0}}{x_{i+1} - x_{i-1}}
    $$

    The fully discretized reduced PDE at grid point $(i, 0)$ in backward time $\tau = T - t$ is:

    $$
    \frac{V_{i,0}^{n+1} - V_{i,0}^n}{\Delta\tau} = (r - q)\frac{V_{i+1,0}^{n+1} - V_{i-1,0}^{n+1}}{x_{i+1} - x_{i-1}} + \kappa\theta \frac{V_{i,1}^{n+1} - V_{i,0}^{n+1}}{\Delta v_0^+} - r V_{i,0}^{n+1}
    $$

    where the right-hand side is evaluated implicitly (or with the appropriate $\theta$-weighting for the ADI scheme). This equation replaces the full Heston PDE at the $j = 0$ boundary row.

---

**Exercise 2.**
At $v = v_{\max}$, a Neumann condition $\partial^2 V / \partial v^2 = 0$ (linear extrapolation) is commonly used. With $v_{\max} = 5\theta$ and $\theta = 0.04$, we have $v_{\max} = 0.20$. For a European call, explain why the option value is approximately linear in $v$ for large $v$. What error is introduced if $v_{\max}$ is too small?

??? success "Solution to Exercise 2"
    **Linear behavior of option price in $v$ for large $v$.** For a European call, the Black-Scholes price in the limit of large volatility satisfies:

    $$
    \lim_{\sigma \to \infty} C_{\text{BS}}(S, K, T, r, \sigma) = S e^{-qT}
    $$

    In the Heston model, the effective integrated variance over $[t, T]$ scales approximately as $v$ when $v$ is large (the mean-reverting drift $\kappa(\theta - v)$ is overwhelmed by the current level). Thus for large $v$:

    $$
    V(t, S, v) \approx S e^{-q(T-t)} - K e^{-r(T-t)} \cdot \Phi(d_2(v))
    $$

    where $d_2(v) \to \infty$ as $v \to \infty$, giving $\mathcal{N}(d_2) \to 1$. The call value saturates at $S e^{-qT} - Ke^{-rT}$ (the forward value minus the discounted strike), and the dependence on $v$ becomes negligible. In the transition region, $V$ is approximately linear in $v$ because the dominant sensitivity is:

    $$
    \frac{\partial V}{\partial v} \approx \text{vega} / (2\sqrt{v})
    $$

    which varies slowly for large $v$, making $V$ nearly affine in $v$.

    **Error from $v_{\max}$ too small.** If $v_{\max}$ is chosen too small, the Neumann condition $\partial^2 V / \partial v^2 = 0$ is imposed where the solution is still genuinely curved in $v$. This forces a linear extrapolation from the interior onto a region where the true solution has significant curvature, introducing an artificial boundary layer.

    The error manifests as:

    - A systematic bias in the option price (typically underpricing, because the Neumann condition underestimates the contribution of high-variance paths)
    - The bias propagates inward through the diffusion operator over multiple time steps
    - With $\theta = 0.04$, the CIR stationary distribution has 99th percentile at approximately $v \approx 3\theta$ to $5\theta$, so $v_{\max} < 3\theta$ would truncate a significant fraction of the probability mass

---

**Exercise 3.**
At $x = x_{\min}$ (very low stock price), the call value is approximately zero: $V(x_{\min}, v, t) = 0$. At $x = x_{\max}$ (very high stock price), the call value approaches $S - Ke^{-r(T-t)}$. Verify these conditions for $K = 100$, $r = 3\%$, $T = 1$, and $x_{\max} = \ln(500)$. Are these Dirichlet conditions exact or approximate?

??? success "Solution to Exercise 3"
    **Verification of stock-price boundary conditions.**

    Given: $K = 100$, $r = 0.03$, $T = 1$, $x_{\max} = \ln(500) \approx 6.2146$, so $S_{\max} = 500$.

    **At $x = x_{\min}$ (call value $\approx 0$).** For very small $S$ (say $S < 1$), the call payoff $(S_T - K)^+$ is nearly zero because the stock would need to increase by more than $100\times$ to finish in-the-money. Under any reasonable model, this probability is negligible, so $V(x_{\min}, v, t) = 0$ is an excellent approximation. This is **approximate**, not exact: there is always a tiny positive probability of a large upward move, but the approximation error is of order $e^{x_{\min}} \ll 1$.

    **At $x = x_{\max}$ (call value $\approx S - Ke^{-r\tau}$).** For $S = 500$ and $\tau = T - t$:

    $$
    V(t, x_{\max}, v) \approx 500 e^{-q\tau} - 100 e^{-0.03\tau}
    $$

    At $t = 0$ ($\tau = 1$) with $q = 0$: $V \approx 500 - 100 e^{-0.03} = 500 - 97.04 = 402.96$.

    This is also **approximate**. The exact call value for $S = 500$ includes a small correction from the possibility that $S_T < K$, but with $S/K = 5$ this probability is negligible. The relative error in the boundary condition is:

    $$
    \frac{|V_{\text{exact}} - V_{\text{BC}}|}{V_{\text{exact}}} \lesssim \Phi\!\left(\frac{-\ln(S/K) - (r - v/2)T}{\sqrt{vT}}\right)
    $$

    For $S/K = 5$, $v = 0.04$, $T = 1$: the argument of $\Phi$ is approximately $\frac{-1.609 - 0.03}{0.2} \approx -8.2$, giving a relative error of order $10^{-16}$---essentially machine precision.

    **Conclusion:** Both conditions are approximate in principle but exact to machine precision for reasonable choices of $x_{\min}$ and $x_{\max}$ (6--8 standard deviations from the log-strike).

---

**Exercise 4.**
When the Feller condition is violated ($2\kappa\theta < \xi^2$), the variance process can hit zero. Discuss two approaches to the $v = 0$ boundary: (a) still use the reduced PDE (ignoring the violation), (b) impose $V(x, 0, t) = V^{\text{BS}}(x, 0, t)$ (Black-Scholes value at zero vol). Which approach is more physically motivated?

??? success "Solution to Exercise 4"
    **Two approaches when the Feller condition is violated** ($2\kappa\theta < \xi^2$):

    **(a) Use the reduced PDE at $v = 0$.**

    The reduced PDE $\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta \frac{\partial V}{\partial v} - rV = 0$ is obtained by setting $v = 0$ in the Heston PDE. This is valid regardless of the Feller condition because the diffusion terms vanish at $v = 0$ purely as a consequence of the $v$-dependence of the coefficients. The drift $\kappa\theta > 0$ still pushes variance into the interior.

    When Feller is violated, the CIR process reaches $v = 0$ with positive probability, but the process is **instantaneously reflecting** (the drift immediately pushes $v$ back up). The reduced PDE captures this behavior: the first-order equation with positive $v$-drift acts as a natural reflecting boundary.

    **(b) Impose Black-Scholes at zero volatility: $V(x, 0, t) = V^{\text{BS}}(x, 0, t)$.**

    At $v = 0$, if variance were to remain at zero forever, the stock price would grow deterministically at rate $r - q$, and the option value would be $V^{\text{BS}}(S, 0) = (S e^{-q\tau} - Ke^{-r\tau})^+$ for a call. This is a Dirichlet condition.

    **Which is more physically motivated?** Approach (a) is more physically motivated for the following reasons:

    1. **Consistency with the SDE.** The reduced PDE is derived directly from the Heston PDE by evaluating at $v = 0$. It makes no assumption about future variance paths---only that variance is currently zero. The $\kappa\theta V_v$ term correctly encodes that variance will increase immediately.

    2. **Approach (b) assumes $v$ stays at zero.** The Black-Scholes value at $\sigma = 0$ assumes zero volatility for all future time, which contradicts the CIR dynamics: even if $v$ hits zero, mean reversion pulls it back up. This makes approach (b) overly pessimistic for calls (underpricing) and overly optimistic for puts.

    3. **Numerical smoothness.** The reduced PDE provides a smooth transition between the $v > 0$ interior and the $v = 0$ boundary. The Dirichlet approach (b) can introduce a discontinuity in $\partial V / \partial v$ at $v = 0$, which may cause spurious oscillations.

    In practice, both approaches give similar results for European options because the CIR process spends very little time at $v = 0$ (even when Feller is violated), but approach (a) is theoretically cleaner and more robust.

---

**Exercise 5.**
Corner points where two boundaries meet (e.g., $v = 0$ and $x = x_{\min}$) require special treatment. For a European call at $(x_{\min}, 0)$, both the stock-price condition ($V = 0$) and the reduced PDE condition apply. Show that they are consistent: if $V = 0$ for all $x \leq x_{\min}$, then all derivatives of $V$ at $x_{\min}$ vanish, satisfying the reduced PDE trivially.

??? success "Solution to Exercise 5"
    **Consistency at the corner $(x_{\min}, 0)$ for a European call.**

    At $x = x_{\min}$ (very low stock price), the Dirichlet condition states $V(x_{\min}, v, t) = 0$ for all $v$ and $t$. We need to show that this is consistent with the reduced PDE at $v = 0$.

    If $V = 0$ for all $x \leq x_{\min}$ (and in particular at $x = x_{\min}$), then at the point $(x_{\min}, 0)$:

    $$
    V(x_{\min}, 0, t) = 0 \quad \text{for all } t
    $$

    **Time derivative:**

    $$
    \frac{\partial V}{\partial t}\bigg|_{(x_{\min}, 0)} = \frac{\partial}{\partial t} [0] = 0
    $$

    **$x$-derivative:** Since $V(x, v, t) \to 0$ as $x \to x_{\min}$ for all $v$ and $t$ (the call is worthless for very small $S$), and $V \geq 0$, the boundary value $V = 0$ is a minimum. At the boundary itself:

    $$
    \frac{\partial V}{\partial x}\bigg|_{(x_{\min}, 0)} = 0
    $$

    This holds because $V(x_{\min}, v, t) = 0$ for all $v$, and $V(x, 0, t)$ approaches zero smoothly from the interior.

    **$v$-derivative:** Since $V(x_{\min}, v, t) = 0$ for all $v$ (the stock-price boundary condition holds across all variance levels):

    $$
    \frac{\partial V}{\partial v}\bigg|_{(x_{\min}, 0)} = 0
    $$

    **Kill term:** $rV = r \cdot 0 = 0$.

    Substituting into the reduced PDE:

    $$
    \frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0 + (r-q) \cdot 0 + \kappa\theta \cdot 0 - 0 = 0
    $$

    The reduced PDE is satisfied trivially. Thus the stock-price Dirichlet condition $V = 0$ and the reduced PDE boundary condition are perfectly consistent at the corner $(x_{\min}, 0)$.

    **Remark.** The same argument applies at $(x_{\max}, 0)$ for a put (where $V = 0$). For the corners where $V \neq 0$ (e.g., $(x_{\min}, 0)$ for a put, where $V = Ke^{-r\tau} - Se^{-q\tau}$), consistency requires verifying that the time derivatives of the Dirichlet condition match the reduced PDE---this also holds because the Dirichlet values are explicit functions of $\tau$ whose derivatives are known.

---

**Exercise 6.**
Design a sensitivity test: compute the European call price with $v_{\max} = 3\theta, 5\theta, 10\theta, 20\theta$ (keeping all other grid parameters fixed) and measure the convergence of the price. At what value of $v_{\max}$ does the price stabilize to 4 significant digits? Why does choosing $v_{\max}$ too large waste grid points?

??? success "Solution to Exercise 6"
    **Sensitivity test design.** Fix the spatial grid at $N_x = 100$, $N_v = 50$, and $N_t = 100$. Use the Hundsdorfer-Verwer ADI scheme with $\theta = 1/2$. Use the standard Heston parameters: $S_0 = K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $T = 1$.

    **Test grid.** For each $v_{\max}$, keep $N_v = 50$ fixed and distribute the grid points over $[0, v_{\max}]$:

    | $v_{\max}$ | $v_{\max}/\theta$ | Grid spacing $\Delta v$ (uniform) |
    |:---------:|:-----------------:|:------:|
    | $0.12$ | 3 | $0.0024$ |
    | $0.20$ | 5 | $0.0040$ |
    | $0.40$ | 10 | $0.0080$ |
    | $0.80$ | 20 | $0.0160$ |

    **Expected results.** Based on the CIR stationary distribution with parameters $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, the variance is Gamma-distributed with shape $\alpha = 2\kappa\theta/\xi^2 \approx 1.33$ and scale $\beta = \xi^2/(2\kappa) = 0.03$. The tail probabilities are:

    $$
    \mathbb{P}(v > v_{\max}) \approx 1 - F_{\text{Gamma}}(v_{\max}; \alpha, \beta)
    $$

    - $v_{\max} = 0.12$: $\mathbb{P}(v > 0.12) \approx 2\%$---noticeable truncation error
    - $v_{\max} = 0.20$: $\mathbb{P}(v > 0.20) \approx 0.1\%$---small truncation error
    - $v_{\max} = 0.40$: $\mathbb{P}(v > 0.40) < 0.001\%$---negligible
    - $v_{\max} = 0.80$: effectively zero truncation

    **Convergence.** The ATM call price should stabilize to 4 significant digits by $v_{\max} = 5\theta = 0.20$. This is consistent with the worked example in the text, which shows error within $\$0.01$ at $v_{\max} = 0.20$.

    **Why $v_{\max}$ too large wastes grid points.** With $N_v$ fixed, increasing $v_{\max}$ stretches the grid spacing $\Delta v$ over a larger domain. The regions that matter most (near $v_0 = 0.04$ and $v = 0$) receive fewer grid points, degrading accuracy where it counts. With a uniform grid and $v_{\max} = 20\theta = 0.80$:

    - Only $\approx 5\%$ of grid points ($\approx 2$--$3$ points) fall in $[0, 0.04]$, the region of highest sensitivity
    - The remaining 95% of grid points cover $[0.04, 0.80]$, a region where the solution is smooth and nearly linear in $v$

    With a non-uniform (sinh) grid this waste is mitigated, but the fundamental issue remains: each additional grid point in the tail of the variance distribution contributes negligibly to accuracy. The optimal strategy is to choose $v_{\max}$ just large enough (5--10$\theta$) and concentrate grid points in the important region.
