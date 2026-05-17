# Penalty Method

Solving the hard early-exercise constraint $V\ge\Phi$ exactly forces an LCP at every time step. The **penalty method** instead glues the constraint into the PDE: add a term $\rho(V-\Phi)^-$ that switches on only when $V$ dips below $\Phi$, pushing $V$ back up with force proportional to $\rho$. As $\rho\to\infty$ the penalty becomes infinitely stiff and the solution converges to the true American price. The payoff is a smooth nonlinear PDE solvable by standard methods -- no LCP solver required.

---

## The Penalty Approximation

### From Complementarity to Penalization

Recall (see [§ LCP — From Variational Inequality to Complementarity](linear_complementarity_formulation.md)): the American option satisfies $(-\partial_t V - \mathcal{L}V + rV)\ge 0$, $V\ge\Phi$, with product zero. The penalty method relaxes the hard constraint $V \geq \Phi$ by adding a **penalty term** that penalizes violations:

$$
\boxed{
\frac{\partial V^\rho}{\partial t} + \mathcal{L}V^\rho - rV^\rho + \rho\,(V^\rho - \Phi)^- = 0
}
$$

where $(x)^- = \min(x, 0)$ is the negative part and $\rho > 0$ is the **penalty parameter**.

!!! info "Intuition"
    When $V^\rho > \Phi$ (continuation region), the penalty term $(V^\rho - \Phi)^- = 0$ vanishes and the standard Black-Scholes PDE holds. When $V^\rho < \Phi$ (violation of the constraint), the penalty term $\rho(V^\rho - \Phi)^-$ is a large negative number that forces $V^\rho$ back toward $\Phi$. As $\rho \to \infty$, the penalized solution $V^\rho$ converges to the true American option price $V$.

### Alternative Penalty Functions

The negative part function $(x)^-$ is the simplest choice, but other penalty functions are used in practice:

| Penalty function $p(x)$ | Formula | Smoothness |
|:---|:---|:---|
| Negative part | $(x)^- = \min(x, 0)$ | Lipschitz (not $C^1$) |
| Smoothed negative part | $-\frac{1}{2}(\sqrt{x^2 + \epsilon^2} - x)$ | $C^\infty$ |
| Exponential | $-\frac{1}{\alpha}e^{-\alpha x}$ for $x < 0$ | $C^\infty$ |
| Power penalty | $[(x)^-]^{1/k}$ with $k > 1$ | $C^0$ |

The smoothed variants avoid the non-differentiability at $x = 0$, which can improve the convergence of Newton's method.

---

## Convergence of the Penalty Approximation

### Error Bound

**Theorem (Penalty Convergence).** *Let $V$ be the solution of the American option variational inequality and $V^\rho$ the solution of the penalized PDE. Then:*

$$
\boxed{0 \leq V - V^\rho \leq \frac{C}{\rho}}
$$

*where $C > 0$ depends on the problem data but not on $\rho$.*

??? note "Proof Sketch"
    **Lower bound** ($V^\rho \leq V$): The penalized equation can be written as

    $$
    -\frac{\partial V^\rho}{\partial t} - \mathcal{L}V^\rho + rV^\rho = \rho(V^\rho - \Phi)^- \leq 0
    $$

    Since $V$ satisfies $-\frac{\partial V}{\partial t} - \mathcal{L}V + rV \geq 0$, the difference $w = V - V^\rho$ satisfies a differential inequality with non-negative boundary and terminal data. By the maximum principle, $w \geq 0$.

    **Upper bound**: In the exercise region where $V = \Phi$, the penalized solution satisfies $V^\rho \geq \Phi - C/\rho$ for some constant $C$ (since the penalty term forces $\rho|V^\rho - \Phi| \leq C$ when $V^\rho < \Phi$). In the continuation region, $V^\rho$ satisfies the same PDE as $V$. Combining these estimates via comparison principles yields the $O(1/\rho)$ bound. $\square$

