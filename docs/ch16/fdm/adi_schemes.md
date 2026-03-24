# ADI Schemes for the Heston PDE

A fully implicit discretization of the two-dimensional Heston PDE produces a large, sparse linear system with $N_x \times N_v$ unknowns at each time step. Solving this system directly has $\mathcal{O}(N_x^2 N_v^2)$ cost---prohibitively expensive for production grids. **Alternating direction implicit (ADI)** schemes split the 2D problem into sequences of 1D implicit solves, each requiring only a **tridiagonal** matrix inversion at $\mathcal{O}(N)$ cost. This section develops three ADI schemes for the Heston PDE: Douglas-Rachford, Craig-Sneyd, and Hundsdorfer-Verwer, each handling the mixed derivative term differently.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Explain why ADI splitting reduces the computational cost from $\mathcal{O}(N^4)$ to $\mathcal{O}(N^2)$
    2. Implement the Douglas-Rachford, Craig-Sneyd, and Hundsdorfer-Verwer schemes
    3. Analyze the stability properties and accuracy order of each scheme
    4. Choose the appropriate scheme based on the strength of correlation $\rho$

!!! tip "Prerequisites"
    This section requires the [2D PDE formulation](two_dimensional_pde_formulation.md) and its operator splitting $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$.

---

## The ADI Principle

Recall the semi-discrete Heston PDE in backward time $\tau = T - t$:

$$
\frac{\partial V}{\partial \tau} = (\mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv} - rI) V
$$

where $\mathcal{L}_x$, $\mathcal{L}_v$ are the directional operators and $\mathcal{L}_{xv}$ is the mixed derivative operator. Denote the discrete matrix representations as $A_x$, $A_v$, and $A_{xv}$, and let $A_0 = A_x + A_v + A_{xv} - rI$ be the full spatial operator.

A **fully implicit** step would solve:

$$
(I - \Delta\tau \, A_0) V^{n+1} = V^n
$$

The matrix $(I - \Delta\tau \, A_0)$ is of size $(N_x N_v) \times (N_x N_v)$ and is sparse but not tridiagonal. ADI schemes instead solve sequences of **tridiagonal** systems by treating each direction implicitly in turn.

---

## Douglas-Rachford Scheme

The Douglas-Rachford (DR) scheme is the simplest ADI method. It treats the $x$-direction implicitly first, then the $v$-direction, while handling the mixed derivative explicitly.

**Stage 0** (explicit predictor):

$$
Y_0 = V^n + \Delta\tau \, A_0 V^n
$$

**Stage 1** ($x$-direction implicit correction):

$$
(I - \theta \Delta\tau \, A_x) Y_1 = Y_0 - \theta \Delta\tau \, A_x V^n
$$

**Stage 2** ($v$-direction implicit correction):

$$
(I - \theta \Delta\tau \, A_v) V^{n+1} = Y_1 - \theta \Delta\tau \, A_v V^n
$$

Here $\theta \in [0, 1]$ is a parameter controlling the implicitness. The choice $\theta = \frac{1}{2}$ gives second-order accuracy in time; $\theta = 1$ gives first-order accuracy but improved stability.

Each stage requires solving a tridiagonal system: Stage 1 involves $N_v$ independent tridiagonal systems of size $N_x$, and Stage 2 involves $N_x$ independent systems of size $N_v$. The total cost per time step is $\mathcal{O}(N_x N_v)$.

!!! note "Mixed Derivative Treatment"
    In the Douglas-Rachford scheme, the mixed derivative $A_{xv}$ appears only in the explicit predictor $Y_0$. This preserves the tridiagonal structure of each implicit stage but limits the scheme's stability when $|\rho|$ is large.

---

## Craig-Sneyd Scheme

The Craig-Sneyd (CS) scheme improves the treatment of the mixed derivative by adding an explicit correction step that partially compensates for the explicit handling.

**Stage 0** (explicit predictor):

$$
Y_0 = V^n + \Delta\tau \, A_0 V^n
$$

**Stage 1** ($x$-direction implicit):

$$
(I - \theta \Delta\tau \, A_x) Y_1 = Y_0 - \theta \Delta\tau \, A_x V^n
$$

**Stage 2** ($v$-direction implicit):

$$
(I - \theta \Delta\tau \, A_v) \tilde{Y} = Y_1 - \theta \Delta\tau \, A_v V^n
$$

**Stage 3** (mixed derivative correction):

$$
\hat{Y}_0 = Y_0 + \frac{1}{2} \Delta\tau (A_{xv} \tilde{Y} - A_{xv} V^n)
$$

**Stage 4** ($x$-direction implicit, repeated):

