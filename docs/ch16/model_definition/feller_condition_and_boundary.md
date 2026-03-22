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

**Proof (sketch for part 1).** The idea is to apply the comparison theorem for SDEs combined with the properties of Bessel processes. The CIR process $v_t$ is related to the squared Bessel process of dimension $\delta = 4\kappa\theta/\sigma_v^2$ by a time change.

Consider the squared Bessel process of dimension $\delta$:

$$
dR_t = \delta\,dt + 2\sqrt{R_t}\,dB_t
$$

The CIR process $v_t$ with parameters $(\kappa, \theta, \sigma_v)$ satisfies $v_t = e^{-\kappa t}R(\psi(t))$ where $\psi(t) = \frac{\sigma_v^2}{4\kappa}(e^{\kappa t} - 1)$ (a deterministic time change). A squared Bessel process of dimension $\delta \geq 2$ never reaches zero. The condition $\delta \geq 2$ is:

$$
\frac{4\kappa\theta}{\sigma_v^2} \geq 2 \qquad \Longleftrightarrow \qquad 2\kappa\theta \geq \sigma_v^2
$$

which is the Feller condition. When $\delta < 2$ (Feller condition violated), the squared Bessel process reaches zero with positive probability. $\square$

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

Monte Carlo simulation of the CIR variance process faces challenges when the Feller condition is violated, because discrete-time Euler steps can produce negative variance values.

??? example "Euler Scheme and Negativity"
    The Euler discretization of the CIR process is:

    $$
    v_{t+\Delta t} = v_t + \kappa(\theta - v_t)\Delta t + \sigma_v\sqrt{v_t}\sqrt{\Delta t}\,Z, \qquad Z \sim N(0,1)
    $$

    Even if $v_t > 0$, the Gaussian noise $Z$ can produce $v_{t+\Delta t} < 0$ when $\sigma_v\sqrt{v_t}\sqrt{\Delta t}|Z|$ exceeds $v_t + \kappa(\theta - v_t)\Delta t$. This is especially likely when $v_t$ is small and $\sigma_v$ is large (Feller condition violated).

Common fixes for negative variance in simulation:

| Scheme | Treatment of Negative $v$ | Bias |
|:---|:---|:---|
| Full truncation | $v_{t+\Delta t} \gets \max(v_{t+\Delta t}, 0)$ | $O(\Delta t)$ |
| Reflection | $v_{t+\Delta t} \gets |v_{t+\Delta t}|$ | $O(\Delta t)$ |
| Partial truncation | Use $\sqrt{\max(v_t, 0)}$ in the diffusion only | $O(\Delta t)$ |
| Exact simulation (Broadie-Kaya) | Sample from non-central $\chi^2$ | Unbiased |
| QE scheme (Andersen) | Match moments exactly | Near-exact |

The exact and QE schemes avoid the negativity problem entirely by sampling from the true or moment-matched distribution. These methods are discussed in the [Monte Carlo section](../monte_carlo/euler_discretization_and_pitfalls.md).

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