!!! tip "Practical Implication"
    The $O(1/\rho)$ convergence rate means that each factor-of-10 increase in $\rho$ gains roughly one decimal digit of accuracy. Typical choices:

    - $\rho = 10^4$: error $\sim 10^{-4}$ (moderate accuracy)
    - $\rho = 10^6$: error $\sim 10^{-6}$ (sufficient for most applications)
    - $\rho = 10^8$: error $\sim 10^{-8}$ (high precision, may cause conditioning issues)

---

## Discrete Formulation

### Time Discretization

Applying implicit Euler to the penalized PDE yields the nonlinear system at each time step:

$$
\frac{\mathbf{u}^{n+1} - \mathbf{u}^n}{\Delta\tau} + A\mathbf{u}^{n+1} + \rho\,\mathbf{p}(\mathbf{u}^{n+1}) = \mathbf{0}
$$

where $\mathbf{p}(\mathbf{u})$ is the componentwise penalty: $p_j(u_j) = (u_j - \Phi_j)^- = \min(u_j - \Phi_j, 0)$.

Rearranging:

$$
(I + \Delta\tau\, A)\mathbf{u}^{n+1} + \Delta\tau\,\rho\,\mathbf{p}(\mathbf{u}^{n+1}) = \mathbf{u}^n
$$

### Matrix Formulation with Indicator

Define the diagonal indicator matrix $P(\mathbf{u})$ with entries:

$$
P_{jj}(\mathbf{u}) = \begin{cases} 1 & \text{if } u_j < \Phi_j \\ 0 & \text{if } u_j \geq \Phi_j \end{cases}
$$

Then the penalty term can be written as $\mathbf{p}(\mathbf{u}) = P(\mathbf{u})(\mathbf{u} - \boldsymbol{\Phi})$, and the system becomes:

$$
\left(I + \Delta\tau\, A + \Delta\tau\,\rho\, P(\mathbf{u}^{n+1})\right)\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau\,\rho\, P(\mathbf{u}^{n+1})\boldsymbol{\Phi}
$$

Since $P$ depends on $\mathbf{u}^{n+1}$, this is a **nonlinear** system that must be solved iteratively.

---

## Newton's Method for the Penalty System

### Linearization

Define the residual:

$$
F(\mathbf{u}) = (I + \Delta\tau\, A)\mathbf{u} + \Delta\tau\,\rho\,\mathbf{p}(\mathbf{u}) - \mathbf{u}^n
$$

Newton's method solves $F(\mathbf{u}) = \mathbf{0}$ iteratively:

$$
\mathbf{u}^{(k+1)} = \mathbf{u}^{(k)} - [J(\mathbf{u}^{(k)})]^{-1} F(\mathbf{u}^{(k)})
$$

The Jacobian is:

$$
J(\mathbf{u}) = I + \Delta\tau\, A + \Delta\tau\,\rho\, P(\mathbf{u})
$$

Since $P$ is diagonal, $J$ is tridiagonal (same sparsity as $I + \Delta\tau A$), so the Newton step reduces to a **tridiagonal solve** --- the same cost as an unconstrained implicit step.

### Convergence of Newton's Method

!!! warning "Non-Smoothness"
    The penalty function $p(x) = (x)^-$ has a discontinuous derivative at $x = 0$. Strictly speaking, Newton's method applies to the generalized Jacobian. In practice, this causes no difficulty: Newton's method converges in 2-4 iterations for typical $\rho$ values.

    Using a smoothed penalty function (e.g., the smoothed negative part with parameter $\epsilon = 1/\rho$) restores classical quadratic convergence of Newton's method.

### Algorithm

!!! abstract "Algorithm: Penalty Method with Newton Iteration"
    **Input:** Time-stepping matrix $I + \Delta\tau A$, previous solution $\mathbf{u}^n$, payoff $\boldsymbol{\Phi}$, penalty parameter $\rho$, tolerance $\varepsilon$.

    **For** each time step $n = 0, 1, \ldots, N-1$:

    1. Set initial guess $\mathbf{u}^{(0)} = \mathbf{u}^n$.
    2. **Repeat** for $k = 0, 1, 2, \ldots$:
        - Compute indicator: $P_{jj} = 1$ if $u_j^{(k)} < \Phi_j$, else $0$.
        - Form $J = I + \Delta\tau A + \Delta\tau\rho\, P$.
        - Compute residual: $F = (I + \Delta\tau A)\mathbf{u}^{(k)} + \Delta\tau\rho\, P(\mathbf{u}^{(k)} - \boldsymbol{\Phi}) - \mathbf{u}^n$.
        - Solve $J\,\delta\mathbf{u} = -F$ (tridiagonal solve).
        - Update: $\mathbf{u}^{(k+1)} = \mathbf{u}^{(k)} + \delta\mathbf{u}$.
        - **If** $\|\delta\mathbf{u}\|_\infty < \varepsilon$, **break**.
    3. Set $\mathbf{u}^{n+1} = \mathbf{u}^{(k+1)}$.

    **End For**

