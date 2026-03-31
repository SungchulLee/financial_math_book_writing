# Discounted Feynman-Kac Formula

The **discounted Feynman-Kac formula** extends the basic Feynman-Kac result by incorporating a **killing** or **discounting** term $r(t, x)$. This extension is essential for finance, where the time value of money requires discounting future cash flows. The discounting rate may be constant (as in Black-Scholes) or state-dependent (as in stochastic interest rate models), leading to a rich interplay between the PDE and probabilistic representations.

!!! tip "Related Content"
    - [Feynman-Kac Formula](feynman_kac_formula.md) -- the general statement
    - [Proof Sketch](feynman_kac_proof_sketch.md) -- detailed derivation
    - [Applications to Option Pricing](feynman_kac_option_pricing.md) -- financial applications

---

## Motivation: Time Value of Money

In finance, a dollar received in the future is worth less than a dollar today. If the risk-free rate is $r$, then receiving $\$1$ at time $T$ is worth $e^{-r(T-t)}$ today at time $t$.

For a derivative with payoff $g(X_T)$ at maturity $T$, the **present value** at time $t$ is:

$$
V(t, x) = \mathbb{E}\!\left[e^{-r(T-t)}\,g(X_T) \,\Big|\, X_t = x\right]
$$

When $r$ depends on the state $X_t$ (e.g., stochastic interest rates), the discount factor becomes path-dependent:

$$
V(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \,\Big|\, X_t = x\right]
$$

The discounted Feynman-Kac formula tells us which PDE this expectation satisfies.

---

## The Discounted Feynman-Kac Formula

### Statement

Consider the SDE:

$$
dX_s = \mu(s, X_s)\,ds + \sigma(s, X_s)\,dW_s, \quad X_t = x
$$

Let $r(t, x) \geq 0$ be a discounting rate and $g$ a terminal payoff. Define:

$$
\boxed{
u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(s, X_s)\,ds}\,g(X_T) \,\Big|\, X_t = x\right]
}
$$

Then $u$ satisfies the PDE:

$$
\boxed{
\frac{\partial u}{\partial t} + \mu(t,x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(t,x)\frac{\partial^2 u}{\partial x^2} - r(t,x)\,u = 0
}
$$

with terminal condition $u(T, x) = g(x)$.

In compact notation:

$$
\partial_t u + \mathcal{L}u - r\,u = 0, \quad u(T, \cdot) = g
$$

### The $-r\,u$ Term

The discounting appears as the **zeroth-order term** $-r\,u$ in the PDE. This term acts as a "sink" -- it continuously removes value from the solution at rate $r$.

**Three equivalent interpretations:**

| Interpretation | Field | Description |
|---|---|---|
| **Discounting** | Finance | Future cash flows are discounted at rate $r$ |
| **Killing** | Probability | The process is "killed" at exponential rate $r$ |
| **Absorption** | Physics | Particles are absorbed at rate $r$ |

---

## Constant Discounting

When $r$ is a constant, the formula simplifies:

$$
u(t, x) = e^{-r(T-t)}\,\mathbb{E}[g(X_T) \mid X_t = x]
$$

The discount factor $e^{-r(T-t)}$ factors out of the expectation because it does not depend on the path.

**PDE:**

$$
\partial_t u + \mathcal{L}u - r\,u = 0
$$

### Relationship to the Undiscounted Case

Let $v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$ solve the backward equation $\partial_t v + \mathcal{L}v = 0$. Then $u = e^{-r(T-t)}v$ satisfies:

$$
\partial_t u = -r\,e^{-r(T-t)}v + e^{-r(T-t)}\partial_t v = -ru + e^{-r(T-t)}\partial_t v
$$

So $\partial_t u + \mathcal{L}u - ru = e^{-r(T-t)}(\partial_t v + \mathcal{L}v) = 0$. $\checkmark$

---

## State-Dependent Discounting

When $r = r(t, X_t)$ depends on the stochastic process, the discount factor $e^{-\int_t^T r(s, X_s)\,ds}$ is **path-dependent** and cannot be factored out of the expectation.

### Example: Stochastic Interest Rates

If $X_t = r_t$ is the short rate itself (e.g., Vasicek or CIR model), then:

$$
u(t, r) = \mathbb{E}\!\left[e^{-\int_t^T r_s\,ds} \,\Big|\, r_t = r\right]
$$

is the **zero-coupon bond price**, and it satisfies:

$$
\partial_t u + \mathcal{L}_r u - r\,u = 0, \quad u(T, r) = 1
$$

The terminal condition $g = 1$ reflects that the bond pays $\$1$ at maturity.

### Example: State-Dependent Killing

In credit risk, the default intensity $\lambda(X_t)$ depends on a credit quality process $X_t$. The survival probability is:

$$
Q(t, x) = \mathbb{E}\!\left[e^{-\int_t^T \lambda(X_s)\,ds} \,\Big|\, X_t = x\right]
$$

This satisfies $\partial_t Q + \mathcal{L}Q - \lambda\,Q = 0$ with $Q(T, x) = 1$.

---

## The Killing Interpretation

The discounting term has a clean **probabilistic interpretation via killing**.

### Killed Diffusion

Define a **killed process** $(X_t, \zeta)$ where $\zeta$ is an independent exponential killing time with rate $r(t, X_t)$. Formally:

$$
\mathbb{P}(\zeta > T \mid \text{path of } X) = e^{-\int_t^T r(s, X_s)\,ds}
$$

Then:

$$
u(t, x) = \mathbb{E}[g(X_T)\,\mathbf{1}_{\{\zeta > T\}} \mid X_t = x]
$$

**Interpretation**: The process lives until a random killing time $\zeta$. We only collect the payoff $g(X_T)$ if the process survives to maturity.

### Why $-r\,u$ in the PDE?

The $-ru$ term represents the rate of "leakage" from the system. At each instant $ds$, a fraction $r\,ds$ of the remaining probability mass is killed. The PDE tracks the expected value conditional on survival, and the $-ru$ term accounts for the continual erosion of this value.

$$
\frac{\partial u}{\partial t} = \underbrace{\mathcal{L}u}_{\text{diffusion}} - \underbrace{r\,u}_{\text{killing}}
$$

---

## Derivation of the $-r\,u$ Term

### From the Undiscounted Backward Equation

Start with the process $Y_s = (X_s, R_s)$ where $R_s = \int_t^s r(\tau, X_\tau)\,d\tau$ is the accumulated discount. Define:

$$
v(t, x, 0) = \mathbb{E}[e^{-R_T}\,g(X_T) \mid X_t = x, R_t = 0]
$$

The function $v(t, x, \rho)$ satisfies the backward equation for the extended process:

$$
\partial_t v + \mu\,\partial_x v + \frac{1}{2}\sigma^2\,\partial_{xx}v + r\,\partial_\rho v = 0
$$

Since $v$ depends on $\rho$ only through $e^{-\rho}\,w(t, x)$ (by the multiplicative structure of the discount factor):

$$
v(t, x, \rho) = e^{-\rho}\,u(t, x)
$$

Substituting: $\partial_\rho v = -e^{-\rho}\,u$, so:

$$
e^{-\rho}\!\left[\partial_t u + \mathcal{L}u - r\,u\right] = 0
$$

This gives $\partial_t u + \mathcal{L}u - r\,u = 0$. $\square$

---

## The Discounted Feynman-Kac with Running Payoff

The most general form includes both a terminal payoff $g$ and a running payoff $f$:

$$
u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r\,ds}\,g(X_T) + \int_t^T e^{-\int_t^s r\,d\tau}\,f(s, X_s)\,ds \,\Big|\, X_t = x\right]
$$

This satisfies:

$$
\partial_t u + \mathcal{L}u - r\,u + f = 0, \quad u(T, x) = g(x)
$$

The running payoff $f$ appears as a source term in the PDE. Financially, it represents **continuous cash flows** (dividends, coupon payments, or running costs).

---

## Applications in Finance

### 1. Black-Scholes Option Pricing

