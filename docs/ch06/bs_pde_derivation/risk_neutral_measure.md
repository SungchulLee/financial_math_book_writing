# Black–Scholes PDE via Risk-Neutral Pricing

This derivation removes the physical drift $\mu$ by **measure change**: instead of eliminating risk by trading, we eliminate the risk premium by changing the probability measure. Under the new measure $\mathbb{Q}$, every asset earns the risk-free rate on average, and the PDE emerges as the condition that discounted prices have zero drift.

By the end of this page you should understand: (1) how $\mathbb{Q}$ is constructed and why it is unique, (2) why the pricing formula **(P)** and the PDE **(A)** are equivalent, and (3) how Itô's formula and Feynman–Kac serve as bridges between the two.


## The Big Picture


The central result of this page is the following equivalence.

!!! tip "Main Theorem (Probabilistic–Analytic Equivalence)"
    Under the Black–Scholes model, suppose $\Phi$ has at most polynomial growth. The following two statements are equivalent.

    **(P) Probabilistic representation.**

    $$
    V(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T) \mid S_t = S\right]
    $$

    **(A) Analytic representation.** $V$ is a $C^{1,2}$ solution on $[0,T) \times (0,\infty)$ with polynomial growth of the Black–Scholes PDE:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0, \qquad V(t,S) \to \Phi(S) \text{ as } t \uparrow T
    $$

    The terminal convergence $V(t,S) \to \Phi(S)$ holds in the appropriate sense; $V$ is classical on $[0,T) \times (0,\infty)$ but need not be smooth at $t = T$ when $\Phi$ is not smooth.

    The two directions are proved by different tools:

    $$\textbf{(P)} \xrightarrow{\quad\text{Itô's formula}\quad} \textbf{(A)} \qquad\qquad \textbf{(A)} \xrightarrow{\quad\text{Feynman–Kac}\quad} \textbf{(P)}$$

The measure $\mathbb{Q}$ in **(P)** is the **risk-neutral measure**: the unique probability measure equivalent to the physical measure $\mathbb{P}$ under which all discounted asset prices are martingales. Its existence and uniqueness are guaranteed by the fundamental theorem of asset pricing, and its construction is the content of the Setup section below.

The rest of this page proves the equivalence in both directions. The forward direction **(P) $\Rightarrow$ (A)** occupies the Derivation section. The converse **(A) $\Rightarrow$ (P)** is the Feynman–Kac theorem. The two representations are not merely numerically equal — they are conceptually complementary: **(P)** is the basis for Monte Carlo simulation and probabilistic intuition, while **(A)** is the basis for finite-difference methods and analytic closed forms.

This route derives the pricing equation from the risk-neutral pricing principle rather than from a local delta-hedging argument (as in [delta hedging](delta_hedging.md)), a change of numéraire (as in the [stock-measure approach](change_of_numeraire.md)), or a preference specification (as in the [equilibrium approach](equilibrium.md)). The economic content lies in the existence and uniqueness of $\mathbb{Q}$; the analytic content lies in Itô's formula and Feynman–Kac.


## Setup


**Model.** The stock price follows geometric Brownian motion under the physical measure $\mathbb{P}$:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constants $\mu$, $\sigma > 0$, and a money market account $B_t = e^{rt}$.

**Construction of $\mathbb{Q}$.** In the Black–Scholes model, the risk-neutral measure $\mathbb{Q}$ is constructed directly by Girsanov's theorem. The process

$$W^{\mathbb{Q}}_t = W_t + \frac{\mu - r}{\sigma}\, t$$

is a $\mathbb{Q}$-Brownian motion, and the stock dynamics under $\mathbb{Q}$ are

$$
dS_t
= rS_t\, dt + \sigma S_t\, \left(dW_t + \frac{\mu - r}{\sigma}\, dt\right)
= rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t
$$

The ratio $\theta = (\mu - r)/\sigma$ is the **market price of risk**: it is the Girsanov drift removal that converts the physical drift $\mu$ to the risk-neutral drift $r$. Since the single risky asset spans the single Brownian source of risk, the market is complete, and the equivalent martingale measure is unique. (This also follows from the [fundamental theorem of asset pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md): no-arbitrage guarantees existence, and completeness guarantees uniqueness.)

**Verification that $\mathbb{Q}$ is an equivalent martingale measure.** The discounted bank account $e^{-rt}B_t = 1$ is constant, hence trivially a martingale. For the discounted stock $\widetilde{S}_t = e^{-rt}S_t$, the product rule and the $\mathbb{Q}$-dynamics give:

$$
d\widetilde{S}_t
= -re^{-rt}S_t\,dt + e^{-rt}\,dS_t
= -re^{-rt}S_t\,dt + e^{-rt}\!\left(rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}\right)
= \sigma\widetilde{S}_t\,dW_t^{\mathbb{Q}}
$$

The $dt$ terms cancel exactly, leaving a driftless SDE. The solution is $\widetilde{S}_t = \widetilde{S}_0\exp\!\left(\sigma W_t^{\mathbb{Q}} - \frac{1}{2}\sigma^2 t\right)$, the exponential martingale associated with a constant integrand. Since $\sigma$ is constant, the Novikov condition is trivially satisfied, and this is a true $\mathbb{Q}$-martingale (not merely a local martingale).

**Derivation of the pricing formula (P).** With $\mathbb{Q}$ constructed, the no-arbitrage price follows. Since the Black–Scholes market is complete, any payoff $\Phi(S_T)$ is replicated by a self-financing portfolio $(\varphi_t, \psi_t)$ in $(S_t, B_t)$, with value $V_t$ satisfying $dV_t = \varphi_t\,dS_t + \psi_t\,dB_t$. Applying the product rule to $\widetilde{V}_t = e^{-rt}V_t$:

$$d\widetilde{V}_t = \varphi_t\,d\widetilde{S}_t$$

This is a stochastic integral against the $\mathbb{Q}$-martingale $\widetilde{S}_t$, so $\widetilde{V}_t$ is a local $\mathbb{Q}$-martingale. Under the square-integrability condition $\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T \varphi_t^2 \widetilde{S}_t^2\,dt\right] < \infty$, it is a true $\mathbb{Q}$-martingale. The martingale property then gives:

$$e^{-rt}V_t = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\Phi(S_T) \mid \mathcal{F}_t\right]$$

Multiplying by $e^{rt}$ yields **(P)**. Equivalently, this pricing formula follows directly from the fundamental theorem of asset pricing without explicit reference to replication: no-arbitrage and the uniqueness of $\mathbb{Q}$ pin the price as the unique no-arbitrage value.

We write $V_t = V(t, S_t)$ for the option price process evaluated along the stock path; in what follows, $V(t,S)$ denotes the deterministic pricing function and $V_t$ the corresponding stochastic process. We assume $V \in C^{1,2}([0,T) \times (0,\infty))$ with polynomial growth. Polynomial growth is imposed to guarantee the relevant expectations are finite and to support uniqueness in the classical solution class. Since geometric Brownian motion has finite moments of all orders, this growth bound suffices.

Note also that conditioning on $S_t = S$ and conditioning on $\mathcal{F}_t$ are interchangeable here because the $\mathbb{Q}$-dynamics of $S_t$ are Markov. Under $\mathbb{Q}$, the stock follows the diffusion

$$
dS_t = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}
$$

which is a time-homogeneous Markov process. Therefore, for any measurable payoff $\Phi$,

$$
\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)\mid \mathcal{F}_t]
=
\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)\mid S_t]
\quad \text{a.s.}
$$

The intuition is that, for a Markov process, the future evolution depends only on the current state and not on the past history. Although $\mathcal{F}_t$ contains the entire path information up to time $t$, this additional information is redundant once $S_t$ is known. Hence the conditional expectation reduces to a function of $(t, S_t)$ alone.

The two sections that follow prove the equivalence **(P) $\Leftrightarrow$ (A)**.

!!! abstract "Proposition (Martingale–PDE equivalence)"
    The discounted price process $e^{-rt}V(t,S_t)$ is a $\mathbb{Q}$-martingale if and only if $V$ solves the Black–Scholes PDE.