---

## Fixed-Point Iteration Alternative

For simplicity, one can use a **fixed-point (Picard) iteration** instead of Newton's method:

1. Given $\mathbf{u}^{(k)}$, compute $P = P(\mathbf{u}^{(k)})$.
2. Solve the **linear** system $(I + \Delta\tau A + \Delta\tau\rho\, P)\mathbf{u}^{(k+1)} = \mathbf{u}^n + \Delta\tau\rho\, P\boldsymbol{\Phi}$.
3. Repeat until convergence.

This is equivalent to "lagging" the indicator $P$ by one iteration. It converges for sufficiently large $\rho$ but may require more iterations than Newton's method. In practice, the fixed-point iteration also converges in 2-5 iterations for well-chosen $\rho$.

---

## Conditioning and Choice of Penalty Parameter

### The Conditioning Dilemma

Large $\rho$ improves the approximation accuracy ($O(1/\rho)$ error) but worsens the conditioning of the Jacobian $J$. The condition number scales as:

$$
\kappa(J) \sim \rho \cdot \Delta\tau
$$

in the exercise region, since the diagonal entries of $J$ in the exercise region are of order $1 + \Delta\tau\rho$.

### Practical Guidelines

| Parameter | Typical range | Notes |
|:---|:---|:---|
| $\rho$ | $10^4$ to $10^8$ | Balance accuracy vs. conditioning |
| Newton tolerance | $10^{-10}$ to $10^{-12}$ | Tighter than penalty error |
| Max Newton iterations | 5-10 | Convergence usually in 2-4 |

!!! tip "Rule of Thumb"
    Choose $\rho$ so that the penalty error $O(1/\rho)$ is smaller than the discretization error $O(\Delta\tau + h^2)$. For a grid with $h = 0.01$ (space) and $\Delta\tau = 0.01$ (time), the discretization error is $O(10^{-2})$, so $\rho = 10^4$ already suffices.

---

## Worked Example

Consider an American put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, on a 3-point interior grid with $S_1 = 40$, $S_2 = 80$, $S_3 = 120$.

**Setup:** $\boldsymbol{\Phi} = (60, 20, 0)^T$, $\mathbf{u}^n = (58, 18, 2)^T$, $\Delta\tau = 0.01$, $\rho = 10^4$.

**Iteration 1:** Starting from $\mathbf{u}^{(0)} = \mathbf{u}^n = (58, 18, 2)^T$.

Compute the indicator: $u_1 = 58 < 60 = \Phi_1$ so $P_{11} = 1$; $u_2 = 18 < 20 = \Phi_2$ so $P_{22} = 1$; $u_3 = 2 > 0 = \Phi_3$ so $P_{33} = 0$.

The Jacobian $J$ has the same structure as $I + \Delta\tau A$ but with $\Delta\tau\rho = 100$ added to diagonal entries $j = 1, 2$. This makes $J_{11}$ and $J_{22}$ very large, effectively forcing $u_1 \approx \Phi_1 = 60$ and $u_2 \approx \Phi_2 = 20$ in the exercise region.

After the Newton step, the solution is approximately:

$$
\mathbf{u}^{(1)} \approx (60.00, 20.00, 2.05)^T
$$

The first two components are pinned to the payoff (up to $O(1/\rho)$ error), while the third satisfies the unconstrained PDE. After one more Newton step, convergence is achieved.

**Comparison with exact LCP solution:** The exact LCP gives $(60, 20, 2.05)^T$, confirming the penalty method with $\rho = 10^4$ is accurate to several decimal places on this grid.

