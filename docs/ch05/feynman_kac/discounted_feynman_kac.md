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