$$
(I - \theta \Delta\tau \, A_x) \hat{Y}_1 = \hat{Y}_0 - \theta \Delta\tau \, A_x V^n
$$

**Stage 5** ($v$-direction implicit, repeated):

$$
(I - \theta \Delta\tau \, A_v) V^{n+1} = \hat{Y}_1 - \theta \Delta\tau \, A_v V^n
$$

The additional Stages 3--5 re-process the solution with an updated mixed derivative contribution. With $\theta = \frac{1}{2}$, the Craig-Sneyd scheme achieves second-order accuracy and better stability than Douglas-Rachford for $|\rho|$ up to approximately 0.8.

---

## Hundsdorfer-Verwer Scheme

The Hundsdorfer-Verwer (HV) scheme provides the best stability properties among the three, at the cost of one additional implicit sweep per direction.

**Stage 0** (explicit predictor):

$$
Y_0 = V^n + \Delta\tau \, A_0 V^n
$$

**Stage 1** ($x$-direction implicit):

$$
(I - \theta \Delta\tau \, A_x) Y_1 = Y_0 - \theta \Delta\tau \, A_x V^n
$$

**Stage 2** ($v$-direction implicit):

$$
(I - \theta \Delta\tau \, A_v) \tilde{Y} = Y_1 - \theta \Delta\tau \, A_v V^n
$$

**Stage 3** (corrector predictor):

$$
\hat{Y}_0 = Y_0 + \frac{1}{2}\Delta\tau \left(A_0 \tilde{Y} - A_0 V^n\right)
$$

**Stage 4** ($x$-direction implicit, repeated):

$$
(I - \theta \Delta\tau \, A_x) \hat{Y}_1 = \hat{Y}_0 - \theta \Delta\tau \, A_x \tilde{Y}
$$

**Stage 5** ($v$-direction implicit, repeated):

$$
(I - \theta \Delta\tau \, A_v) V^{n+1} = \hat{Y}_1 - \theta \Delta\tau \, A_v \tilde{Y}
$$

The key difference from Craig-Sneyd is in Stage 3: the **full** operator $A_0$ (including both directional and mixed derivative operators) is used in the correction, not just $A_{xv}$. This provides unconditional stability for all values of $\rho$ with $\theta = \frac{1}{2}$.

---

## Stability and Accuracy Comparison

| Property | Douglas-Rachford | Craig-Sneyd | Hundsdorfer-Verwer |
|----------|:----------------:|:-----------:|:------------------:|
| Time accuracy ($\theta = \frac{1}{2}$) | $\mathcal{O}(\Delta\tau^2)$ | $\mathcal{O}(\Delta\tau^2)$ | $\mathcal{O}(\Delta\tau^2)$ |
| Time accuracy ($\theta = 1$) | $\mathcal{O}(\Delta\tau)$ | $\mathcal{O}(\Delta\tau)$ | $\mathcal{O}(\Delta\tau)$ |
| Stability for $|\rho| \leq 0.5$ | Unconditional | Unconditional | Unconditional |
| Stability for $|\rho| \approx 0.7$ | Conditional | Unconditional | Unconditional |
| Stability for $|\rho| \to 1$ | Unstable | Conditional | Unconditional |
| Tridiagonal solves per step | 2 | 4 | 4 |
| Cost per step (relative) | 1.0 | 2.0 | 2.0 |

!!! warning "Correlation and Stability"
    For equity markets where $\rho \in [-0.9, -0.5]$ is typical, the Douglas-Rachford scheme may exhibit oscillations near $v = 0$ or large $S$. The Hundsdorfer-Verwer scheme is recommended as the default for Heston implementations because it maintains unconditional stability across all parameter regimes.

---

## Implementation Structure

Each ADI time step follows this pattern:

1. **Form the right-hand side** using the explicit parts of $A_0$
2. **Sweep in $x$-direction**: for each fixed $v_j$, solve a tridiagonal system of size $N_x$
3. **Sweep in $v$-direction**: for each fixed $x_i$, solve a tridiagonal system of size $N_v$
4. For CS and HV: **repeat** steps 1--3 with the corrected right-hand side

The tridiagonal systems are solved using the **Thomas algorithm** (LU decomposition for tridiagonal matrices) in $\mathcal{O}(N)$ operations. The matrix entries depend on $v$ through the diffusion and drift coefficients but are constant along each $v$-line, allowing the LU factorization to be cached.