---

## Comparison with PSOR

| Aspect | Penalty method | PSOR |
|:---|:---|:---|
| **Formulation** | Smooth nonlinear PDE | Iterative LCP solve |
| **Constraint handling** | Soft (penalty approximation) | Exact (projection) |
| **Approximation error** | $O(1/\rho)$ from penalization | None (solves LCP exactly to tolerance) |
| **Solver per time step** | Newton (2-4 iterations) | PSOR (5-20 iterations) |
| **Cost per iteration** | One tridiagonal solve | One sweep ($O(m)$) |
| **Parameter tuning** | $\rho$ (penalty) | $\omega$ (relaxation) |
| **Extension to higher dimensions** | Natural (standard PDE solver) | More complex |
| **Conditioning** | Degrades with large $\rho$ | Unaffected |

!!! tip "When to Use Which"

    - **Penalty method**: Preferred when an existing PDE solver infrastructure is available, or in higher dimensions where PSOR is less natural. The penalty term is easy to add to any implicit time-stepping code.
    - **PSOR**: Preferred when exact LCP solutions are required without approximation error, or when conditioning is a concern.

---

## Extension to Higher Dimensions

A major advantage of the penalty method is its natural extension to multi-dimensional problems (e.g., American options on multiple assets). The penalized PDE in $d$ dimensions is:

$$
\frac{\partial V^\rho}{\partial t} + \mathcal{L}_d V^\rho - rV^\rho + \rho(V^\rho - \Phi)^- = 0
$$

where $\mathcal{L}_d$ is the multi-dimensional Black-Scholes operator. The penalty term does not change the sparsity structure of the discretization matrix, so standard multi-dimensional PDE solvers (ADI, operator splitting) can be used with only minor modifications.

---

## Summary

| Concept | Key point |
|:---|:---|
| Core idea | Replace hard constraint $V \geq \Phi$ with penalty term $\rho(V - \Phi)^-$ |
| Convergence | $V^\rho \to V$ as $\rho \to \infty$ with error $O(1/\rho)$ |
| Discrete solver | Newton's method on penalized nonlinear system (2-4 iterations) |
| Cost per step | Same as unconstrained solve (tridiagonal) plus Newton iterations |
| Conditioning | Degrades with large $\rho$; balance against discretization error |
| Advantage | Simple implementation, natural multi-dimensional extension |
| Limitation | Introduces approximation error; conditioning sensitivity |

---

## Exercises

**Exercise 1.** For the penalty method with $\rho = 10^6$, estimate the penalty approximation error $O(1/\rho)$. If the discretization error is $O(h^2)$ with $h = 0.01$, is the penalty error negligible? What value of $\rho$ would balance the penalty and discretization errors?

??? success "Solution to Exercise 1"
    **Penalty approximation error with $\rho = 10^6$:**

    The error bound is $|V - V^\rho| \leq C/\rho$. For $\rho = 10^6$:

    $$
    |V - V^\rho| \leq \frac{C}{10^6} \sim O(10^{-6})
    $$

    (assuming the constant $C$ is of order unity, which is typical for option prices of order $\$1$-$\$100$).

    **Comparison with discretization error:**

    The spatial discretization error is $O(h^2) = O(0.01^2) = O(10^{-4})$. Since $10^{-6} \ll 10^{-4}$, the penalty error is indeed negligible compared to the discretization error.

    **Balancing the errors:**

    To balance the penalty error and discretization error, we set:

    $$
    \frac{C}{\rho} = h^2 = 10^{-4}
    $$

    $$
    \rho = \frac{C}{h^2} = \frac{C}{10^{-4}} = 10^4 C
    $$

    For $C \sim O(1)$, this gives $\rho \approx 10^4$. Using $\rho$ much larger than $10^4$ does not improve the overall accuracy since the spatial error dominates. The choice $\rho = 10^6$ is two orders of magnitude beyond what is needed, which is safe but may unnecessarily worsen conditioning.

---

