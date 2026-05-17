# Feller Condition and Boundary Behavior

The variance process in the Heston model follows a CIR diffusion on $[0, \infty)$, and the boundary at $v = 0$ plays a special role. Whether the process can reach zero, and what happens if it does, depends on a single inequality involving the parameters $\kappa$, $\theta$, and $\sigma_v$. This inequality -- the **Feller condition** -- determines the qualitative behavior of the variance path: either it stays strictly positive for all time, or it touches zero with positive probability. Understanding this boundary behavior is essential for simulation (how to handle $v_t = 0$), for PDE pricing (what boundary condition to impose at $v = 0$), and for calibration (most calibrated parameters violate the Feller condition).

This section states and proves the Feller condition, classifies the zero boundary using Feller's boundary theory, and discusses the practical implications. We assume familiarity with the Heston SDE from the [preceding section](heston_sde_and_parameters.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the Feller condition and compute the Feller ratio for given parameters
    - Prove that $2\kappa\theta \geq \sigma_v^2$ implies strict positivity of the CIR process
    - Classify the $v = 0$ boundary as entrance or regular using Feller's boundary taxonomy
    - Explain the difference between reflection and absorption at zero
    - Describe the practical implications for Monte Carlo simulation and finite difference methods

---

## The Feller Condition

### Intuition

The CIR variance process $dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t$ has two competing forces near $v = 0$. The mean-reversion drift $\kappa(\theta - v_t) \to \kappa\theta > 0$ pushes the process away from zero. The diffusion $\sigma_v\sqrt{v_t} \to 0$ vanishes at zero. If the drift is strong enough relative to the diffusion, the process is pushed away from zero before the diffusion can bring it there. The Feller condition quantifies "strong enough."

### Statement and Proof

!!! success "Theorem: Feller Condition"
    Consider the CIR process:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t, \qquad v_0 > 0
    $$

    with $\kappa > 0$, $\theta > 0$, $\sigma_v > 0$.

    1. If $2\kappa\theta \geq \sigma_v^2$ (Feller condition satisfied), then $v_t > 0$ a.s. for all $t > 0$
    2. If $2\kappa\theta < \sigma_v^2$ (Feller condition violated), then $\mathbb{P}(v_t = 0 \text{ for some } t > 0) > 0$

    In both cases, $v_t \geq 0$ a.s. for all $t \geq 0$.

**Proof (sketch for part 1).** Recall (see [§ CIR Variance Process Solution](../variance_dynamics/cir_variance_process_solution.md)): the CIR process is a deterministically time-changed squared Bessel process of dimension $\delta = 4\kappa\theta/\sigma_v^2$. A squared Bessel process of dimension $\delta \geq 2$ never reaches zero, and $\delta \geq 2 \Longleftrightarrow 2\kappa\theta \geq \sigma_v^2$. When $\delta < 2$, the boundary is hit with positive probability. $\square$

!!! info "Definition: Feller Ratio"
    The **Feller ratio** is defined as:

    $$
    F = \frac{2\kappa\theta}{\sigma_v^2}
    $$

    The Feller condition is $F \geq 1$. Equivalently, the CIR dimension parameter $\delta = 2F$, and the condition $\delta \geq 2$ is the boundary for strict positivity.

---

## Feller's Boundary Classification

### Overview of Boundary Types

Feller's boundary classification for one-dimensional diffusions on $(0, \infty)$ categorizes the boundary $v = 0$ based on two questions: (1) can the process reach the boundary in finite time? (2) if it reaches the boundary, can it leave? This leads to four boundary types.

| Boundary Type | Reachable? | Can Leave? | Behavior |
|:---|:---:|:---:|:---|
| Natural | No | N/A | Process never reaches boundary |
| Entrance | No | N/A | Process can start from boundary but never returns |
| Exit | Yes | No | Process reaches boundary and is absorbed |
| Regular | Yes | Yes | Process reaches boundary and can be reflected or absorbed |

### Scale Function and Speed Measure