Under $\mathbb{Q}$: $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$

The option price satisfies the **Black-Scholes PDE**:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

Here $\mu = rS$, $\sigma_{\text{diff}} = \sigma S$, and the discount rate is the constant $r$. The $-rV$ term is the Feynman-Kac discounting.

### 2. Vasicek Bond Pricing

Short rate: $dr_t = \kappa(\theta - r_t)\,dt + \sigma_r\,dW_t$

Bond price PDE:

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma_r^2\frac{\partial^2 P}{\partial r^2} - rP = 0
$$

The discounting rate $r$ is the state variable itself. The explicit solution is:

$$
P(t, r; T) = \exp\!\left(A(\tau) - B(\tau)\,r\right)
$$

where $\tau = T - t$ and:

$$
B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}, \quad A(\tau) = \left(\theta - \frac{\sigma_r^2}{2\kappa^2}\right)(B(\tau) - \tau) - \frac{\sigma_r^2}{4\kappa}B(\tau)^2
$$

### 3. CIR Bond Pricing

Short rate: $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$

The bond price again satisfies the discounted Feynman-Kac PDE, and the affine structure yields:

$$
P(t, r; T) = A(\tau)\,e^{-B(\tau)\,r}
$$

with more complex but still explicit functions $A(\tau)$ and $B(\tau)$.

### 4. Dividend-Paying Stock

For a stock paying continuous dividends at rate $q$:

$$
dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The option price satisfies:

$$
\partial_t V + (r-q)S\,\partial_S V + \frac{1}{2}\sigma^2 S^2\,\partial_{SS}V - rV = 0
$$

The dividend yield $q$ modifies the drift (reducing the risk-neutral growth rate) but the discounting is still at rate $r$.

---

## Comparison: With and Without Discounting

| Aspect | Undiscounted ($r = 0$) | Discounted ($r > 0$) |
|---|---|---|
| **PDE** | $\partial_t u + \mathcal{L}u = 0$ | $\partial_t u + \mathcal{L}u - ru = 0$ |
| **Solution** | $\mathbb{E}[g(X_T)]$ | $\mathbb{E}[e^{-\int r\,ds}\,g(X_T)]$ |
| **Process** | $u(s, X_s)$ is a martingale | $e^{-\int_t^s r\,d\tau}\,u(s, X_s)$ is a martingale |
| **Max principle** | $\max u$ on parabolic boundary | Still holds (with $r \geq 0$) |
| **Steady state** | $\mathcal{L}u = 0$ | $\mathcal{L}u - ru = 0$ |
| **Financial name** | Undiscounted expectation | Risk-neutral pricing |

---

## Summary

$$
\boxed{
\partial_t u + \mathcal{L}u - r\,u = 0 \quad \Longleftrightarrow \quad u(t,x) = \mathbb{E}\!\left[e^{-\int_t^T r(s,X_s)\,ds}\,g(X_T) \,\Big|\, X_t = x\right]
}
$$

| Component | PDE Role | Probabilistic Role | Financial Role |
|---|---|---|---|
| $\mathcal{L}u$ | Diffusion operator | Generator of $X_t$ | Drift + volatility of underlying |
| $-r\,u$ | Zeroth-order sink | Killing rate | Time value of money |
| $g(x)$ | Terminal condition | Terminal payoff | Derivative payoff at maturity |
| $r(t,x)$ | PDE coefficient | Killing intensity | Short rate / discount rate |

**The discounted Feynman-Kac formula is the mathematical foundation of risk-neutral pricing. The $-r\,u$ term in the PDE encodes the time value of money, transforming expected future payoffs into present values. This single extension of the Kolmogorov backward equation underlies virtually all of derivatives pricing theory.**

---

## See Also

- [Feynman-Kac Formula](feynman_kac_formula.md) -- the general statement with running payoff
- [Proof Sketch](feynman_kac_proof_sketch.md) -- detailed derivation via martingale methods
- [Applications to Option Pricing](feynman_kac_option_pricing.md) -- Black-Scholes, barriers, and more
- [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md) -- the $r = 0$ case

