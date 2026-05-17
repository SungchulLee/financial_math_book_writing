# Vega and Rho via Bumping

The FDM grid discretizes the state space $(S,\tau)$ but treats $\sigma$ and $r$ as fixed numbers baked into the operator. So $\partial V/\partial\sigma$ cannot be read off a single grid -- there is nothing to difference against. The remedy is **bumping**: solve the PDE twice, once at $\sigma$ and once at $\sigma+\delta\sigma$, then approximate $\mathcal{V}\approx(V(\sigma+\delta\sigma)-V(\sigma-\delta\sigma))/(2\delta\sigma)$. The same recipe gives $\rho$ for the interest rate. Bumping doubles (or triples) the cost, but it is the only route to parameter Greeks.

---

## Definitions

**Vega** measures the sensitivity to volatility:

$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$

**Rho** measures the sensitivity to the risk-free interest rate:

$$
\rho = \frac{\partial V}{\partial r}
$$

Both are partial derivatives with respect to **model parameters** (not state variables), so they cannot be read from a single FDM solution grid.

!!! info "Why Bumping Is Necessary"
    The FDM grid discretizes the state space $(S, \tau)$ but treats parameters $\sigma$ and $r$ as fixed inputs. To compute $\partial V / \partial \sigma$, we need two solutions: one at $\sigma$ and one at $\sigma + \delta\sigma$. This is the bump-and-revalue approach.

---

## The Bump-and-Revalue Method

### Forward Difference (Two Solves)

Solve the PDE at the base parameter value and at the bumped value:

$$
\mathcal{V} \approx \frac{V(\sigma + \delta\sigma) - V(\sigma)}{\delta\sigma}
$$

$$
\rho \approx \frac{V(r + \delta r) - V(r)}{\delta r}
$$

Accuracy: $O(\delta\sigma)$ and $O(\delta r)$, respectively.

### Central Difference (Three Solves)

Solve the PDE at both up-bumped and down-bumped parameter values:

$$
\boxed{\mathcal{V} \approx \frac{V(\sigma + \delta\sigma) - V(\sigma - \delta\sigma)}{2\delta\sigma}}
$$

$$
\boxed{\rho \approx \frac{V(r + \delta r) - V(r - \delta r)}{2\delta r}}
$$

Accuracy: $O((\delta\sigma)^2)$ and $O((\delta r)^2)$. The central difference cancels the leading-order error term and is the standard choice.

### Cost Summary

| Method | Additional PDE solves | Accuracy |
|--------|----------------------|----------|
| Forward difference | 1 per Greek | $O(\delta p)$ |
| Central difference | 2 per Greek | $O((\delta p)^2)$ |
| Both vega and rho (central) | 4 | $O((\delta p)^2)$ |

where $\delta p$ denotes the bump size for the relevant parameter.

---

## Bump Size Selection

### The Tradeoff

The bump size $\delta p$ must balance two competing errors:

1. **Truncation error**: Arises from the finite difference approximation. For central differences:

$$
\text{Truncation error} = \frac{1}{6}\frac{\partial^3 V}{\partial p^3}(\delta p)^2 + O((\delta p)^4)
$$

Decreasing $\delta p$ reduces this error.

2. **Cancellation error**: The difference $V(p + \delta p) - V(p - \delta p)$ involves subtracting two nearly equal numbers. If each PDE solution has error $\varepsilon_{\text{FDM}}$ (from spatial and temporal discretization):

$$
\text{Cancellation error} \approx \frac{2\varepsilon_{\text{FDM}}}{\delta p}
$$

Decreasing $\delta p$ **increases** this error.

### Optimal Bump Size

The total error for a central difference is approximately:

$$
E(\delta p) \approx C_1 (\delta p)^2 + \frac{C_2 \varepsilon_{\text{FDM}}}{\delta p}
$$

Minimizing with respect to $\delta p$:

$$
\frac{dE}{d(\delta p)} = 2C_1 \delta p - \frac{C_2 \varepsilon_{\text{FDM}}}{(\delta p)^2} = 0
$$

$$
\boxed{(\delta p)^*_{\text{central}} \sim \varepsilon_{\text{FDM}}^{1/3}}
$$

For forward differences, the optimal bump size is:

$$
(\delta p)^*_{\text{forward}} \sim \varepsilon_{\text{FDM}}^{1/2}
$$

### Practical Recommendations

For a typical FDM solution with $\varepsilon_{\text{FDM}} \sim 10^{-4}$ to $10^{-6}$:

| Greek | Bump type | Optimal $\delta p$ range |
|-------|-----------|------------------------|
| Vega | Central in $\sigma$ | $\delta\sigma \sim 10^{-2}$ to $10^{-3}$ |
| Rho | Central in $r$ | $\delta r \sim 10^{-3}$ to $10^{-4}$ |

For vega, a common choice is $\delta\sigma = 0.01$ (a 1% absolute bump in volatility). For rho, $\delta r = 0.0001$ (a 1 basis point bump) is typical.

!!! warning "Bump Too Small"
    If $\delta p$ is too small relative to the FDM error, the central difference becomes dominated by cancellation noise and the Greek estimate is unreliable. Always ensure $\delta p \gg \varepsilon_{\text{FDM}}^{1/2}$ for forward differences or $\delta p \gg \varepsilon_{\text{FDM}}^{1/3}$ for central differences.

---

## Vega in Detail

Recall (see [BS Greeks closed forms](../../ch10/greeks/greeks_in_black_scholes_model.md)): the analytical vega is $\mathcal{V} = S\sqrt{T}\,\phi(d_1)$, peaks ATM, decays with $\sqrt{T}$, and is identical for calls and puts by parity.

### FDM Bumping for Vega

The bumping procedure:

1. Solve the Black-Scholes PDE with $\sigma_{\text{up}} = \sigma + \delta\sigma$
2. Solve the Black-Scholes PDE with $\sigma_{\text{down}} = \sigma - \delta\sigma$
3. Extract prices at the target node $S_j$ from both solutions
4. Compute $\mathcal{V}_j = (V_j^{\text{up}} - V_j^{\text{down}}) / (2\delta\sigma)$

Note that **both the diffusion and drift coefficients change** when $\sigma$ is bumped:

- Diffusion: $\frac{1}{2}\sigma^2 S^2 \to \frac{1}{2}(\sigma \pm \delta\sigma)^2 S^2$
- Drift (log-price): $r - \sigma^2/2 \to r - (\sigma \pm \delta\sigma)^2/2$

---

## Rho in Detail

Recall (see [BS Greeks closed forms](../../ch10/greeks/greeks_in_black_scholes_model.md)): $\rho_{\text{call}} = KTe^{-rT}\mathcal{N}(d_2) > 0$ and $\rho_{\text{put}} = -KTe^{-rT}\mathcal{N}(-d_2) < 0$.

### FDM Bumping for Rho

When bumping $r$, the following change:

1. **Drift term**: $rS\,\partial V/\partial S$ becomes $(r \pm \delta r)S\,\partial V/\partial S$
2. **Discount term**: $rV$ becomes $(r \pm \delta r)V$
3. **Boundary conditions**: $V(t, S_{\max}) \approx S_{\max} - Ke^{-(r\pm\delta r)(T-t)}$, etc.

All three effects must be consistently updated in the bumped PDE solve. Failing to update the boundary conditions is a common implementation error that leads to incorrect rho estimates, especially for deep in-the-money options where boundary values contribute significantly.

---

## Second-Order Parameter Sensitivities

### Vomma (Volga)

The second derivative of option price with respect to volatility:

$$
\text{Vomma} = \frac{\partial^2 V}{\partial \sigma^2} \approx \frac{V(\sigma + \delta\sigma) - 2V(\sigma) + V(\sigma - \delta\sigma)}{(\delta\sigma)^2}
$$

This is the "gamma of vega" and measures the convexity of the price in $\sigma$. It uses the same three PDE solutions as the central difference vega.

### Vanna (Cross-Gamma)

The mixed derivative:

$$
\text{Vanna} = \frac{\partial^2 V}{\partial S \,\partial \sigma} = \frac{\partial \Delta}{\partial \sigma}
$$

This can be estimated by computing delta from each bumped solution:

$$
\text{Vanna} \approx \frac{\Delta(\sigma + \delta\sigma) - \Delta(\sigma - \delta\sigma)}{2\delta\sigma}
$$

where each $\Delta$ is extracted from the respective FDM grid.

---

## Consistency Checks

### Vega-Theta Relationship

From the Black-Scholes PDE, there is a structural relationship between vega and gamma:

$$
\mathcal{V} = \sigma S^2 T_{\text{eff}} \, \Gamma
$$

where $T_{\text{eff}}$ is an effective time parameter. More precisely, for ATM options:

$$
\mathcal{V} \approx \sigma S^2 \Gamma \cdot T
$$