**Exercise 2.** Write out one iteration of Newton's method for the penalty system at a single time step. Given $\mathbf{u}^{(0)} = \mathbf{u}^n = (58, 18, 2)^T$ with $\boldsymbol{\Phi} = (60, 20, 0)^T$ and $\rho = 10^4$, compute the indicator matrix $P$ and describe qualitatively how the Newton step adjusts the solution.

??? success "Solution to Exercise 2"
    **Setting up Newton's method:**

    The residual is $F(\mathbf{u}) = (I + \Delta\tau A)\mathbf{u} + \Delta\tau\rho\,\mathbf{p}(\mathbf{u}) - \mathbf{u}^n$ where $p_j(u_j) = \min(u_j - \Phi_j, 0)$.

    Starting from $\mathbf{u}^{(0)} = \mathbf{u}^n = (58, 18, 2)^T$ with $\boldsymbol{\Phi} = (60, 20, 0)^T$ and $\rho = 10^4$:

    **Compute the indicator matrix $P$:**

    - $u_1^{(0)} = 58 < 60 = \Phi_1$: $P_{11} = 1$
    - $u_2^{(0)} = 18 < 20 = \Phi_2$: $P_{22} = 1$
    - $u_3^{(0)} = 2 > 0 = \Phi_3$: $P_{33} = 0$

    So $P = \operatorname{diag}(1, 1, 0)$.

    **The Jacobian:**

    $$
    J = I + \Delta\tau A + \Delta\tau\rho\, P
    $$

    With $\Delta\tau\rho = 0.01 \times 10^4 = 100$, the diagonal entries $J_{11}$ and $J_{22}$ each receive an additional $+100$, making them very large (of order 101). The entry $J_{33}$ is unaffected.

    **Qualitative effect of the Newton step:**

    The residual at $\mathbf{u}^{(0)}$ has large components at $j = 1, 2$ because $p_1 = 58 - 60 = -2$ and $p_2 = 18 - 20 = -2$. The penalty contributions are $\Delta\tau\rho \times (-2) = -200$ at each of these components.

    The Newton step $\delta\mathbf{u} = -J^{-1}F$ adjusts the solution to approximately satisfy the penalized system. Because $J_{11}$ and $J_{22}$ are dominated by the $\Delta\tau\rho$ term, the Newton correction drives $u_1$ and $u_2$ very close to $\Phi_1 = 60$ and $\Phi_2 = 20$ respectively. Specifically:

    $$
    \delta u_j \approx -\frac{F_j}{J_{jj}} \approx -\frac{\Delta\tau\rho(u_j - \Phi_j)}{\Delta\tau\rho} = \Phi_j - u_j
    $$

    So $u_1^{(1)} \approx 60$ and $u_2^{(1)} \approx 20$ (pinned to the payoff). For $j = 3$, the penalty term is zero, and the Newton step adjusts $u_3$ according to the unconstrained PDE, giving $u_3^{(1)} \approx 2.05$.

---

**Exercise 3.** The penalty function $(x)^- = \min(x, 0)$ has a discontinuous derivative at $x = 0$. Describe the smoothed penalty function $p(x) = -\frac{1}{2}(\sqrt{x^2 + \epsilon^2} - x)$ and explain how it approximates $(x)^-$. For what choice of $\epsilon$ relative to $\rho$ does the smoothing not affect the overall penalty accuracy?