For a one-dimensional diffusion $dv_t = \mu(v)\,dt + \sigma(v)\,dW_t$ on $(0, \infty)$, the boundary classification is determined by the **scale function** $s(v)$ and the **speed measure** $m(v)$.

The scale function derivative is:

$$
s'(v) = \exp\!\left(-\int^v \frac{2\mu(y)}{\sigma^2(y)}\,dy\right)
$$

For the CIR process with $\mu(v) = \kappa(\theta - v)$ and $\sigma^2(v) = \sigma_v^2 v$:

$$
s'(v) = \exp\!\left(-\int^v \frac{2\kappa(\theta - y)}{\sigma_v^2 y}\,dy\right) = \exp\!\left(-\frac{2\kappa\theta}{\sigma_v^2}\ln v + \frac{2\kappa}{\sigma_v^2}v\right) = v^{-\delta/2}\,\exp\!\left(\frac{2\kappa}{\sigma_v^2}v\right)
$$

where $\delta = 4\kappa\theta/\sigma_v^2$. The speed measure density is:

$$
m(v) = \frac{1}{\sigma^2(v)\,s'(v)} = \frac{1}{\sigma_v^2 v}\,v^{\delta/2}\,\exp\!\left(-\frac{2\kappa}{\sigma_v^2}v\right) = \frac{v^{\delta/2 - 1}}{\sigma_v^2}\,\exp\!\left(-\frac{2\kappa}{\sigma_v^2}v\right)
$$

### Boundary Classification for the CIR Process

The boundary at $v = 0$ is classified by the integrability of $s'$ and $m$ near zero.

!!! success "Theorem: CIR Boundary Classification at v = 0"
    For the CIR process with Feller dimension $\delta = 4\kappa\theta/\sigma_v^2$:

    - **If $\delta \geq 2$ (Feller condition satisfied):** The boundary $v = 0$ is an **entrance boundary**. The process can start from $v = 0$ and immediately enter $(0, \infty)$, but it can never reach $v = 0$ from the interior. No boundary condition is needed.

    - **If $1 \leq \delta < 2$:** The boundary $v = 0$ is **regular** and **instantaneously reflecting**. The process reaches $v = 0$ with positive probability but is immediately pushed back into $(0, \infty)$ by the drift $\kappa\theta > 0$.

    - **If $0 < \delta < 1$:** The boundary $v = 0$ is **regular**. Without specifying a boundary condition, the behavior is ambiguous; the standard CIR convention is instantaneous reflection.

**Proof (entrance case).** When $\delta \geq 2$, the scale function near zero satisfies $s'(v) \sim v^{-\delta/2}$ as $v \to 0^+$. Since $\delta/2 \geq 1$, we have $\int_0^{\epsilon} s'(v)\,dv = \infty$, which means the boundary is unattainable. The speed measure satisfies $m(v) \sim v^{\delta/2 - 1}/\sigma_v^2$ near zero. Since $\delta/2 - 1 \geq 0$, we have $\int_0^{\epsilon} m(v)\,dv < \infty$, which means the boundary is an entrance (not natural). $\square$

!!! warning "Feller Condition in Practice"
    In calibrated Heston models for equity indices, the Feller condition is almost always violated. Typical calibrated values give Feller ratios $F = 2\kappa\theta/\sigma_v^2$ in the range $0.3$--$0.8$. This means the variance process touches zero with positive probability, and simulation schemes must handle this gracefully.

---

## Reflection vs. Absorption at Zero

When the Feller condition is violated and the CIR process reaches $v = 0$, two possible behaviors can be imposed:

**Instantaneous reflection.** The process immediately bounces back into $(0, \infty)$. This is the natural behavior of the CIR process (without imposing any absorbing boundary condition) and is the standard convention in the Heston model. The drift $\kappa\theta > 0$ at $v = 0$ ensures the process cannot stay at zero.

**Absorption.** The process is killed upon reaching $v = 0$ (or remains at zero forever). This is not the standard CIR convention and would change the nature of the model fundamentally -- once variance is absorbed at zero, the asset price becomes deterministic.

!!! info "Definition: Reflecting CIR Process"
    The **reflecting CIR process** is the unique strong solution of:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t^+}\,dW_t, \qquad v_t \geq 0
    $$

    where $v_t^+ = \max(v_t, 0)$. The process satisfies $v_t \geq 0$ for all $t$ and, when $2\kappa\theta > 0$, spends zero Lebesgue time at $v = 0$ (the set $\{t : v_t = 0\}$ has measure zero).