---

## Exercises

**Exercise 1.**
For a European call option under $\mathbb{Q}$ with constant $r = 0.05$, $\sigma = 0.30$, and $S_0 = 100$, write the Black-Scholes PDE with the $-rV$ discounting term and identify each component: generator $\mathcal{L}$, discount rate, and terminal condition for strike $K = 100$.

---

**Exercise 2.**
Show that if $r$ is constant, the discounted Feynman-Kac expectation $u(t,x) = \mathbb{E}[e^{-r(T-t)}g(X_T) | X_t = x]$ can be written as $e^{-r(T-t)}v(t,x)$ where $v$ solves the undiscounted backward equation $\partial_t v + \mathcal{L}v = 0$. Verify by substitution that $u$ then satisfies $\partial_t u + \mathcal{L}u - ru = 0$.

---

**Exercise 3.**
In the Vasicek model with $\kappa = 0.5$, $\theta = 0.04$, $\sigma_r = 0.01$, and $r_0 = 0.03$, the zero-coupon bond price satisfies $\partial_t P + \kappa(\theta - r)\partial_r P + \frac{1}{2}\sigma_r^2 \partial_{rr}P - rP = 0$ with $P(T,r) = 1$. Explain why $r$ appears both in the drift coefficient $\kappa(\theta - r)$ and as the discount rate $-rP$. What makes this PDE different from the standard Black-Scholes PDE?

---

**Exercise 4.**
Consider the discounted Feynman-Kac formula with running payoff: $u(t,x) = \mathbb{E}[\int_t^T e^{-\int_t^s r\,d\tau}f(s, X_s)\,ds | X_t = x]$. This satisfies $\partial_t u + \mathcal{L}u - ru + f = 0$ with $u(T,x) = 0$. Give a financial example where a running payoff arises, and explain why the terminal condition is zero.

---

**Exercise 5.**
In the killing interpretation, a process $X_t$ is killed at an exponential rate $r(t,X_t)$. Write the survival probability $\mathbb{P}(\zeta > T | \text{path of } X) = e^{-\int_t^T r(s,X_s)\,ds}$. If $r$ is constant at $r = 0.05$ and $T - t = 10$, compute the survival probability. Explain the financial interpretation in terms of discounting.

---

**Exercise 6.**
For a dividend-paying stock with continuous yield $q$ under $\mathbb{Q}$: $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$. Write the PDE for an option price $V(t,S)$ including the $-rV$ discounting term. Identify how $q$ affects the drift but not the discount rate.

---

**Exercise 7.**
Derive the $-ru$ term in the discounted Feynman-Kac PDE by considering the extended process $Y_s = (X_s, R_s)$ where $R_s = \int_t^s r(\tau, X_\tau)\,d\tau$. Show that $v(t, x, \rho) = e^{-\rho}u(t,x)$ satisfies $\partial_\rho v = -e^{-\rho}u$, and use this to derive $\partial_t u + \mathcal{L}u - ru = 0$ from the backward equation for the extended process.

---

## Solutions

??? success "Solution to Exercise 1"
    The Black-Scholes PDE with the given parameters is:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    Substituting $r = 0.05$ and $\sigma = 0.30$:

    $$
    \frac{\partial V}{\partial t} + 0.05\,S\frac{\partial V}{\partial S} + \frac{1}{2}(0.09)\,S^2\frac{\partial^2 V}{\partial S^2} - 0.05\,V = 0
    $$

    **Components:**

    - **Generator** $\mathcal{L}$: Under $\mathbb{Q}$, the stock follows $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, so $\mu(S) = rS = 0.05S$ and $\sigma_{\text{diff}}(S) = \sigma S = 0.30S$. The generator is $\mathcal{L}V = 0.05S\,\partial_S V + \frac{1}{2}(0.09)S^2\,\partial_{SS}V$.
    - **Discount rate**: The constant risk-free rate $r = 0.05$, appearing in the $-rV = -0.05V$ term.
    - **Terminal condition**: For a call with strike $K = 100$, we have $V(T, S) = (S - 100)^+$.