??? success "Solution to Exercise 3"
    **The smoothed penalty function:**

    $$
    p(x) = -\frac{1}{2}\left(\sqrt{x^2 + \epsilon^2} - x\right)
    $$

    **Behavior:**

    - For $x \gg \epsilon$: $\sqrt{x^2 + \epsilon^2} \approx |x| = x$, so $p(x) \approx -\frac{1}{2}(x - x) = 0$. The penalty vanishes (continuation region).
    - For $x \ll -\epsilon$: $\sqrt{x^2 + \epsilon^2} \approx |x| = -x$, so $p(x) \approx -\frac{1}{2}(-x - x) = x$. This matches $(x)^- = x$ for $x < 0$ (exercise region).
    - For $x = 0$: $p(0) = -\frac{\epsilon}{2}$, which is close to $0 = (0)^-$ when $\epsilon$ is small.

    The smoothed function is $C^\infty$ everywhere (the square root is smooth since $x^2 + \epsilon^2 > 0$) and approximates $(x)^-$ with maximum error $O(\epsilon)$:

    $$
    |p(x) - (x)^-| \leq \frac{\epsilon}{2}
    $$

    Its derivative is:

    $$
    p'(x) = -\frac{1}{2}\left(\frac{x}{\sqrt{x^2 + \epsilon^2}} - 1\right)
    $$

    which is continuous everywhere, enabling classical Newton convergence (quadratic rate).

    **Choice of $\epsilon$ relative to $\rho$:**

    The smoothing introduces an additional error of $O(\epsilon)$ in the penalty function. Combined with the penalty approximation error $O(1/\rho)$, the total error is $O(1/\rho + \epsilon)$.

    To ensure the smoothing does not degrade the penalty accuracy, choose $\epsilon$ so that $\epsilon \lesssim 1/\rho$, i.e.:

    $$
    \epsilon = O(1/\rho)
    $$

    For example, $\epsilon = 1/\rho$. With this choice, the total approximation error remains $O(1/\rho)$, and the smoothed penalty function is well-conditioned for Newton's method.

---

**Exercise 4.** The condition number of the Jacobian scales as $\kappa(J) \sim \rho\Delta\tau$ in the exercise region. For $\rho = 10^8$ and $\Delta\tau = 0.01$, estimate $\kappa(J)$. At what point does the conditioning become problematic for double-precision floating-point arithmetic?

??? success "Solution to Exercise 4"
    **Condition number estimate:**

    With $\rho = 10^8$ and $\Delta\tau = 0.01$:

    $$
    \kappa(J) \sim \rho\,\Delta\tau = 10^8 \times 0.01 = 10^6
    $$

    The largest diagonal entries (in the exercise region) are of order $1 + \Delta\tau\rho = 1 + 10^6 \approx 10^6$. The smallest entries (in the continuation region) are of order $1 + \Delta\tau\,a_{jj} \approx O(1)$. The ratio gives $\kappa(J) \sim 10^6$.

    **When does conditioning become problematic?**

    In double-precision floating-point arithmetic (IEEE 754), approximately 15-16 significant decimal digits are available ($\epsilon_{\text{machine}} \approx 10^{-16}$). The effective accuracy of a linear solve is roughly:

    $$
    \text{relative error} \sim \kappa(J) \times \epsilon_{\text{machine}}
    $$

    - $\kappa = 10^6$: relative error $\sim 10^{-10}$. This is still very accurate --- no problem.
    - $\kappa = 10^8$ (e.g., $\rho = 10^{10}$, $\Delta\tau = 0.01$): relative error $\sim 10^{-8}$. Starting to lose accuracy but still adequate for most applications.
    - $\kappa = 10^{12}$: relative error $\sim 10^{-4}$. Only 4 significant digits --- problematic for accurate pricing.
    - $\kappa = 10^{16}$: relative error $\sim 1$. Complete loss of accuracy.

    The conditioning becomes practically problematic when $\rho\,\Delta\tau \gtrsim 10^{10}$, i.e., when the condition number exceeds approximately $10^{10}$. For $\Delta\tau = 0.01$, this corresponds to $\rho \gtrsim 10^{12}$.

    In practice, the rule of thumb is to choose $\rho$ so that $\kappa(J) \lesssim 10^{8}$ to maintain at least 8 significant digits. For $\Delta\tau = 0.01$, this means $\rho \lesssim 10^{10}$, which is far beyond the range needed for practical accuracy.

---

**Exercise 5.** Compare the penalty method and PSOR for pricing an American put. If the penalty method uses 3 Newton iterations per time step (each costing one tridiagonal solve) and PSOR uses 12 iterations per time step (each costing one sweep), which method is faster per time step? Consider that a tridiagonal solve costs approximately $5M$ operations and a PSOR sweep costs approximately $3M$ operations.