---

## Implications for Simulation

Recall (see [§ Euler Discretization and Pitfalls](../monte_carlo/euler_discretization_and_pitfalls.md)): when the Feller condition is violated, Euler steps for the CIR variance can produce negative values, and remedies (full truncation, reflection, exact Broadie-Kaya, Andersen QE) trade off bias versus variance. The takeaway for this section is that boundary-touching variance paths are the rule rather than the exception in calibrated parameter sets, so the simulation scheme must accommodate them.

---

## Implications for PDE Methods

When solving the Heston PDE on a grid $(S, v) \in [0, S_{\max}] \times [0, v_{\max}]$, the boundary $v = 0$ requires special treatment.

At $v = 0$, the diffusion coefficient of the variance process vanishes, and the Heston PDE degenerates from a parabolic PDE to a first-order equation in $v$. The appropriate boundary condition depends on the Feller condition:

- **Feller condition satisfied ($\delta \geq 2$):** The boundary is entrance, so the process never reaches $v = 0$. The PDE solution is determined by the interior equation alone. In practice, one uses the degenerate PDE at $v = 0$:

$$
\frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \kappa\theta\frac{\partial V}{\partial v} = rV
$$

- **Feller condition violated ($\delta < 2$):** The boundary is regular-reflecting. The same degenerate PDE applies, because reflection is the natural boundary behavior.

!!! note "No Artificial Boundary Condition at v = 0"
    Unlike the boundaries at $S = 0$, $S = S_{\max}$, and $v = v_{\max}$ (which are artificial truncation boundaries requiring imposed conditions), the boundary $v = 0$ is a natural boundary of the CIR process. The correct treatment is to use the degenerate form of the PDE, not to impose an artificial Dirichlet or Neumann condition. This is discussed further in the [FDM boundary conditions section](../fdm/boundary_conditions_for_variance.md).

---

## Worked Example: Feller Ratio for Common Parameter Sets

??? example "Equity Index Parameters"
    | Parameter Set | $\kappa$ | $\theta$ | $\sigma_v$ | $F = 2\kappa\theta/\sigma_v^2$ | Feller? |
    |:---|:---:|:---:|:---:|:---:|:---:|
    | Moderate vol-of-vol | 2.0 | 0.04 | 0.3 | $2(2)(0.04)/0.09 = 1.78$ | Yes |
    | Typical calibrated | 2.0 | 0.04 | 0.5 | $2(2)(0.04)/0.25 = 0.64$ | No |
    | High vol-of-vol | 1.5 | 0.04 | 0.8 | $2(1.5)(0.04)/0.64 = 0.19$ | No |
    | Strong mean-reversion | 5.0 | 0.04 | 0.5 | $2(5)(0.04)/0.25 = 1.60$ | Yes |
    | Low theta | 2.0 | 0.01 | 0.3 | $2(2)(0.01)/0.09 = 0.44$ | No |

    The table illustrates that achieving $F \geq 1$ requires either low vol-of-vol, high mean-reversion speed, or high long-run variance -- combinations that are often incompatible with market-calibrated parameters. This is why the Feller condition is violated in most practical applications.

---

## Summary

The Feller condition $2\kappa\theta \geq \sigma_v^2$ is the threshold that determines whether the CIR variance process in the Heston model remains strictly positive. When satisfied, the zero boundary is an entrance boundary that the process never reaches. When violated, the process can touch zero but is instantaneously reflected by the drift. In practice, calibrated Heston parameters typically violate the Feller condition, making it essential to use simulation schemes that handle zero-touching variance gracefully and to apply the degenerate PDE (rather than an artificial boundary condition) at $v = 0$ in finite difference methods.

