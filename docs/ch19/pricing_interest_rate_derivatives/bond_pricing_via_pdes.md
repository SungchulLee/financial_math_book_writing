# Bond Pricing via PDEs


In short-rate models, zero-coupon bond prices can be characterized as solutions of **partial differential equations (PDEs)**. The PDE approach provides intuition about boundary conditions and links interest-rate pricing to diffusion theory.

---

## Setup


Let $r_t$ follow a risk-neutral short-rate diffusion

$$
dr_t = \mu^{\mathbb{Q}}(t,r_t)\,dt + \sigma(t,r_t)\,dW_t^{\mathbb{Q}}
$$



Define the zero-coupon bond price

$$
P(t,T,r) = \text{price at }t\text{ of }1\text{ paid at }T
$$


given $r_t=r$.

---

## Pricing PDE


By standard arbitrage arguments, $P(t,T,r)$ satisfies

$$
\partial_t P

+ \mu^{\mathbb{Q}}(t,r)\,\partial_r P
+ \tfrac12 \sigma(t,r)^2\,\partial_{rr}P
- rP = 0
$$


with terminal condition

$$
P(T,T,r)=1
$$



This PDE is backward in time.

---

## Boundary conditions


Appropriate boundary conditions depend on the model:

- as $r\to \infty$: bond price decays to zero,
- as $r\to -\infty$ (if allowed): growth must remain controlled,
- at boundaries like $r=0$ (CIR): degeneracy requires careful handling.

Correct boundary treatment is crucial for numerical stability.

---

## Analytical solutions


For affine models (Vasicek, CIR):

- the PDE admits closed-form solutions,
- solutions take exponential-affine form,
- coefficients satisfy ODEs.

For more general models, numerical PDE methods are required.

---

## Numerical PDE methods


Common schemes include:

- finite differences (implicit, Crank–Nicolson),
- alternating-direction implicit (ADI) methods,
- grid truncation and stabilization techniques.

Bond PDEs are one-dimensional and relatively tractable.

---

## Key takeaways


- Bond prices satisfy linear parabolic PDEs.
- PDEs clarify boundary behavior and numerical issues.
- Closed forms arise in affine short-rate models.

---

## Further reading


- Wilmott, *Derivatives*.
- Brigo & Mercurio, bond pricing PDEs.

---

## Exercises

**Exercise 1.** Consider the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$. Write down the bond pricing PDE for $P(t,T,r)$ explicitly in terms of $\kappa$, $\theta$, and $\sigma$. Verify that the terminal condition $P(T,T,r) = 1$ is satisfied by the known Vasicek closed-form solution.

??? success "Solution to Exercise 1"

    In the Vasicek model the risk-neutral drift is $\mu^{\mathbb{Q}}(t,r) = \kappa(\theta - r)$ and the diffusion is $\sigma(t,r) = \sigma$ (constant). Substituting into the general bond pricing PDE:

    $$
    \partial_t P + \kappa(\theta - r)\,\partial_r P + \tfrac{1}{2}\sigma^2\,\partial_{rr}P - rP = 0
    $$

    with terminal condition $P(T,T,r) = 1$.

    The known Vasicek closed-form solution is $P(t,T,r) = e^{A(\tau) - B(\tau)r}$ where $\tau = T - t$ and:

    $$
    B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}, \qquad A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
    $$

    At $\tau = 0$ (i.e., $t = T$): $B(0) = 0$ and $A(0) = 0$, so $P(T,T,r) = e^{0 + 0} = 1$, confirming the terminal condition.

    To verify it satisfies the PDE, compute the partial derivatives. Writing $P = e^{A - Br}$:

    - $\partial_r P = -B P$, so $\partial_{rr}P = B^2 P$
    - $\partial_t P = (-A' + B'r)P$ where primes denote derivatives with respect to $\tau$ with a sign change since $\tau = T - t$, giving $\partial_t P = (A'(\tau) - B'(\tau)r)P$ where $A' = dA/d\tau$ and $B' = dB/d\tau$ but $\partial_t = -\partial_\tau$, so $\partial_t P = (-A'(\tau) + B'(\tau)r)P$

    Substituting into the PDE and dividing by $P$:

    $$
    -A' + B'r + \kappa(\theta - r)(-B) + \tfrac{1}{2}\sigma^2 B^2 - r = 0
    $$

    Collecting terms in $r$ and constant terms:

    $$
    r(B' + \kappa B - 1) + (-A' - \kappa\theta B + \tfrac{1}{2}\sigma^2 B^2) = 0
    $$

    For this to hold for all $r$, both coefficients must vanish:

    $$
    B'(\tau) = 1 - \kappa B(\tau), \qquad B(0) = 0
    $$

    $$
    A'(\tau) = -\kappa\theta B(\tau) + \tfrac{1}{2}\sigma^2 B(\tau)^2, \qquad A(0) = 0
    $$

    Solving the first ODE gives $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$, and integrating the second gives the known expression for $A(\tau)$, confirming consistency.

