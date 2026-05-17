# Greeks and Martingale Representation


In complete diffusion models, martingale representation yields a conceptual foundation for delta hedging: delta is the integrand in the stochastic integral representation of the discounted price.

---

## Discounted asset and wealth


Recall (see [§ Black–Scholes formula](../../ch06/black_scholes_formula/bs_formula_statement.md)): under $\mathbb{Q}$, $\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t$ and $B_t = e^{rt}$. Define the discounted asset $\widetilde{S}_t := B_t^{-1}S_t$. Then

$$
\mathrm{d}\widetilde{S}_t = \sigma \widetilde{S}_t\,\mathrm{d}W_t
$$

so $\widetilde{S}$ is a $\mathbb{Q}$-martingale.

---

## Discounted option price is a martingale


Let $V(t,S_t)$ be the price process and define $\widetilde{V}_t := B_t^{-1}V(t,S_t)$. Under $\mathbb{Q}$,


$$
\widetilde{V}_t
=
\mathbb{E}^{\mathbb{Q}}[\widetilde{V}_T\mid \mathcal{F}_t]
$$



so $\widetilde{V}$ is a martingale.

---

## Martingale representation


In a Brownian filtration, any square-integrable martingale can be represented as


$$
\boxed{
\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s\,\mathrm{d}W_s
}
$$



for some predictable $Z$ with $\mathbb{E}\int_0^T Z_s^2\,\mathrm{d}s<\infty$.

---

## Identification of delta


By Itô’s formula and the PDE cancellation of drift (Recall — see [§ BS PDE structure](../../ch06/bs_pde_structure/discounting_and_killing_term.md)),

$$
\mathrm{d}\widetilde{V}_t
=
B_t^{-1}\sigma S_t V_S(t,S_t)\,\mathrm{d}W_t
$$

Thus

$$
\boxed{
Z_t = B_t^{-1}\sigma S_t\,\Delta(t,S_t),
\qquad \Delta=V_S
}
$$

Recall (see [§ Hedging applications](../../ch11/index.md)): this identifies delta as the self-financing hedge ratio.



---

## What to remember


- Discounted option prices are martingales under $\mathbb{Q}$.
- Martingale representation gives the stochastic integrand.
- Delta is the hedge ratio in complete diffusion models.

---

## Exercises

**Exercise 1.** Starting from $\mathrm{d}\widetilde{S}_t = \sigma \widetilde{S}_t \, \mathrm{d}W_t$, verify that $\widetilde{S}_t$ is a $\mathbb{Q}$-martingale by checking that $\mathbb{E}^{\mathbb{Q}}[\widetilde{S}_t \mid \mathcal{F}_s] = \widetilde{S}_s$ for $s < t$.

??? success "Solution to Exercise 1"
    We need to show $\mathbb{E}^{\mathbb{Q}}[\widetilde{S}_t \mid \mathcal{F}_s] = \widetilde{S}_s$ for $s < t$.

    Since $\mathrm{d}\widetilde{S}_u = \sigma \widetilde{S}_u \,\mathrm{d}W_u$, this SDE has the solution:

    $$
    \widetilde{S}_t = \widetilde{S}_s \exp\!\left(-\frac{1}{2}\sigma^2(t-s) + \sigma(W_t - W_s)\right)
    $$

    Taking the conditional expectation given $\mathcal{F}_s$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\widetilde{S}_t \mid \mathcal{F}_s] = \widetilde{S}_s \cdot \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\frac{1}{2}\sigma^2(t-s) + \sigma(W_t - W_s)\right) \,\Big|\, \mathcal{F}_s\right]
    $$

    Since $W_t - W_s$ is independent of $\mathcal{F}_s$ and distributed as $N(0, t-s)$:

    $$
    \mathbb{E}\!\left[\exp\!\left(-\frac{1}{2}\sigma^2(t-s) + \sigma(W_t - W_s)\right)\right] = \exp\!\left(-\frac{1}{2}\sigma^2(t-s)\right) \cdot \exp\!\left(\frac{1}{2}\sigma^2(t-s)\right) = 1
    $$

    where we used the moment generating function $\mathbb{E}[e^{aZ}] = e^{a^2/2}$ for $Z \sim N(0,1)$ with $a = \sigma\sqrt{t-s}$. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}[\widetilde{S}_t \mid \mathcal{F}_s] = \widetilde{S}_s
    $$

    confirming that $\widetilde{S}$ is a $\mathbb{Q}$-martingale.

