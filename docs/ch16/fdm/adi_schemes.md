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

Recall (see [§ Two-Dimensional PDE Formulation](two_dimensional_pde_formulation.md)) the operator splitting $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$. In backward time $\tau = T - t$, $\partial_\tau V = (\mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv} - rI) V$. Denote the discrete matrix representations as $A_x$, $A_v$, $A_{xv}$, and let $A_0 = A_x + A_v + A_{xv} - rI$.

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

??? success "Solution to Exercise 1"
    **Banded Crank-Nicolson cost.** The grid has $N_x = 200$, $N_v = 100$, so there are $N = N_x N_v = 20{,}000$ unknowns. A banded solver with bandwidth $\mathcal{O}(N_x)$ costs $\mathcal{O}(N_x^2 N_v)$ per time step. For $N_t = 200$ steps:

    $$
    C_{\text{CN}} = N_t \cdot N_x^2 \cdot N_v = 200 \times 200^2 \times 100 = 8 \times 10^8
    $$

    **ADI cost.** Each ADI time step costs $\mathcal{O}(N_x N_v)$ (with a small constant multiplier for the number of tridiagonal sweeps). For $N_t = 200$ steps:

    $$
    C_{\text{ADI}} = N_t \cdot N_x \cdot N_v = 200 \times 200 \times 100 = 4 \times 10^6
    $$

    **Speedup factor.**

    $$
    \text{Speedup} = \frac{C_{\text{CN}}}{C_{\text{ADI}}} = \frac{8 \times 10^8}{4 \times 10^6} = 200
    $$

    The speedup equals $N_x = 200$, which is not a coincidence. The banded solver has an extra factor of $N_x$ in its cost (from the bandwidth), so the ADI speedup scales linearly with $N_x$. For a $400 \times 200$ grid, the speedup would be approximately 400.

---

**Exercise 2.**
The Douglas-Rachford scheme treats the mixed derivative explicitly. For $\rho = -0.9$, explain why the CFL-type stability constraint becomes binding. If $\Delta t = T/N_t$ with $T = 1$ and $N_t = 100$, is this time step small enough for stability on a typical Heston grid?

??? success "Solution to Exercise 2"
    **Why the mixed derivative causes instability.** In the Douglas-Rachford scheme, the mixed derivative operator $A_{xv}$ appears only in the explicit predictor stage $Y_0 = V^n + \Delta\tau A_0 V^n$. For the explicit treatment to be stable, the time step must satisfy a CFL-type condition relating $\Delta\tau$ to the magnitude of $A_{xv}$.

    The mixed derivative coefficient is $\rho \xi v$. At a typical variance level $v \approx 0.04$ and with $\rho = -0.9$, $\xi = 0.3$:

    $$
    |\rho \xi v| = 0.9 \times 0.3 \times 0.04 = 0.0108
    $$

    The explicit stability condition for the mixed derivative on a grid with spacings $\Delta x$ and $\Delta v$ is approximately:

    $$
    \Delta\tau \lesssim \frac{\Delta x \, \Delta v}{2 |\rho \xi v|}
    $$

    For a typical grid with $\Delta x \approx 0.02$ and $\Delta v \approx 0.004$:

    $$
    \Delta\tau \lesssim \frac{0.02 \times 0.004}{2 \times 0.0108} \approx 0.0037
    $$

    With $T = 1$ and $N_t = 100$, the time step is $\Delta t = 0.01$, which exceeds this stability bound. The Douglas-Rachford scheme is therefore **not stable** with these parameters. One would need $N_t \gtrsim 270$ to satisfy the CFL constraint, or alternatively, one should use the Craig-Sneyd or Hundsdorfer-Verwer scheme, which handle the mixed derivative more robustly.

    The instability manifests as oscillations, particularly near $v = 0$ (where the CIR drift is strongest) and for deep in-the-money or out-of-the-money options where $\partial^2 V / \partial x \partial v$ is largest.

---

**Exercise 3.**
The Craig-Sneyd scheme adds a correction step that updates the cross-term. Write the four stages explicitly for the Heston PDE operators $\mathcal{A}_0$, $\mathcal{A}_1$, $\mathcal{A}_2$ with $\theta = 1/2$. Explain why Stage 4 (cross-term correction) improves the local truncation error from $\mathcal{O}(\Delta t)$ to $\mathcal{O}(\Delta t^2)$.

