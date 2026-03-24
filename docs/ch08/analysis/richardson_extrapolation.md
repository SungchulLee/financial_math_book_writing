# Richardson Extrapolation

Richardson extrapolation combines numerical solutions computed on two or more grids to cancel leading-order error terms, producing a more accurate approximation without redesigning the numerical scheme. It is a powerful and general technique for improving convergence order.

---

## The Error Expansion

### Asymptotic Form

Suppose a numerical method with mesh parameter $h$ produces an approximation $V(h)$ to the exact value $V^*$. If the method has order $p$, the error admits an asymptotic expansion:

$$
V(h) = V^* + c_p h^p + c_{p+1} h^{p+1} + c_{p+2} h^{p+2} + \cdots
$$

where the constants $c_p, c_{p+1}, \ldots$ are independent of $h$.

**Key assumption**: The error is a **smooth function of $h$** with a power series structure. This holds when the PDE solution is sufficiently smooth.

### Example: Crank-Nicolson

Crank-Nicolson for the Black-Scholes equation has second-order accuracy:

$$
V(\Delta S, \Delta\tau) = V^* + c_1 (\Delta S)^2 + c_2 (\Delta\tau)^2 + \text{higher order}
$$

If we refine both $\Delta S$ and $\Delta\tau$ proportionally (using a single mesh parameter $h$):

$$
V(h) = V^* + c h^2 + d h^4 + O(h^6)
$$

---

## The Extrapolation Formula

### Eliminating the Leading Error Term

Compute $V(h)$ on a grid with spacing $h$ and $V(h/r)$ on a refined grid with spacing $h/r$ (typically $r = 2$). The errors are:

$$
V(h) = V^* + c h^p + O(h^{p+1})
$$

$$
V(h/r) = V^* + c (h/r)^p + O(h^{p+1}) = V^* + c h^p / r^p + O(h^{p+1})
$$

Eliminating $c h^p$ from these two equations:

$$
r^p V(h/r) - V(h) = (r^p - 1) V^* + O(h^{p+1})
$$

!!! info "Richardson Extrapolation Formula"
    The extrapolated value is:

    $$
    \boxed{V_{\text{ext}} = \frac{r^p V(h/r) - V(h)}{r^p - 1}}
    $$

    This has accuracy $O(h^{p+1})$, one order higher than the original scheme.

### Special Case: $r = 2$ (Grid Doubling)

For the common choice of doubling the number of grid points ($r = 2$):

$$
V_{\text{ext}} = \frac{2^p V(h/2) - V(h)}{2^p - 1}
$$

| Original order $p$ | Extrapolated order | Formula |
|--------------------|-------------------|---------|
| 1 (Euler) | 2 | $2V(h/2) - V(h)$ |
| 2 (Crank-Nicolson) | 4 | $\frac{4V(h/2) - V(h)}{3}$ |

---

## Application to First-Order Methods

### Backward Euler (Implicit Scheme)

The implicit scheme for the heat equation has error:

$$
V(h) = V^* + c_1 h + c_2 h^2 + O(h^3)
$$

where $h$ represents the time step $\Delta\tau$ (assuming spatial error is negligible or handled separately).

Compute with $N$ and $2N$ time steps:

$$
V_{\text{ext}} = 2V(h/2) - V(h)
$$

This cancels the $O(h)$ term, yielding a second-order approximation from a first-order scheme.

### Numerical Example

Consider pricing a European call with $K = 100$, $S = 100$, $T = 1$, $\sigma = 0.2$, $r = 0.05$. Using the implicit scheme with $M = 200$ spatial points:

| Time steps $N$ | FDM price $V(h)$ | Error |
|------|------|------|
| 50 | 10.4312 | $2.0 \times 10^{-2}$ |
| 100 | 10.4412 | $1.0 \times 10^{-2}$ |
| 200 | 10.4462 | $5.0 \times 10^{-3}$ |

**Extrapolation** ($p=1$, $r=2$):

$$
V_{\text{ext}} = 2 \times 10.4412 - 10.4312 = 10.4512
$$

The exact Black-Scholes price is $V^* = 10.4506$, so the extrapolated error ($6 \times 10^{-4}$) is roughly 17 times smaller than the $N=100$ error.

---

## Application to Second-Order Methods

### Crank-Nicolson

With second-order convergence ($p = 2$):

$$
V_{\text{ext}} = \frac{4V(h/2) - V(h)}{3}
$$