??? success "Solution to Exercise 5"
    **Penalty method cost per time step:**

    Each Newton iteration requires one tridiagonal solve costing approximately $5M$ operations. With 3 Newton iterations:

    $$
    C_{\text{penalty}} = 3 \times 5M = 15M
    $$

    **PSOR cost per time step:**

    Each PSOR sweep costs approximately $3M$ operations. With 12 iterations:

    $$
    C_{\text{PSOR}} = 12 \times 3M = 36M
    $$

    **Comparison:**

    $$
    \frac{C_{\text{PSOR}}}{C_{\text{penalty}}} = \frac{36M}{15M} = 2.4
    $$

    PSOR is approximately 2.4 times more expensive per time step than the penalty method for these parameters.

    **Per time step:** The penalty method requires $15M$ operations and PSOR requires $36M$ operations. The penalty method is faster by a factor of 2.4.

    However, the comparison is not purely about operation count:

    - The tridiagonal solve in the penalty method requires $O(M)$ *sequential* operations (forward and back substitution). PSOR sweeps are also sequential but have simpler per-element operations.
    - The penalty method introduces an approximation error $O(1/\rho)$ that PSOR does not have.
    - On modern hardware, memory access patterns may matter more than raw operation counts. Both methods have similar memory access patterns (sequential sweeps through the grid).

    Overall, the penalty method with Newton iteration is the faster approach when $K_{\text{iter}} > \frac{5}{3}N_{\text{Newton}} = \frac{5}{3}(3) = 5$ PSOR iterations would be needed. Since 12 well exceeds 5, the penalty method wins comfortably here.

---

**Exercise 6.** The penalty method extends naturally to multi-dimensional problems. For a two-asset American option with a 2D spatial grid of size $M \times M$, the penalty term does not change the sparsity structure of the discretization matrix. Explain why this is a significant advantage over PSOR, which is less natural in higher dimensions.

??? success "Solution to Exercise 6"
    **Why the penalty method's sparsity preservation is advantageous in higher dimensions:**

    For a two-asset American option on an $M \times M$ grid, the unknowns are $\{u_{i,j}\}$ for $i, j = 1, \ldots, M$, giving $M^2$ total unknowns. The discretization of the 2D Black-Scholes operator produces a sparse matrix $A$ with a banded structure (5-point or 9-point stencil, depending on the treatment of cross-derivative terms).

    **Penalty method in 2D:**

    The penalty term $\rho\,\mathbf{p}(\mathbf{u})$ is a *diagonal* perturbation: the indicator $P_{(i,j),(i,j)} = 1$ if $u_{i,j} < \Phi_{i,j}$. Adding this to the Jacobian $J = I + \Delta\tau A + \Delta\tau\rho P$ preserves the sparsity structure of $A$ exactly. Standard 2D PDE solvers (ADI splitting, multigrid, sparse direct solvers) can be applied without modification --- only the diagonal entries change in the exercise region.

    **PSOR in 2D:**

    PSOR requires a componentwise sweep through all $M^2$ unknowns, updating each one using its neighbors. In 1D, the natural ordering of grid points makes this straightforward. In 2D:

    - The sweep ordering (row-by-row, column-by-column, red-black) affects convergence.
    - The optimal $\omega$ is harder to determine analytically.
    - Convergence deteriorates: the spectral radius of the Gauss-Seidel iteration for 2D problems is $\rho(G_1) \approx 1 - c/M^2$, requiring $O(M^2)$ iterations per time step.
    - Multigrid acceleration is possible but adds significant implementation complexity.

    **Significance:**

    The penalty method leverages the full power of existing multi-dimensional PDE solvers. For example, ADI (Alternating Direction Implicit) methods split the 2D operator into 1D sweeps, each requiring tridiagonal solves. The penalty term integrates seamlessly: in each ADI sub-step, the diagonal entries are modified for exercise-region points. The total cost per time step is $O(M^2)$ (a few tridiagonal solves of size $M$, repeated $M$ times), compared to $O(M^2 \times K_{\text{iter}})$ for PSOR with potentially large $K_{\text{iter}}$.

    This advantage grows with dimension: in $d$ dimensions with $M$ points per dimension, the penalty method cost scales as $O(M^d)$ per Newton step (same as an unconstrained PDE solve), while PSOR cost scales as $O(M^d \times K_{\text{iter}})$ with $K_{\text{iter}}$ potentially growing with $M$.