??? success "Solution to Exercise 3"
    **Craig-Sneyd stages with Heston operators.** Let $\mathcal{A}_0 = A_x + A_v + A_{xv} - rI$ be the full operator, and set $\theta = 1/2$. The six stages are:

    **Stage 0** (explicit predictor):

    $$
    Y_0 = V^n + \Delta\tau \, \mathcal{A}_0 V^n
    $$

    **Stage 1** ($x$-implicit):

    $$
    \left(I - \tfrac{1}{2}\Delta\tau \, A_x\right) Y_1 = Y_0 - \tfrac{1}{2}\Delta\tau \, A_x V^n
    $$

    **Stage 2** ($v$-implicit):

    $$
    \left(I - \tfrac{1}{2}\Delta\tau \, A_v\right) \tilde{Y} = Y_1 - \tfrac{1}{2}\Delta\tau \, A_v V^n
    $$

    **Stage 3** (cross-term correction):

    $$
    \hat{Y}_0 = Y_0 + \tfrac{1}{2}\Delta\tau \left(A_{xv} \tilde{Y} - A_{xv} V^n\right)
    $$

    **Stage 4** ($x$-implicit, repeated):

    $$
    \left(I - \tfrac{1}{2}\Delta\tau \, A_x\right) \hat{Y}_1 = \hat{Y}_0 - \tfrac{1}{2}\Delta\tau \, A_x V^n
    $$

    **Stage 5** ($v$-implicit, repeated):

    $$
    \left(I - \tfrac{1}{2}\Delta\tau \, A_v\right) V^{n+1} = \hat{Y}_1 - \tfrac{1}{2}\Delta\tau \, A_v V^n
    $$

    **Why Stage 3 improves accuracy.** Without the correction (i.e., in the Douglas-Rachford scheme), the cross-derivative is evaluated only at $V^n$. The local truncation error from the mixed derivative is:

    $$
    \Delta\tau \, A_{xv} V^n = \Delta\tau \, A_{xv} V^{n+1} - \Delta\tau^2 \, A_{xv} \dot{V} + \mathcal{O}(\Delta\tau^3)
    $$

    The $\mathcal{O}(\Delta\tau^2)$ term is a first-order temporal error in the mixed derivative treatment.

    Stage 3 replaces $A_{xv} V^n$ with $\frac{1}{2}(A_{xv} V^n + A_{xv} \tilde{Y})$. Since $\tilde{Y} = V^{n+1} + \mathcal{O}(\Delta\tau)$, this gives a trapezoidal average:

    $$
    \frac{1}{2}A_{xv}(V^n + \tilde{Y}) = A_{xv} V^{n+1/2} + \mathcal{O}(\Delta\tau^2)
    $$

    The error in the mixed derivative drops from $\mathcal{O}(\Delta\tau)$ to $\mathcal{O}(\Delta\tau^2)$, making the overall scheme second-order in time.

---

**Exercise 4.**
Compare the computational cost per time step of the three ADI schemes. If Thomas's algorithm costs $5N$ operations for a tridiagonal system of size $N$, compute the total operations for: (a) Douglas-Rachford ($N_v$ solves of size $N_x$ + $N_x$ solves of size $N_v$), (b) Craig-Sneyd (same plus one explicit cross-term evaluation), (c) Hundsdorfer-Verwer (double the implicit sweeps). Use $N_x = 200$, $N_v = 100$.

??? success "Solution to Exercise 4"
    **Thomas algorithm cost.** Each tridiagonal solve of size $N$ costs $5N$ operations (2 divisions, 2 multiplications, 1 subtraction in each of the forward elimination and back-substitution phases, approximately).

    **(a) Douglas-Rachford.**

    - $x$-sweep: $N_v$ tridiagonal systems of size $N_x$, cost $= N_v \times 5N_x = 100 \times 5 \times 200 = 100{,}000$
    - $v$-sweep: $N_x$ tridiagonal systems of size $N_v$, cost $= N_x \times 5N_v = 200 \times 5 \times 100 = 100{,}000$
    - Explicit predictor $Y_0$: matrix-vector product with $A_0$, cost $\approx c \cdot N_x N_v$ where $c$ is the stencil width (about 7--9 nonzeros per row), so approximately $7 \times 20{,}000 = 140{,}000$

    $$
    C_{\text{DR}} \approx 100{,}000 + 100{,}000 + 140{,}000 = 340{,}000 \text{ operations}
    $$

    **(b) Craig-Sneyd.**

    - Same as DR plus: one explicit cross-term evaluation ($A_{xv} \tilde{Y}$ costs $\approx 5 \times 20{,}000 = 100{,}000$ using the 4-point stencil) and one additional pair of implicit sweeps (same cost as the first pair: $200{,}000$)

    $$
    C_{\text{CS}} \approx 340{,}000 + 100{,}000 + 200{,}000 = 640{,}000 \text{ operations}
    $$

    **(c) Hundsdorfer-Verwer.**

    - Same as DR plus: one explicit full-operator evaluation ($A_0 \tilde{Y}$, cost $\approx 140{,}000$) and one additional pair of implicit sweeps ($200{,}000$)

    $$
    C_{\text{HV}} \approx 340{,}000 + 140{,}000 + 200{,}000 = 680{,}000 \text{ operations}
    $$

    **Ratios:** $C_{\text{CS}} / C_{\text{DR}} \approx 1.88$ and $C_{\text{HV}} / C_{\text{DR}} \approx 2.00$, confirming the factor-of-2 rule of thumb from the comparison table.

---

