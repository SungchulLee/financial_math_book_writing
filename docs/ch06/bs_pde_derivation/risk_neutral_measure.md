# Black–Scholes PDE via Risk-Neutral Pricing


The risk-neutral derivation obtains the Black–Scholes PDE by starting from the **fundamental theorem of asset pricing**: in an arbitrage-free, complete market, there exists a unique equivalent martingale measure $\mathbb{Q}$ under which discounted asset prices are martingales. The option price is $V(t,S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$, and the PDE emerges as the condition for the discounted price process $e^{-rt}V(t, S_t)$ to be a $\mathbb{Q}$-martingale.

This is the most direct route from the no-arbitrage principle to the pricing equation: there is no portfolio construction (as in [delta hedging](delta_hedging.md)), no choice of numéraire (as in the [stock-measure approach](change_of_numeraire.md)), and no preference specification (as in the [equilibrium approach](equilibrium.md)). The economic content is concentrated in the existence and uniqueness of $\mathbb{Q}$; the rest is Itô calculus.


## Setup


**Model.** The stock price follows geometric Brownian motion under the physical measure $\mathbb{P}$:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constants $\mu$, $\sigma > 0$, and a money market account $B_t = e^{rt}$.

**Equivalent martingale measure.** By the [fundamental theorem of asset pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md), the absence of arbitrage and completeness of the market guarantee a unique probability measure $\mathbb{Q} \sim \mathbb{P}$ such that $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. By Girsanov's theorem, the process

$$W^{\mathbb{Q}}_t = W_t + \frac{\mu - r}{\sigma}\, t$$

is a $\mathbb{Q}$-Brownian motion, and the stock dynamics under $\mathbb{Q}$ are

$$dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$$

The ratio $\theta = (\mu - r)/\sigma$ is the **market price of risk**: it is the Girsanov drift removal that converts the physical drift $\mu$ to the risk-neutral drift $r$.

**Pricing formula.** The price of a European derivative with payoff $\Phi(S_T)$ at maturity $T$ is

$$V(t, S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T) \mid S_t = S\right]$$

We assume $V \in C^{1,2}([0,T) \times (0,\infty))$. The goal is to derive the PDE that $V$ must satisfy.


## Derivation: Martingale Condition via Itô's Formula


Define the discounted option price:

$$M_t = e^{-rt}\, V(t, S_t)$$

Since $V(t, S_t) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$, we have $M_t = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid \mathcal{F}_t]$, which is a $\mathbb{Q}$-martingale by the tower property. The PDE is the **consequence** of this martingale property.

Apply Itô's formula to $M_t = e^{-rt}\, V(t, S_t)$. By the product rule (noting that $e^{-rt}$ has zero quadratic variation):

$$dM_t = -r e^{-rt} V\, dt + e^{-rt}\, dV$$

where Itô's formula gives

$$dV = \frac{\partial V}{\partial t}\, dt + \frac{\partial V}{\partial S}\, dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}\, (dS)^2$$

Substituting $dS = rS\, dt + \sigma S\, dW^{\mathbb{Q}}$ and $(dS)^2 = \sigma^2 S^2\, dt$ (under $\mathbb{Q}$):

$$dV = \left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW^{\mathbb{Q}}$$

Therefore:

$$dM_t = e^{-rt}\!\left(\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV\right) dt + e^{-rt}\, \sigma S \frac{\partial V}{\partial S}\, dW^{\mathbb{Q}}$$

Since $M_t$ is a $\mathbb{Q}$-martingale, its $dt$ coefficient must vanish:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

with terminal condition $V(T, S) = \Phi(S)$. This is the **Black–Scholes PDE**.

!!! note "Direction of implication"
    The derivation runs: FTAP guarantees $\mathbb{Q}$ exists $\Rightarrow$ the pricing formula defines $V$ $\Rightarrow$ $e^{-rt}V$ is a martingale $\Rightarrow$ the drift vanishes $\Rightarrow$ the PDE holds. The PDE is a *consequence* of the martingale property, not a condition we impose. This is the opposite direction from the delta-hedging approach, which derives the PDE from a hedging argument and then uses Feynman–Kac to recover the pricing formula.


## The Feynman–Kac Connection


The relationship between the pricing formula and the PDE is an instance of the **Feynman–Kac theorem**, which provides the general bridge between parabolic PDEs and conditional expectations of diffusion processes.

**Theorem (Feynman–Kac).** *Let $S_t$ solve $dS_t = rS_t\, dt + \sigma S_t\, dW_t$ under $\mathbb{Q}$. If $u(t, S)$ is a $C^{1,2}$ solution of*

$$\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} - ru = 0, \qquad u(T, S) = \Phi(S)$$

*satisfying appropriate growth conditions, then*

$$u(t, S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T) \mid S_t = S\right]$$

The converse also holds: if $V(t,S)$ is defined by the conditional expectation and is sufficiently smooth, then it solves the PDE.

