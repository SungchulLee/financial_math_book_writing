# Vega and Rho via Bumping

Vega and rho measure the sensitivity of the option price to the volatility and interest rate parameters, respectively. Unlike delta and gamma, which are derivatives with respect to the state variable $S$ available directly from the FDM grid, vega and rho require **bumping** --- perturbing the parameter and re-solving the PDE.

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

### Black-Scholes Analytical Vega

For a European call under Black-Scholes:

$$
\mathcal{V} = S\sqrt{T}\,\phi(d_1)
$$

where $\phi$ is the standard normal density and $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$. This is always positive: higher volatility increases option value.

### Properties of Vega

- **Vega is maximized at-the-money**: $S \approx Ke^{-rT}$
- **Vega decays with time**: $\mathcal{V} \propto \sqrt{T}$ for ATM options
- **Vega is the same for calls and puts**: By put-call parity, $\mathcal{V}_{\text{call}} = \mathcal{V}_{\text{put}}$

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

### Black-Scholes Analytical Rho

For a European call:

$$
\rho_{\text{call}} = KTe^{-rT}\Phi(d_2)
$$

For a European put:

$$
\rho_{\text{put}} = -KTe^{-rT}\Phi(-d_2)
$$

Call rho is positive (higher rates increase call values), and put rho is negative.

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

---

**Exercise 2.** The optimal bump size for central differences scales as $\delta p \sim \varepsilon_{\text{FDM}}^{1/3}$. If the FDM solution has accuracy $\varepsilon_{\text{FDM}} = 10^{-6}$, compute the optimal $\delta\sigma$ for vega estimation. What bump size is optimal if $\varepsilon_{\text{FDM}} = 10^{-3}$?

---

**Exercise 3.** When bumping the interest rate $r$ to compute rho, three things change in the PDE: the drift term, the discount term, and the boundary conditions. Explain what happens to the rho estimate if you update the PDE coefficients but forget to update the boundary condition $V(t, S_{\max}) = S_{\max} - Ke^{-r(T-t)}$.

---

**Exercise 4.** Vomma (the second derivative of price with respect to volatility) can be computed from the same three PDE solutions used for vega: $\text{Vomma} = (V(\sigma + \delta\sigma) - 2V(\sigma) + V(\sigma - \delta\sigma))/(\delta\sigma)^2$. Using the values from Exercise 1, compute vomma. If the analytical vomma for this option is approximately $75$, assess the accuracy of the estimate.

---

**Exercise 5.** The vega-gamma relationship $\mathcal{V} \approx \sigma S^2 T \Gamma$ provides a cross-check. For an ATM call with $S = 100$, $\sigma = 0.25$, $T = 0.5$, and $\Gamma = 0.032$ (from the FDM grid), estimate vega using this relationship. Compare to the bumped estimate if $V(\sigma + 0.01) = 8.15$ and $V(\sigma - 0.01) = 7.35$.

---

**Exercise 6.** A complete set of Greeks requires 5 PDE solves (base + 2 vega bumps + 2 rho bumps). If each PDE solve takes 0.1 seconds with $M = 500$ and $N = 200$, what is the total time for all Greeks? Propose a strategy to reduce this cost by sharing computations across bumped solves.