**Exercise 5.**
Design a convergence study for the Craig-Sneyd scheme: compute the European call price on grids $(N_x, N_v, N_t) = (50, 25, 50)$, $(100, 50, 100)$, $(200, 100, 200)$ and compare with the COS reference. If the scheme is second-order, the error should decrease by a factor of 4 each time. Verify this by computing the convergence rate $p = \log_2(\text{error}_1 / \text{error}_2)$.

??? success "Solution to Exercise 5"
    **Convergence study design.** Let the three grid levels be indexed by $\ell = 1, 2, 3$:

    | Level $\ell$ | $N_x$ | $N_v$ | $N_t$ | $\Delta x$ factor | $\Delta v$ factor | $\Delta\tau$ factor |
    |:-----------:|:-----:|:-----:|:-----:|:-----------------:|:-----------------:|:------------------:|
    | 1 | 50 | 25 | 50 | 1 | 1 | 1 |
    | 2 | 100 | 50 | 100 | 1/2 | 1/2 | 1/2 |
    | 3 | 200 | 100 | 200 | 1/4 | 1/4 | 1/4 |

    At each level, compute the European call price $V_\ell$ (e.g., at $S = K$, $v = v_0$) and the error $e_\ell = |V_\ell - V_{\text{ref}}|$ where $V_{\text{ref}}$ is the COS Fourier reference.

    **Second-order convergence prediction.** The Craig-Sneyd scheme with $\theta = 1/2$ is second-order in both space and time. Since all grid parameters are halved simultaneously:

    $$
    e_\ell = C \cdot h_\ell^2 + \mathcal{O}(h_\ell^3)
    $$

    where $h_\ell$ represents the characteristic mesh size at level $\ell$. With halving:

    $$
    \frac{e_1}{e_2} \approx 4, \qquad \frac{e_2}{e_3} \approx 4
    $$

    **Convergence rate computation.** The numerical convergence rate between levels $\ell$ and $\ell+1$ is:

    $$
    p = \log_2\!\left(\frac{e_\ell}{e_{\ell+1}}\right)
    $$

    For a second-order scheme, $p \approx 2$. In practice, one typically observes $p \in [1.8, 2.2]$ due to boundary effects, non-uniform grid stretching, and the explicit treatment of the mixed derivative. If $p$ is significantly less than 2, this may indicate that the mixed derivative treatment or the boundary conditions are limiting the convergence order.

    **Richardson extrapolation.** With the three grid levels, one can also compute an extrapolated price:

    $$
    V_{\text{extrap}} = \frac{4 V_3 - V_2}{3}
    $$

    which should be accurate to $\mathcal{O}(h_3^4)$ if the scheme is genuinely second-order.

---

**Exercise 6.**
The Hundsdorfer-Verwer scheme performs two sets of implicit sweeps per time step. Describe the advantage: unconditional stability allows larger $\Delta t$. If the Craig-Sneyd scheme requires $N_t = 200$ steps for stability while Hundsdorfer-Verwer requires only $N_t = 100$ for the same accuracy, which scheme is faster overall? Account for the fact that Hundsdorfer-Verwer costs twice as much per step.

??? success "Solution to Exercise 6"
    **Cost comparison.** Let $C_1$ denote the cost of one tridiagonal sweep pair (one $x$-sweep and one $v$-sweep). Then:

    - Craig-Sneyd costs $2C_1$ per step (two pairs of sweeps plus explicit evaluations)
    - Hundsdorfer-Verwer costs $2C_1$ per step (same number of sweeps, slightly more expensive explicit evaluation, but approximately equal)

    With the given time step requirements:

    **Craig-Sneyd total cost:**

    $$
    C_{\text{CS}} = N_t^{\text{CS}} \times 2C_1 = 200 \times 2C_1 = 400 \, C_1
    $$

    **Hundsdorfer-Verwer total cost:**

    $$
    C_{\text{HV}} = N_t^{\text{HV}} \times 2C_1 = 100 \times 2C_1 = 200 \, C_1
    $$

    **Hundsdorfer-Verwer is faster by a factor of 2** despite costing the same per step, because its unconditional stability allows a time step twice as large.

    **The key insight** is that the per-step cost ratio between CS and HV is approximately 1:1 (both require four tridiagonal sweeps), but HV's unconditional stability means the number of time steps is determined purely by accuracy, not by stability. When $|\rho|$ is large, the CS scheme's conditional stability forces smaller $\Delta\tau$ than accuracy alone would require, creating a gap between the stability-limited and accuracy-limited step counts.

    More generally, if the CS stability limit requires $N_t^{\text{CS}}$ steps while accuracy alone requires $N_t^{\text{acc}}$, then HV is faster whenever:

    $$
    \frac{N_t^{\text{CS}}}{N_t^{\text{acc}}} > 1
    $$

    For typical equity parameters with $\rho \in [-0.9, -0.5]$, this ratio ranges from 1.5 to 3, making HV the preferred scheme in practice.