??? success "Solution to Exercise 2"
    Let $v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$, which solves the undiscounted backward equation $\partial_t v + \mathcal{L}v = 0$ with $v(T, x) = g(x)$.

    Define $u(t, x) = e^{-r(T-t)}v(t, x)$. Since $r$ is constant, the discount factor $e^{-r(T-t)}$ does not depend on the path of $X$, so:

    $$
    u(t, x) = e^{-r(T-t)}\mathbb{E}[g(X_T) \mid X_t = x] = \mathbb{E}[e^{-r(T-t)}g(X_T) \mid X_t = x]
    $$

    which is the discounted Feynman-Kac expectation.

    **Verification by substitution.** Compute each derivative of $u = e^{-r(T-t)}v$:

    $$
    \partial_t u = re^{-r(T-t)}v + e^{-r(T-t)}\partial_t v = ru + e^{-r(T-t)}\partial_t v
    $$

    $$
    \partial_x u = e^{-r(T-t)}\partial_x v, \quad \partial_{xx}u = e^{-r(T-t)}\partial_{xx}v
    $$

    Therefore:

    $$
    \mathcal{L}u = e^{-r(T-t)}\mathcal{L}v
    $$

    Substituting into $\partial_t u + \mathcal{L}u - ru$:

    $$
    \partial_t u + \mathcal{L}u - ru = ru + e^{-r(T-t)}\partial_t v + e^{-r(T-t)}\mathcal{L}v - ru = e^{-r(T-t)}(\partial_t v + \mathcal{L}v) = 0
    $$

    since $v$ solves $\partial_t v + \mathcal{L}v = 0$. $\checkmark$

??? success "Solution to Exercise 3"
    In the Vasicek model, the short rate $r_t$ is the **state variable** itself. This creates a dual role for $r$:

    1. **In the drift $\kappa(\theta - r)$**: The short rate is mean-reverting toward $\theta$, and the current value $r$ determines the drift of the process. This is the standard role of the state variable in the generator $\mathcal{L}$.

    2. **In the discount term $-rP$**: The same variable $r$ serves as the instantaneous discounting rate. This arises because the bond price is $P(t, r) = \mathbb{E}[e^{-\int_t^T r_s\,ds} \mid r_t = r]$, and the Feynman-Kac formula produces the $-r\,P$ term.

    **Difference from Black-Scholes**: In the Black-Scholes PDE, the discount rate $r$ is a fixed constant, independent of the state variable $S$. The state variable $S$ appears in the drift ($rS$) and the diffusion ($\sigma S$), but $r$ in the $-rV$ term is simply a parameter. In the Vasicek PDE, the discount rate is the state variable: the coefficient of $-P$ is $r$ itself, which varies stochastically. This makes the problem inherently different because the discounting is path-dependent, and the discount factor $e^{-\int_t^T r_s\,ds}$ cannot be factored out of the expectation.

??? success "Solution to Exercise 4"
    **Financial example**: A coupon bond that pays continuous coupons at rate $c$ per unit time. The holder receives a stream of payments $f(s, X_s) = c$ over $[t, T]$, each discounted to present value. With no terminal payoff ($g = 0$, or equivalently with a face value $g = 1$ at maturity for a standard bond), the value is:

    $$
    u(t, x) = \mathbb{E}\!\left[\int_t^T e^{-\int_t^s r(\tau, X_\tau)\,d\tau}\,c\,ds \,\Big|\, X_t = x\right]
    $$

    Other examples include: a stock paying continuous dividends at rate $qS$, where $f(s, S_s) = qS_s$; or a floating-rate note with running interest payments.

    **Why the terminal condition is zero**: The formula $u(t,x) = \mathbb{E}[\int_t^T e^{-\int_t^s r\,d\tau}f(s, X_s)\,ds \mid X_t = x]$ represents only the running payoff component. At maturity $T$, there are no remaining future running payments to collect (the integral $\int_T^T \cdots\,ds = 0$), so $u(T, x) = 0$. If there were also a terminal payoff $g(X_T)$, it would be added separately, and the terminal condition would be $u(T, x) = g(x)$.

