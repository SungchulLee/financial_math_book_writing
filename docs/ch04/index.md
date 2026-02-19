# Chapter 4: Measure Change and Girsanov's Theorem

This chapter develops the theory of probability measure changes in continuous time and its central application to derivative pricing. Starting from local martingales and stochastic exponentials, we state and prove Girsanov's theorem, construct the risk-neutral measure via drift removal, and explore the numeraire framework and forward measures. The chapter concludes with the financial interpretation of measure change—the distinction between pricing and hedging, and between the physical and risk-neutral worlds.

## Key Concepts

**Martingale Foundations**
A **local martingale** is a process that becomes a true martingale when stopped at an increasing sequence of stopping times $\tau_n \to \infty$; the distinction is crucial because many natural price processes (e.g., Ito integrals of unbounded integrands) are local martingales but not martingales. The deep connection between no-arbitrage and martingales extends to continuous time: absence of arbitrage is equivalent to the existence of an equivalent probability measure $\mathbb{Q} \sim \mathbb{P}$ under which discounted prices are (local) martingales. The **risk-neutral valuation principle** follows:
$$V_t = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\, ds}\, \Phi(X_T) \;\middle|\; \mathcal{F}_t\right]$$
The **stochastic exponential** (Doleans-Dade exponential) $\mathcal{E}(X)_t = \exp(X_t - X_0 - \frac{1}{2}\langle X \rangle_t)$ solves $d\mathcal{E} = \mathcal{E}\, dX$ and provides the Radon-Nikodym derivative for measure changes. The **martingale representation theorem** states that under the Brownian filtration, every square-integrable martingale $M_t$ admits the representation $M_t = M_0 + \int_0^t \phi_s\, dW_s$ for some adapted process $\phi$—this is the mathematical basis for perfect hedging in complete markets. The **Novikov condition** $\mathbb{E}[\exp(\frac{1}{2}\int_0^T \theta_s^2\, ds)] < \infty$ and the weaker **Kazamaki condition** ensure the stochastic exponential is a true martingale, validating the measure change.

**Girsanov's Theorem**
Girsanov's theorem resolves the apparent paradox of how a process with drift can become driftless without changing its paths. The key insight: drift is not a path property but a property of how probability is distributed across paths. Given an adapted process $\theta_t$ satisfying Novikov's condition, define the exponential martingale
$$Z_t = \exp\!\left(-\int_0^t \theta_s\, dW_s - \frac{1}{2}\int_0^t \theta_s^2\, ds\right)$$
and the new measure $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T} = Z_T$. Then $W_t^{\mathbb{Q}} = W_t + \int_0^t \theta_s\, ds$ is a $\mathbb{Q}$-Brownian motion. The proof verifies that $Z_t$ is a $\mathbb{P}$-martingale (via Ito's lemma) and checks the Brownian motion axioms under $\mathbb{Q}$. The financial meaning of the drift adjustment: Girsanov removes the risk premium $\theta = (\mu - r)/\sigma$ from asset dynamics, converting the physical drift $\mu$ to the risk-free rate $r$.

**The Risk-Neutral Measure**
Construction of $\mathbb{Q}$ proceeds by identifying the **market price of risk** $\theta_t = (\mu_t - r_t)/\sigma_t$—the excess return per unit of volatility—and applying Girsanov's theorem to make the discounted price $\tilde{S}_t = S_t/B_t$ a $\mathbb{Q}$-martingale. Under $\mathbb{Q}$, the stock dynamics become $dS_t = r_t S_t\, dt + \sigma_t S_t\, dW_t^{\mathbb{Q}}$. Worked examples cover the Black-Scholes model (constant parameters), multi-asset settings, and stochastic interest rate models.

**Numeraire and Forward Measures**
Each strictly positive traded asset $N_t$ defines a **numeraire measure** $\mathbb{Q}^N$ under which prices normalized by $N_t$ are martingales. The change-of-numeraire formula relates any two numeraire measures via $d\mathbb{Q}^N / d\mathbb{Q}^M |_{\mathcal{F}_t} = (N_t / M_t) \cdot (M_0 / N_0)$. The **$T$-forward measure** $\mathbb{Q}^T$ uses the zero-coupon bond $P(t,T)$ as numeraire, with Radon-Nikodym derivative $d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_t} = P(t,T)/(P(0,T) B_t)$. Under $\mathbb{Q}^T$, the forward price $F(t,T) = S_t / P(t,T)$ is a martingale, which simplifies the pricing of caplets, swaptions, and other interest rate derivatives by eliminating stochastic discounting.

**Financial Interpretation**
Pricing and hedging are distinct problems: pricing asks "what is the fair value?" (answered by the $\mathbb{Q}$-expectation), while hedging asks "what portfolio replicates the payoff?" (answered by the martingale representation integrand $\phi_t$). The physical measure $\mathbb{P}$ describes how prices actually evolve—with risk premia, empirical return distributions, and investor preferences—while $\mathbb{Q}$ is a mathematical pricing tool under which expected excess returns vanish. The risk premium $\mu - r = \sigma\theta$ decomposes the physical drift into the risk-free rate and compensation for bearing volatility risk. Measure change can fail when markets are incomplete (non-unique $\mathbb{Q}$), when the Novikov condition is violated, or when bubbles cause the local martingale property to be strict.

!!! note "Role in the Book"
    Girsanov's theorem and the risk-neutral measure are the theoretical engine behind the Black-Scholes PDE derivation (Chapter 6), the Feynman-Kac connection between expectations and PDEs (Chapter 5), and interest rate modeling via forward measures (Chapter 19).

---