## Forward Direction: (P) $\Rightarrow$ (A) via Itô's Formula


Starting from the pricing formula **(P)**, we derive the Black–Scholes PDE **(A)**.

Define the discounted option price:

$$M_t = e^{-rt}\, V(t, S_t)$$

Since $V(t, S_t) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$, we have $M_t = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$, which is a $\mathbb{Q}$-martingale by the tower property.

Apply Itô's formula to $M_t = e^{-rt}\, V(t, S_t)$. By the product rule:

$$dM_t = -r e^{-rt} V\, dt + e^{-rt}\, dV$$

where Itô's formula under $\mathbb{Q}$ gives:

$$dV = \left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW^{\mathbb{Q}}$$

using $dS = rS\, dt + \sigma S\, dW^{\mathbb{Q}}$ and $(dS)^2 = \sigma^2 S^2\, dt$. Therefore:

$$dM_t = e^{-rt}\!\left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV\right) dt + e^{-rt}\, \sigma S \frac{\partial V}{\partial S}\, dW^{\mathbb{Q}}$$

Since $M_t$ is a $\mathbb{Q}$-martingale, the $dt$ coefficient must vanish identically, giving the Black–Scholes PDE **(A)**:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

with terminal condition $V(T, S) = \Phi(S)$. $\square$

!!! note "What this direction says"
    The pricing formula **(P)** forces $e^{-rt}V$ to be a $\mathbb{Q}$-martingale. Itô's formula then computes the drift of $e^{-rt}V$ explicitly. Setting that drift to zero is not a choice — it is a necessity. The PDE **(A)** is a **consequence** of the martingale property, not a condition imposed from outside.


## Converse Direction: (A) $\Rightarrow$ (P) via Feynman–Kac


Starting from the PDE **(A)**, we recover the pricing formula **(P)**. This is the content of the Feynman–Kac theorem.

**Theorem (Feynman–Kac).** *Let $S_t$ solve $dS_t = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$ under $\mathbb{Q}$. Suppose $u \in C^{1,2}([0,T) \times (0,\infty))$ satisfies the polynomial growth condition $|u(t,S)| \leq C(1 + S^p)$ and solves:*

$$\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} - ru = 0, \qquad u(T, S) = \Phi(S)$$

*Then:*

$$u(t, S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T) \mid S_t = S\right]$$

*Proof sketch.* Define $N_t = e^{-rt}\,u(t, S_t)$. Apply Itô's formula exactly as in the forward direction. The PDE **(A)** says precisely that the $dt$ coefficient of $dN_t$ vanishes, so $N_t$ is a local $\mathbb{Q}$-martingale. Because geometric Brownian motion has finite moments of all orders, the polynomial growth bound on $u$ implies sufficient integrability for $N_t$ to be a true $\mathbb{Q}$-martingale. The martingale property at times $t$ and $T$ then gives:

$$e^{-rt}\,u(t,S_t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\,u(T,S_T) \mid \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-rT}\,\Phi(S_T) \mid \mathcal{F}_t\right]$$

Multiplying by $e^{rt}$ gives **(P)**. $\square$

!!! note "What this direction says"
    The PDE **(A)** zeroes the drift of $e^{-rt}u(t,S_t)$ — the same Itô calculation as in the forward direction, read in reverse. This makes $e^{-rt}u$ a martingale, which directly produces the conditional expectation **(P)**. Itô's formula is the bridge in both directions: the PDE and the martingale condition are two expressions of the same zero-drift requirement.

The equivalence also has practical significance. The two representations suggest different computational strategies:

- **(P)** $\to$ evaluate $\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$ by Monte Carlo simulation, or in closed form for GBM.
- **(A)** $\to$ solve the PDE backward from terminal data by finite differences, or by transformation to the heat equation.


## Generator Formulation


The same derivation can be expressed more compactly using the **infinitesimal generator** of the risk-neutral diffusion process.

**Generator of GBM under $\mathbb{Q}$.** For the diffusion $dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$, the infinitesimal generator acting on $f \in C^2(0,\infty)$ is