This produces a **fourth-order** approximation.

### Numerical Example (Continued)

Using Crank-Nicolson with $M = 200$:

| Time steps $N$ | FDM price $V(h)$ | Error |
|------|------|------|
| 25 | 10.4496 | $1.0 \times 10^{-3}$ |
| 50 | 10.4504 | $2.5 \times 10^{-4}$ |
| 100 | 10.4505 | $6.3 \times 10^{-5}$ |

**Extrapolation** ($p=2$, $r=2$):

$$
V_{\text{ext}} = \frac{4 \times 10.4504 - 10.4496}{3} = \frac{41.8016 - 10.4496}{3} = 10.45067
$$

The extrapolated error ($\sim 10^{-5}$) is roughly 25 times smaller than the $N=50$ error.

---

## Repeated Richardson Extrapolation

### The Romberg Table

Repeated extrapolation can further increase the order. Starting from solutions on grids $h, h/2, h/4, \ldots$:

**Level 0** (original solutions):

$$
V_0^{(0)} = V(h), \quad V_1^{(0)} = V(h/2), \quad V_2^{(0)} = V(h/4), \quad \ldots
$$

**Level $k$** (extrapolated):

$$
V_j^{(k)} = \frac{2^{pk} V_{j+1}^{(k-1)} - V_j^{(k-1)}}{2^{pk} - 1}
$$

where $p$ is the original order and the effective order at level $k$ is $p + k$.

### Example Table (Crank-Nicolson, $p = 2$)

| | $V^{(0)}$ (order 2) | $V^{(1)}$ (order 4) | $V^{(2)}$ (order 6) |
|---|---|---|---|
| $h$ | $V(h)$ | | |
| $h/2$ | $V(h/2)$ | $\frac{4V(h/2) - V(h)}{3}$ | |
| $h/4$ | $V(h/4)$ | $\frac{4V(h/4) - V(h/2)}{3}$ | $\frac{16V^{(1)}_1 - V^{(1)}_0}{15}$ |

Each column increases the effective order by 2 (since only even powers appear in the Crank-Nicolson error expansion).

---

## Convergence Order Verification

Richardson extrapolation provides a robust way to **verify the convergence order** of a numerical method without knowing the exact solution.

### The Richardson Error Estimator

From the error expansion $V(h) = V^* + ch^p + O(h^{p+1})$:

$$
V(h) - V(h/2) \approx ch^p - c(h/2)^p = ch^p\left(1 - \frac{1}{2^p}\right)
$$

$$
V(h/2) - V(h/4) \approx c(h/2)^p\left(1 - \frac{1}{2^p}\right)
$$

The **Richardson ratio** is:

$$
\boxed{R = \frac{V(h) - V(h/2)}{V(h/2) - V(h/4)} \approx 2^p}
$$

!!! tip "Convergence Order Test"
    If $R \approx 2$, the method is first-order ($p = 1$).
    If $R \approx 4$, the method is second-order ($p = 2$).
    If $R \approx 8$, the method is third-order ($p = 3$).

### Extracting the Order

Solving for $p$ directly:

$$
p \approx \log_2 R = \frac{\ln R}{\ln 2}
$$

This is the **observed convergence order**, which should match the theoretical order when the solution is smooth and the asymptotic regime has been reached.

---

## Spatial and Temporal Extrapolation

### Independent Extrapolation

When spatial and temporal errors are controlled independently, extrapolation can be applied in each direction separately.

**Step 1**: Fix $\Delta\tau$ and extrapolate in space:

$$
V_{\text{ext},S} = \frac{4V(\Delta S / 2) - V(\Delta S)}{3}
$$

**Step 2**: Fix $\Delta S$ and extrapolate in time:

$$
V_{\text{ext},\tau} = \frac{4V(\Delta\tau / 2) - V(\Delta\tau)}{3}
$$

**Step 3**: Apply both extrapolations (requires four solutions):

$$
V_{\text{ext}} = \frac{16 V(\Delta S/2, \Delta\tau/2) - 4V(\Delta S, \Delta\tau/2) - 4V(\Delta S/2, \Delta\tau) + V(\Delta S, \Delta\tau)}{9}
$$

### Proportional Refinement

Alternatively, refine $\Delta S$ and $\Delta\tau$ proportionally (setting $h = \Delta S = \alpha \Delta\tau$ for some fixed $\alpha$). Then a single extrapolation handles both errors simultaneously.

