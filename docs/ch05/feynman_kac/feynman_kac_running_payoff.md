# Feynman–Kac with Running Payoff

This page isolates what is *specific* to the source term $+f$ in the Feynman–Kac formula: the **intuition** for what it represents and the **cancellation** that makes the martingale argument go through. The full canonical statement (with all four ingredients $\mathcal{L}u$, $-ru$, $+f$, $g$) lives in [§ The Feynman–Kac Formula](feynman_kac_formula.md#the-classical-feynmankac-formula); the general martingale derivation lives in [§ Proof Sketch](feynman_kac_proof_sketch.md).

Throughout: $X_t$ is a diffusion with generator $\mathcal{L}$, $g$ is the terminal payoff, $r$ is the discount/killing rate, and $f$ is the **running payoff** (source term).

---

## The Source-Term Specialization

Strip the discounting and the terminal payoff to isolate what the source term alone contributes:

$$
u_t + \mathcal{L}u + f = 0, \qquad u(T,x) = 0, \qquad u(t,x) = \mathbb{E}\!\left[\int_t^T f(s, X_s)\,ds \,\Big|\, X_t = x\right].
$$

Read this as "accumulated cashflow (or accumulated heat generation) along the diffusion path." The full canonical formula reinstates discounting on each contribution and adds the terminal payoff back on top.

---

## Why the Source Term Cancels

Recall (see [§ Proof Sketch — Direction 1](feynman_kac_proof_sketch.md#direction-1-pde-solution-implies-expectation-formula)): the unaugmented process $D(t,s)u(s,X_s)$ has drift $D(t,s)[\partial_s u + \mathcal{L}u - r\,u]\,ds$. With a source term in the PDE this drift equals $-D\,f\,ds$, which is **not** zero.

The fix is to enrich the candidate martingale with the discounted running payoff already collected:

$$
Y_s := D(t,s)\,u(s,X_s) + \int_t^s D(t,\tau)\,f(\tau,X_\tau)\,d\tau, \qquad D(t,s) = e^{-\int_t^s r\,d\tau}.
$$

The integral contributes $+D(t,s)\,f(s,X_s)\,ds$ to $dY_s$, exactly cancelling the $-D\,f\,ds$ from the PDE. The drift of $Y_s$ vanishes, $Y_s$ becomes a martingale, and $Y_t=\mathbb{E}[Y_T\mid\mathcal{F}_t]$ gives the stated formula. $\square$

---

## Interpretation

- $f$ acts as a **source term** (heat generation, dividends, coupons).
- $r$ acts as **discounting**, **killing**, or **absorption** — see [§ Discounted Feynman–Kac § The -ru Term: Three Equivalent Interpretations](discounted_feynman_kac.md#the--ru-term-three-equivalent-interpretations).

---

## Exercises

**Exercise 1.**
Consider the PDE $u_t + \frac{1}{2}\sigma^2 u_{xx} - ru + g(x) = 0$ with $u(T, x) = 0$ and constant $r$, $g(x) = 1$. Use the Feynman-Kac representation with running payoff to write $u(t, x)$ as an expectation. Evaluate explicitly for the process $dX_s = \sigma\,dW_s$.

??? success "Solution to Exercise 1"
    The PDE is $u_t + \frac{1}{2}\sigma^2 u_{xx} - ru + 1 = 0$ with $u(T, x) = 0$. By Feynman-Kac with running payoff $g(x) = 1$, terminal payoff $f(x) = 0$, and constant discount rate $r$:

    $$
    u(t, x) = \mathbb{E}\!\left[\int_t^T e^{-r(s-t)} \cdot 1\,ds \,\Big|\, X_t = x\right]
    $$

    Since $g = 1$ is constant and $dX_s = \sigma\,dW_s$ (the process does not appear in the integrand), the expectation simplifies to:

    $$
    u(t, x) = \int_t^T e^{-r(s-t)}\,ds = \frac{1}{r}\!\left(1 - e^{-r(T-t)}\right)
    $$

    Note that $u$ does not depend on $x$, which makes sense because neither the running payoff nor the terminal payoff depends on the spatial variable.

    **Verification**: $u_t = -e^{-r(T-t)}$. Since $u$ does not depend on $x$, $u_{xx} = 0$. Also $ru = 1 - e^{-r(T-t)}$. Then:

    $$
    u_t + \frac{1}{2}\sigma^2 u_{xx} - ru + 1 = -e^{-r(T-t)} + 0 - (1 - e^{-r(T-t)}) + 1 = 0 \;\checkmark
    $$

---

**Exercise 2.**
A bond with continuous coupon payments at rate $c$ has value $V(t, r) = \mathbb{E}[\int_t^T e^{-\int_t^s r_u\,du}\,c\,ds + e^{-\int_t^T r_u\,du} | r_t = r]$. Write the PDE that $V$ satisfies. Identify the running payoff $g = c$, the terminal payoff $f = 1$, and the discounting rate.

??? success "Solution to Exercise 2"
    The bond value includes both a running payoff (continuous coupons at rate $c$) and a terminal payoff (face value $1$ at maturity). By the Feynman-Kac formula:

    $$
    V(t, r) = \mathbb{E}\!\left[\int_t^T e^{-\int_t^s r_u\,du}\,c\,ds + e^{-\int_t^T r_u\,du} \,\Big|\, r_t = r\right]
    $$

    Identifying the components:

    - **Running payoff**: $g = c$ (the continuous coupon rate)
    - **Terminal payoff**: $f = 1$ (the face value at maturity)
    - **Discounting rate**: $r_t$ (the short rate, which is the state variable)

    The PDE that $V$ satisfies is:

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}_r V - r\,V + c = 0, \quad V(T, r) = 1
    $$

    where $\mathcal{L}_r$ is the generator of the short rate process. For example, in the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma_r\,dW_t$:

    $$
    \frac{\partial V}{\partial t} + \kappa(\theta - r)\frac{\partial V}{\partial r} + \frac{1}{2}\sigma_r^2\frac{\partial^2 V}{\partial r^2} - r\,V + c = 0
    $$

---

**Exercise 3.**
In the proof sketch, the process $Y_s = Z_s u(X_s, s) + \int_t^s Z_\tau g(X_\tau, \tau)\,d\tau$ is claimed to be a local martingale. Show that when the PDE $u_t + \mathcal{L}u - ru + g = 0$ holds, the drift of $Y_s$ vanishes. Identify where the running payoff $g$ cancels.

??? success "Solution to Exercise 3"
    We compute $dY_s$ where $Y_s = Z_s\,u(X_s, s) + \int_t^s Z_\tau\,g(X_\tau, \tau)\,d\tau$ and $Z_s = e^{-\int_t^s r(X_u, u)\,du}$.

    First, by the product rule and Ito's lemma:

    $$
    d(Z_s\,u) = Z_s\,du + u\,dZ_s = Z_s\!\left[u_t + \mathcal{L}u\right]ds + Z_s\,\sigma\,u_x\,dW_s + u\,(-r\,Z_s)\,ds
    $$

    $$
    = Z_s\!\left[u_t + \mathcal{L}u - r\,u\right]ds + Z_s\,\sigma\,u_x\,dW_s
    $$

    Second, the integral term contributes: $d\!\left(\int_t^s Z_\tau\,g\,d\tau\right) = Z_s\,g(X_s, s)\,ds$.

    Combining:

    $$
    dY_s = Z_s\!\left[u_t + \mathcal{L}u - r\,u + g\right]ds + Z_s\,\sigma\,u_x\,dW_s
    $$

    When the PDE $u_t + \mathcal{L}u - r\,u + g = 0$ holds, the drift vanishes. The cancellation occurs as follows: the PDE gives $u_t + \mathcal{L}u - r\,u = -g$, so the drift becomes $Z_s(-g + g) = 0$. The running payoff $g$ from the integral term exactly cancels the $-g$ arising from the PDE, leaving only the martingale part $Z_s\,\sigma\,u_x\,dW_s$.

---

**Exercise 4.**
A derivative pays a continuous dividend at rate $q S_t$ (proportional to the stock price) plus a terminal payoff $g(S_T)$. Write the Feynman-Kac representation with both running and terminal payoffs, and derive the corresponding PDE.

??? success "Solution to Exercise 4"
    A stock paying continuous dividends at rate $qS_t$ generates a running cash flow. Under $\mathbb{Q}$, the stock follows $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$.

    The derivative value with running dividend payments and terminal payoff is:

    $$
    V(t, S) = \mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T e^{-r(s-t)}\,qS_s\,ds + e^{-r(T-t)}\,g(S_T) \,\Big|\, S_t = S\right]
    $$

    Here the running payoff is $f(s, S_s) = qS_s$ and the terminal payoff is $g(S_T)$.

    The corresponding PDE is:

    $$
    \frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV + qS = 0
    $$

    with $V(T, S) = g(S)$. The $+qS$ term is the source from the running dividend payments.

---

**Exercise 5.**
Show that the running payoff formula reduces to the discounted Feynman-Kac formula when $g = 0$ (no running payoff). Show that it reduces to a pure annuity-like formula when $f = 0$ (no terminal payoff) and $g$ is constant.

??? success "Solution to Exercise 5"
    **Case $g = 0$ (no running payoff)**: The general formula becomes:

    $$
    u(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r(X_s, s)\,ds}\,f(X_T) \,\Big|\, X_t = x\right]
    $$

    with PDE $u_t + \mathcal{L}u - r\,u = 0$ and $u(T, x) = f(x)$. This is exactly the **discounted Feynman-Kac formula**, which applies to standard option pricing with a terminal payoff and no intermediate cash flows.

    **Case $f = 0$ (no terminal payoff) with constant $g$**: The formula becomes:

    $$
    u(t, x) = \mathbb{E}\!\left[\int_t^T e^{-\int_t^s r(X_\tau, \tau)\,d\tau}\,g\,ds \,\Big|\, X_t = x\right]
    $$

    If $r$ is also constant, then $e^{-\int_t^s r\,d\tau} = e^{-r(s-t)}$ and:

    $$
    u(t, x) = g\int_t^T e^{-r(s-t)}\,ds = \frac{g}{r}\!\left(1 - e^{-r(T-t)}\right)
    $$

    This is the present value of a **continuous annuity** paying $g$ per unit time for $(T - t)$ years at discount rate $r$. The formula recovers the standard annuity pricing formula from fixed-income mathematics.

---

**Exercise 6.**
Consider $u_t + \mu u_x + \frac{1}{2}\sigma^2 u_{xx} + g(x, t) = 0$ (no discounting, $r = 0$) with $u(T, x) = 0$. Write the Feynman-Kac representation and verify that $u(t, x) = \mathbb{E}[\int_t^T g(X_s, s)\,ds | X_t = x]$. Compute explicitly for $g(x, t) = x$ and $dX_s = \mu\,ds + \sigma\,dW_s$.

??? success "Solution to Exercise 6"
    With $r = 0$ and $u(T, x) = 0$, the Feynman-Kac representation gives:

    $$
    u(t, x) = \mathbb{E}\!\left[\int_t^T g(X_s, s)\,ds \,\Big|\, X_t = x\right]
    $$

    For $g(x, t) = x$ and $dX_s = \mu\,ds + \sigma\,dW_s$ with $X_t = x$:

    $$
    X_s = x + \mu(s - t) + \sigma(W_s - W_t)
    $$

    Therefore $\mathbb{E}[X_s \mid X_t = x] = x + \mu(s - t)$, and:

    $$
    u(t, x) = \int_t^T \!\left[x + \mu(s - t)\right]ds = x(T - t) + \mu\frac{(T - t)^2}{2}
    $$

    **Verification**: Let $\tau = T - t$. Then $u = x\tau + \frac{1}{2}\mu\tau^2$.

    $$
    u_t = -x - \mu\tau, \quad u_x = \tau, \quad u_{xx} = 0
    $$

    $$
    u_t + \mu u_x + \frac{1}{2}\sigma^2 u_{xx} + x = (-x - \mu\tau) + \mu\tau + 0 + x = 0 \;\checkmark
    $$

    Terminal condition: $u(T, x) = x \cdot 0 + 0 = 0$. $\checkmark$

---

**Exercise 7.**
In mathematical physics, the source term $g(x,t)$ represents heat generation at rate $g$ in a medium with thermal diffusivity $\sigma^2/2$. The killing term $-ru$ represents heat loss proportional to temperature. Give the financial analogues of each term and explain why the general Feynman-Kac formula with all terms ($\mathcal{L}u$, $-ru$, $f$, $g$) is needed for realistic derivative pricing.

??? success "Solution to Exercise 7"
    **Financial analogues of each physics term:**

    | Physics Term | Physics Meaning | Financial Analogue |
    |---|---|---|
    | $\mathcal{L}u$ (diffusion/advection) | Heat conduction and convection | Risk-neutral drift and volatility of the underlying asset |
    | $-r\,u$ (killing/absorption) | Heat loss proportional to temperature | Discounting at the risk-free rate (time value of money) |
    | $g(x, t)$ (source/generation) | Internal heat generation | Continuous cash flows: dividends, coupons, running costs |
    | $f(x)$ (terminal condition) | Initial/boundary temperature | Derivative payoff at maturity (e.g., $(S_T - K)^+$) |

    **Why all terms are needed**: Realistic derivatives often involve multiple cash flow components simultaneously:

    - A **convertible bond** has a terminal payoff (conversion or redemption value), continuous coupons (running payoff $g$), and discounting at the risk-free rate ($-r\,u$). The underlying stock dynamics enter through $\mathcal{L}u$.
    - A **total return swap** involves running payments based on the asset return plus a terminal settlement.
    - **Employee stock options** may include continuous vesting schedules (running payoff), a terminal exercise payoff, and discounting for the time value of money, all while the stock evolves stochastically.

    Omitting any term would restrict the framework to special cases. The full Feynman-Kac formula with $\mathcal{L}u - r\,u + g = -u_t$ is the minimal PDE structure that captures all economically relevant cash flow patterns in derivatives pricing.