This provides a cross-check: if vega and gamma are computed independently, their ratio should be approximately $\sigma S^2 T$.

### Finite Difference Convergence

As $\delta\sigma \to 0$ (with sufficiently accurate PDE solutions), the bumped vega estimate should converge to the analytical value. Plotting the vega estimate against $\delta\sigma$ and checking for a plateau region identifies the range of reliable bump sizes.

---

## Practical Workflow

For a complete set of Greeks from a single FDM framework:

1. **Solve base PDE** ($\sigma, r$) $\to$ extract $V$, $\Delta$, $\Gamma$ from the grid
2. **Compute theta** from the PDE: $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2\Gamma$
3. **Solve up-bumped PDE** ($\sigma + \delta\sigma, r$) $\to$ extract $V^{\text{up}}$
4. **Solve down-bumped PDE** ($\sigma - \delta\sigma, r$) $\to$ extract $V^{\text{down}}$
5. **Vega**: $(V^{\text{up}} - V^{\text{down}}) / (2\delta\sigma)$
6. **Vomma**: $(V^{\text{up}} - 2V + V^{\text{down}}) / (\delta\sigma)^2$
7. **Solve up-bumped PDE** ($\sigma, r + \delta r$) $\to$ extract $V^{\text{up},r}$
8. **Solve down-bumped PDE** ($\sigma, r - \delta r$) $\to$ extract $V^{\text{down},r}$
9. **Rho**: $(V^{\text{up},r} - V^{\text{down},r}) / (2\delta r)$

Total PDE solves: **5** (base + 2 vega bumps + 2 rho bumps).

---

## Summary

$$
\boxed{
\mathcal{V} \approx \frac{V(\sigma + \delta\sigma) - V(\sigma - \delta\sigma)}{2\delta\sigma}, \qquad
\rho \approx \frac{V(r + \delta r) - V(r - \delta r)}{2\delta r}
}
$$

| Aspect | Recommendation |
|--------|---------------|
| **Method** | Central differences (second-order accuracy) |
| **Vega bump** | $\delta\sigma \approx 0.01$ (1 vol point) |
| **Rho bump** | $\delta r \approx 0.0001$ (1 basis point) |
| **Bump too large** | Truncation error dominates |
| **Bump too small** | Cancellation error dominates |
| **Optimal scaling** | $\delta p \sim \varepsilon_{\text{FDM}}^{1/3}$ for central differences |
| **Common error** | Forgetting to update boundary conditions when bumping $r$ |

Vega and rho require additional PDE solves beyond the base case, making them more expensive than delta and gamma. However, the bump-and-revalue approach is straightforward, robust, and extends naturally to any model parameter sensitivity.

---

## Exercises

**Exercise 1.** A base PDE solve gives $V(\sigma = 0.20) = 10.45$. Bumped solves give $V(\sigma = 0.21) = 11.23$ and $V(\sigma = 0.19) = 9.69$. Compute the central difference vega and the forward difference vega. Which is more accurate, and by how much?

??? success "Solution to Exercise 1"
    Given $V(\sigma = 0.20) = 10.45$, $V(\sigma = 0.21) = 11.23$, $V(\sigma = 0.19) = 9.69$.

    **Central difference vega** ($\delta\sigma = 0.01$):

    $$
    \mathcal{V}_{\text{central}} = \frac{V(0.21) - V(0.19)}{2 \times 0.01} = \frac{11.23 - 9.69}{0.02} = \frac{1.54}{0.02} = 77.0
    $$

    **Forward difference vega** ($\delta\sigma = 0.01$):

    $$
    \mathcal{V}_{\text{forward}} = \frac{V(0.21) - V(0.20)}{0.01} = \frac{11.23 - 10.45}{0.01} = \frac{0.78}{0.01} = 78.0
    $$

    The central difference estimate is $77.0$ and the forward difference estimate is $78.0$. They differ by $1.0$.

    The central difference is more accurate because its truncation error is $O((\delta\sigma)^2)$ while the forward difference has error $O(\delta\sigma)$. Specifically, the forward difference error is approximately $\frac{1}{2}\frac{\partial^2 V}{\partial\sigma^2}\delta\sigma$, while the central difference error is approximately $\frac{1}{6}\frac{\partial^3 V}{\partial\sigma^3}(\delta\sigma)^2$. For $\delta\sigma = 0.01$, the central difference error is roughly $(\delta\sigma)$ times smaller, i.e., about 100 times smaller. The difference of $1.0$ between the two estimates is primarily the first-order bias in the forward difference.