---

## When Richardson Extrapolation Fails

### Non-Smooth Data

The error expansion $V(h) = V^* + ch^p + O(h^{p+1})$ assumes smooth dependence on $h$. This breaks down when:

1. **Payoff kinks**: The payoff $(S-K)^+$ has a discontinuous derivative at $S = K$. The error expansion may contain fractional powers of $h$ or logarithmic terms
2. **Barrier options**: Discontinuities in the boundary condition disrupt the error expansion
3. **American options**: The free boundary introduces additional non-smoothness

In these cases, the Richardson ratio $R$ may deviate significantly from $2^p$, and the extrapolated value may be **less accurate** than the fine-grid solution alone.

### Remedies

- **Rannacher smoothing**: Apply a few implicit steps first to smooth the solution, restoring the regular error expansion
- **Payoff smoothing**: Replace the kink with a smooth approximation over a small interval
- **Grid alignment**: Place grid points exactly at the strike $K$ so the kink coincides with a node

After smoothing, Richardson extrapolation typically recovers its full effectiveness.

### Pre-Asymptotic Regime

Extrapolation also fails if the grid is too coarse for the asymptotic expansion to be valid. Always verify that the Richardson ratio is close to $2^p$ before trusting the extrapolated value.

---

## Summary

$$
\boxed{
V_{\text{ext}} = \frac{r^p V(h/r) - V(h)}{r^p - 1}
}
$$

| Aspect | Detail |
|--------|--------|
| **Purpose** | Cancel leading error term, gain one order |
| **Requirement** | Smooth error expansion in powers of $h$ |
| **For Euler ($p=1$)** | $V_{\text{ext}} = 2V(h/2) - V(h)$ gives order 2 |
| **For C-N ($p=2$)** | $V_{\text{ext}} = \frac{4V(h/2) - V(h)}{3}$ gives order 4 |
| **Order verification** | Richardson ratio $R \approx 2^p$ confirms order $p$ |
| **Limitation** | Requires smooth solutions; fails near kinks and free boundaries |

Richardson extrapolation is a cost-effective way to improve accuracy: computing two solutions on different grids and combining them is often cheaper than solving once on a very fine grid. Combined with Rannacher smoothing, it provides a practical route to high-accuracy option pricing.

---

## Exercises

**Exercise 1.** An implicit scheme with $N = 50$ time steps gives a price of $V(h) = 10.4312$, and with $N = 100$ gives $V(h/2) = 10.4412$. Assuming first-order convergence ($p = 1$), compute the Richardson-extrapolated value $V_{\text{ext}} = 2V(h/2) - V(h)$. If the exact price is $10.4506$, compare the errors of $V(h/2)$ and $V_{\text{ext}}$.

---

**Exercise 2.** For a second-order method (Crank-Nicolson), three grid solutions give: $V(h) = 10.4496$, $V(h/2) = 10.4504$, $V(h/4) = 10.4505$. Compute the Richardson ratio $R = (V(h) - V(h/2))/(V(h/2) - V(h/4))$. Is $R \approx 4$ consistent with second-order convergence?

---

**Exercise 3.** Construct the Romberg table for a Crank-Nicolson solver using solutions at $h$, $h/2$, and $h/4$ with values $V(h) = 10.44$, $V(h/2) = 10.449$, $V(h/4) = 10.4504$. Compute the two level-1 extrapolated values (order 4) and the single level-2 value (order 6).

---

**Exercise 4.** Explain why Richardson extrapolation fails when the payoff has a kink at $S = K$. Specifically, what happens to the error expansion $V(h) = V^* + ch^p + \cdots$ when the solution is not smooth? What does the Richardson ratio look like in this case?

---

**Exercise 5.** For independent spatial and temporal extrapolation, four PDE solutions are needed: $V(\Delta S, \Delta\tau)$, $V(\Delta S/2, \Delta\tau)$, $V(\Delta S, \Delta\tau/2)$, and $V(\Delta S/2, \Delta\tau/2)$. Write down the combined extrapolation formula that eliminates leading-order errors in both space and time for a second-order scheme. What is the effective order of the result?

---

**Exercise 6.** A practitioner wants to improve the accuracy of an implicit (first-order) scheme without switching to Crank-Nicolson. By running the implicit scheme on two grids and applying Richardson extrapolation, they can obtain a second-order result. Compare the total computational cost of this approach to running Crank-Nicolson on the fine grid alone.