$$\mathcal{L}^{\mathbb{Q}} f(S) = rS\, f'(S) + \frac{1}{2}\sigma^2 S^2\, f''(S)$$

**Extended generator.** For a time-dependent function $g(t, S)$, the extended generator of the space-time process $(t, S_t)$ is

$$\mathcal{A}\, g(t, S) = \frac{\partial g}{\partial t} + \mathcal{L}^{\mathbb{Q}} g(t, S)$$

For $g \in C^{1,2}$, Itô's formula shows that $g(t, S_t)$ is a local martingale under $\mathbb{Q}$ if and only if the drift term vanishes, i.e., $\mathcal{A}\, g = 0$.

**Application.** Applying the extended generator to $M(t, S) = e^{-rt}\, V(t, S)$:

$$\mathcal{A}\!\left[e^{-rt} V\right] = e^{-rt}\!\left(\frac{\partial V}{\partial t} - rV + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)$$

Setting $\mathcal{A}[e^{-rt}V] = 0$ recovers the Black–Scholes PDE. The generator formulation makes the structure transparent: the PDE is the statement that the discounted price lies in the **null space of the extended generator**, which is equivalent to the martingale property.

!!! note "Backward Kolmogorov equation"
    The Black–Scholes PDE is a special case of the **backward Kolmogorov equation** associated with the $\mathbb{Q}$-diffusion. If $p^{\mathbb{Q}}(t, S; T, S')$ is the transition density of $S_t$ under $\mathbb{Q}$, it satisfies $\partial_t p + \mathcal{L}^{\mathbb{Q}}_S p = 0$ in the backward variables $(t, S)$. Integrating against the discounted payoff $e^{-r(T-t)} \Phi(S')$ recovers the Black–Scholes PDE for $V$.


## Summary


The full logical structure of the page is as follows.

**Step 1. FTAP + Girsanov** (Setup). No-arbitrage and completeness guarantee a unique $\mathbb{Q} \sim \mathbb{P}$. Girsanov's theorem constructs it explicitly via $\theta = (\mu-r)/\sigma$, giving $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ under $\mathbb{Q}$.

**Step 2. Verification** (Setup). The discounted bank account $e^{-rt}B_t = 1$ and discounted stock $\widetilde{S}_t = e^{-rt}S_t$ are both confirmed to be true $\mathbb{Q}$-martingales.

**Step 3. Pricing formula (P)** (Setup). Replication and self-financing force $e^{-rt}V_t$ to be a $\mathbb{Q}$-martingale, giving the unique no-arbitrage price **(P)**.

**Step 4. (P) $\Rightarrow$ (A)**: Itô's formula computes the drift of $e^{-rt}V(t,S_t)$; the martingale condition forces it to zero, yielding the PDE **(A)**.

**Step 5. (A) $\Rightarrow$ (P)**: Feynman–Kac reads the same Itô calculation in reverse — the PDE makes $e^{-rt}u$ a martingale, recovering **(P)**.

Steps 4 and 5 together establish **(P) $\Leftrightarrow$ (A)**: the risk-neutral measure and the pricing PDE are two representations of the same object — one probabilistic (martingale), one analytic (generator).


## References


- Harrison, J. M. and Pliska, S. R. (1981). *Martingales and stochastic integrals in the theory of continuous trading.* Stochastic Processes and their Applications, 11(3), 215–260.

- Karatzas, I. and Shreve, S. E. (1998). *Methods of Mathematical Finance.* Springer.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.

---

## Exercises