---

**Exercise 2.** The optimal bump size for central differences scales as $\delta p \sim \varepsilon_{\text{FDM}}^{1/3}$. If the FDM solution has accuracy $\varepsilon_{\text{FDM}} = 10^{-6}$, compute the optimal $\delta\sigma$ for vega estimation. What bump size is optimal if $\varepsilon_{\text{FDM}} = 10^{-3}$?

??? success "Solution to Exercise 2"
    The optimal bump size for central differences scales as:

    $$
    (\delta p)^* \sim \varepsilon_{\text{FDM}}^{1/3}
    $$

    **Case 1: $\varepsilon_{\text{FDM}} = 10^{-6}$**

    $$
    (\delta\sigma)^* \sim (10^{-6})^{1/3} = 10^{-2} = 0.01
    $$

    This matches the standard practical recommendation of a 1 percentage point volatility bump.

    **Case 2: $\varepsilon_{\text{FDM}} = 10^{-3}$**

    $$
    (\delta\sigma)^* \sim (10^{-3})^{1/3} = 10^{-1} = 0.1
    $$

    With a coarser FDM solution ($\varepsilon = 10^{-3}$), the optimal bump is much larger --- $0.1$ or 10 percentage points. A smaller bump would cause the cancellation error $\varepsilon_{\text{FDM}}/\delta\sigma$ to dominate, making the vega estimate noisy and unreliable.

    This illustrates an important principle: the bump size must be matched to the accuracy of the underlying PDE solver. Using a high-accuracy bump ($\delta\sigma = 0.01$) with a low-accuracy solver ($\varepsilon = 10^{-3}$) would give a cancellation error of $10^{-3}/10^{-2} = 0.1$, which could be unacceptably large relative to the true vega.

---

**Exercise 3.** When bumping the interest rate $r$ to compute rho, three things change in the PDE: the drift term, the discount term, and the boundary conditions. Explain what happens to the rho estimate if you update the PDE coefficients but forget to update the boundary condition $V(t, S_{\max}) = S_{\max} - Ke^{-r(T-t)}$.

??? success "Solution to Exercise 3"
    When bumping $r$ to $r + \delta r$, the PDE coefficients change:

    - Drift: $rS \to (r+\delta r)S$
    - Discount: $rV \to (r+\delta r)V$
    - Boundary: $V(t, S_{\max}) = S_{\max} - Ke^{-r(T-t)} \to S_{\max} - Ke^{-(r+\delta r)(T-t)}$

    If the boundary condition is **not** updated, the solver uses the **old** boundary value $S_{\max} - Ke^{-r(T-t)}$ instead of the correct bumped value $S_{\max} - Ke^{-(r+\delta r)(T-t)}$. The difference is:

    $$
    Ke^{-r(T-t)} - Ke^{-(r+\delta r)(T-t)} = Ke^{-r(T-t)}(1 - e^{-\delta r(T-t)}) \approx K\delta r(T-t)e^{-r(T-t)}
    $$

    This boundary error propagates inward from $S_{\max}$ and contaminates the solution. The effect is most severe for **deep in-the-money calls** (or deep out-of-the-money puts), where the option value near $S_{\max}$ is large and the boundary condition contribution to the price is significant.

    The resulting rho estimate will be biased: it will underestimate the true rho because the boundary value does not respond to the rate change. The error is proportional to $K(T-t)e^{-r(T-t)}$, which is precisely the analytical rho of the boundary payoff. For at-the-money options far from the boundary, the error may be small, but for robust implementation, all three components (drift, discount, boundary) must be updated consistently.

---

**Exercise 4.** Vomma (the second derivative of price with respect to volatility) can be computed from the same three PDE solutions used for vega: $\text{Vomma} = (V(\sigma + \delta\sigma) - 2V(\sigma) + V(\sigma - \delta\sigma))/(\delta\sigma)^2$. Using the values from Exercise 1, compute vomma. If the analytical vomma for this option is approximately $75$, assess the accuracy of the estimate.