This theorem makes precise the equivalence between the **analytical** formulation (solve the PDE backward from terminal data) and the **probabilistic** formulation (compute the conditional expectation under $\mathbb{Q}$). The two representations give different computational strategies for the same object: the PDE can be solved by finite differences or transformation to the heat equation, while the expectation can be evaluated by Monte Carlo simulation or, for GBM, in closed form (yielding the Black–Scholes formula).


## Generator Formulation


The same derivation can be expressed more compactly using the **infinitesimal generator** of the risk-neutral diffusion process.

**Generator of GBM under $\mathbb{Q}$.** For the diffusion $dS_t = rS_t\, dt + \sigma S_t\, dW^{\mathbb{Q}}_t$, the infinitesimal generator acting on $f \in C^2(0,\infty)$ is

$$\mathcal{L}^{\mathbb{Q}} f(S) = rS\, f'(S) + \frac{1}{2}\sigma^2 S^2\, f''(S)$$

This is the second-order differential operator that encodes the drift and diffusion of $S_t$ under $\mathbb{Q}$.

**Extended generator.** For a time-dependent function $g(t, S)$, the extended generator of the space-time process $(t, S_t)$ is

$$\mathcal{A}\, g(t, S) = \frac{\partial g}{\partial t} + \mathcal{L}^{\mathbb{Q}} g(t, S)$$

This is precisely the operator that appears in Itô's formula: $g(t, S_t)$ is a local martingale under $\mathbb{Q}$ if and only if $\mathcal{A}\, g = 0$.

**Application.** Applying the extended generator to $M(t, S) = e^{-rt}\, V(t, S)$:

$$\mathcal{A}\!\left[e^{-rt} V\right] = \frac{\partial}{\partial t}\!\left[e^{-rt} V\right] + \mathcal{L}^{\mathbb{Q}}\!\left[e^{-rt} V\right] = e^{-rt}\!\left(\frac{\partial V}{\partial t} - rV\right) + e^{-rt}\!\left(rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)$$

Setting $\mathcal{A}[e^{-rt}V] = 0$ and dividing by $e^{-rt}$ recovers the Black–Scholes PDE. The generator formulation makes the structure transparent: the PDE is the statement that the discounted price lies in the **null space of the extended generator**, which is equivalent to the martingale property.

!!! note "Backward Kolmogorov equation"
    The Black–Scholes PDE is a special case of the **backward Kolmogorov equation** associated with the $\mathbb{Q}$-diffusion. If $p^{\mathbb{Q}}(t, S; T, S')$ is the transition density of $S_t$ under $\mathbb{Q}$, it satisfies $\partial_t p + \mathcal{L}^{\mathbb{Q}}_S p = 0$ in the backward variables $(t, S)$. Integrating against the discounted payoff $e^{-r(T-t)} \Phi(S')$ recovers the Black–Scholes PDE for $V$.


## Summary


The risk-neutral derivation proceeds in three steps:

1. **FTAP and Girsanov**: the absence of arbitrage and market completeness guarantee a unique measure $\mathbb{Q}$ under which $dS = rS\, dt + \sigma S\, dW^{\mathbb{Q}}$.
2. **Pricing formula**: $V(t,S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$, so $e^{-rt}V$ is a $\mathbb{Q}$-martingale.
3. **Itô's formula**: the vanishing of the $dt$ term in $d(e^{-rt}V)$ yields the PDE.

The Feynman–Kac theorem provides the converse: any sufficiently regular solution of the PDE with the correct terminal condition equals the risk-neutral expectation. Together, these establish the equivalence of the PDE and probabilistic formulations of option pricing.


## References

- Harrison, J. M. and Pliska, S. R. (1981). *Martingales and stochastic integrals in the theory of continuous trading.* Stochastic Processes and their Applications, 11(3), 215–260.

- Karatzas, I. and Shreve, S. E. (1998). *Methods of Mathematical Finance.* Springer.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.

---

## Exercises

**Exercise 1.** Starting from the risk-neutral pricing formula $V(t,S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$, apply Ito's lemma to $e^{-rt}V(t, S_t)$ under $\mathbb{Q}$ and show that setting the drift to zero yields the Black-Scholes PDE.

---

**Exercise 2.** The market price of risk is $\theta = (\mu - r)/\sigma$. Explain its economic interpretation and show that Girsanov's theorem uses $\theta$ to transform $W_t$ under $\mathbb{P}$ into $W_t^{\mathbb{Q}} = W_t + \theta t$ under $\mathbb{Q}$. Verify that under $\mathbb{Q}$, the stock drift becomes $r$.

---

**Exercise 3.** The fundamental theorem of asset pricing states that no-arbitrage implies the existence of $\mathbb{Q}$, and completeness implies its uniqueness. In the Black-Scholes market with one stock and one Brownian motion, explain why the market is complete and $\mathbb{Q}$ is unique. What changes if the stock price is driven by two independent Brownian motions?

---

**Exercise 4.** Verify that the Black-Scholes PDE is the backward Kolmogorov equation associated with the $\mathbb{Q}$-diffusion $dS_t = rS_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}$, including the discounting term $-rV$. Write down the corresponding forward (Fokker-Planck) equation for the transition density.

---

**Exercise 5.** The Feynman-Kac theorem provides the converse: any smooth solution of the Black-Scholes PDE with terminal condition $V(T,S) = \Phi(S)$ equals the risk-neutral expectation. State the regularity conditions on $\Phi$ and $V$ required for the theorem to hold. Give an example of a payoff where these conditions are violated and explain how this is handled in practice.

---

**Exercise 6.** Using the risk-neutral measure approach, price a European option with payoff $\Phi(S_T) = S_T \mathbf{1}_{\{S_T > K\}}$ (an asset-or-nothing call). Show that the price is $V = S\mathcal{N}(d_1)$ and interpret this as the "stock term" in the Black-Scholes call formula.

---

## Solutions

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

??? success "Solution to Exercise 3"
    In the Black–Scholes market there is one source of randomness (a single Brownian motion $W_t$) and one risky asset (the stock $S_t$). The market is **complete** because any contingent claim can be replicated by trading in $S_t$ and $B_t$. Formally, any $\mathcal{F}_T$-measurable payoff $\Phi$ satisfying an integrability condition can be written as:

    $$\Phi = V_0 + \int_0^T \phi_t\, dS_t$$

    for some predictable process $\phi_t$. This is possible because the single Brownian motion generates the entire filtration, and a single risky asset is sufficient to span all risk.

    **Uniqueness of $\mathbb{Q}$:** The Girsanov transformation requires choosing a drift removal $\theta$ such that $dW_t^{\mathbb{Q}} = dW_t + \theta\, dt$ makes $e^{-rt}S_t$ a martingale. This uniquely determines $\theta = (\mu - r)/\sigma$. Since the entire filtration is generated by one Brownian motion, there is exactly one equivalent martingale measure.

    **Two independent Brownian motions:** If $dS_t = \mu S_t\, dt + \sigma_1 S_t\, dW_t^{(1)} + \sigma_2 S_t\, dW_t^{(2)}$, the filtration is generated by $(W_t^{(1)}, W_t^{(2)})$. The Girsanov theorem now requires two drift parameters $(\theta_1, \theta_2)$ with the constraint $\sigma_1 \theta_1 + \sigma_2 \theta_2 = \mu - r$. This is one equation in two unknowns, so there is a one-parameter family of equivalent martingale measures. The market is **incomplete**: there are two sources of risk but only one risky asset, so not all contingent claims can be replicated. Different choices of $(\theta_1, \theta_2)$ lead to different option prices, and the no-arbitrage principle alone does not uniquely determine the price.

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

??? success "Solution to Exercise 5"
    **Feynman–Kac theorem (precise statement).** Let $S_t$ solve $dS_t = rS_t\, dt + \sigma S_t\, dW_t$ under $\mathbb{Q}$, and suppose $u \in C^{1,2}([0,T) \times (0,\infty))$ solves:

    $$\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} - ru = 0, \qquad u(T,S) = \Phi(S)$$

    **Regularity conditions required:**

    1. **Growth condition on $\Phi$:** There exist constants $C > 0$ and $p \geq 1$ such that $|\Phi(S)| \leq C(1 + S^p)$. This ensures the expectation $\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)]$ is finite.
    2. **Growth condition on $u$:** The solution must satisfy $|u(t,S)| \leq C(1 + S^p)$ uniformly on $[0,T] \times (0,\infty)$, to ensure that $e^{-rt}u(t,S_t)$ is a true martingale (not just a local martingale).
    3. **Smoothness of $u$:** $u \in C^{1,2}$ on $[0,T) \times (0,\infty)$ is needed for Itô's formula to apply.

    Under these conditions, $u(t,S) = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$.

    **Example of violation:** Consider a **digital (binary) option** with payoff $\Phi(S) = \mathbf{1}_{\{S > K\}}$. This payoff is discontinuous at $S = K$, so it is not even continuous, let alone satisfying a polynomial growth bound with differentiability. However, this does not cause a fundamental problem:

    - The expectation $V(t,S) = e^{-r(T-t)}\,\mathbb{Q}(S_T > K \mid S_t = S)$ is well-defined and finite.
    - For $t < T$, the function $V(t,S)$ is smooth ($C^\infty$) in both variables, because the log-normal density smooths out the discontinuity.
    - The PDE holds for all $t < T$, and $V(t,S) \to \Phi(S)$ as $t \to T^-$ pointwise (except at $S = K$).

    In practice, the discontinuity is handled by working with the probabilistic (Feynman–Kac) representation directly, or by approximating $\Phi$ with smooth payoffs and passing to the limit.

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