---

**Exercise 2.** Explain why the bond pricing PDE is **backward** in time. Describe the change of variable $\tau = T - t$ and rewrite the PDE as a forward equation in $\tau$. What is the initial condition in terms of $\tau$?

??? success "Solution to Exercise 2"

    The bond pricing PDE is backward in time because it has a **terminal** condition at $t = T$ rather than an initial condition at $t = 0$. Economically, we know the bond's payoff at maturity ($P(T,T,r) = 1$) and we must propagate this information backward to find today's price. This is characteristic of financial pricing problems: the payoff is known in the future, and we discount backward.

    Introducing the time-to-maturity variable $\tau = T - t$, so $t = T - \tau$ and $\partial_t = -\partial_\tau$, the PDE becomes:

    $$
    -\partial_\tau P + \mu^{\mathbb{Q}}(T-\tau, r)\,\partial_r P + \tfrac{1}{2}\sigma(T-\tau, r)^2\,\partial_{rr}P - rP = 0
    $$

    Rearranging:

    $$
    \partial_\tau P = \mu^{\mathbb{Q}}(T-\tau, r)\,\partial_r P + \tfrac{1}{2}\sigma(T-\tau, r)^2\,\partial_{rr}P - rP
    $$

    This is now a **forward** equation in $\tau$, meaning we march forward from $\tau = 0$ toward larger $\tau$. The initial condition in terms of $\tau$ is:

    $$
    P(\tau = 0, r) = P(T, T, r) = 1 \quad \text{for all } r
    $$

    This forward-in-$\tau$ formulation is convenient for numerical implementation because standard time-stepping methods (explicit, implicit, Crank--Nicolson) naturally advance from a known initial state.

---

**Exercise 3.** For the CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}$, the diffusion coefficient vanishes at $r = 0$. Discuss the type of boundary condition required at $r = 0$ and explain how the Feller condition $2\kappa\theta \geq \sigma^2$ affects boundary behavior. What happens to the PDE solution when the Feller condition is violated?

??? success "Solution to Exercise 3"

    In the CIR model, $\sigma(r) = \sigma\sqrt{r}$, so $\sigma^2(r) = \sigma^2 r$. The diffusion coefficient vanishes at $r = 0$, making the PDE degenerate at this boundary.

    **Boundary condition at $r = 0$:** When $r = 0$, the second-order term $\frac{1}{2}\sigma^2 r\,\partial_{rr}P$ vanishes, and the PDE reduces to a first-order equation:

    $$
    \partial_t P + \kappa\theta\,\partial_r P = 0
    $$

    Since $\kappa\theta > 0$, the drift points away from $r = 0$ (inward), so $r = 0$ is an **entrance boundary** (under the Feller condition) and no explicit boundary condition needs to be imposed. The PDE solution is determined by the degeneracy itself.

    **Feller condition $2\kappa\theta \geq \sigma^2$:** This condition determines whether the origin is reached by the diffusion:

    - When $2\kappa\theta \geq \sigma^2$ (Feller condition satisfied): the drift dominates near $r = 0$, and $r = 0$ is never reached. The boundary is inaccessible, and no boundary condition is needed. The process stays strictly positive.

    - When $2\kappa\theta < \sigma^2$ (Feller condition violated): the diffusion is strong enough near zero that $r_t$ can reach $r = 0$. The boundary becomes accessible, and one must specify what happens there. In the standard CIR model, a reflecting boundary condition is imposed (instantaneous reflection), ensuring $r_t \geq 0$.

    **Effect on PDE solution when Feller is violated:** The PDE solution can still be well-defined if a reflecting boundary condition is imposed at $r = 0$. Numerically, this means setting $\partial_r P(t, T, 0) = \partial_r P$ at the boundary using a one-sided difference and using the degenerate form of the PDE. However, the solution may exhibit reduced regularity near $r = 0$, and numerical schemes require finer grids near the origin to maintain accuracy.