**Exercise 1.** Starting from the risk-neutral pricing formula $V(t,S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$, apply Ito's lemma to $e^{-rt}V(t, S_t)$ under $\mathbb{Q}$ and show that setting the drift to zero yields the Black-Scholes PDE.

??? success "Solution to Exercise 1"
    The risk-neutral pricing formula gives $V(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$. Define the discounted price $M_t = e^{-rt}\, V(t, S_t)$. By the tower property, $M_t = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$, which is a $\mathbb{Q}$-martingale.

    Apply Itô's formula to $M_t = e^{-rt}\, V(t, S_t)$. Since $e^{-rt}$ has zero quadratic variation, the product rule gives:

    $$dM_t = -re^{-rt}V\, dt + e^{-rt}\, dV$$

    Under $\mathbb{Q}$, the stock satisfies $dS_t = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$, so Itô's formula gives:

    $$dV = \left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S\frac{\partial V}{\partial S}\, dW_t^{\mathbb{Q}}$$

    Substituting:

    $$dM_t = e^{-rt}\!\left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV\right)dt + e^{-rt}\sigma S\frac{\partial V}{\partial S}\, dW_t^{\mathbb{Q}}$$

    Since $M_t$ is a $\mathbb{Q}$-martingale, the drift must vanish:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    This is the Black–Scholes PDE.

---

**Exercise 2.** The market price of risk is $\theta = (\mu - r)/\sigma$. Explain its economic interpretation and show that Girsanov's theorem uses $\theta$ to transform $W_t$ under $\mathbb{P}$ into $W_t^{\mathbb{Q}} = W_t + \theta t$ under $\mathbb{Q}$. Verify that under $\mathbb{Q}$, the stock drift becomes $r$.

??? success "Solution to Exercise 2"
    The **market price of risk** $\theta = (\mu - r)/\sigma$ measures the excess return per unit of volatility that the market demands for bearing one unit of Brownian risk. It is the continuous-time Sharpe ratio of the stock.

    **Girsanov's theorem** states: if we define $W_t^{\mathbb{Q}} = W_t + \theta t$, then under the measure $\mathbb{Q}$ defined by the Radon–Nikodym derivative:

    $$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\theta W_t - \frac{1}{2}\theta^2 t\right)$$

    the process $W_t^{\mathbb{Q}}$ is a standard Brownian motion.

    **Verification that the stock drift becomes $r$:** Under $\mathbb{P}$, $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$. Substitute $dW_t = dW_t^{\mathbb{Q}} - \theta\, dt$:

    $$dS_t = \mu S_t\, dt + \sigma S_t\bigl(dW_t^{\mathbb{Q}} - \theta\, dt\bigr) = (\mu - \sigma\theta)S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$$

    Since $\sigma\theta = \sigma \cdot (\mu - r)/\sigma = \mu - r$:

    $$dS_t = (\mu - (\mu - r))S_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}} = rS_t\, dt + \sigma S_t\, dW_t^{\mathbb{Q}}$$

    Under $\mathbb{Q}$, the stock drift is $r$, as required.

---

**Exercise 3.** The fundamental theorem of asset pricing states that no-arbitrage implies the existence of $\mathbb{Q}$, and completeness implies its uniqueness. In the Black-Scholes market with one stock and one Brownian motion, explain why the market is complete and $\mathbb{Q}$ is unique. What changes if the stock price is driven by two independent Brownian motions?

??? success "Solution to Exercise 3"
    In the Black–Scholes market there is one source of randomness (a single Brownian motion $W_t$) and one risky asset (the stock $S_t$). The market is **complete** because any contingent claim can be replicated by trading in $S_t$ and $B_t$. Formally, any $\mathcal{F}_T$-measurable payoff $\Phi$ satisfying an integrability condition can be written as:

    $$\Phi = V_0 + \int_0^T \phi_t\, dS_t$$

    for some predictable process $\phi_t$. This is possible because the single Brownian motion generates the entire filtration, and a single risky asset is sufficient to span all risk.

    **Uniqueness of $\mathbb{Q}$:** The Girsanov transformation requires choosing a drift removal $\theta$ such that $dW_t^{\mathbb{Q}} = dW_t + \theta\, dt$ makes $e^{-rt}S_t$ a martingale. This uniquely determines $\theta = (\mu - r)/\sigma$. Since the entire filtration is generated by one Brownian motion, there is exactly one equivalent martingale measure.

    **Two independent Brownian motions:** If $dS_t = \mu S_t\, dt + \sigma_1 S_t\, dW_t^{(1)} + \sigma_2 S_t\, dW_t^{(2)}$, the filtration is generated by $(W_t^{(1)}, W_t^{(2)})$. The Girsanov theorem now requires two drift parameters $(\theta_1, \theta_2)$ with the constraint $\sigma_1 \theta_1 + \sigma_2 \theta_2 = \mu - r$. This is one equation in two unknowns, so there is a one-parameter family of equivalent martingale measures. The market is **incomplete**: there are two sources of risk but only one risky asset, so not all contingent claims can be replicated. Different choices of $(\theta_1, \theta_2)$ lead to different option prices, and the no-arbitrage principle alone does not uniquely determine the price.