The [next section](moment_explosions_and_constraints.md) examines a different type of parameter constraint: the conditions under which moments of the asset price $\mathbb{E}[S_T^p]$ are finite.

---

## Exercises

**Exercise 1.** For $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.4$, check whether the Feller condition $2\kappa\theta \geq \sigma_v^2$ is satisfied. Repeat for $\sigma_v = 0.3$. In each case, describe the qualitative behavior of $V_t$ near zero.

??? success "Solution to Exercise 1"
    **Case 1: $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.4$.**

    $$
    2\kappa\theta = 2(1.5)(0.04) = 0.12
    $$

    $$
    \sigma_v^2 = (0.4)^2 = 0.16
    $$

    Since $0.12 < 0.16$, the Feller condition is **violated**. The Feller ratio is $F = 0.12/0.16 = 0.75$, and the CIR dimension is $\delta = 4\kappa\theta/\sigma_v^2 = 4(1.5)(0.04)/0.16 = 1.5 < 2$.

    Near $v = 0$, the drift $\kappa\theta = 0.06 > 0$ pushes the process upward, but the diffusion is strong enough relative to this drift that the process can reach zero. The boundary is regular and instantaneously reflecting: $V_t$ touches zero with positive probability but is immediately pushed back by the positive drift $\kappa\theta$. In simulation, Euler schemes may produce negative values.

    **Case 2: $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.3$.**

    $$
    2\kappa\theta = 0.12
    $$

    $$
    \sigma_v^2 = (0.3)^2 = 0.09
    $$

    Since $0.12 > 0.09$, the Feller condition is **satisfied**. The Feller ratio is $F = 0.12/0.09 \approx 1.33$, and $\delta = 4(1.5)(0.04)/0.09 \approx 2.67 > 2$.

    The boundary $v = 0$ is an entrance boundary: the process can never reach zero from the interior. The variance $V_t > 0$ almost surely for all $t > 0$. The drift at zero ($\kappa\theta = 0.06$) is strong enough relative to the diffusion to prevent the process from reaching the boundary. Simulation is straightforward since the probability of near-zero variance is very small.

---

**Exercise 2.** The dimension parameter of the CIR non-central chi-squared transition density is $\nu = 4\kappa\theta/\sigma_v^2$. Show that $\nu \geq 2$ is equivalent to the Feller condition. For $\nu < 2$, the density has a mass at $V_T = 0$; compute $\nu$ for $\kappa = 2$, $\theta = 0.02$, $\sigma_v = 0.5$.

??? success "Solution to Exercise 2"
    The CIR process $dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t$ has an exact transition density. Conditional on $V_t = v$, the distribution of $V_T$ (where $T > t$) is a scaled non-central chi-squared:

    $$
    V_T = \frac{\sigma_v^2(1 - e^{-\kappa(T-t)})}{4\kappa}\,\chi^2_\nu(\lambda)
    $$

    where $\chi^2_\nu(\lambda)$ denotes the non-central chi-squared distribution with $\nu$ degrees of freedom and non-centrality parameter $\lambda$. The dimension parameter is:

    $$
    \nu = \frac{4\kappa\theta}{\sigma_v^2}
    $$

    The Feller condition $2\kappa\theta \geq \sigma_v^2$ is equivalent to:

    $$
    \frac{4\kappa\theta}{\sigma_v^2} \geq 2 \qquad \Longleftrightarrow \qquad \nu \geq 2
    $$

    When $\nu \geq 2$, the non-central chi-squared density is continuous on $(0, \infty)$ with no mass at zero, confirming that $\mathbb{P}(V_T = 0) = 0$.

    When $\nu < 2$, the density has a **point mass at zero**: $\mathbb{P}(V_T = 0) > 0$. The chi-squared density with $\nu < 2$ degrees of freedom diverges as $V \to 0^+$, and the transition distribution has an atom at $V = 0$.

    For $\kappa = 2$, $\theta = 0.02$, $\sigma_v = 0.5$:

    $$
    \nu = \frac{4(2)(0.02)}{(0.5)^2} = \frac{0.16}{0.25} = 0.64
    $$

    Since $\nu = 0.64 < 2$, the Feller condition is violated. The transition density has a point mass at $V_T = 0$, and the variance process reaches zero with positive probability. The low value of $\nu$ indicates that the boundary-touching behavior is frequent.