---

**Exercise 4.** Show that if $P(t,T,r) = e^{A(t,T) + B(t,T)\,r}$ (exponential-affine form), substitution into the general bond pricing PDE yields a system of ODEs for $A$ and $B$ when the drift and diffusion are affine in $r$:

$$
\mu^{\mathbb{Q}}(t,r) = a(t) + b(t)\,r, \qquad \sigma(t,r)^2 = c(t) + d(t)\,r
$$

Derive the ODEs and their terminal conditions.

??? success "Solution to Exercise 4"

    Assume $P(t,T,r) = e^{A(t,T) + B(t,T)r}$ with affine drift and diffusion:

    $$
    \mu^{\mathbb{Q}}(t,r) = a(t) + b(t)r, \qquad \sigma(t,r)^2 = c(t) + d(t)r
    $$

    Compute the partial derivatives:

    $$
    \partial_t P = (\partial_t A + \partial_t B \cdot r)P, \quad \partial_r P = B\,P, \quad \partial_{rr}P = B^2 P
    $$

    Substituting into the PDE $\partial_t P + \mu^{\mathbb{Q}}\partial_r P + \frac{1}{2}\sigma^2\partial_{rr}P - rP = 0$ and dividing by $P$:

    $$
    \partial_t A + \partial_t B \cdot r + (a + br)B + \tfrac{1}{2}(c + dr)B^2 - r = 0
    $$

    Regrouping into terms constant in $r$ and terms linear in $r$:

    $$
    \underbrace{(\partial_t A + aB + \tfrac{1}{2}cB^2)}_{\text{constant}} + r\underbrace{(\partial_t B + bB + \tfrac{1}{2}dB^2 - 1)}_{\text{coefficient of } r} = 0
    $$

    Since this must hold for all $r$, each coefficient must vanish separately:

    **ODE for $B$:**

    $$
    \partial_t B(t,T) + b(t)\,B(t,T) + \tfrac{1}{2}d(t)\,B(t,T)^2 - 1 = 0, \qquad B(T,T) = 0
    $$

    This is a Riccati ODE for $B$.

    **ODE for $A$:**

    $$
    \partial_t A(t,T) + a(t)\,B(t,T) + \tfrac{1}{2}c(t)\,B(t,T)^2 = 0, \qquad A(T,T) = 0
    $$

    This is a linear ODE for $A$ once $B$ is known (it can be solved by direct integration).

    The terminal conditions $A(T,T) = 0$ and $B(T,T) = 0$ follow from $P(T,T,r) = e^0 = 1$.

    **Special cases:**

    - Vasicek: $a = \kappa\theta$, $b = -\kappa$, $c = \sigma^2$, $d = 0$. The $B$-ODE is linear (not Riccati), giving $B(\tau) = (1-e^{-\kappa\tau})/\kappa$.
    - CIR: $a = \kappa\theta$, $b = -\kappa$, $c = 0$, $d = \sigma^2$. The $B$-ODE is a genuine Riccati equation with a known closed-form solution.

---