---

**Exercise 2.** In the martingale representation $\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s \, \mathrm{d}W_s$, the integrand $Z_t$ satisfies $Z_t = B_t^{-1}\sigma S_t \Delta(t, S_t)$. For a European call in the Black--Scholes model, express $Z_t$ explicitly in terms of $S_t$, $\sigma$, $r$, $\tau$, and the normal CDF $N(\cdot)$.

??? success "Solution to Exercise 2"
    In the Black-Scholes model, the European call delta is $\Delta(t, S_t) = N(d_1)$ where:

    $$
    d_1 = \frac{\ln(S_t / K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}, \qquad \tau = T - t
    $$

    The integrand in the martingale representation is:

    $$
    Z_t = B_t^{-1}\sigma S_t \Delta(t, S_t) = e^{-rt}\sigma S_t N(d_1)
    $$

    Equivalently, using $\widetilde{S}_t = e^{-rt}S_t$:

    $$
    Z_t = \sigma \widetilde{S}_t N(d_1)
    $$

    This gives the explicit martingale representation:

    $$
    \widetilde{V}_t = \widetilde{V}_0 + \int_0^t \sigma \widetilde{S}_s N(d_1(s, S_s)) \,\mathrm{d}W_s
    $$

    where $d_1(s, S_s)$ is evaluated at time $s$ with spot $S_s$ and time-to-maturity $T - s$.

---

**Exercise 3.** Show that if $V(t,S)$ satisfies the Black--Scholes PDE, applying Ito's formula to $\widetilde{V}_t = e^{-rt}V(t,S_t)$ produces a process with zero $\mathrm{d}t$ drift, confirming that $\widetilde{V}_t$ is a martingale.

??? success "Solution to Exercise 3"
    Apply Ito's formula to $\widetilde{V}_t = e^{-rt}V(t, S_t)$:

    $$
    \mathrm{d}\widetilde{V}_t = e^{-rt}\!\left[-rV + V_t + rS_t V_S + \frac{1}{2}\sigma^2 S_t^2 V_{SS}\right]\mathrm{d}t + e^{-rt}\sigma S_t V_S \,\mathrm{d}W_t
    $$

    The $\mathrm{d}t$ coefficient can be rewritten as:

    $$
    e^{-rt}\!\left[\left(V_t + rS_t V_S + \frac{1}{2}\sigma^2 S_t^2 V_{SS}\right) - rV\right]
    $$

    The Black-Scholes PDE states that $V_t + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS} - rV = 0$. Therefore the entire $\mathrm{d}t$ drift vanishes, and we are left with:

    $$
    \mathrm{d}\widetilde{V}_t = e^{-rt}\sigma S_t V_S(t, S_t)\,\mathrm{d}W_t
    $$

    Since the drift is zero, $\widetilde{V}_t$ is a local martingale. Under standard integrability conditions (which hold for the Black-Scholes call and put), it is a true martingale.

---

**Exercise 4.** In a complete market, the martingale representation theorem guarantees uniqueness of the integrand $Z_t$. Explain why this uniqueness is essential for the claim that "delta is the hedge ratio." What happens to this argument in an incomplete market?

??? success "Solution to Exercise 4"
    **Uniqueness and hedging.** The martingale representation theorem in a Brownian filtration states that for any square-integrable $\mathcal{F}_T$-measurable random variable $\widetilde{V}_T$, there exists a **unique** predictable process $Z_t$ such that:

    $$
    \widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s \,\mathrm{d}W_s
    $$

    The uniqueness of $Z_t$ is essential because it implies there is exactly **one** hedge ratio $\Delta_t$ (determined by $Z_t = B_t^{-1}\sigma S_t \Delta_t$) that replicates the claim. If the integrand were not unique, multiple hedging strategies could replicate the same claim, and "the" delta hedge would be ambiguous.

    **Incomplete markets.** In an incomplete market (e.g., with jumps or stochastic volatility driven by an additional Brownian motion), the martingale representation theorem with respect to a single Brownian motion fails. Not every square-integrable martingale can be written as a stochastic integral against $W$ alone. Consequently:

    - Perfect replication is generally impossible.
    - There is no unique hedge ratio; instead one must choose a hedging criterion (e.g., minimum variance, superhedging, utility-based).
    - The risk-neutral measure $\mathbb{Q}$ is not unique, and different choices of $\mathbb{Q}$ lead to different prices and different "deltas."

