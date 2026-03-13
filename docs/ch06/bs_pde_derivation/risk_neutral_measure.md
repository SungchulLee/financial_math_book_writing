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