**Exercise 5.** Consider the Crank--Nicolson finite difference scheme applied to the bond pricing PDE on a uniform grid in $(t, r)$ with spacing $\Delta t$ and $\Delta r$. Write out the scheme explicitly. Under what conditions on the ratio $\sigma^2 \Delta t / (\Delta r)^2$ does the scheme remain stable? Compare the order of accuracy with a fully implicit scheme.

??? success "Solution to Exercise 5"

    Consider the bond pricing PDE in $\tau = T - t$:

    $$
    \partial_\tau P = \mu^{\mathbb{Q}}(r)\partial_r P + \tfrac{1}{2}\sigma^2\partial_{rr}P - rP
    $$

    Let $P_j^n$ denote the numerical approximation at grid point $(n\Delta\tau, r_{\min} + j\Delta r)$.

    **Crank--Nicolson scheme:** Average of explicit and implicit:

    $$
    \frac{P_j^{n+1} - P_j^n}{\Delta t} = \frac{1}{2}\left[\mathcal{L}P_j^n + \mathcal{L}P_j^{n+1}\right]
    $$

    where $\mathcal{L}$ is the spatial operator. Explicitly:

    $$
    \frac{P_j^{n+1} - P_j^n}{\Delta t} = \frac{1}{2}\left[\mu_j\frac{P_{j+1}^n - P_{j-1}^n}{2\Delta r} + \frac{\sigma^2}{2}\frac{P_{j+1}^n - 2P_j^n + P_{j-1}^n}{(\Delta r)^2} - r_j P_j^n\right]
    $$

    $$

    + \frac{1}{2}\left[\mu_j\frac{P_{j+1}^{n+1} - P_{j-1}^{n+1}}{2\Delta r} + \frac{\sigma^2}{2}\frac{P_{j+1}^{n+1} - 2P_j^{n+1} + P_{j-1}^{n+1}}{(\Delta r)^2} - r_j P_j^{n+1}\right]
    $$

    where $\mu_j = \mu^{\mathbb{Q}}(r_j)$ and $r_j = r_{\min} + j\Delta r$.

    **Stability:** The Crank--Nicolson scheme is **unconditionally stable** for the diffusion equation (no restriction on $\sigma^2\Delta t/(\Delta r)^2$). However, for the advection-diffusion-reaction equation with the $-rP$ term, the scheme remains unconditionally stable in the von Neumann sense, but oscillations can occur if the mesh Peclet number $|\mu|\Delta r/\sigma^2$ is too large. For smooth solutions, the ratio $\sigma^2\Delta t/(\Delta r)^2$ does not need to satisfy a CFL-type restriction, though keeping it $O(1)$ is good practice for accuracy.

    **Order of accuracy:** Crank--Nicolson is second-order in both time and space: $O((\Delta t)^2 + (\Delta r)^2)$. By contrast, a fully implicit scheme is first-order in time and second-order in space: $O(\Delta t + (\Delta r)^2)$. The fully implicit scheme is also unconditionally stable but less accurate in time, requiring smaller time steps for the same level of accuracy.

---

**Exercise 6.** A zero-coupon bond in the Vasicek model has price $P(t,T,r) = e^{A(\tau) + B(\tau)\,r}$ where $\tau = T - t$,

$$
B(\tau) = \frac{1 - e^{-\kappa \tau}}{\kappa}
$$

and $A(\tau)$ is known. Verify that as $r \to \infty$, $P \to 0$ (provided $B(\tau) < 0$) and interpret this boundary condition economically.