---

**Exercise 3.** Explain why calibrated Heston parameters frequently violate the Feller condition. Give a typical set of calibrated parameters from equity markets and compute $2\kappa\theta$ vs $\sigma_v^2$.

??? success "Solution to Exercise 3"
    Calibrated Heston parameters frequently violate the Feller condition because the market-implied dynamics require a combination of parameters that is incompatible with $2\kappa\theta \geq \sigma_v^2$.

    **Why this happens:**

    1. **High vol-of-vol ($\sigma_v$) is needed to fit the smile.** The curvature of the implied volatility smile, especially for short maturities, requires a large $\sigma_v$ (typically $0.3$--$1.0$). This makes $\sigma_v^2$ large.

    2. **Moderate $\kappa\theta$ is needed to fit the term structure.** The long-run variance $\theta$ is determined by long-dated implied volatilities (typically $\theta \approx 0.03$--$0.06$). The mean-reversion speed $\kappa$ is constrained by the rate at which the smile flattens across maturities (typically $\kappa \approx 1$--$5$).

    3. **The product $2\kappa\theta$ is bounded.** With $\kappa \approx 2$ and $\theta \approx 0.04$, we get $2\kappa\theta = 0.16$, while $\sigma_v = 0.5$ gives $\sigma_v^2 = 0.25$, violating the condition.

    **Typical calibrated example (S&P 500):** $\kappa = 1.8$, $\theta = 0.035$, $\sigma_v = 0.55$, $\rho = -0.72$, $V_0 = 0.04$.

    $$
    2\kappa\theta = 2(1.8)(0.035) = 0.126
    $$

    $$
    \sigma_v^2 = (0.55)^2 = 0.3025
    $$

    The Feller ratio is $F = 0.126/0.3025 \approx 0.42$, far below 1. This is representative: in practice, Feller ratios of $0.3$--$0.8$ are the norm for equity indices. The market "demands" more vol-of-vol than is consistent with strict positivity of variance.

---

**Exercise 4.** In Euler discretization of the CIR process, the update $\hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t + \sigma_v\sqrt{\hat{V}_n}\sqrt{\Delta t}\,Z$ can produce negative values. Describe three remedies: full truncation, reflection, and the Higham-Mao scheme. Which preserves the correct mean?