??? success "Solution to Exercise 5"
    With constant killing rate $r = 0.05$ and time horizon $T - t = 10$:

    $$
    \mathbb{P}(\zeta > T \mid \text{path of } X) = e^{-\int_t^T r\,ds} = e^{-0.05 \times 10} = e^{-0.5} \approx 0.6065
    $$

    So approximately $60.65\%$ of the probability mass survives to time $T$.

    **Financial interpretation**: The survival probability $e^{-r(T-t)}$ is exactly the **discount factor** used to compute present values. A payoff of $\$1$ received at time $T$ is worth $e^{-0.5} \approx \$0.6065$ today. In the killing interpretation, we imagine the process being "killed" at random with intensity $r = 0.05$ per year. After 10 years, the probability that the process has not been killed is $e^{-0.5}$. The expected payoff, conditional on survival, times the survival probability gives the discounted expected value -- this is exactly how risk-neutral pricing works.

??? success "Solution to Exercise 6"
    Under $\mathbb{Q}$, the dividend-paying stock follows $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, so the drift is $\mu(S) = (r - q)S$ and the diffusion coefficient is $\sigma_{\text{diff}}(S) = \sigma S$.

    Applying the discounted Feynman-Kac formula with discount rate $r$, the PDE for $V(t, S)$ is:

    $$
    \frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    **How $q$ affects the PDE**: The dividend yield $q$ enters only through the drift term $(r - q)S\,\partial_S V$. Compared to the non-dividend case (where the drift coefficient is $rS$), the effective risk-neutral growth rate is reduced from $r$ to $r - q$. Intuitively, dividends "leak" value from the stock at rate $q$, so the capital appreciation under $\mathbb{Q}$ is slower.

    **The discount rate is unchanged**: The $-rV$ term remains at rate $r$, not $r - q$. This is because discounting reflects the time value of money (the risk-free rate), which is independent of whether the stock pays dividends. The dividend yield affects the dynamics of the underlying but not the rate at which future payoffs are discounted.

??? success "Solution to Exercise 7"
    Consider the extended process $Y_s = (X_s, R_s)$ where $dX_s = \mu(s, X_s)\,ds + \sigma(s, X_s)\,dW_s$ and $dR_s = r(s, X_s)\,ds$ with $R_t = 0$. The function:

    $$
    v(t, x, \rho) = \mathbb{E}\!\left[e^{-R_T}\,g(X_T) \mid X_t = x, R_t = \rho\right]
    $$

    satisfies the backward equation for the joint process $(X_s, R_s)$:

    $$
    \partial_t v + \mu\,\partial_x v + \frac{1}{2}\sigma^2\,\partial_{xx}v + r\,\partial_\rho v = 0
    $$

    The term $r\,\partial_\rho v$ arises because $R_s$ has drift $r(s, X_s)$ and zero diffusion.

    Now, by the multiplicative structure of $e^{-R_T} = e^{-\rho}\,e^{-\int_t^T r\,ds}$ (since $R_T = \rho + \int_t^T r(s, X_s)\,ds$), we can write:

    $$
    v(t, x, \rho) = e^{-\rho}\,u(t, x)
    $$

    where $u(t, x) = \mathbb{E}[e^{-\int_t^T r\,ds}\,g(X_T) \mid X_t = x]$.

    Computing the partial derivative: $\partial_\rho v = -e^{-\rho}\,u$.

    Substituting into the backward equation:

    $$
    e^{-\rho}\,\partial_t u + e^{-\rho}\,\mu\,\partial_x u + \frac{1}{2}e^{-\rho}\,\sigma^2\,\partial_{xx}u + r\,(-e^{-\rho}\,u) = 0
    $$

    Dividing through by $e^{-\rho} > 0$:

    $$
    \partial_t u + \mu\,\partial_x u + \frac{1}{2}\sigma^2\,\partial_{xx}u - r\,u = 0
    $$

    which is $\partial_t u + \mathcal{L}u - r\,u = 0$. $\square$