??? success "Solution to Exercise 4"
    Using the values from Exercise 1: $V(\sigma = 0.21) = 11.23$, $V(\sigma = 0.20) = 10.45$, $V(\sigma = 0.19) = 9.69$, $\delta\sigma = 0.01$.

    $$
    \text{Vomma} = \frac{V(\sigma + \delta\sigma) - 2V(\sigma) + V(\sigma - \delta\sigma)}{(\delta\sigma)^2}
    $$

    $$
    = \frac{11.23 - 2(10.45) + 9.69}{(0.01)^2} = \frac{11.23 - 20.90 + 9.69}{0.0001} = \frac{0.02}{0.0001} = 200
    $$

    The analytical vomma is approximately $75$. The numerical estimate of $200$ is significantly larger, indicating poor accuracy.

    The discrepancy arises because vomma is a **second derivative** with respect to the bump parameter, and the central second difference amplifies errors by $1/(\delta\sigma)^2$. With $\delta\sigma = 0.01$, even small errors in the PDE solutions (say $\varepsilon \sim 10^{-3}$) produce an amplified error of order $\varepsilon/(\delta\sigma)^2 = 10^{-3}/(10^{-4}) = 10$, which is comparable to the vomma itself. A larger bump size (e.g., $\delta\sigma = 0.02$ or $0.05$) or a finer FDM grid would be needed for reliable vomma estimates.

---

**Exercise 5.** The vega-gamma relationship $\mathcal{V} \approx \sigma S^2 T \Gamma$ provides a cross-check. For an ATM call with $S = 100$, $\sigma = 0.25$, $T = 0.5$, and $\Gamma = 0.032$ (from the FDM grid), estimate vega using this relationship. Compare to the bumped estimate if $V(\sigma + 0.01) = 8.15$ and $V(\sigma - 0.01) = 7.35$.

??? success "Solution to Exercise 5"
    Using the vega-gamma relationship $\mathcal{V} \approx \sigma S^2 T \Gamma$ with $S = 100$, $\sigma = 0.25$, $T = 0.5$, $\Gamma = 0.032$:

    $$
    \mathcal{V}_{\text{approx}} = 0.25 \times 100^2 \times 0.5 \times 0.032 = 0.25 \times 10000 \times 0.5 \times 0.032 = 40.0
    $$

    **Bumped estimate** with $V(\sigma + 0.01) = 8.15$ and $V(\sigma - 0.01) = 7.35$:

    $$
    \mathcal{V}_{\text{bumped}} = \frac{8.15 - 7.35}{2 \times 0.01} = \frac{0.80}{0.02} = 40.0
    $$

    The two estimates agree exactly at $\mathcal{V} = 40.0$, providing a strong cross-check. This confirms the consistency between the spatial Greek (gamma from the grid) and the parameter Greek (vega from bumping). In practice, small discrepancies between the two estimates indicate either grid resolution issues or that the ATM approximation in the vega-gamma relationship is not perfectly applicable (e.g., for options away from the money).

---

**Exercise 6.** A complete set of Greeks requires 5 PDE solves (base + 2 vega bumps + 2 rho bumps). If each PDE solve takes 0.1 seconds with $M = 500$ and $N = 200$, what is the total time for all Greeks? Propose a strategy to reduce this cost by sharing computations across bumped solves.

??? success "Solution to Exercise 6"
    **Total time:** 5 PDE solves at 0.1 seconds each gives:

    $$
    \text{Total time} = 5 \times 0.1 = 0.5 \text{ seconds}
    $$

    **Strategies to reduce cost:**

    1. **Share the LU factorization.** For the implicit and Crank-Nicolson schemes, each time step requires solving a tridiagonal system $(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = \mathbf{b}$. When bumping $\sigma$, the matrix $A$ changes (because the diffusion coefficient $\frac{1}{2}\sigma^2 S^2$ changes), so the factorization cannot be directly reused. However, when bumping $r$, the changes to $A$ are smaller (only the drift and discount terms change), and if using the Sherman-Morrison formula or a rank-1 update to the existing factorization, the cost per solve can be reduced.

    2. **Use forward differences instead of central differences.** This reduces the total solves from 5 to 3 (base + 1 vega bump + 1 rho bump), cutting the time to 0.3 seconds. The accuracy drops from $O((\delta p)^2)$ to $O(\delta p)$, but for many applications this is acceptable.

    3. **Parallelize the bumped solves.** The 4 bumped PDE solves are independent of each other and of the base solve (once the grid and boundary conditions are set up). On a machine with 4+ cores, all bumped solves can run simultaneously, reducing wall-clock time from 0.5 seconds to approximately 0.2 seconds (base solve + one round of parallel bumped solves).

    4. **Reuse the base solution as an initial guess.** For iterative solvers (relevant for higher-dimensional problems), the bumped solution is close to the base solution. Starting the iterative solve from the base solution reduces the number of iterations needed for convergence.
