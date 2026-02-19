# Chapter 10: Greeks and Asymptotics

This chapter develops the theory of option price sensitivities (Greeks) from three complementary perspectives—direct differentiation, PDE analysis, and probabilistic representation—then analyzes their behavior in asymptotic regimes. The interplay between these viewpoints provides both practical computation methods and deep structural insight into how option prices respond to changes in market variables and model parameters.

## Key Concepts

**Greeks as Derivatives of the Pricing Operator**
The pricing map $\mathcal{P}\Phi(t,S) = \mathbb{E}^{t,S}[e^{-r(T-t)}\Phi(S_T)]$ sends payoffs to price surfaces. Greeks are partial derivatives of this operator with respect to state variables ($S$, $t$) and model parameters ($\sigma$, $r$). The five fundamental Greeks—Delta $\Delta = \partial V/\partial S$, Gamma $\Gamma = \partial^2 V/\partial S^2$, Vega $\nu = \partial V/\partial \sigma$, Theta $\Theta = \partial V/\partial t$, and Rho $\rho = \partial V/\partial r$—quantify first- and second-order sensitivities. In the Black–Scholes model, these reduce to explicit closed-form expressions: $\Delta_{\text{call}} = N(d_1)$, $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$, $\nu = S\sqrt{\tau}\,N'(d_1)$, all derived using the key identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$. Higher-order cross-Greeks—Charm, Vanna, and Volga—capture second-order interactions and are essential for smile dynamics and volatility surface risk management. The martingale representation theorem identifies delta as the predictable integrand $Z_t = e^{-rt}\sigma S_t \Delta(t,S_t)$ in the stochastic integral representation of the discounted option price, providing the rigorous foundation for delta hedging in complete markets.

**PDE Perspective on Greeks**
Differentiating the Black–Scholes PDE $\partial_t V + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$ with respect to state variables and parameters yields **sensitivity PDEs** that the Greeks themselves satisfy. Delta solves a modified Black–Scholes PDE with an extra drift term $\sigma^2 S\Gamma$; gamma satisfies its own PDE with terminal condition $\Gamma(T,S) = \Phi''(S) = \delta(S-K)$ for vanilla options. Vega and rho satisfy inhomogeneous parabolic PDEs with zero terminal data, where the source terms involve derivatives of the generator $\mathcal{L}_\sigma$ with respect to parameters. The theta-gamma relation $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ expresses theta algebraically in terms of the other Greeks. Boundary and terminal behavior—delta approaching a step function, gamma concentrating near the strike as $\tau \to 0$—guide numerical boundary conditions for finite-difference solvers. Parabolic regularity theory (Schauder estimates) guarantees $V \in C^\infty$ for $t < T$ even when the payoff has kinks, though the Black–Scholes operator degenerates at $S = 0$, requiring log-coordinates for uniform ellipticity. For American options, free boundaries reduce regularity: delta remains continuous (smooth pasting) but gamma may have jump discontinuities.

**Probabilistic Computation of Greeks**
Three probabilistic methods provide expectation representations for Greeks, each with distinct advantages:

- *Feynman–Kac and pathwise differentiation*: differentiating through the stochastic flow $\partial S_T/\partial S = S_T/S$ yields $\Delta = \mathbb{E}^{t,S}[e^{-r\tau}\Phi'(S_T)S_T/S]$, with analogous formulas for vega and rho. This requires payoff smoothness (at least Lipschitz) and provides low-variance Monte Carlo estimators
- *Likelihood ratio (score function) method*: moves derivatives from the payoff to the density via $V'(\theta) = \mathbb{E}[\Phi(X)\partial_\theta \log p_\theta(X)]$, yielding $\Delta = \mathbb{E}[e^{-r\tau}\Phi(S_T) \cdot Z/(S\sigma\sqrt{\tau})]$ and an explicit gamma formula involving $Z^2 - Z\sigma\sqrt{\tau} - 1$. This handles non-smooth payoffs (digital options, barriers) at the cost of higher variance
- *Malliavin calculus*: provides the systematic framework underlying LR methods via integration by parts on Wiener space, with weights expressed through Hermite polynomials and the Skorokhod integral

Sensitivities as conditional expectations clarify the hedging interpretation: in incomplete markets (stochastic volatility), the martingale representation decomposes into hedgeable and unhedgeable components, with only the tradable-asset component corresponding to a realizable hedge.

**Pricing Asymptotics**
Option prices exhibit characteristic behavior in extreme parameter regimes:

- *Short maturity* ($\tau \to 0$): ATM call prices scale as $C_{\text{ATM}} \approx S\sigma\sqrt{\tau/(2\pi)}$, while OTM prices decay exponentially as $\exp(-(\ln(K/S))^2/(2\sigma^2\tau))$ with rate function $I = x^2/(2\sigma^2)$ connecting to heat kernel small-time expansions. Short-maturity implied volatility converges to local volatility
- *Extreme strikes*: large-$K$ call prices have Gaussian tail decay $\exp(-(\ln K)^2/(2\sigma^2\tau))$; Roger Lee's moment formula relates the implied volatility wing slopes $\beta_{R,L}$ to the existence of moments of $S_T$
- *Small volatility* ($\sigma \to 0$): OTM prices shrink as $\exp(-c/(2\sigma^2))$ where $c = (\ln(K/S) - r\tau)^2/\tau$ is the squared geodesic distance from the deterministic trajectory, interpretable via Varadhan's lemma and large deviations theory
- *Large time* ($T \to \infty$): Black–Scholes is non-ergodic in $S$ (call prices approach $S_0$, Greeks degenerate); mean-reverting factors in stochastic volatility models are ergodic, with long-dated implied vol converging to $\sqrt{\bar{v}}$

**Greeks Asymptotics and Scaling Laws**
Near expiry, Greeks exhibit universal scaling controlled by the diffusive length scale $\sigma\sqrt{\tau}$:

- *Gamma blow-up*: $\Gamma_{\text{ATM}} \sim (S\sigma\sqrt{2\pi\tau})^{-1} \sim \tau^{-1/2}$, with the peak localizing near $S = K$ in a band of width $\mathcal{O}(\sigma\sqrt{\tau})$ in log-moneyness while maintaining unit area—a Gaussian approximation to the Dirac delta $\Phi''(S) = \delta(S-K)$
- *Delta step-function behavior*: the transition from 0 to 1 occurs in a boundary layer of width $\Delta S \approx 2K\sigma\sqrt{\tau}$, creating pin risk and discrete hedging difficulties
- *Vega scaling*: $\nu_{\text{ATM}} \approx S\sqrt{\tau}/\sqrt{2\pi} \sim \sqrt{\tau}$ vanishes at expiry; the identity $\nu = \sigma S^2\tau\,\Gamma$ links vega and gamma risk in Black–Scholes. In smile models, vega generalizes to bucket vegas and model-parameter sensitivities
- *Unified scaling*: the inner-layer variable $z = \ln(S/K)/(\sigma\sqrt{\tau})$ provides a universal asymptotic description; OTM Greeks decay exponentially as $\exp(-z^2/2)$. Dimensional analysis confirms all scalings from $V_{\text{ATM}} \sim S\sigma\sqrt{\tau}$

The theta-gamma duality $\Theta \approx -\frac{1}{2}\sigma^2 S^2\Gamma$ encapsulates a fundamental trade-off: convexity benefit (positive gamma) is paid for through time decay (negative theta).

!!! note "Role in the Book"
    The Greeks computed here using closed-form Black–Scholes expressions (Chapter 6) and Feynman–Kac representations (Chapter 5) serve as benchmarks for later chapters. Implied volatility (Chapter 7) reinterprets vega as surface sensitivity, stochastic volatility models (Chapter 9) break the vega-gamma proportionality, and numerical methods rely on the PDE structure and boundary behavior developed here.

---