---

**Exercise 4.** Verify that the Black-Scholes PDE is the backward Kolmogorov equation associated with the $\mathbb{Q}$-diffusion $dS_t = rS_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}$, including the discounting term $-rV$. Write down the corresponding forward (Fokker-Planck) equation for the transition density.

??? success "Solution to Exercise 4"
    The Black–Scholes PDE is:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    The **backward Kolmogorov equation** for a diffusion $dS_t = b(S)\, dt + a(S)\, dW_t$ describes how the transition density $p(t, S; T, S')$ evolves in the backward variables $(t, S)$:

    $$\frac{\partial p}{\partial t} + b(S)\frac{\partial p}{\partial S} + \frac{1}{2}a(S)^2 \frac{\partial^2 p}{\partial S^2} = 0$$

    For the $\mathbb{Q}$-diffusion $dS_t = rS\, dt + \sigma S\, dW_t^{\mathbb{Q}}$, we have $b(S) = rS$ and $a(S) = \sigma S$, giving:

    $$\frac{\partial p}{\partial t} + rS\frac{\partial p}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 p}{\partial S^2} = 0$$

    The Black–Scholes PDE for $V$ is this backward Kolmogorov equation supplemented by the discounting term $-rV$. Since $V(t,S) = e^{-r(T-t)}\int_0^\infty \Phi(S')\, p(t,S;T,S')\, dS'$, the discounting factor $e^{-r(T-t)}$ generates the additional $-rV$ term when differentiated in $t$.

    **The forward (Fokker–Planck) equation** describes the evolution of $p$ in the forward variables $(T, S')$:

    $$\frac{\partial p}{\partial T} = -\frac{\partial}{\partial S'}\bigl[rS'\, p\bigr] + \frac{1}{2}\frac{\partial^2}{\partial S'^2}\bigl[\sigma^2 S'^2\, p\bigr]$$

    Expanding the derivatives:

    $$\frac{\partial p}{\partial T} = -rS'\frac{\partial p}{\partial S'} - rp + \frac{1}{2}\sigma^2\frac{\partial^2}{\partial S'^2}(S'^2 p)$$

    This governs the forward evolution of the risk-neutral transition density and is the adjoint of the backward Kolmogorov operator.

---

**Exercise 5.** The Feynman-Kac theorem provides the converse: any smooth solution of the Black-Scholes PDE with terminal condition $V(T,S) = \Phi(S)$ equals the risk-neutral expectation. State the regularity conditions on $\Phi$ and $V$ required for the theorem to hold. Give an example of a payoff where these conditions are violated and explain how this is handled in practice.