---

**Exercise 5.** Consider a portfolio that replicates a European claim $H$ using $\Delta_t$ shares of the underlying and a position in the money market. Write the self-financing condition for the discounted portfolio and show that it is equivalent to the martingale representation of $\widetilde{V}_t$.

??? success "Solution to Exercise 5"
    Consider a self-financing portfolio consisting of $\Delta_t$ shares of $S$ and a money market position. The portfolio value is $\Pi_t = \Delta_t S_t + \psi_t B_t$. The self-financing condition is:

    $$
    \mathrm{d}\Pi_t = \Delta_t \,\mathrm{d}S_t + \psi_t \,\mathrm{d}B_t
    $$

    Define the discounted portfolio $\widetilde{\Pi}_t = B_t^{-1}\Pi_t$. Then:

    $$
    \mathrm{d}\widetilde{\Pi}_t = \Delta_t \,\mathrm{d}\widetilde{S}_t = \Delta_t \sigma \widetilde{S}_t \,\mathrm{d}W_t
    $$

    where we used the self-financing condition and the fact that $\mathrm{d}\widetilde{S}_t = \sigma\widetilde{S}_t\,\mathrm{d}W_t$. Integrating:

    $$
    \widetilde{\Pi}_t = \widetilde{\Pi}_0 + \int_0^t \Delta_s \sigma \widetilde{S}_s \,\mathrm{d}W_s
    $$

    For this portfolio to replicate the European claim $H$, we need $\widetilde{\Pi}_t = \widetilde{V}_t$ for all $t$. Comparing with the martingale representation:

    $$
    \widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s \,\mathrm{d}W_s
    $$

    we see that replication requires $\widetilde{\Pi}_0 = \widetilde{V}_0$ (correct initial investment) and:

    $$
    \Delta_t \sigma \widetilde{S}_t = Z_t = B_t^{-1}\sigma S_t \Delta(t, S_t)
    $$

    Since $\widetilde{S}_t = B_t^{-1}S_t$, this simplifies to $\Delta_t = \Delta(t, S_t) = V_S(t, S_t)$, confirming that the self-financing replicating strategy uses the PDE delta as the hedge ratio.

---

**Exercise 6.** Suppose $\sigma$ is replaced by a deterministic time-varying function $\sigma(t)$ in the Black--Scholes model. Does the martingale representation still hold? Does the identification $Z_t = B_t^{-1} \sigma(t) S_t \Delta(t, S_t)$ remain valid? Justify your answers.

??? success "Solution to Exercise 6"
    **Does the martingale representation still hold?** Yes. The martingale representation theorem applies in any filtration generated by a Brownian motion $W$. Whether $\sigma$ is constant or a deterministic function $\sigma(t)$ does not affect this: the filtration is still $\mathcal{F}_t = \sigma(W_s : s \le t)$, and any square-integrable $\mathcal{F}_T$-measurable martingale can be written as a stochastic integral against $W$.

    **Does the identification remain valid?** Yes. The dynamics become $\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma(t)S_t\,\mathrm{d}W_t$, and the discounted asset satisfies:

    $$
    \mathrm{d}\widetilde{S}_t = \sigma(t)\widetilde{S}_t\,\mathrm{d}W_t
    $$

    Applying Ito's formula to $\widetilde{V}_t = e^{-rt}V(t, S_t)$ with the time-dependent volatility PDE:

    $$
    V_t + rSV_S + \frac{1}{2}\sigma(t)^2 S^2 V_{SS} - rV = 0
    $$

    the drift cancels exactly as before, yielding:

    $$
    \mathrm{d}\widetilde{V}_t = e^{-rt}\sigma(t)S_t V_S(t, S_t)\,\mathrm{d}W_t
    $$

    Therefore:

    $$
    Z_t = B_t^{-1}\sigma(t)S_t\,\Delta(t, S_t)
    $$

    The only change is that $\sigma$ is replaced by $\sigma(t)$ everywhere. The structural relationship between the martingale integrand and delta is preserved because the model remains complete (one source of randomness, one tradable asset).