??? success "Solution to Exercise 4"
    The Euler discretization of the CIR process is:

    $$
    \hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t + \sigma_v\sqrt{\hat{V}_n}\sqrt{\Delta t}\,Z_n, \qquad Z_n \sim N(0,1)
    $$

    When $\hat{V}_n$ is small and $\sigma_v$ is large, the Gaussian noise can drive $\hat{V}_{n+1} < 0$. Three remedies:

    **1. Full truncation (Higham and Mao, Lord et al.):**

    $$
    \hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_n^+)\Delta t + \sigma_v\sqrt{\hat{V}_n^+}\sqrt{\Delta t}\,Z_n
    $$

    where $V^+ = \max(V, 0)$. Both the drift and diffusion use the truncated value. If the result is negative, set $\hat{V}_{n+1} = 0$. This scheme has $O(\Delta t)$ weak convergence. It does **not** exactly preserve the correct mean because the truncation introduces a bias: the diffusion is suppressed when $V$ is near zero, making the process "stick" near zero slightly more than it should.

    **2. Reflection:**

    $$
    \hat{V}_{n+1} = \left|\hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t + \sigma_v\sqrt{\hat{V}_n}\sqrt{\Delta t}\,Z_n\right|
    $$

    Negative values are reflected to positive values via absolute value. This preserves $O(\Delta t)$ weak convergence. It approximately preserves the first moment because reflection maps $-\epsilon$ to $+\epsilon$, but introduces a small bias in the distribution near zero.

    **3. Higham-Mao implicit scheme:**

    $$
    \hat{V}_{n+1} = \hat{V}_n + \kappa(\theta - \hat{V}_{n+1})\Delta t + \sigma_v\sqrt{\hat{V}_n^+}\sqrt{\Delta t}\,Z_n
    $$

    Solving for $\hat{V}_{n+1}$:

    $$
    \hat{V}_{n+1} = \frac{\hat{V}_n + \kappa\theta\Delta t + \sigma_v\sqrt{\hat{V}_n^+}\sqrt{\Delta t}\,Z_n}{1 + \kappa\Delta t}
    $$

    The implicit treatment of the mean-reversion drift stabilizes the scheme. The denominator $1 + \kappa\Delta t > 1$ damps large fluctuations. This can still produce negative values but is more stable. Among these, the **full truncation scheme** is the most widely used in practice because it is simple and has been shown to achieve the best trade-off between bias and variance in empirical studies by Lord, Koekkoek, and van Dijk (2010).

    **Which preserves the correct mean?** None of the three exactly preserves $\mathbb{E}[\hat{V}_{n+1}] = \hat{V}_n + \kappa(\theta - \hat{V}_n)\Delta t$ because all modify the process near zero. The reflection scheme comes closest for the first moment, but the exact simulation methods (Broadie-Kaya, Andersen QE) are needed for unbiased moment matching.

---

**Exercise 5.** For the PDE pricing approach, the Heston PDE degenerates at $v = 0$ (the second-order term in $v$ vanishes). Explain why no boundary condition should be imposed at $v = 0$; instead, the PDE itself becomes a first-order equation. What boundary condition is appropriate at $v = v_{\max}$ (large $v$)?

??? success "Solution to Exercise 5"
    The Heston PDE for a European derivative $U(t, S, v)$ is:

    $$
    \frac{\partial U}{\partial t} + (r-q)S\frac{\partial U}{\partial S} + \kappa(\theta - v)\frac{\partial U}{\partial v} + \tfrac{1}{2}vS^2\frac{\partial^2 U}{\partial S^2} + \rho\sigma_v vS\frac{\partial^2 U}{\partial S\partial v} + \tfrac{1}{2}\sigma_v^2 v\frac{\partial^2 U}{\partial v^2} = rU
    $$

    At $v = 0$, all terms containing $v$ as a factor vanish:

    $$
    \frac{\partial U}{\partial t} + (r-q)S\frac{\partial U}{\partial S} + \kappa\theta\frac{\partial U}{\partial v} = rU
    $$

    The second-order terms in $S$ and $v$ (the terms $\frac{1}{2}vS^2 U_{SS}$, $\rho\sigma_v vS\,U_{Sv}$, and $\frac{1}{2}\sigma_v^2 v\,U_{vv}$) all vanish because they are proportional to $v$. The PDE degenerates from a second-order (parabolic) equation to a first-order (hyperbolic) equation.

    **No boundary condition should be imposed at $v = 0$** because:

    - When the Feller condition holds ($\delta \geq 2$), $v = 0$ is an entrance boundary that the process never reaches from the interior. The solution is uniquely determined by the interior PDE alone.
    - When the Feller condition is violated ($\delta < 2$), $v = 0$ is a regular-reflecting boundary. The natural (reflecting) behavior is automatically captured by the degenerate PDE at $v = 0$: the drift $\kappa\theta > 0$ in the $\partial U/\partial v$ term pushes information into the interior, which is the correct reflection behavior.

    Imposing an artificial Dirichlet or Neumann condition at $v = 0$ would overconstrain the problem and introduce error.

    **Boundary condition at $v = v_{\max}$:** At the truncation boundary $v = v_{\max}$ (an artificial boundary introduced by the finite grid), one typically imposes a condition that reflects the behavior for large variance. Common choices:

    - **Linear extrapolation (Neumann):** $\frac{\partial^2 U}{\partial v^2}\big|_{v=v_{\max}} = 0$, assuming the option price is approximately linear in $v$ for very large $v$.
    - **Asymptotic condition:** For a European call, as $v \to \infty$, the option value approaches $S e^{-qT}$ (the forward value), so $U(t, S, v_{\max}) \approx Se^{-q(T-t)}$.
    - **Zero second derivative:** This is equivalent to assuming the curvature in $v$ vanishes far from the origin.

    The boundary at $v_{\max}$ should be placed far enough (e.g., $v_{\max} = 5\theta$ to $10\theta$) that the choice of condition has minimal impact on the interior solution.