??? success "Solution to Exercise 5"
    **Feynman–Kac theorem (precise statement).** Let $S_t$ solve $dS_t = rS_t\, dt + \sigma S_t\, dW_t$ under $\mathbb{Q}$, and suppose $u \in C^{1,2}([0,T) \times (0,\infty))$ solves:

    $$\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} - ru = 0, \qquad u(T,S) = \Phi(S)$$

    **Regularity conditions required:**

    1. **Growth condition on $\Phi$:** There exist constants $C > 0$ and $p \geq 1$ such that $|\Phi(S)| \leq C(1 + S^p)$. This ensures the expectation $\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)]$ is finite.
    2. **Growth condition on $u$:** The solution must satisfy $|u(t,S)| \leq C(1 + S^p)$ uniformly on $[0,T] \times (0,\infty)$, to ensure that $e^{-rt}u(t,S_t)$ is a true martingale (not just a local martingale).
    3. **Smoothness of $u$:** $u \in C^{1,2}$ on $[0,T) \times (0,\infty)$ is needed for Itô's formula to apply.

    Under these conditions, $u(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$.

    **Example of violation:** Consider a **digital (binary) option** with payoff $\Phi(S) = \mathbf{1}_{\{S > K\}}$. This payoff is discontinuous at $S = K$, violating continuity — though it is bounded, hence it still satisfies the polynomial growth condition. The issue is regularity at maturity, not integrability. However, this does not cause a fundamental problem:

    - The expectation $V(t,S) = e^{-r(T-t)}\,\mathbb{Q}(S_T > K \mid S_t = S)$ is well-defined and finite.
    - For $t < T$, the function $V(t,S)$ is smooth ($C^\infty$) in both variables, because the log-normal density smooths out the discontinuity.
    - The PDE holds for all $t < T$, and $V(t,S) \to \Phi(S)$ as $t \to T^-$ pointwise (except at $S = K$).

    In practice, the discontinuity is handled by working with the probabilistic (Feynman–Kac) representation directly, or by approximating $\Phi$ with smooth payoffs and passing to the limit.

---

**Exercise 6.** Using the risk-neutral measure approach, price a European option with payoff $\Phi(S_T) = S_T \mathbf{1}_{\{S_T > K\}}$ (an asset-or-nothing call). Show that the price is $V = S\mathcal{N}(d_1)$ and interpret this as the "stock term" in the Black-Scholes call formula.

??? success "Solution to Exercise 6"
    The payoff is $\Phi(S_T) = S_T \mathbf{1}_{\{S_T > K\}}$. By risk-neutral pricing:

    $$V(t,S) = e^{-r\tau}\,\mathbb{E}^{\mathbb{Q}}\!\left[S_T \mathbf{1}_{\{S_T > K\}} \mid S_t = S\right]$$

    where $\tau = T - t$. Under $\mathbb{Q}$, $S_T = S\exp\!\bigl((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}\, Z\bigr)$ where $Z \sim \mathcal{N}(0,1)$. The condition $S_T > K$ is equivalent to:

    $$Z > \frac{\ln(K/S) - (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = -d_2$$

    where $d_2 = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$. Therefore:

    $$V = e^{-r\tau}\int_{-d_2}^{\infty} S\exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}\, z\right) \frac{e^{-z^2/2}}{\sqrt{2\pi}}\, dz$$

    $$= S\int_{-d_2}^{\infty} \exp\!\left(-\tfrac{1}{2}\sigma^2\tau + \sigma\sqrt{\tau}\, z\right) \frac{e^{-z^2/2}}{\sqrt{2\pi}}\, dz$$

    Complete the square in the exponent:

    $$-\frac{1}{2}\sigma^2\tau + \sigma\sqrt{\tau}\, z - \frac{z^2}{2} = -\frac{1}{2}(z - \sigma\sqrt{\tau})^2$$

    Substituting $w = z - \sigma\sqrt{\tau}$:

    $$V = S\int_{-d_2 - \sigma\sqrt{\tau}}^{\infty} \frac{e^{-w^2/2}}{\sqrt{2\pi}}\, dw = S\int_{-d_1}^{\infty} \frac{e^{-w^2/2}}{\sqrt{2\pi}}\, dw$$

    where $d_1 = d_2 + \sigma\sqrt{\tau} = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$. Therefore:

    $$V = S\,\mathcal{N}(d_1)$$

    **Interpretation:** The standard Black–Scholes call price is $C = S\,\mathcal{N}(d_1) - Ke^{-r\tau}\,\mathcal{N}(d_2)$, which can be decomposed as:

    $$C = \underbrace{S\,\mathcal{N}(d_1)}_{\text{asset-or-nothing call}} - K\underbrace{e^{-r\tau}\,\mathcal{N}(d_2)}_{\text{cash-or-nothing call}}$$

    The term $S\,\mathcal{N}(d_1)$ is the price of the asset-or-nothing call (pays $S_T$ if $S_T > K$, nothing otherwise). The term $Ke^{-r\tau}\mathcal{N}(d_2)$ is $K$ times the price of a cash-or-nothing call (pays \$1 if $S_T > K$). A standard call is economically equivalent to being long one asset-or-nothing call and short $K$ cash-or-nothing calls.