??? example "Tridiagonal System Structure"
    For the $x$-sweep at variance level $v_j$, the system has the form:

    $$
    -\alpha_i V_{i-1,j}^{n+1} + (1 + \beta_i) V_{i,j}^{n+1} - \gamma_i V_{i+1,j}^{n+1} = \text{RHS}_i
    $$

    where the coefficients are:

    $$
    \alpha_i = \theta \Delta\tau \left[\frac{v_j}{h_i^-(h_i^+ + h_i^-)} + \frac{r - q - v_j/2}{h_i^+ + h_i^-}\cdot\frac{h_i^+}{h_i^-}\right]
    $$

    and $\beta_i, \gamma_i$ are analogous. These are assembled once per time step and reused for the repeated sweeps in CS and HV.

---

## Worked Example

Consider the standard Heston parameters with $N_x = 100$, $N_v = 50$, $N_t = 100$:

| Grid | Total unknowns | DR time (relative) | HV time (relative) | HV error vs Fourier |
|------|:--------------:|:------------------:|:------------------:|:-------------------:|
| $50 \times 25$ | 1,250 | 1.0 | 2.0 | $\$0.08$ |
| $100 \times 50$ | 5,000 | 4.0 | 8.0 | $\$0.02$ |
| $200 \times 100$ | 20,000 | 16.0 | 32.0 | $\$0.005$ |

The quadratic scaling in grid size is clearly visible. For the $100 \times 50$ grid with the HV scheme and $\theta = \frac{1}{2}$, the pricing error for an ATM European call is within $\$0.02$ of the Fourier reference, with a computation time of a few seconds on a modern workstation.

---

## Summary

ADI schemes transform the two-dimensional Heston PDE into sequences of one-dimensional tridiagonal solves, reducing the per-step cost from $\mathcal{O}(N_x^2 N_v^2)$ to $\mathcal{O}(N_x N_v)$. The Douglas-Rachford scheme is simplest but can be unstable for large $|\rho|$. The Craig-Sneyd scheme improves mixed derivative treatment. The Hundsdorfer-Verwer scheme provides **unconditional stability** for all correlation values and is the recommended default. All three achieve second-order temporal accuracy with $\theta = \frac{1}{2}$. The ADI framework extends naturally to [American options via PSOR](american_options_psor.md), where the early exercise constraint is applied after each time step.

---

## Exercises

**Exercise 1.**
A fully implicit Crank-Nicolson scheme on a grid with $N_x = 200$ and $N_v = 100$ produces a sparse system of size $20{,}000 \times 20{,}000$. If solving this system with a banded solver costs $\mathcal{O}(N_x^2 N_v)$ per time step, compare the total cost for $N_t = 200$ steps with the ADI cost of $\mathcal{O}(N_x N_v \cdot N_t)$. Compute the speedup factor.

---

**Exercise 2.**
The Douglas-Rachford scheme treats the mixed derivative explicitly. For $\rho = -0.9$, explain why the CFL-type stability constraint becomes binding. If $\Delta t = T/N_t$ with $T = 1$ and $N_t = 100$, is this time step small enough for stability on a typical Heston grid?

---

**Exercise 3.**
The Craig-Sneyd scheme adds a correction step that updates the cross-term. Write the four stages explicitly for the Heston PDE operators $\mathcal{A}_0$, $\mathcal{A}_1$, $\mathcal{A}_2$ with $\theta = 1/2$. Explain why Stage 4 (cross-term correction) improves the local truncation error from $\mathcal{O}(\Delta t)$ to $\mathcal{O}(\Delta t^2)$.

---

**Exercise 4.**
Compare the computational cost per time step of the three ADI schemes. If Thomas's algorithm costs $5N$ operations for a tridiagonal system of size $N$, compute the total operations for: (a) Douglas-Rachford ($N_v$ solves of size $N_x$ + $N_x$ solves of size $N_v$), (b) Craig-Sneyd (same plus one explicit cross-term evaluation), (c) Hundsdorfer-Verwer (double the implicit sweeps). Use $N_x = 200$, $N_v = 100$.

---

**Exercise 5.**
Design a convergence study for the Craig-Sneyd scheme: compute the European call price on grids $(N_x, N_v, N_t) = (50, 25, 50)$, $(100, 50, 100)$, $(200, 100, 200)$ and compare with the COS reference. If the scheme is second-order, the error should decrease by a factor of 4 each time. Verify this by computing the convergence rate $p = \log_2(\text{error}_1 / \text{error}_2)$.

---

**Exercise 6.**
The Hundsdorfer-Verwer scheme performs two sets of implicit sweeps per time step. Describe the advantage: unconditional stability allows larger $\Delta t$. If the Craig-Sneyd scheme requires $N_t = 200$ steps for stability while Hundsdorfer-Verwer requires only $N_t = 100$ for the same accuracy, which scheme is faster overall? Account for the fact that Hundsdorfer-Verwer costs twice as much per step.