---

**Exercise 6.** Show that even when the Feller condition is violated, the CIR process is well-defined as a weak solution of the SDE and the characteristic function formula remains valid. Why does this mean that the Feller condition is a regularity condition for simulation, not a requirement for pricing?

??? success "Solution to Exercise 6"
    **Well-posedness without the Feller condition.** The CIR SDE $dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t$ with $\kappa > 0$, $\theta > 0$, $\sigma_v > 0$, and $V_0 > 0$ has a unique strong solution $V_t \geq 0$ for all $t \geq 0$, regardless of whether the Feller condition holds. This follows from the Yamada-Watanabe theorem.

    The diffusion coefficient $\sigma_v\sqrt{v}$ is Holder continuous of order $\frac{1}{2}$ but not Lipschitz at $v = 0$. The standard Picard-Lindelof uniqueness theorem does not apply. However, the Yamada-Watanabe condition for pathwise uniqueness requires:

    $$
    \int_0^\epsilon \frac{1}{\sigma^2(v)}\,dv = \int_0^\epsilon \frac{1}{\sigma_v^2 v}\,dv = \frac{1}{\sigma_v^2}\ln\left(\frac{\epsilon}{0^+}\right) = +\infty
    $$

    This integral diverges, so the Yamada-Watanabe condition is satisfied, guaranteeing pathwise uniqueness. The Feller condition only determines whether $V_t$ stays strictly positive ($V_t > 0$) or can touch zero ($V_t = 0$ with positive probability). In either case, the process exists, is unique, and satisfies $V_t \geq 0$.

    **Validity of the characteristic function.** The Heston characteristic function $\phi(u, \tau) = \exp(C(\tau, u) + D(\tau, u)v + iux)$ is derived from the Feynman-Kac theorem applied to the backward Kolmogorov equation. The derivation requires:

    1. The joint process $(x_t, V_t)$ is well-defined (which it is, by Yamada-Watanabe).
    2. The exponential-affine ansatz satisfies the PDE.
    3. The Riccati ODEs for $C$ and $D$ have solutions on $[0, T]$ (which they do for $u$ in the strip of analyticity).

    None of these steps require the Feller condition. The Riccati solutions $C(\tau, u)$ and $D(\tau, u)$ are the same regardless of whether $2\kappa\theta \geq \sigma_v^2$ or $2\kappa\theta < \sigma_v^2$. The characteristic function formula, and all Fourier pricing methods derived from it, remain valid.

    **Conclusion.** The Feller condition is a **regularity condition for simulation**, not a requirement for pricing:

    - **For pricing** (Fourier methods, PDE methods): The CF formula is exact and does not depend on the Feller condition. The PDE is well-posed with the degenerate boundary treatment at $v = 0$.
    - **For simulation** (Monte Carlo): When the Feller condition is violated, discrete-time schemes can produce negative variance, requiring ad hoc fixes (truncation, reflection) that introduce bias. The Feller condition ensures that this problem does not arise.

    In practice, since calibrated parameters almost always violate the Feller condition, practitioners use Fourier methods (which are unaffected) for pricing and employ careful simulation schemes (QE, exact) for Monte Carlo applications.