??? success "Solution to Exercise 6"

    The Vasicek bond price is $P(t,T,r) = e^{A(\tau) + B(\tau)r}$ where $\tau = T - t$ and:

    $$
    B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    **Note on sign convention:** In the formula given, $B(\tau) > 0$ for $\tau > 0$ (since $e^{-\kappa\tau} < 1$). The exponent contains $+B(\tau)r$, but in many references the convention is $P = e^{A(\tau) - B(\tau)r}$ with $B(\tau) > 0$. The exercise states "provided $B(\tau) < 0$" which refers to the coefficient of $r$ in the exponent being negative.

    Under the convention $P = e^{A(\tau) - B(\tau)r}$ with $B(\tau) = (1 - e^{-\kappa\tau})/\kappa > 0$:

    As $r \to \infty$:

    $$
    P(t,T,r) = e^{A(\tau) - B(\tau)r} \to 0
    $$

    since $B(\tau) > 0$ means the exponent $A(\tau) - B(\tau)r \to -\infty$.

    **Economic interpretation:** When the short rate $r$ is extremely high, the cost of discounting over the interval $[t,T]$ is enormous. The expected value of $e^{-\int_t^T r_s\,ds}$ becomes vanishingly small because even though $r_s$ mean-reverts, the path integral is dominated by the very large current rate. In the limit $r \to \infty$, the bond is essentially worthless because the discounting factor kills the payoff.

    This boundary condition is economically sensible: no rational agent would pay a positive amount for a bond when the prevailing short rate is infinitely high, as the present value of any future cashflow would be zero.

---

**Exercise 7.** Suppose you need to price a 30-year zero-coupon bond under a short-rate model that does not admit a closed-form solution. Design a finite difference grid by specifying: (a) the range of $r$ values to use, (b) the grid spacing in both $r$ and $t$, and (c) the boundary conditions at the edges of the $r$-grid. Discuss how you would verify the accuracy of your numerical solution.

??? success "Solution to Exercise 7"

    **Design of the finite difference grid:**

    **(a) Range of $r$ values:**

    The grid should cover the range of plausible short rates over a 30-year horizon. A reasonable choice is:

    $$
    r \in [r_{\min}, r_{\max}] = [-0.05, 0.25]
    $$

    The lower bound allows for mildly negative rates (if the model permits), and the upper bound covers scenarios of very high rates. The range should be wide enough that boundary effects are negligible. One guideline: set $r_{\max}$ and $r_{\min}$ at approximately $\theta \pm 5\sigma/\sqrt{2\kappa}$ (i.e., several standard deviations of the stationary distribution for mean-reverting models).

    **(b) Grid spacing:**

    - **In $r$:** Use $\Delta r = 0.001$ to $0.005$ (10 to 50 bps), giving $N_r = (r_{\max} - r_{\min})/\Delta r \approx 60$ to 300 spatial grid points. For higher accuracy near the current rate, a non-uniform grid with refinement around $r_0$ can be used.
    - **In $t$ (or $\tau$):** With $T = 30$ years and $\Delta t = 0.01$ (roughly 3.6 days), we get $N_t = 3000$ time steps. For Crank--Nicolson, the time step can be larger (e.g., $\Delta t = 0.05$), but for the explicit scheme, the CFL condition $\sigma^2\Delta t/(\Delta r)^2 \leq 1$ must be satisfied.

    **(c) Boundary conditions:**

    - At $r = r_{\max}$: $P(t,T,r_{\max}) \approx 0$. For very large $r$, the bond price is negligible due to heavy discounting.
    - At $r = r_{\min}$: If negative rates are allowed, use $P(t,T,r_{\min}) \approx e^{-r_{\min}(T-t)}$ (the bond price when the rate stays constant at $r_{\min}$, which is an upper bound). Alternatively, impose a linear boundary condition: $\partial_{rr}P = 0$ at $r_{\min}$, which extrapolates linearly.

    **Verification of accuracy:**

    1. **Convergence test:** Halve $\Delta r$ and $\Delta t$ repeatedly and check that the price converges (Richardson extrapolation can accelerate convergence).
    2. **Benchmark against closed forms:** If the model has a special case with a known solution (e.g., Vasicek parameters), verify the numerical solution matches.
    3. **Check PDE residual:** Substitute the numerical solution back into the PDE and verify the residual is small.
    4. **Monte Carlo comparison:** Independently price the bond by Monte Carlo simulation of $\exp(-\int_0^T r_s\,ds)$ using a large number of paths and compare.
    5. **Conservation check:** Verify that the terminal condition is exactly satisfied and that the numerical solution remains bounded and positive throughout the grid.
